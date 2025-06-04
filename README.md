# ghBlogger 🧠→📖: Automated Blog Generator for GitHub Repositories

Ever wished your GitHub repositories could write their own blog posts? 

With **ghBlogger**, they can! 

This agentic system automatically generates high-quality technical blog posts by analyzing your GitHub repositories. Perfect for developers who want to document their projects without the hassle of writing from scratch.

## 🌟 Overview

ghBlogger is an **agentic system** built with LangGraph and LangChain that:

1. Fetches your repository files from GitHub
2. Analyzes the codebase structure and purpose
3. Generates a comprehensive technical blog post
4. Reviews and refines the content for quality

The system uses four specialized AI agents working in a pipeline to ensure high-quality output.

---

## 🎯 Use Cases

- Quickly generate documentation for your projects
- Create technical blog posts showcasing your work
- Automate project documentation for your team
- Save hours of writing time while maintaining quality content

---

## 🏗️ Built Using - 

This whole system is built using:
- **LangGraph**: To orchestrate the agent workflow
- **LangChain**: For the core agent logic and LLM interactions
- **GitHub Token**: For accessing the repositories and fecthing the code files.
- **Groq API**: For ultra-fast LLM inference using LLaMA 3
- **Streamlit**: For the user-friendly web interface

---

## 📂 File Structure

Here's what each file in the repository does:

- `agents.py`: Contains the four core agents (ingestor, writer, reviewer, refiner) and GitHub file fetcher
- `app.py`: Streamlit web interface for user interaction
- `github_utils.py`: Helper functions for GitHub API interactions
- `graph.py`: LangGraph workflow definition and state management
- `prompts.py`: Contains all the LLM prompts used by the agents
- `requirements.txt`: Project dependencies

---

## 🛠️ Requirements

Before you begin, ensure you have:
- Python 3.9+
- A GitHub account (for repository access)
- API keys for:
  - Groq (free tier available)
  - GitHub (personal access token)
 
---

## 🔑 Getting API Keys

1. **Groq API**:
   - Sign up at [console.groq.com](https://console.groq.com/)
   - Create an API key in the dashboard
   - Add to `.env` as `GROQ_API_KEY=your_key_here`

2. **GitHub Token**:
   - Go to GitHub Settings → Developer settings → Personal access tokens
   - Create a token with `repo` scope
   - Add to `.env` as `GITHUB_TOKEN=your_token_here`
  
---

## 🚀 Local Setup
 Clone the repository into your desired location you using :
 ```
git clone https://github.com/Keerthanareddy17/ghBlogger.git
```

Follow these steps to run ghBlogger locally:

1. **Create virtual environment**:
   
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   ```
2. **Install dependencies**:
   ```
   pip install -r requirements.txt
   ```
3. **Create .env file**:
   ```
   touch .env
   ```
   Add your API keys as mentioned previously!
4. **Run the app**:
   ```
   streamlit run app.py
   ```
---

## 🤖 Agentic System Flow

Here's how the magic happens:

**Fetch Phase**:
  - User provides GitHub repo URL
  - System fetches all code files using GitHub API
    
**Ingest Phase**:
  - Ingestor agent analyzes files and creates structured summary
    
**Write Phase**:
  - Writer agent converts summary into complete blog draft
    
**Review Phase**:
  - Reviewer agent provides constructive feedback
    
**Refine Phase**:
  - Refiner agent improves the blog based on suggestions
    
**Output**:
  - Final polished blog is displayed and available for download :)


<img width="227" alt="Screenshot 2025-06-04 at 12 08 20" src="https://github.com/user-attachments/assets/695153ad-b14b-4971-ba73-7b11b9db0162" />

---

## 💡 Pro Tips

- For private repos, ensure your GitHub token has proper access
- The system works best with well-structured repositories
- You can customize the prompts in `prompts.py` for different writing styles and lengths!

---

📬 Let's Connect!

Loved ghBlogger? Hate it? Want to improve it? I'd love to hear from you!

- Open an issue for bugs or feature requests
- Star the repo if you find it useful
- Connect with me on [LinkedIn](https://www.linkedin.com/in/keerthana-reddy-katasani-b07238268/)
- Mail me at katasanikeerthanareddy@gmail.com
  
Happy blogging! 🚀

---
## Quick Snapshots of ghBlogger - 

<img width="1709" alt="Screenshot 2025-06-04 at 11 02 33" src="https://github.com/user-attachments/assets/96c268cc-c19c-48a6-93cc-7439e932d89a" />

<img width="1710" alt="Screenshot 2025-06-04 at 11 02 47" src="https://github.com/user-attachments/assets/5545d705-fa81-4a6d-acb7-f39c37182612" />

<img width="1710" alt="Screenshot 2025-06-04 at 11 03 58" src="https://github.com/user-attachments/assets/f90ec8ca-fd82-434f-8b20-593d88b4fe3e" />


 
