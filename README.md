# Newsglance AI

## Description
Newsglance AI is a web application that summarizes real-time news articles from Google News. The website provides:
- A summarized version of news articles with headings and content.
- A link to the original news article.
- The ability to customize news based on country and categories like politics, sports, business, etc.

The website fetches news from Google News and uses the Gemini Fash1.5 language model (LLM) to summarize the content, powered by LangChain, Google Gemini, and Serapi.

## Features
- Real-time news summarization.
- Customizable country and category selection.
- Summarized content with headings and article link.
- Supports categories like Politics, Sports, Business, etc.

## Requirements

1. Python 3.7+ (or compatible version)
2. Required Python libraries:
   - LangChain
   - Google Gemini
   - Serapi
   - Streamlit

### Install Dependencies
You can install all required dependencies from the `requirements.txt` file by running:

```bash
pip install -r requirements.txt
