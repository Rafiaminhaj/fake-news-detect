import requests
import sys

def create_github_issue():
    # Target Repository
    repo_owner = "abhisheks008"
    repo_name = "DL-Simplified"
    
    print("=====================================================")
    print("🚀 GSSoC '26 Issue Creator Automation Script")
    print("=====================================================")
    print("To post an issue, you need a GitHub Personal Access Token (PAT).")
    print("Create a temporary one here: https://github.com/settings/tokens")
    print("*(Select the 'repo' scope checkbox when creating).*")
    print("=====================================================")
    
    token = input("🔑 Paste your GitHub PAT (starts with ghp_): ").strip()
    if not token:
        print("❌ Error: Token cannot be empty.")
        return
        
    title = "[GSSoC '26] Proposal: Add Fine-Tuned DistilBERT Classifier and PDF AI RAG Chatbot Notebooks"
    
    body = """Hello Mentor (@abhisheks008),

I would like to contribute two completed, portfolio-ready deep learning projects as Jupyter Notebooks (.ipynb) to this repository under GSSoC '26. 

Here are the details of the projects I have fully built and tested on Google Colab T4 GPU:

1. **Fake News Detection for Indian News using Fine-Tuned DistilBERT with XAI**
   - Fine-tunes a pre-trained `distilbert-base-uncased` model using PyTorch and Hugging Face Trainer.
   - Includes **Explainable AI (XAI)** self-attention visualization to highlight exactly which words the model focused on (Real/Fake).
   - Features an interactive HTML GUI widget inside Colab using `ipywidgets`.
   - Repo: https://github.com/Rafiaminhaj/fake-news-detect

2. **PDF AI Assistant & Chatbot (RAG System)**
   - Implements a local Retrieval-Augmented Generation (RAG) pipeline.
   - Uses `all-MiniLM-L6-v2` embeddings, `FAISS` vector database, and local quantized `Qwen/Qwen2.5-1.5B-Instruct` model for hallucination-free generation.
   - Includes a custom interactive chat interface showing answers alongside source reference page chunks.
   - Repo: https://github.com/Rafiaminhaj/-pdf-ai-assistant

Please assign this issue to me so I can raise a Pull Request (PR) and contribute these notebooks. Thank you!"""

    url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/issues"
    
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    
    payload = {
        "title": title,
        "body": body,
        "labels": ["gssoc", "enhancement"]
    }
    
    print(f"\nSending request to create issue on {repo_owner}/{repo_name}...")
    try:
        response = requests.post(url, json=payload, headers=headers)
        if response.status_code == 201:
            issue_data = response.json()
            print("\n🎉 Success! Issue created successfully.")
            print(f"🔗 View your issue here: {issue_data.get('html_url')}")
        else:
            print(f"\n❌ Failed to create issue. Status code: {response.status_code}")
            print(f"Response details: {response.text}")
    except Exception as e:
        print(f"❌ Error communicating with GitHub API: {e}")

if __name__ == "__main__":
    create_github_issue()
