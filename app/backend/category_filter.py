from langchain_google_genai import GoogleGenerativeAI,ChatGoogleGenerativeAI

from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import PromptTemplate
import streamlit as st
from pydantic import BaseModel, Field
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableLambda,RunnableParallel
from langchain.agents import tool
from serpapi import GoogleSearch
from dotenv import load_dotenv
import os

load_dotenv()

os.environ["LANGSMITH_TRACING"]="true"
os.environ["LANGSMITH_ENDPOINT"]="https://api.smith.langchain.com"
os.environ["LANGSMITH_API_KEY"]="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"
os.environ["LANGSMITH_PROJECT"]="newsglance-ai"

model_key=st.secrets["GOOGLE_MODEL_API_KEY"]
search_key=st.secrets['GOOGLE_SEARCH_API_KEY']



model=ChatGoogleGenerativeAI(model="gemini-1.5-flash",google_api_key=model_key)



template="""
**Input (User's Question):**
    {question}
**Output (Google News API Query):**
Extract the key topics and format them into a query string with logical operators (AND, OR, quotes for exact matches) to ensure accurate news search results.

For example:  
- If the question includes time (like "latest updates"), add "AND latest."  
- If specific regions or categories are mentioned, include them as keywords.
- Keep the query concise and relevant to the original question.

**Transformed Query:**  
 
"""

prompt=PromptTemplate.from_template(template=template)









def search_news(query):
    search=GoogleSearch({
    "q": query,   # search search
    "tbm": "nws",  # news
    "tbs": "qdr:d", # last 24h
    "num":20,"api_key": search_key,"gl":"in"
    })
    result=search.get_dict()
    news=[]
    for i in result["news_results"]:
        new_entry={
            "Title" : i["title"],
            "Snippet":i["snippet"],
            "Link":i["link"]
        }
        news.append(new_entry)
    return news


def news_summary(query):
    template="""You are an advanced AI summarizer and filter. Your task is to process a list of articles based on a user query and only include relevant articles that provide useful and meaningful information. Articles that are vague, generic, or do not add value to the query should be excluded, even if they match the query. For each relevant article, generate a structured output with the following details:

- **Title**: Rewrite the provided title to be concise and relevant, capturing the essence of the article in 5-7 words.
- **Summary**: Combine the snippet and title to create a clear, concise, and informative summary in 3-5 sentences. Ensure the summary provides value by including specific details or insights relevant to the query.
- **Link**: Include the provided link. If no link is provided, state "No link provided."

### Conditions:
1. The article must explicitly relate to the query.
2. The article must provide useful and specific information. If the content is vague, generic, or lacks valuable insights, exclude it.
3. Do not include any text like as if you are generatining from given data and do not show you like a AI,you should act like human
4.do not refer the artcile or content,i want direct answer
\n{format_instructions}\n

Input:
- Query: {query}
- Articles: {articles}

Output:  
Generate a filtered list of articles relevant to the query. Format the output as List[json1,json2]:

[
  
    "title": "Concise and relevant title",
    "summary": "Clear, concise summary providing valuable insights based on the query.",
    "link": "Provided link or 'No link provided'"
  ,
  
    "title": "Another relevant title",
    "summary": "Informative summary that adds value, highlighting specific insights.",
    "link": "Provided link or 'No link provided'"
  
]

"""

    #prompt=PromptTemplate.from_template(template=template)


    class neww(BaseModel):
        title: str = Field(description="title of the article")
        summary: str = Field(description="summary of the article")
        linl: str=Field(description="link of the article")


   
    # Set up a parser + inject instructions into the prompt template.
    parser = JsonOutputParser(pydantic_object=neww)


    prompt = PromptTemplate(
    template=template,
    input_variables=["query","articles"],
    partial_variables={"format_instructions": parser.get_format_instructions()},
)

    formatted_prompt=prompt.format_prompt(query=query,articles=search_news(query))



    return formatted_prompt


news=(RunnableLambda(lambda x:news_summary(x))|model|JsonOutputParser())  #|StrOutputParser()

#query="donald trump india"


question_parser=prompt|model|StrOutputParser()

result=question_parser|news       #RunnableParallel(branches={"pros": output})


def output(query):


    output=result.invoke({"question":query})
    return output

