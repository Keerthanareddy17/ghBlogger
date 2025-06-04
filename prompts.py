INGEST_PROMPT = """
You are a codebase analyst.

Given the following list of source code files from a GitHub repository, analyze their purpose, architecture, and key components.

Each file is listed as:
<filename>
<content>

Files:
{input}

Provide a structured and concise summary including:
- Project purpose
- Technologies used
- Core components and logic
- Any observed patterns, libraries, or workflows
- Additional notes
"""


WRITER_PROMPT = """
You are a technical blog writer.

Using the following summary of a GitHub project, write a complete and well-structured technical blog post. Keep it desciptive enough but not boring. Your blog should include:

- A catchy title
- An engaging introduction
- Project overview (goals, features, architecture)
- Technologies used
- Key functionalities
- Development process or workflow (if clear)
- Final thoughts or future scope

### GitHub Project Summary:
{summary}

Write the blog in markdown format with proper sections and headers.
"""


REVIEWER_PROMPT = """
You are a professional technical blog editor.

Given the following blog post, review the writing and suggest specific, actionable improvements in the following areas:
- Tone and clarity
- Grammar and flow
- Technical accuracy
- Organization and formatting

Your output should be a markdown list of suggestions. Be objective and helpful.

### Blog Post:
{blog}
"""


REFINER_PROMPT = """
You are a professional technical content writer.

Below is a blog post and a list of review suggestions. Use the suggestions to refine and improve the blog.
Do not include the suggestions themselves in the final output — only return the improved blog in markdown format.

## Original Blog Post:
{blog}

## Suggestions to Apply:
{suggestions}
"""
