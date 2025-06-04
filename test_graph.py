from graph import build_blog_graph
from agents import fetch_repo_files_from_github

def test_blog_pipeline():
    repo_url = "https://github.com/Keerthanareddy17/KJ-BOT"  
    files = fetch_repo_files_from_github(repo_url)

    app = build_blog_graph()
    final_state = app.invoke({
        "repo_url": repo_url,
        "files": files
    })

    print("\n FINAL BLOG OUTPUT:\n")
    print(final_state["final_blog"])

if __name__ == "__main__":
    test_blog_pipeline()
