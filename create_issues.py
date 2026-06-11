import requests
import sys

def create_github_issue():
    print("=====================================================")
    print("🚀 GSSoC '26 Multi-Project Issue Creator")
    print("=====================================================")
    print("Select the GSSoC project you want to submit a proposal to:")
    print("1. DL-Simplified (Add your BERT Fake News and RAG PDF Notebooks)")
    print("2. SnapPass-AI (Add Python AI Auto Background Removal / Face Centering)")
    print("3. KisanAI (Add Multilingual Crop Chatbot / FAISS RAG Pipeline)")
    print("=====================================================")
    
    choice = input("Enter choice (1, 2, or 3): ").strip()
    
    if choice == "1":
        owner = "abhisheks008"
        repo = "DL-Simplified"
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
        labels = ["gssoc", "enhancement"]
        
    elif choice == "2":
        owner = "souma9830"
        repo = "SnapPass-AI"
        title = "[GSSoC '26] Feature: Add Automated Background Removal and Face Centering Python Pipeline"
        body = """Hello Mentor (@souma9830),

I would like to contribute to SnapPass-AI by implementing a robust Python AI pipeline for:
1. **Automated Background Removal** using pre-trained deep learning segmentation models.
2. **Auto Face Centering and Alignment** to ensure correct passport and ID dimensions.

I have strong experience working with Python, PyTorch, OpenCV, and deep learning pipelines. I would love to build this modular backend feature so it can be integrated with the Express API.

Please assign this issue to me under GSSoC '26. Thank you!"""
        labels = ["gssoc", "feature"]
        
    elif choice == "3":
        owner = "asheesh109"
        repo = "KisanAI"
        title = "[GSSoC '26] Feature: Add Multilingual AI Crop Assistant Chatbot using RAG and FAISS"
        body = """Hello Mentor (@asheesh109),

I would like to contribute to KisanAI by implementing a multilingual agricultural Q&A assistant chatbot. 

I propose to use a **RAG (Retrieval-Augmented Generation)** pipeline that:
1. Indexes government agricultural handbooks, schemes, or disease guides in a local `FAISS` Vector database using sentence embeddings.
2. Uses a quantized open-source LLM (like Qwen or Llama) to retrieve context and answer farmer queries accurately without hallucinations.
3. Supports a user-friendly conversational interface showing source documents as references.

I have built a similar fully-functioning RAG Chatbot on Colab with T4 GPU and would love to integrate this feature into KisanAI.

Please assign this issue to me under GSSoC '26. Thank you!"""
        labels = ["gssoc", "feature"]
        
    else:
        print("❌ Invalid choice. Exiting.")
        return

    print("\nTo post this issue, you need a GitHub Personal Access Token (PAT).")
    print("Create a temporary one here: https://github.com/settings/tokens")
    print("*(Select the 'repo' scope checkbox when creating).*")
    print("=====================================================")
    
    token = input("🔑 Paste your GitHub PAT (starts with ghp_): ").strip()
    if not token:
        print("❌ Error: Token cannot be empty.")
        return
        
    url = f"https://api.github.com/repos/{owner}/{repo}/issues"
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    payload = {
        "title": title,
        "body": body,
        "labels": labels
    }
    
    print(f"\nSending request to create issue on {owner}/{repo}...")
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
