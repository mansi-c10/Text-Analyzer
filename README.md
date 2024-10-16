# Text Analyzer

## Overview

The Text Analyzer is a Python application designed to analyze text reviews using Azure's Text Analytics services. This project was developed during the Infosys AI Training program and focuses on providing insights such as language detection, sentiment analysis, key phrase extraction, and entity recognition.

## Features

- **Language Detection**: Identifies the primary language of the text.
- **Sentiment Analysis**: Analyzes the sentiment of the text (positive, negative, neutral).
- **Key Phrase Extraction**: Extracts important phrases from the text.
- **Entity Recognition**: Identifies and categorizes entities mentioned in the text.
- **Linked Entity Recognition**: Recognizes entities and provides relevant links.

## Requirements

- Python 3.6 or higher
- Azure Text Analytics API subscription
- Python packages listed in `requirements.txt`

## Installation

To set up the Text Analyzer, follow these steps:

1. **Clone the repository**:

   git clone https://github.com/yourusername/text-analyzer.git
   cd text-analyzer

2. **Install required packages**:

   Ensure you have Python installed, then install the required libraries:

   pip install -r requirements.txt
   

3. **Set up environment variables**:

   Create a `.env` file in the project root directory and add your Azure service credentials:

   AI_SERVICE_ENDPOINT=your_azure_endpoint
   AI_SERVICE_KEY=your_azure_key

## Usage

Run the application using the following command:

python text_analyzer.py

### Input

- Place your text review files in the `reviews` directory. The application will process each file in that directory.

### Output

The analyzer will display results including:

- Detected language
- Sentiment of each review
- Key phrases
- Recognized entities
- Linked entities with URLs

## Example

When you run the application, it processes each review and provides output like this:

Processing: review1.txt

Review Content:
This product is fantastic! I loved it.

Language Detected: English

Sentiment: Positive

Key Phrases:
    fantastic
    loved

Entities:
    product (Product)

Linked Entities:
    fantastic (https://en.wikipedia.org/wiki/Fantastic)
    
## Acknowledgments

- Thanks to the Infosys AI Training team for their guidance and support.
- Acknowledgment to Microsoft for providing the Azure Text Analytics services used in this project.
