# 📰 Fake News Detection for Indian News using Fine-Tuned BERT

This repository contains a complete, production-grade, and self-contained Google Colab notebook for building and training a **Fake News Detection System** optimized for the Indian media ecosystem.

The system uses Hugging Face's **DistilBERT** (`distilbert-base-uncased`) — a lightweight, fast, and highly efficient transformer model — fine-tuned on a programmatically generated, balanced dataset of Indian news headlines.

---

## 🌟 Key Features

1. **Synthetic Indian News Dataset**:
   - Programmatically generates **500 balanced headlines** (250 Real, 250 Fake).
   - Tailored specifically to Indian entities, including space research (**ISRO**), sports (**IPL/BCCI**), politics (**Modi**, **RBI**), business, and Bollywood.
   - Fake news samples incorporate common patterns such as WhatsApp forwards, clickbait, and internet hoaxes (e.g., UNESCO certifications, micro-chips in currency notes, home-remedy health claims).
2. **Exploratory Data Analysis (EDA)**:
   - Uses `matplotlib` and `seaborn` to plot the distribution of news headline lengths.
   - Generates comparative **WordClouds** for Real (Green) and Fake (Red) headlines using custom domain-specific stopword filtering.
3. **Fine-Tuning Pipeline**:
   - Custom PyTorch `Dataset` wrapper.
   - Fine-tuned using the Hugging Face `Trainer` API with learning rate scheduling, weight decay, and automatic saving of the best model.
4. **Comprehensive Evaluation & Diagnostics**:
   - Accuracy score and full classification report (Precision, Recall, F1-score).
   - Styled confusion matrix heatmap.
   - Plots **Training & Validation Loss curves** and **Validation Accuracy curves** over steps using HF Trainer log states.
5. **Real-world Custom Inference**:
   - A dedicated testing block with **10 handcrafted headlines** (5 real, 5 fake) demonstrating direct predictions.
6. **🎨 Interactive Web-Widget client**:
   - Embeds an **interactive GUI** inside Colab using `ipywidgets` and HTML. Users can type any news headline in real-time, click "Analyze Headline", and view color-coded probability confidence bars immediately.

---

## 🚀 How to Run in Google Colab

To run this project, you only need the `.ipynb` file in this repository:

1. **Download** the notebook file: [`Fake_News_Detection_Indian_News.ipynb`](Fake_News_Detection_Indian_News.ipynb).
2. **Open** [Google Colab](https://colab.research.google.com/).
3. **Upload** the notebook (`File > Upload notebook`).
4. **Change Runtime Type** to GPU for faster training:
   - Click `Runtime > Change runtime type` in the top menu.
   - Select **T4 GPU** (or any available GPU) under *Hardware accelerator*.
5. **Run all cells** sequentially (`Runtime > Run all`).

---

## 📊 Methodology

### 1. Dataset Generation & Preprocessing
The dataset is balanced containing 50% Real and 50% Fake news. Text is split 80% for training (400 headlines) and 20% for testing (100 headlines) using a stratified split to preserve label distributions.

### 2. Model Architecture
- **Base Model**: `distilbert-base-uncased` (6 layers, 768 hidden dimension, 12 attention heads, 66M parameters).
- **Classification Head**: Single linear layer mapping the pooled CLS token representation to 2 class logits (Real vs. Fake).

### 3. Hyperparameters
- **Epochs**: 3
- **Batch Size**: 16
- **Warmup Steps**: 50
- **Weight Decay**: 0.01
- **Optimizer**: AdamW (default in Trainer)

---

## 📁 Repository Structure

```text
├── Fake_News_Detection_Indian_News.ipynb   # Main Google Colab Jupyter Notebook
├── generate_notebook.py                    # Script used to generate the notebook programmatically
├── README.md                               # Project documentation
└── .gitignore                              # Git exclusion rules
```

---

## 🛠️ Local Setup (Optional)

If you wish to run the generator script locally or review the notebook, you can install the necessary dependencies:

```bash
pip install -r requirements.txt
```

*(Note: Dependencies inside the notebook are installed automatically using pip cells when executed in Colab).*

---

## 📜 License
This project is open-source and available under the [MIT License](LICENSE).
