import os
import json
import requests
from dotenv import load_dotenv
from langchain_core.tools import tool
from langchain.chains.llm import LLMChain
from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq
from typing import Dict, Any
from prompts import INGEST_PROMPT, WRITER_PROMPT, REVIEWER_PROMPT, REFINER_PROMPT

load_dotenv()
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

groq_llm = ChatGroq(model="llama-3.3-70b-versatile", api_key=os.getenv("GROQ_API_KEY"))

@tool
def fetch_repo_files_from_github(repo_url: str) -> list:
    """
    Fetches all readable source code and markdown files from a public or private GitHub repository.
    """
    headers = {
        "Authorization": f"token {GITHUB_TOKEN}",
        "Accept": "application/vnd.github.v3+json"
    }

    # Extract owner and repo name
    try:
        path_parts = repo_url.strip("/").split("/")
        owner = path_parts[-2]
        repo = path_parts[-1]
    except:
        return [{"error": "Invalid GitHub URL format"}]

    api_url = f"https://api.github.com/repos/{owner}/{repo}/contents"

    def recurse_fetch(url):
        contents = []
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            return []
        for item in response.json():
            if item["type"] == "file" and item["name"].endswith((".py", ".ipynb", ".md")):
                file_response = requests.get(item["download_url"], headers=headers)
                if file_response.status_code == 200:
                    contents.append({
                        "path": item["path"],
                        "content": file_response.text
                    })
            elif item["type"] == "dir":
                contents += recurse_fetch(item["url"])
        return contents

    return recurse_fetch(api_url)

def get_ingestor_agent():
    """
    Returns an LLMChain that summarizes a list of files into a structured project overview.
    """
    prompt = PromptTemplate.from_template(INGEST_PROMPT)

    return LLMChain(llm=groq_llm, prompt=prompt)

def get_writer_agent():
    """
    Returns an LLMChain that converts a summary into a complete blog post in markdown.
    """
    prompt = PromptTemplate.from_template(WRITER_PROMPT)
    return LLMChain(llm=groq_llm, prompt=prompt)

def get_reviewer_agent():
    """
    Returns an LLMChain that reviews a blog post and suggests improvements.
    """
    prompt = PromptTemplate.from_template(REVIEWER_PROMPT)
    return LLMChain(llm=groq_llm, prompt=prompt)

def get_refiner_agent():
    """
    Returns an LLMChain that refines a blog post using suggestions from a reviewer.
    """
    prompt = PromptTemplate.from_template(REFINER_PROMPT)
    return LLMChain(llm=groq_llm,prompt=prompt)

