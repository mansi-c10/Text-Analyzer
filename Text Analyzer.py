from dotenv import load_dotenv
import os
from azure.core.credentials import AzureKeyCredential
from azure.ai.textanalytics import TextAnalyticsClient

def load_config():
    """Load Azure service configuration from environment variables."""
    load_dotenv()
    return os.getenv('AI_SERVICE_ENDPOINT'), os.getenv('AI_SERVICE_KEY')

def create_client(endpoint, key):
    """Create a Text Analytics client."""
    credentials = AzureKeyCredential(key)
    return TextAnalyticsClient(endpoint=endpoint, credential=credentials)

def analyze_review(file_path):
    """Analyze the contents of a single review file."""
    with open(file_path, encoding='utf8') as file:
        content = file.read()
    return content

def process_text(client, text):
    """Process the text through various analyses."""
    # Language detection
    language_result = client.detect_language(documents=[text])[0]
    print(f"\nLanguage Detected: {language_result.primary_language.name}")

    # Sentiment analysis
    sentiment_result = client.analyze_sentiment(documents=[text])[0]
    print(f"\nSentiment: {sentiment_result.sentiment}")

    # Key phrase extraction
    key_phrases_result = client.extract_key_phrases(documents=[text])[0].key_phrases
    if key_phrases_result:
        print("\nKey Phrases:")
        for phrase in key_phrases_result:
            print(f"\t{phrase}")

    # Entity recognition
    entities_result = client.recognize_entities(documents=[text])[0].entities
    if entities_result:
        print("\nEntities:")
        for entity in entities_result:
            print(f"\t{entity.text} ({entity.category})")

    # Linked entity recognition
    linked_entities_result = client.recognize_linked_entities(documents=[text])[0].entities
    if linked_entities_result:
        print("\nLinked Entities:")
        for linked_entity in linked_entities_result:
            print(f"\t{linked_entity.name} ({linked_entity.url})")

def main():
    try:
        # Load configuration and create client
        endpoint, key = load_config()
        text_client = create_client(endpoint, key)

        # Process each review file
        reviews_directory = 'reviews'
        for review_file in os.listdir(reviews_directory):
            review_path = os.path.join(reviews_directory, review_file)
            print(f'\n-------------\nProcessing: {review_file}')
            review_text = analyze_review(review_path)
            print(f'\nReview Content:\n{review_text}')
            process_text(text_client, review_text)

    except Exception as error:
        print(f"An error occurred: {error}")

if _name_ == "_main_":
    main()
