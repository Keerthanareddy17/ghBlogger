import requests
import os
from dotenv import load_dotenv

load_dotenv()
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
print("TOKEN LOADED:", GITHUB_TOKEN[:6], "..." if GITHUB_TOKEN else "NOT FOUND")

HEADERS = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}

def parse_github_url(repo_url):
    """Extract owner and repo name from GitHub URL"""
    parts = repo_url.strip().rstrip('/').split('/')
    return parts[-2], parts[-1]  # owner, repo

def fetch_repo_files(repo_url, file_extensions=('.py', '.ipynb', '.md'), max_files=15):
    """Fetch relevant files (by extension) and return their contents"""
    owner, repo = parse_github_url(repo_url)
    api_url = f"https://api.github.com/repos/{owner}/{repo}/contents"

    relevant_files = []

    def _fetch_dir_contents(url):
        response = requests.get(url, headers=HEADERS)
        if response.status_code != 200:
            print(f"Failed to fetch {url}")
            return
        for item in response.json():
            if item['type'] == 'file' and item['name'].endswith(file_extensions):
                relevant_files.append(item['download_url'])
                if len(relevant_files) >= max_files:
                    return
            elif item['type'] == 'dir':
                _fetch_dir_contents(item['url'])
                if len(relevant_files) >= max_files:
                    return

    _fetch_dir_contents(api_url)

    file_contents = []
    for file_url in relevant_files:
        content = requests.get(file_url).text
        file_contents.append({"filename": file_url.split('/')[-1], "content": content})

    return file_contents
