import requests
import sys

# Ensure UTF-8 output encoding for Windows terminals to print emojis
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8')

def create_github_issue():
    print("=====================================================")
    print("🚀 GSSoC '26 Multi-Project Issue Creator")
    print("=====================================================")
    print("Select the GSSoC project(s) you want to submit a proposal to:")
    print("1. DL-Simplified (Add your BERT Fake News and RAG PDF Notebooks)")
    print("2. SnapPass-AI (Add Python AI Auto Background Removal / Face Centering)")
    print("3. KisanAI (Add Multilingual Crop Chatbot / FAISS RAG Pipeline)")
    print("4. Career-pilot (Add AI Resume Parser / ATS Job Matcher)")
    print("5. StudyPlan (Add NLP Task & Deadline Extraction)")
    print("6. AgentAPI (Add Hugging Face LLM Client Integration)")
    print("7. Med-genie (Add Symptom Classifier & Medical RAG Pipeline)")
    print("8. AI Developer Assistant (Add Code Syntax Linter & LLM Refinement)")
    print("9. DoVER (Add Gemini-powered Document Auditing & Anomaly Engine)")
    print("=====================================================")
    print("*(You can select one choice like '1', or multiple separated by commas like '1,2,3,4')*")
    print("=====================================================")
    
    choice_input = input("Enter choice(s): ").strip()
    
    # Parse inputs (splits by comma and cleans spaces and quotes)
    cleaned_input = choice_input.replace("'", "").replace('"', "")
    selected_choices = [c.strip() for c in cleaned_input.split(",") if c.strip() in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]]
    
    if not selected_choices:
        print("❌ Invalid choice(s). Exiting.")
        return
        
    # Get token once
    print("\nTo post these issues, you need a GitHub Personal Access Token (PAT).")
    print("Create a temporary one here: https://github.com/settings/tokens")
    print("*(Select the 'repo' scope checkbox when creating).*")
    print("=====================================================")
    
    token = input("🔑 Paste your GitHub PAT (starts with ghp_): ").strip()
    if not token:
        print("❌ Error: Token cannot be empty.")
        return

    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }

    # Execute requests in a loop
    for choice in selected_choices:
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

        elif choice == "4":
            owner = "anurag3407"
            repo = "career-pilot"
            title = "[GSSoC '26] Feature: Implement PDF Resume Parser and ATS Job Matcher using Gemini API"
            body = """Hello Mentor (@anurag3407),

I would like to contribute to Career-pilot by building a PDF Resume Parser and ATS Job Matcher feature.

I propose to implement:
1. **PDF Text Extraction:** Parses uploaded candidate resume PDFs.
2. **ATS Scoring:** Matches extracted resume skills, experience, and keywords against a target job description.
3. **Optimized Suggestions:** Uses Gemini API/LLM prompts to generate specific resume improvements (e.g. missing keywords, formatting edits).

I have strong experience working with Python, LLMs, and RAG pipelines, and I have recently built a PDF AI Assistant project. I would love to work on this feature!

Please assign this issue to me under GSSoC '26. Thank you!"""

        elif choice == "5":
            owner = "Charushi06"
            repo = "StudyPlan"
            title = "[GSSoC '26] Feature: Add NLP Task & Deadline Extraction from Messy Input Texts"
            body = """Hello Mentor (@Charushi06),

I would like to contribute to StudyPlan by adding a smart NLP Task and Deadline Extraction engine.

This feature will:
1. Parse unstructured inputs (e.g., chat logs, messy assignment briefs, emails).
2. Extract calendar deadlines, subjects, and specific tasks using regular expressions combined with an NLP zero-shot classifier or LLM prompt wrapper.
3. Output a structured JSON payload to automatically sync with the database and frontend calendar.

I have strong experience working with Python and NLP libraries (Transformers, Spacy, NLTK) and would love to build this parser backend.

Please assign this issue to me under GSSoC '26. Thank you!"""

        elif choice == "6":
            owner = "prajwalsuryawanshi"
            repo = "AgentAPI"
            title = "[GSSoC '26] Feature: Add Hugging Face LLM Client Integration and Response Streaming"
            body = """Hello Mentor (@prajwalsuryawanshi),

I would like to contribute to AgentAPI by adding support for Hugging Face Inference Client integration and response streaming.

This feature will:
1. Allow the framework to natively connect to Hugging Face Hub inference endpoints for model loading.
2. Enable fast response streaming using FastAPI's `StreamingResponse` objects.
3. Provide simple wrapper classes for easily swapping model IDs (like Qwen, Mistral, Llama).

I have built similar Hugging Face LLM RAG pipelines and would love to contribute this developer feature to the project.

Please assign this issue to me under GSSoC '26. Thank you!"""

        elif choice == "7":
            owner = "aayushraj1010"
            repo = "med-genie"
            title = "[GSSoC '26] Proposal: Add Symptom Classification Model and Medical Handbook RAG Pipeline"
            body = """Hello Mentor (@aayushraj1010),

I would like to contribute a highly technical improvement to Med-genie under GSSoC '26.

I propose to implement two core modules:
1. **BERT-based Symptom Classifier:** A fine-tuned `distilbert-base-uncased` NLP model that takes a patient's raw text symptoms and classifies them into disease categories with high accuracy.
2. **Medical Handbook RAG Pipeline:** A Retrieval-Augmented Generation pipeline using `FAISS` and a local lightweight LLM (or Hugging Face API) to index medical Q&A handbooks, allowing users to query and receive factual, cited health tips.

Please assign this issue to me under GSSoC '26. Thank you!"""

        elif choice == "8":
            owner = "imDarshanGK"
            repo = "AI-dev-assistant"
            title = "[GSSoC '26] Proposal: Add Python Code Syntax Linter and LLM-powered Refinement Engine"
            body = """Hello Mentor (@imDarshanGK),

I would like to contribute a backend feature to AI Developer Assistant under GSSoC '26.

I propose to add a modular backend python service that:
1. **Linter & Syntax Analyzer:** Parses uploaded code strings using Python's `ast` (Abstract Syntax Trees) module and returns precise line-by-line linting errors and logical syntax warnings.
2. **LLM Refinement Generator:** Connects to an LLM client (e.g. Gemini API or Hugging Face Client) to generate instant, plain-English refactoring suggestions and bug-fix solutions based on the code analysis.

Please assign this issue to me under GSSoC '26. Thank you!"""

        elif choice == "9":
            owner = "yellowgram1543"
            repo = "DoVER"
            title = "[GSSoC '26] Proposal: Add Gemini-Powered Document Content Auditing and Semantic Anomaly Engine"
            body = """Hello Mentor (@yellowgram1543),

I would like to contribute an advanced auditing feature to DoVER under GSSoC '26.

I propose to build a Python-based **Security Intelligence** pipeline consisting of:
1. **Document Content Audit:** Leverages the Gemini API to analyze PDF/Text documents, auditing them for semantic discrepancies, logical errors, or formatting anomalies.
2. **Tamper & Anomaly Reports:** Generates a structured JSON audit report identifying potential text manipulation, verification status, and confidence scores to be saved securely.

Please assign this issue to me under GSSoC '26. Thank you!"""

        url = f"https://api.github.com/repos/{owner}/{repo}/issues"
        payload = {
            "title": title,
            "body": body
        }
        
        print(f"\nSending request to create issue on {owner}/{repo}...")
        try:
            response = requests.post(url, json=payload, headers=headers)
            if response.status_code == 201:
                issue_data = response.json()
                print(f"🎉 Success! Issue created on {owner}/{repo}.")
                print(f"🔗 View here: {issue_data.get('html_url')}")
            else:
                print(f"❌ Failed to create issue on {owner}/{repo}. Status code: {response.status_code}")
                print(f"Response: {response.text}")
        except Exception as e:
            print(f"❌ Error communicating with GitHub API for {owner}/{repo}: {e}")

if __name__ == "__main__":
    create_github_issue()
