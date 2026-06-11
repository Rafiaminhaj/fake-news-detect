import json
import os

# Define the notebook structure
notebook = {
    "cells": [],
    "metadata": {
        "kernelspec": {
            "display_name": "Python 3",
            "language": "python",
            "name": "python3"
        },
        "language_info": {
            "name": "python"
        }
    },
    "nbformat": 4,
    "nbformat_minor": 0
}

def add_markdown(source):
    # source is a list of strings (lines)
    notebook["cells"].append({
        "cell_type": "markdown",
        "metadata": {},
        "source": [line + "\n" for line in source]
    })

def add_code(source):
    # source is a list of strings (lines)
    notebook["cells"].append({
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": [line + "\n" for line in source]
    })

# --- CELL 1: TITLE & DOCUMENTATION ---
add_markdown([
    "# 📰 Fake News Detection System for Indian News",
    "### Fine-Tuning BERT (DistilBERT) for Sequence Classification",
    "",
    "This notebook provides a complete walk-through of a sequence classification project. We will fine-tune a pre-trained HuggingFace `distilbert-base-uncased` transformer model to distinguish between **Real** and **Fake** news headlines targeting the Indian ecosystem.",
    "",
    "#### Portfolio Highlights:",
    "1. **Synthetic Indian News Dataset**: 500 headlines covering space (ISRO), politics, economics, sports (Cricket), and Bollywood, generated using clean templates to maintain balance (250 Real vs. 250 Fake).",
    "2. **NLP Text Preprocessing & EDA**: Tokenization, stopword cleaning, sentence length analysis, and visual WordClouds.",
    "3. **HuggingFace Fine-Tuning**: Setting up PyTorch custom datasets and fine-tuning DistilBERT using the HuggingFace `Trainer` API.",
    "4. **Visual Performance Reporting**: Metrics reporting and confusion matrix heatmap plotting.",
    "5. **Custom Headline Inference**: Testing on 10 realistic Indian news headlines to verify inference results.",
    "",
    "Let's get started!"
])

# --- CELL 2: INSTALLATION ---
add_markdown([
    "## 🛠️ Step 1: Install Required Packages",
    "First, we install HuggingFace's `transformers` and library dependencies: `datasets`, `evaluate`, `accelerate` (for optimization), `wordcloud` (for EDA), and `scikit-learn`."
])
add_code([
    "# Install dependencies silently",
    "!pip install -q transformers datasets evaluate accelerate wordcloud scikit-learn seaborn matplotlib"
])

# --- CELL 3: IMPORTS ---
add_markdown([
    "## 📦 Step 2: Import Libraries and Set Seed",
    "We import standard packages for data manipulation, visualization, PyTorch, and HuggingFace wrappers. We set random seeds to ensure consistent runs."
])
add_code([
    "import os",
    "import random",
    "import re",
    "import numpy as np",
    "import pandas as pd",
    "import matplotlib.pyplot as plt",
    "import seaborn as sns",
    "from sklearn.model_selection import train_test_split",
    "from sklearn.metrics import accuracy_score, classification_report, confusion_matrix",
    "from wordcloud import WordCloud, STOPWORDS",
    "",
    "import torch",
    "from torch.utils.data import Dataset",
    "from transformers import DistilBertTokenizerFast, DistilBertForSequenceClassification",
    "from transformers import Trainer, TrainingArguments",
    "",
    "# Set seeds for reproducibility",
    "def set_seed(seed=42):",
    "    random.seed(seed)",
    "    np.random.seed(seed)",
    "    torch.manual_seed(seed)",
    "    if torch.cuda.is_available():",
    "        torch.cuda.manual_seed_all(seed)",
    "",
    "set_seed(42)",
    "print(f\"Using device: {'cuda' if torch.cuda.is_available() else 'cpu'}\")"
])

# --- CELL 4: DATASET INTRO ---
add_markdown([
    "## 📝 Step 3: Dataset Generation",
    "Since public Indian fake news datasets are often sparse or unbalanced, we generate **500 unique synthetic headlines** (250 Real, 250 Fake) using context-specific templates covering space research (ISRO), finance (RBI), sports (BCCI/IPL), and Bollywood stars."
])

# --- CELL 5: DATASET CODE ---
add_code([
    "# Lists of entity variations to insert into templates",
    "satellites = ['EOS-07', 'Aditya-L1', 'INSAT-3DS', 'Cartosat-3', 'GSAT-20', 'Gaganyaan TV', 'NVS-01', 'Oceansat-3']",
    "infrastructures = ['metro rail bypass', 'highway link road', 'solar power grid', 'AI research park', 'hydroelectric dam', 'bullet train corridor']",
    "cities = ['Bengaluru', 'Mumbai', 'New Delhi', 'Chennai', 'Hyderabad', 'Kolkata', 'Ahmedabad', 'Pune']",
    "percentages = ['6.8', '7.2', '7.5', '8.1', '6.5', '7.0', '7.4', '8.3']",
    "tournaments = ['T20 World Cup', 'ODI Series', 'Asia Cup', 'Test Championship', 'IPL tournament']",
    "countries = ['Australia', 'England', 'South Africa', 'New Zealand', 'Sri Lanka', 'Bangladesh', 'West Indies']",
    "amounts = ['150', '280', '420', '500', '750', '1200']",
    "court_topics = ['digital privacy rights', 'environmental rules', 'labor wage laws', 'consumer protection standards']",
    "industries = ['fintech applications', 'electric vehicles', 'smartphone assembly', 'solar panel grids', 'software services']",
    "years = ['2026', '2027']",
    "",
    "# Fake variations",
    "fake_discoveries = ['ancient Sanskrit scripts', 'massive gold veins', 'alien relics', 'immortality roots', 'fossilized space monkeys']",
    "fake_foods = ['raw garlic mixed with honey', 'boiled banana skins', 'turmeric tea with salt', 'crushed papaya seeds', 'argemone seed extracts']",
    "fake_disasters = ['a sudden polarity shift', 'an asteroid impact', 'a 9.8 magnitude earthquake', 'a massive space storm', 'a three-day grid failure']",
    "fake_bans = ['all mobile web services', 'driving private diesel vehicles', 'using foreign email tools', 'all cash transactions', 'working over 5 hours']",
    "denominations = ['200', '500', '2000']",
    "clean_cities = ['Indore', 'Surat', 'Navi Mumbai', 'Mysuru']",
    "stars = ['Shah Rukh Khan', 'Salman Khan', 'Deepika Padukone', 'Ranbir Kapoor', 'Alia Bhatt']",
    "",
    "# Real templates",
    "real_templates = [",
    "    'ISRO successfully launches {satellite} satellite from Sriharikota spaceport',",
    "    'Prime Minister Modi inaugurates new {infrastructure} in {city}',",
    "    'Indian GDP grew by {pct}% in the last quarter: RBI official reports',",
    "    'India wins {tournament} cricket match against {country} in {city}',",
    "    'Government announces new subsidies for electric vehicles to boost clean energy',",
    "    'Startups in {city} raise record funding of ${amount} million in {year}',",
    "    'Supreme Court delivers landmark judgment protecting {court_topic}',",
    "    'Diwali celebrations begin across India with vibrant lights and displays',",
    "    'IPL {year} starts with spectacular opening ceremony in {city} stadium',",
    "    'India becomes the third-largest market for {industry} globally',",
    "    'BCCI announces new annual contract rankings for Indian cricket players',",
    "    'Metro rail lines expanded in {city} to ease daily traffic congestions',",
    "    'Indian software export revenue hits new record of ${amount} billion this fiscal',",
    "    'Government partners with private sector to deploy {infrastructure} in {city}',",
    "    'RBI leaves interest rates unchanged at {pct}% to manage price inflation',",
    "    'Tata Motors rolls out its newest budget EV with {pct} km range',",
    "    'International Yoga Day celebrated across India with mass participation in New Delhi',",
    "    'Tech giants in {city} set up massive new data facilities',",
    "    'President of India confers National Art Awards in New Delhi ceremony',",
    "    'India successfully tests new defense missile shield system in Odisha coast'",
    "]",
    "",
    "# Fake templates",
    "fake_templates = [",
    "    'Breaking: Indian scientists discover {fake_discovery} on Mars surface',",
    "    'UNESCO declares Indian national anthem as the most peaceful anthem in the world',",
    "    'RBI announces free Rs {amount} cash reward for all account holders under new welfare scheme',",
    "    'Shocking: Eating {fake_food} instantly cures COVID-19 and high sugar levels',",
    "    'NASA warns that India will face {fake_disaster} starting next week',",
    "    'Prime Minister Modi announces complete ban on {fake_ban} from midnight',",
    "    'Alien spaceship spotted hovering behind Taj Mahal in Agra, viral video claims',",
    "    '{star} arrested in Mumbai for funding secret underground space program',",
    "    'Alert: GPS microchips embedded in new Rs {denomination} notes can track location',",
    "    'UNESCO names {clean_city} as the cleanest city in the entire universe',",
    "    'Breaking: RBI to cancel all bank accounts not linked to Aadhar by midnight',",
    "    'Warning: WhatsApp will start charging Rs 5 per message from tomorrow morning',",
    "    'WHO states that India has eradicated diabetes completely overnight with new herbal syrup',",
    "    'Archaeologists discover hidden {fake_discovery} buried directly under Taj Mahal',",
    "    'Viral: Video shows flying dragon over Himalayas in Ladakh border post',",
    "    'RBI to completely replace paper currency with smart plastic banknotes by {year}',",
    "    'Shocking: Drinking {fake_food} grants complete immunity from all flu viruses',",
    "    'Alert: Central Government bans the use of {fake_ban} nationwide',",
    "    'Shocking: {star} secretly quits films to join a Mars colonization crew',",
    "    'Viral: NASA satellite image shows India glowing brighter than rest of Asia on Diwali'",
    "]",
    "",
    "# Generate headlines unique set",
    "real_headlines = set()",
    "while len(real_headlines) < 250:",
    "    temp = random.choice(real_templates)",
    "    headline = temp.format(",
    "        satellite=random.choice(satellites),",
    "        infrastructure=random.choice(infrastructures),",
    "        city=random.choice(cities),",
    "        pct=random.choice(percentages),",
    "        tournament=random.choice(tournaments),",
    "        country=random.choice(countries),",
    "        amount=random.choice(amounts),",
    "        court_topic=random.choice(court_topics),",
    "        industry=random.choice(industries),",
    "        year=random.choice(years)",
    "    )",
    "    real_headlines.add(headline)",
    "",
    "fake_headlines = set()",
    "while len(fake_headlines) < 250:",
    "    temp = random.choice(fake_templates)",
    "    headline = temp.format(",
    "        fake_discovery=random.choice(fake_discoveries),",
    "        amount=random.choice(amounts),",
    "        fake_food=random.choice(fake_foods),",
    "        fake_disaster=random.choice(fake_disasters),",
    "        fake_ban=random.choice(fake_bans),",
    "        star=random.choice(stars),",
    "        denomination=random.choice(denominations),",
    "        clean_city=random.choice(clean_cities),",
    "        year=random.choice(years)",
    "    )",
    "    fake_headlines.add(headline)",
    "",
    "# Create DataFrame",
    "data_list = []",
    "for h in real_headlines:",
    "    data_list.append({'headline': h, 'label': 0, 'label_name': 'Real'})",
    "for h in fake_headlines:",
    "    data_list.append({'headline': h, 'label': 1, 'label_name': 'Fake'})",
    "",
    "df = pd.DataFrame(data_list)",
    "# Shuffle the dataset",
    "df = df.sample(frac=1, random_state=42).reset_index(drop=True)",
    "df.to_csv('indian_news_dataset.csv', index=False)",
    "print(f\"Generated {len(df)} total news records successfully!\")",
    "print(df.head(10))"
])

# --- CELL 6: EDA INTRO ---
add_markdown([
    "## 📊 Step 4: Exploratory Data Analysis & Text Preprocessing",
    "Let's visualize the vocabulary difference between real and fake news using WordClouds. We clean up punctuation, lowercase the text, and remove stopwords specific to this dataset."
])

# --- CELL 7: EDA CODE ---
add_code([
    "# Stopwords setup",
    "custom_stopwords = set(STOPWORDS)",
    "# Add context filler words that do not carry classification weight",
    "custom_stopwords.update(['rs', 'crore', 'lakh', 'video', 'shows', 'viral', 'breaking', 'alert', 'shocking'])",
    "",
    "real_text = ' '.join(df[df['label'] == 0]['headline'].str.lower())",
    "fake_text = ' '.join(df[df['label'] == 1]['headline'].str.lower())",
    "",
    "# Build clouds",
    "real_wc = WordCloud(width=800, height=400, background_color='white', stopwords=custom_stopwords, colormap='Greens').generate(real_text)",
    "fake_wc = WordCloud(width=800, height=400, background_color='black', stopwords=custom_stopwords, colormap='Reds').generate(fake_text)",
    "",
    "# Plot WordClouds side by side",
    "fig, axes = plt.subplots(1, 2, figsize=(16, 8))",
    "axes[0].imshow(real_wc, interpolation='bilinear')",
    "axes[0].set_title('Top Words in Real Indian News (Green)', fontsize=16, color='green')",
    "axes[0].axis('off')",
    "",
    "axes[1].imshow(fake_wc, interpolation='bilinear')",
    "axes[1].set_title('Top Words in Fake Indian News (Red)', fontsize=16, color='red')",
    "axes[1].axis('off')",
    "plt.tight_layout()",
    "plt.show()",
    "",
    "# Plot word lengths distribution",
    "df['word_count'] = df['headline'].apply(lambda x: len(x.split()))",
    "plt.figure(figsize=(10, 5))",
    "sns.histplot(data=df, x='word_count', hue='label_name', kde=True, bins=15, palette={'Real': 'green', 'Fake': 'red'})",
    "plt.title('Distribution of News Headline Lengths')",
    "plt.xlabel('Number of Words')",
    "plt.ylabel('Density')",
    "plt.show()"
])

# --- CELL 8: TOKENIZATION INTRO ---
add_markdown([
    "## 🔠 Step 5: Dataset Split & Tokenization",
    "We split the headlines into an **80% training set** and a **20% testing validation set**, ensuring stratified splits. We then use Hugging Face's `DistilBertTokenizerFast` to tokenize the text sequences to fit DistilBERT's expected formats."
])

# --- CELL 9: TOKENIZATION CODE ---
add_code([
    "# Train-test split (80-20)",
    "train_texts, val_texts, train_labels, val_labels = train_test_split(",
    "    df['headline'].tolist(),",
    "    df['label'].tolist(),",
    "    test_size=0.2,",
    "    random_state=42,",
    "    stratify=df['label'].tolist()",
    ")",
    "",
    "# Instantiate pre-trained DistilBERT tokenizer",
    "tokenizer = DistilBertTokenizerFast.from_pretrained('distilbert-base-uncased')",
    "",
    "# Tokenize lists of text strings",
    "train_encodings = tokenizer(train_texts, truncation=True, padding=True, max_length=64)",
    "val_encodings = tokenizer(val_texts, truncation=True, padding=True, max_length=64)",
    "",
    "# Define custom Dataset format for PyTorch loader",
    "class NewsDataset(Dataset):",
    "    def __init__(self, encodings, labels):",
    "        self.encodings = encodings",
    "        self.labels = labels",
    "        ",
    "    def __getitem__(self, idx):",
    "        item = {key: torch.tensor(val[idx]) for key, val in self.encodings.items()}",
    "        item['labels'] = torch.tensor(self.labels[idx])",
    "        return item",
    "        ",
    "    def __len__(self):",
    "        return len(self.labels)",
    "",
    "train_dataset = NewsDataset(train_encodings, train_labels)",
    "val_dataset = NewsDataset(val_encodings, val_labels)",
    "print(f\"Data split: {len(train_dataset)} training headlines, {len(val_dataset)} validation headlines\")"
])

# --- CELL 10: FINE TUNING INTRO ---
add_markdown([
    "## ⚙️ Step 6: Model Initialization and Training Setup",
    "We load a pre-trained `DistilBertForSequenceClassification` model with 2 classification labels. We also write a metric computing callback and set our TrainingArguments (e.g. learning rate, batch size, epoch counts)."
])

# --- CELL 11: FINE TUNING CODE ---
add_code([
    "# Load pre-trained sequence classifier",
    "model = DistilBertForSequenceClassification.from_pretrained('distilbert-base-uncased', num_labels=2)",
    "",
    "# Define evaluation metric calculations",
    "def compute_metrics(eval_pred):",
    "    logits, labels = eval_pred",
    "    predictions = np.argmax(logits, axis=-1)",
    "    acc = accuracy_score(labels, predictions)",
    "    report = classification_report(labels, predictions, output_dict=True)",
    "    ",
    "    return {",
    "        'accuracy': acc,",
    "        'f1': report['macro avg']['f1-score'],",
    "        'precision': report['macro avg']['precision'],",
    "        'recall': report['macro avg']['recall']",
    "    }",
    "",
    "# Set Training Arguments",
    "training_args = TrainingArguments(",
    "    output_dir='./results',",
    "    num_train_epochs=3,                  # Epoch count",
    "    per_device_train_batch_size=16,      # Batch size for training",
    "    per_device_eval_batch_size=16,       # Batch size for validation",
    "    warmup_steps=50,                     # Warmup steps",
    "    weight_decay=0.01,                   # Weight decay rate",
    "    logging_dir='./logs',",
    "    logging_steps=10,",
    "    evaluation_strategy='epoch',         # Evaluate at end of each epoch",
    "    save_strategy='epoch',               # Save checkpoints at end of each epoch",
    "    load_best_model_at_end=True,         # Load the best model at end of training",
    "    metric_for_best_model='accuracy',",
    "    report_to='none'                     # Suppress third party logging trackers",
    ")",
    "",
    "# Create Trainer instance",
    "trainer = Trainer(",
    "    model=model,",
    "    args=training_args,",
    "    train_dataset=train_dataset,",
    "    eval_dataset=val_dataset,",
    "    compute_metrics=compute_metrics",
    ")"
])

# --- CELL 12: TRAINING INTRO ---
add_markdown([
    "## 🚀 Step 7: Train the Model",
    "Let's execute the training loops. On a standard GPU runtime, this should take less than 1-2 minutes."
])

# --- CELL 13: TRAINING CODE ---
add_code([
    "# Execute training",
    "trainer.train()"
])

# --- CELL 14: EVALUATION INTRO ---
add_markdown([
    "## 📈 Step 8: System Evaluation & Performance Metrics",
    "We evaluate the fine-tuned model against the validation dataset. We display classification metrics and render a confusion matrix heatmap."
])

# --- CELL 15: EVALUATION CODE ---
add_code([
    "# Generate predictions",
    "predictions = trainer.predict(val_dataset)",
    "preds = np.argmax(predictions.predictions, axis=-1)",
    "",
    "# Compute scores",
    "accuracy = accuracy_score(val_labels, preds)",
    "print(f\"Test Validation Accuracy: {accuracy * 100:.2f}%\\n\")",
    "print(\"Classification Report:\")",
    "print(classification_report(val_labels, preds, target_names=['Real', 'Fake']))",
    "",
    "# Plot Confusion Matrix",
    "cm = confusion_matrix(val_labels, preds)",
    "plt.figure(figsize=(6, 5))",
    "sns.heatmap(cm, annot=True, fmt='d', cmap='Greens', xticklabels=['Real', 'Fake'], yticklabels=['Real', 'Fake'])",
    "plt.title('Confusion Matrix - Indian Fake News Detector')",
    "plt.ylabel('True Class')",
    "plt.xlabel('Predicted Class')",
    "plt.show()"
])

# --- CELL 16: INFERENCE INTRO ---
add_markdown([
    "## 🔮 Step 9: Real-world Testing on Custom Headlines",
    "Now, we test our classifier on **10 custom headlines** (5 real, 5 fake) that mimic standard Indian news patterns, Whatsapp forwards, and clickbait to observe predictions."
])

# --- CELL 17: INFERENCE CODE ---
add_code([
    "# Handcrafted evaluation list",
    "custom_test_headlines = [",
    "    'ISRO launches Aditya-L1 spacecraft to study the Sun',",
    "    'Reserve Bank of India raises repo rate by 25 basis points',",
    "    'Virat Kohli scores his 50th ODI century in World Cup semi-final',",
    "    'Government of India introduces new startup tax exemption scheme',",
    "    'Mumbai metro line 3 begins commercial operations for commuters',",
    "    'UNESCO declares Modi as the best Prime Minister in the universe',",
    "    'New Rs 2000 notes contain a micro-nano GPS tracker chip inside',",
    "    'Eating raw garlic cured corona virus in 24 hours, claims viral video',",
    "    'NASA satellite shows Taj Mahal glowing with green cosmic rays',",
    "    'RBI is giving free laptop and internet to every Indian student'",
    "]",
    "",
    "# Prediction wrapper function",
    "def classify_headlines(headlines):",
    "    model.eval()",
    "    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')",
    "    model.to(device)",
    "    ",
    "    # Tokenize input list",
    "    inputs = tokenizer(headlines, padding=True, truncation=True, max_length=64, return_tensors='pt')",
    "    inputs = {k: v.to(device) for k, v in inputs.items()}",
    "    ",
    "    with torch.no_grad():",
    "        outputs = model(**inputs)",
    "        probs = torch.softmax(outputs.logits, dim=-1).cpu().numpy()",
    "        preds = np.argmax(probs, axis=-1)",
    "        ",
    "    results = []",
    "    for hl, prob, pred in zip(headlines, probs, preds):",
    "        label = 'Fake' if pred == 1 else 'Real'",
    "        confidence = prob[pred] * 100",
    "        results.append({",
    "            'Headline': hl,",
    "            'Prediction': label,",
    "            'Confidence': f\"{confidence:.2f}%\",",
    "            'Real Probability': f\"{prob[0]*100:.2f}%\",",
    "            'Fake Probability': f\"{prob[1]*100:.2f}%\"",
    "        })",
    "    return pd.DataFrame(results)",
    "",
    "# Classify the custom list",
    "results_table = classify_headlines(custom_test_headlines)",
    "results_table"
])

# --- CELL 18: LOSS CURVE INTRO ---
add_markdown([
    "## 📉 Step 10: Plot Training & Validation Curves",
    "Let's visualize how our loss decreases and accuracy improves during the training process by plotting training metrics collected during execution."
])

# --- CELL 19: LOSS CURVE CODE ---
add_code([
    "# Extract and plot training curves",
    "history = trainer.state.log_history",
    "train_loss = [x['loss'] for x in history if 'loss' in x]",
    "train_steps = [x['step'] for x in history if 'loss' in x]",
    "eval_loss = [x['eval_loss'] for x in history if 'eval_loss' in x]",
    "eval_steps = [x['step'] for x in history if 'eval_loss' in x]",
    "eval_acc = [x['eval_accuracy'] for x in history if 'eval_accuracy' in x]",
    "",
    "plt.figure(figsize=(12, 5))",
    "",
    "# Plot Loss",
    "plt.subplot(1, 2, 1)",
    "plt.plot(train_steps, train_loss, label='Training Loss', color='royalblue', marker='o')",
    "if eval_loss:",
    "    plt.plot(eval_steps, eval_loss, label='Validation Loss', color='tomato', marker='x')",
    "plt.title('Training and Validation Loss')",
    "plt.xlabel('Training Steps')",
    "plt.ylabel('Loss')",
    "plt.legend()",
    "plt.grid(True, linestyle='--', alpha=0.6)",
    "",
    "# Plot Accuracy",
    "plt.subplot(1, 2, 2)",
    "if eval_acc:",
    "    plt.plot(eval_steps, [x * 100 for x in eval_acc], label='Validation Accuracy', color='forestgreen', marker='s')",
    "plt.title('Validation Accuracy')",
    "plt.xlabel('Training Steps')",
    "plt.ylabel('Accuracy (%)')",
    "plt.legend()",
    "plt.grid(True, linestyle='--', alpha=0.6)",
    "",
    "plt.tight_layout()",
    "plt.show()"
])

# --- CELL 20: EXPLAINABILITY INTRO ---
add_markdown([
    "## 🧠 Step 11: Explainable AI (XAI) - Model Attention Highlights",
    "One of the biggest advantages of transformers is **Self-Attention**. When classifying a headline, the model pays different levels of attention to different words. We can extract the attention matrices from DistilBERT's last layer to visualize exactly which words the model focused on to make its decision (Real/Fake)."
])

# --- CELL 21: EXPLAINABILITY CODE ---
add_code([
    "def explain_attention(headline):",
    "    model.eval()",
    "    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')",
    "    model.to(device)",
    "    ",
    "    # Tokenize input",
    "    inputs = tokenizer(headline, return_tensors='pt')",
    "    inputs = {k: v.to(device) for k, v in inputs.items()}",
    "    ",
    "    with torch.no_grad():",
    "        # output_attentions=True returns self-attention tensors",
    "        outputs = model(**inputs, output_attentions=True)",
    "        logits = outputs.logits",
    "        pred = np.argmax(logits.cpu().numpy(), axis=-1)[0]",
    "        ",
    "        # Get attention weights from last transformer layer",
    "        # Shape: (1, num_heads, sequence_length, sequence_length)",
    "        attentions = outputs.attentions[-1]",
    "        ",
    "        # Average weights across all attention heads",
    "        avg_attn = attentions[0].mean(dim=0).cpu().numpy()",
    "        ",
    "        # Extract attention weights from [CLS] classification token to all other tokens",
    "        cls_attn = avg_attn[0]",
    "        ",
    "    # Convert input token IDs to readable string tokens",
    "    tokens = tokenizer.convert_ids_to_tokens(inputs['input_ids'][0].tolist())",
    "    ",
    "    # Filter out special helper tokens ([CLS], [SEP], [PAD])",
    "    valid_indices = [i for i, t in enumerate(tokens) if t not in ['[CLS]', '[SEP]', '[PAD]']]",
    "    if not valid_indices:",
    "        return ''",
    "        ",
    "    scores = [cls_attn[i] for i in valid_indices]",
    "    min_s, max_s = min(scores), max(scores)",
    "    ",
    "    # Normalize scores between 0 and 1 for transparency opacity",
    "    norm_scores = [(s - min_s) / (max_s - min_s) if max_s > min_s else 0.5 for s in scores]",
    "    ",
    "    # Build HTML string highlighting the words",
    "    html_str = \"<div style='margin-top: 15px; border-top: 1px dashed #ccc; padding-top: 12px; font-size: 14px;'><strong>🧠 AI Model Word Focus (Self-Attention Highlights):</strong><br><div style='line-height: 2.2; margin-top: 8px;'>\"",
    "    for idx, (token_idx, score) in enumerate(zip(valid_indices, norm_scores)):",
    "        token = tokens[token_idx]",
    "        # Format word pieces back together",
    "        if token.startswith('##'):",
    "            token = token[2:]",
    "        else:",
    "            if idx > 0:",
    "                html_str += ' '",
    "        ",
    "        # Red background for Fake, Green for Real, opacity matches attention score",
    "        color = f'rgba(220, 53, 69, {score * 0.6 + 0.15})' if pred == 1 else f'rgba(40, 167, 69, {score * 0.6 + 0.15})'",
    "        html_str += f\"<span style='background-color: {color}; padding: 3px 6px; border-radius: 4px; border: 1px dashed rgba(0,0,0,0.1); font-weight: bold;'>{token}</span>\"",
    "    ",
    "    html_str += \"</div><p style='font-size: 11px; color:#6c757d; margin-top: 8px; margin-bottom: 0;'>Note: Darker background highlight indicates stronger attention weight allocated by the model.</p></div>\"",
    "    return html_str",
    "",
    "# Test explainability on a sample fake news headline",
    "from IPython.display import HTML",
    "HTML(explain_attention('UNESCO declares Modi as the best Prime Minister in the universe'))"
])

# --- CELL 22: INTERACTIVE INTRO ---
add_markdown([
    "## 🎛️ Step 12: Interactive Headline Analyzer with Explainable AI",
    "Use this interactive widget to test any Indian news headline! Enter a headline below, click **Analyze Headline**, and watch the model predict, compute confidence, and highlight the exact words it focused on."
])

# --- CELL 23: INTERACTIVE CODE ---
add_code([
    "import ipywidgets as widgets",
    "from IPython.display import display, HTML",
    "",
    "# Define interactive widgets",
    "text_input = widgets.Text(",
    "    value='ISRO is preparing to launch a new weather satellite next month.',",
    "    placeholder='Enter an Indian news headline...',",
    "    description='Headline:',",
    "    layout=widgets.Layout(width='70%')",
    ")",
    "",
    "button = widgets.Button(",
    "    description='Analyze Headline',",
    "    button_style='success',",
    "    tooltip='Click to run BERT inference',",
    "    icon='search'",
    ")",
    "",
    "output = widgets.Output()",
    "",
    "def on_button_clicked(b):",
    "    with output:",
    "        output.clear_output()",
    "        headline = text_input.value.strip()",
    "        if not headline:",
    "            print(\"Please enter a valid headline!\")",
    "            return",
    "        ",
    "        # Perform predictions",
    "        res_df = classify_headlines([headline])",
    "        pred = res_df.iloc[0]['Prediction']",
    "        conf = res_df.iloc[0]['Confidence']",
    "        real_p = float(res_df.iloc[0]['Real Probability'].replace('%', ''))",
    "        fake_p = float(res_df.iloc[0]['Fake Probability'].replace('%', ''))",
    "        ",
    "        # Compute attention highlights",
    "        attn_highlights = explain_attention(headline)",
    "        ",
    "        # Beautiful HTML Card",
    "        color = '#28a745' if pred == 'Real' else '#dc3545'",
    "        emoji = '🌱' if pred == 'Real' else '⚠️'",
    "        ",
    "        html_content = f\"\"\"",
    "        <div style='padding: 15px; border-radius: 8px; border-left: 6px solid {color}; background-color: #f8f9fa; box-shadow: 0 4px 6px rgba(0,0,0,0.05); margin-top: 15px; font-family: sans-serif;'>",
    "            <h3 style='color: {color}; margin-top: 0; margin-bottom: 8px;'>{emoji} Prediction: {pred} ({conf} Confidence)</h3>",
    "            <p style='font-size: 14px; color: #333; margin-top: 0;'><strong>Headline Analyzed:</strong> \"{headline}\"</p>",
    "            <div style='margin-top: 12px;'>",
    "                <strong>Confidence Breakdown:</strong>",
    "                <div style='display: flex; align-items: center; margin-top: 8px;'>",
    "                    <span style='width: 120px; font-size: 13px;'>Real Probability:</span>",
    "                    <div style='background-color: #e9ecef; border-radius: 4px; flex-grow: 1; height: 16px; margin: 0 12px; overflow: hidden;'>",
    "                        <div style='background-color: #28a745; width: {real_p}%; height: 100%;'></div>",
    "                    </div>",
    "                    <span style='width: 50px; text-align: right; font-weight: bold; font-size: 13px;'>{real_p:.1f}%</span>",
    "                </div>",
    "                <div style='display: flex; align-items: center; margin-top: 6px;'>",
    "                    <span style='width: 120px; font-size: 13px;'>Fake Probability:</span>",
    "                    <div style='background-color: #e9ecef; border-radius: 4px; flex-grow: 1; height: 16px; margin: 0 12px; overflow: hidden;'>",
    "                        <div style='background-color: #dc3545; width: {fake_p}%; height: 100%;'></div>",
    "                    </div>",
    "                    <span style='width: 50px; text-align: right; font-weight: bold; font-size: 13px;'>{fake_p:.1f}%</span>",
    "                </div>",
    "                {attn_highlights}",
    "                <p style='font-size: 11px; color: #777; margin-top: 12px; margin-bottom: 0;'>Model used: Fine-tuned DistilBERT (Self-Attention Activated)</p>",
    "            </div>",
    "        </div>",
    "        \"\"\"",
    "        display(HTML(html_content))",
    "",
    "button.on_click(on_button_clicked)",
    "display(widgets.VBox([",
    "    widgets.HTML(\"<h4 style='color:#333;'>🔮 Enter news headline to check real-time classification:</h4>\"),",
    "    text_input,",
    "    button,",
    "    output",
    "]))"
])

# Write to file
file_path = "C:/Users/adiqu/.gemini/antigravity/scratch/fake-news-detector/Fake_News_Detection_Indian_News.ipynb"
os.makedirs(os.path.dirname(file_path), exist_ok=True)
with open(file_path, "w", encoding="utf-8") as f:
    json.dump(notebook, f, indent=2)

print(f"Jupyter Notebook generated successfully at {file_path}")
