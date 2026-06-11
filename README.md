# 📰 Fake News Detection for Indian News using Fine-Tuned BERT with Explainable AI (XAI)

[![Google Colab](https://img.shields.io/badge/Run%20in-Colab-orange?style=flat-square&logo=google-colab)](https://colab.research.google.com/)
[![Hugging Face](https://img.shields.io/badge/%F0%9F%A5%97-Hugging%20Face-yellow?style=flat-square)](https://huggingface.co/)
[![PyTorch](https://img.shields.io/badge/Framework-PyTorch-red?style=flat-square&logo=pytorch)](https://pytorch.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg?style=flat-square)](LICENSE)

An end-to-end, production-grade Natural Language Processing (NLP) pipeline that fine-tunes a pre-trained **DistilBERT** transformer model to classify Indian news headlines as **Real** or **Fake**. 

This repository features **Explainable AI (XAI)** capabilities by extracting and visualizing the model's self-attention weights to highlight the exact words that influenced the classification decision.

---

## 🗺️ System Architecture

```text
       [ Indian News Headline ]
                  │
                  ▼
      [ DistilBERT Tokenization ] (Max Length = 64)
                  │
                  ▼
    [ Fine-Tuned DistilBERT Model ] (Trained on T4 GPU)
         /                     \
        /                       \
       ▼                         ▼
 [ Logit Predictions ]     [ Self-Attention Weights ] (Last Layer)
       │                         │
       ▼ (Softmax)               ▼ (Mean across Heads)
 [ Probabilities ]         [ CLS-to-Token Weights ]
       │                         │
       ▼                         ▼ (Min-Max Normalized)
 [ Real vs Fake Class ] ──► [ HTML Attention Highlighter ]
                  │
                  ▼
      [ Interactive UI Result Card ]
```

---

## 📸 Notebook Interface Preview

Here is a visual preview of the Google Colab Notebook interface and execution outputs:

![Fake News Detector Colab Preview](screenshots/preview.png)

---

## 🌟 Key Features

1. **Self-Attention Explainability (XAI)**:
   - Extracts self-attention matrices from the final layer of the transformer model.
   - Calculates the average attention allocated by the `[CLS]` token to all other tokens.
   - Dynamically highlights words in **Red (for Fake)** or **Green (for Real)** with opacity matching their relative attention scores, showing exactly *why* the model made its choice.
2. **Interactive Jupyter Widget Client**:
   - Embeds a clean, styled HTML/CSS GUI dashboard inside Google Colab using `ipywidgets`.
   - Allows users to enter headlines and view real-time confidence scores and attention highlights instantly.
3. **Synthetic Dataset Engineering**:
   - Programmatically generates **700 balanced headlines** (350 Real, 350 Fake).
   - Covers Indian contexts: space (**ISRO**), banking (**RBI**), sports (**IPL/BCCI**), politics, and Bollywood.
   - Mimics typical clickbaits and WhatsApp hoaxes (e.g., GPS note microchips, fake UNESCO announcements).
4. **Data Analytics & EDA**:
   - Renders side-by-side vocabulary **WordClouds** (Green for Real, Red for Fake) with custom stopword filters.
   - Plots sentence length distributions using `Seaborn`.
5. **Hugging Face Fine-Tuning Pipeline**:
   - Built on PyTorch custom `Dataset` loaders and Hugging Face's `Trainer` API.
   - Implements learning rate scheduling, warmup steps, and checkpoint saving.
6. **Robust Metrics Dashboard**:
   - Plots training/validation loss curves.
   - Renders a clean Seaborn heatmap confusion matrix.
   - Outputs complete metrics reports (Precision, Recall, F1-Score, and Accuracy).

---

## 🚀 How to Run in Google Colab

1. **Download** the notebook: [`Fake_News_Detection_Indian_News.ipynb`](Fake_News_Detection_Indian_News.ipynb).
2. **Open** [Google Colab](https://colab.research.google.com/).
3. **Upload** the notebook (`File > Upload notebook`).
4. **Enable GPU Acceleration**:
   - Go to `Runtime > Change runtime type` in the top menu.
   - Select **T4 GPU** under *Hardware accelerator* and click **Save**.
5. **Run all cells** sequentially (`Runtime > Run all` or `Ctrl + F9`).

---

## 📊 Model Training & Hyperparameters

The model is fine-tuned on the synthetic Indian news dataset with the following parameters:

| Hyperparameter | Value | Description |
| :--- | :--- | :--- |
| **Base Model** | `distilbert-base-uncased` | Lightweight BERT model (66M parameters) |
| **Epochs** | 3 | Full passes over the training dataset |
| **Batch Size** | 16 | Training & Evaluation batch size |
| **Learning Rate** | Default AdamW | Managed by Hugging Face Trainer |
| **Warmup Steps** | 50 | Steps to increase learning rate gradually |
| **Weight Decay** | 0.01 | L2 regularization rate to prevent overfitting |
| **Validation Split** | 20% (Stratified) | Evaluates performance on unseen dataset |

---

## 📁 Repository Directory Structure

```text
├── Fake_News_Detection_Indian_News.ipynb  # Primary Google Colab Jupyter Notebook
├── generate_notebook.py                   # Script used to compile the notebook JSON
├── app.py                                 # Local Flask application for web hosting
├── templates/
│   └── index.html                         # Premium Flask web UI templates
├── resume_content.md                      # Resume bullet points for portfolio highlight
├── README.md                              # Repository documentation
└── .gitignore                             # Git exclusion rules
```

---

## 💻 Running Locally (Optional Flask App)

If you want to view the detector inside your local web browser:

1. **Install requirements**:
   ```bash
   pip install flask transformers torch
   ```
2. **Start the Flask server**:
   ```bash
   python app.py
   ```
3. Open **`http://localhost:5000`** in Chrome to interact with the web app UI!

---

## 📜 License
This project is open-source and licensed under the [MIT License](LICENSE).
