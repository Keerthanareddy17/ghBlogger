from agents import get_writer_agent

# Simulated summary from ingestor agent
sample_summary = """
Codebase Summary
Project Purpose: The purpose of this project is to develop a Retrieval-Augmented Generation (RAG) based chatbot, named KJC-BOT, for Kristu Jayanti College. The chatbot aims to provide accurate and concise answers to user queries about the college, utilizing a structured knowledge base and sentence embeddings for efficient information retrieval.

Technologies Used:

FAISS Vector DB: For efficient similarity search and information retrieval.
Groq's Llama-3.3-70B model: For generating precise responses to user queries.
Sentence Transformers: For converting text into embeddings.
Streamlit: For building the chatbot's user interface.
Python: As the primary programming language.
BeautifulSoup and requests: For web scraping.
Core Components and Logic:

Data Collection: The project involves scraping structured data from the college website using scraping.py and links.py.
Data Preprocessing: The scraped data is cleaned and preprocessed using cleaning.py and structuring.py.
Embeddings Generation: The preprocessed data is used to generate embeddings using embeddings.py.
FAISS Indexing: The embeddings are indexed using FAISS for efficient similarity search.
Chatbot Interface: The chatbot's user interface is built using Streamlit in app.py.
Query Processing: User queries are processed using the Groq API and FAISS index to retrieve relevant information.
Observed Patterns, Libraries, or Workflows:

Modular Code Structure: The project is organized into separate files for each component, making it easy to maintain and update.
Use of Environment Variables: The project uses environment variables to store sensitive information like API keys.
Dependency Management: The project uses popular libraries and frameworks, making it easy to manage dependencies.
Data Processing Pipeline: The project follows a clear data processing pipeline, from data collection to embeddings generation and indexing.
Additional Notes:

Scalability: The project can be scaled to cover more data and improve the chatbot's accuracy.
Maintenance: Regular updates to the data and models can ensure the chatbot remains accurate and relevant.
Security: The project should ensure proper security measures are in place to protect sensitive information like API keys.
User Experience: The chatbot's user interface can be improved to provide a better user experience, such as adding more features or improving the response time."""

def test_writer_agent():
    writer_chain = get_writer_agent()
    result = writer_chain.invoke({"summary": sample_summary})
    print("\n=== GENERATED BLOG ===\n")
    print(result["text"])

if __name__ == "__main__":
    test_writer_agent()
