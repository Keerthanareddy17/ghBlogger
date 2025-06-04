from agents import get_refiner_agent

sample_blog = """
# Building KJC-BOT: A Retrieval-Augmented Generation Based Chatbot for Kristu Jayanti College
## Introduction
In today's digital age, chatbots have become an essential tool for providing instant support and information to users. With the advancements in natural language processing (NLP) and machine learning, chatbots can now understand and respond to complex user queries with accuracy. In this blog post, we will explore the development of KJC-BOT, a Retrieval-Augmented Generation (RAG) based chatbot designed for Kristu Jayanti College. The chatbot aims to provide accurate and concise answers to user queries about the college, utilizing a structured knowledge base and sentence embeddings for efficient information retrieval.

## Project Overview
The primary goal of the KJC-BOT project is to create a chatbot that can provide accurate and relevant information to users about Kristu Jayanti College. The project involves several key features, including:
* Data collection: Scraping structured data from the college website
* Data preprocessing: Cleaning and structuring the scraped data
* Embeddings generation: Generating sentence embeddings for efficient information retrieval
* FAISS indexing: Indexing the embeddings for efficient similarity search
* Chatbot interface: Building the chatbot's user interface using Streamlit

The architecture of the project is modular, with separate files for each component, making it easy to maintain and update. The project uses environment variables to store sensitive information like API keys and follows a clear data processing pipeline.

## Technologies Used
The KJC-BOT project utilizes several cutting-edge technologies, including:
* **FAISS Vector DB**: For efficient similarity search and information retrieval
* **Groq's Llama-3.3-70B model**: For generating precise responses to user queries
* **Sentence Transformers**: For converting text into embeddings
* **Streamlit**: For building the chatbot's user interface
* **Python**: As the primary programming language
* **BeautifulSoup and requests**: For web scraping

## Key Functionalities
The KJC-BOT chatbot has several key functionalities, including:
* **Data collection**: The chatbot can scrape structured data from the college website using scraping.py and links.py
* **Data preprocessing**: The chatbot can clean and preprocess the scraped data using cleaning.py and structuring.py
* **Embeddings generation**: The chatbot can generate sentence embeddings for efficient information retrieval using embeddings.py
* **FAISS indexing**: The chatbot can index the embeddings for efficient similarity search
* **Query processing**: The chatbot can process user queries using the Groq API and FAISS index to retrieve relevant information

## Development Process
The development process of the KJC-BOT project follows a clear workflow, including:
1. **Data collection**: Scraping structured data from the college website
2. **Data preprocessing**: Cleaning and structuring the scraped data
3. **Embeddings generation**: Generating sentence embeddings for efficient information retrieval
4. **FAISS indexing**: Indexing the embeddings for efficient similarity search
5. **Chatbot interface development**: Building the chatbot's user interface using Streamlit
6. **Query processing**: Processing user queries using the Groq API and FAISS index to retrieve relevant information

## Final Thoughts and Future Scope
The KJC-BOT project has the potential to be scaled up to cover more data and improve the chatbot's accuracy. Regular updates to the data and models can ensure the chatbot remains accurate and relevant. Additionally, the project should ensure proper security measures are in place to protect sensitive information like API keys. The chatbot's user interface can also be improved to provide a better user experience, such as adding more features or improving the response time. With the advancements in NLP and machine learning, the possibilities for chatbot development are endless, and the KJC-BOT project is just the beginning."""


sample_suggestions = """
### Suggestions for Improvement
* **Tone and Clarity**:
  + Use a more conversational tone to engage readers, while maintaining technical accuracy and professionalism.
  + Avoid repetitive phrases, such as "The chatbot can..." to improve sentence variety.
  + Consider adding a brief overview of the project's background and motivation to provide context for readers.
* **Grammar and Flow**:
  + Use transitional phrases to connect sections and improve the overall flow of the blog post.
  + Ensure consistent verb tenses throughout the post.
  + Break up long sentences into shorter, simpler ones to enhance readability.
* **Technical Accuracy**:
  + Provide more detailed explanations of technical concepts, such as Retrieval-Augmented Generation (RAG) and sentence embeddings, for non-expert readers.
  + Consider adding diagrams or illustrations to help visualize the chatbot's architecture and workflow.
  + Ensure that technical terms and acronyms are defined or explained when first introduced.
* **Organization and Formatting**:
  + Use clear and descriptive headings to separate sections and improve navigation.
  + Consider adding a table of contents or index to facilitate quick access to specific sections.
  + Use bullet points or numbered lists consistently throughout the post to present information in a clear and concise manner.
  + Use code blocks or formatting to distinguish code snippets from regular text.
  + Consider adding a conclusion section to summarize the main points and reiterate the project's significance.
* **Specific Section Improvements**:
  + In the **Introduction** section, consider adding a brief overview of the project's goals and objectives.
  + In the **Project Overview** section, provide more details about the project's architecture and workflow.
  + In the **Technologies Used** section, consider adding a brief description of each technology and its role in the project.
  + In the **Key Functionalities** section, use a consistent format to present each functionality, including a brief description and technical details.
  + In the **Development Process** section, consider adding a diagram or illustration to visualize the workflow.
  + In the **Final Thoughts and Future Scope** section, provide more specific ideas for future improvements and potential applications of the project.
"""

def test_refiner_agent():
    refiner = get_refiner_agent()
    result = refiner.invoke({
        "blog": sample_blog,
        "suggestions": sample_suggestions
    })
    print("\n=== FINAL BLOG OUTPUT ===\n")
    print(result["text"])

if __name__ == "__main__":
    test_refiner_agent()
