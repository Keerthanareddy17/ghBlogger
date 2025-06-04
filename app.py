import streamlit as st
from agents import fetch_repo_files_from_github
from graph import app

st.set_page_config(page_title="ghBlogger 🧠→📖", layout="wide")

st.markdown("""
    <style>
    .big-font {
        font-size: 22px;
        font-weight: 500;
    }
    .title-font {
        font-size: 28px;
        font-weight: 700;
        color: #4A90E2;
    }
    .summary-box {
        padding: 1rem;
        margin-bottom: 1.5rem;
    }
    .final-blog-box {
        padding: 0;
        margin-bottom: 1.5rem;
    }
    .repo-box {
        padding: 0.25rem 0;
        margin-bottom: 0.25rem;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("<div class='title-font'>ghBlogger 🧠 → 📖</div>", unsafe_allow_html=True)
st.markdown(
    """
    <div class='big-font'>
    Automate blog generation for your GitHub repositories with just one click!  
    ghBlogger fetches your codebase, understands its structure, and writes beautiful, readable blog articles — saving you hours of effort.
    </div>
    """, unsafe_allow_html=True
)

st.markdown("---")

repo_url = st.text_input("🔗 Enter GitHub Repository URL:")

fetch_btn_col = st.columns([3, 1, 3])[1]
with fetch_btn_col:
    if st.button("📂 Fetch Repository Files"):
        with st.spinner("🔄 Fetching files from GitHub..."):
            files = fetch_repo_files_from_github(repo_url)
            if files and not files[0].get("error"):
                st.session_state["files"] = files
                st.success(f"✅ Successfully fetched {len(files)} files!")
            else:
                st.error(f"❌ Failed to fetch files: {files[0].get('error', 'Unknown error')}")

if "files" in st.session_state:
    with st.expander("📄 Preview Fetched Files", expanded=False):
        for file in st.session_state["files"]:
            st.markdown(f"<div class='repo-box'><strong>{file['path']}</strong></div>", unsafe_allow_html=True)
            content_preview = file["content"][:500] + "..." if len(file["content"]) > 500 else file["content"]
            st.code(content_preview)

if "files" in st.session_state:
    st.markdown("### 🛠️ Ready to generate your blog?")

    gen_btn_col = st.columns([3, 1, 3])[1]
    generate_clicked = gen_btn_col.button("🧠 Generate Blog with LangGraph")

    if generate_clicked:
        with st.spinner("⏳ Running the LangGraph pipeline..."):
            try:
                final_output = app.invoke({"files": st.session_state["files"]})
                st.session_state["langgraph_output"] = final_output
                st.success("🎉 Blog generated successfully!")

                st.subheader("📑 Project Summary")
                with st.expander("🔍 View Summary"):
                    st.markdown(
                        f"<div class='summary-box'>{final_output.get('summary', 'No summary generated.')}</div>",
                        unsafe_allow_html=True
                    )

                st.subheader("📖 Final Blog Post")
                st.markdown(
                    f"<div class='final-blog-box'>{final_output.get('final_blog', 'No blog generated.')}</div>",
                    unsafe_allow_html=True
                )

                blog_text = final_output.get("final_blog", "")
                if blog_text:
                    st.download_button(
                        label="📥 Download Blog as .txt",
                        data=blog_text,
                        file_name="ghBlogger_blog.txt",
                        mime="text/plain"
                    )

            except Exception as e:
                st.error(f"⚠️ Error running blog generation: {e}")
