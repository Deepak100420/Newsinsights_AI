
# 📰Newsglance AI

## Description
Newsglance AI is a web application that summarizes real-time news articles from Google News. The website provides:
- A summarized version of news articles with headings and content.
- A link to the original news article.
- The ability to customize news based on country and categories like politics, sports, business, etc.

The website fetches news from Google News and uses the Gemini Flash1.5 language model (LLM) to summarize the content, powered by LangChain, Google Gemini, and Serapi.

## Features
- Real-time news summarization.
- Customizable country and category selection.
- Summarized content with headings and article link.
- Supports categories like Politics, Sports, Business, etc.


### **Tool Stack**:
- **LangChain**: A framework to build and orchestrate complex workflows using generative AI models. It simplifies chaining multiple components such as models, tools, and API calls to build more advanced applications. 
  - **`RunnableLambda`**: Allows defining custom, executable logic that can be incorporated into workflows.
  - **`RunnableParallel`**: Facilitates the parallel execution of multiple tasks, improving efficiency in workflows.
  
- **GoogleGenerativeAI**: Provides access to Google's generative AI models for creating responses, summarizing content, and generating insights from user inputs related to news.

- **SerpAPI**: A service that enables fetching search results from Google, which is used for gathering the latest news articles based on user queries.

- **Streamlit**: A web framework used for building interactive applications that present the insights and results from the backend in an easy-to-use interface.

- **Pydantic**: Ensures the validation of data input and output throughout the system, maintaining structure and ensuring consistency.

- **Dotenv**: Manages environment variables securely, particularly for handling sensitive information like API keys.

---

### **Integration of LangChain Agents**:
- **`tool` Module**: This crucial component is used to connect different systems and models in the backend. It allows the integration of various tools and services, enabling dynamic data fetching and processing. For example, the tool is used to fetch news from SerpAPI and process it through GoogleGenerativeAI for insightful analysis.
  
- **Agents**: LangChain's agent-based architecture is leveraged to build dynamic decision-making workflows. The agents utilize `RunnableLambda` and `RunnableParallel` for executing tasks in a defined sequence or in parallel, ensuring the platform can handle complex queries efficiently.
  
- **News Processing**: LangChain agents manage the orchestration of tasks such as:
  1. **Query Handling**: The agents receive user queries and determine whether to fetch news from SerpAPI or generate AI-powered insights.
  2. **Data Flow**: It handles the flow of data between the various models and APIs, ensuring seamless integration and timely responses.
  3. **Real-time Insights**: The agents work in tandem to provide real-time, actionable insights by processing multiple data points from different sources.







## Requirements

1. Python 3.7+ (or compatible version)
2. Required Python libraries:
   - LangChain
   - Google Gemini
   - Serapi
   - Streamlit

### Install Dependencies
You can install all required dependencies from the `requirements.txt` file by running:


### pip install -r requirements.txt 


### Key sections explained:
- **Project Setup**:
  - Cloning the repo
  - Installing dependencies from `requirements.txt`
  - Setting up API keys (if needed)
  - Creating an `.env` file for environment variables (optional but common)
  
- **Run Instructions**:
  - Command to run the app (`streamlit run main.py`)

