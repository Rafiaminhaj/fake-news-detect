from flask import Flask, request, jsonify, render_template
from transformers import pipeline
import os

app = Flask(__name__)

# Use a lightweight pre-trained fake news classifier (~17MB)
# It downloads instantly and runs in milliseconds on local CPU without GPU!
MODEL_NAME = "mrm8488/bert-tiny-finetuned-fake-news-detection"

print("Loading Fake News classification model (Tiny BERT, ~17MB)...")
try:
    classifier = pipeline("text-classification", model=MODEL_NAME)
    print("Model loaded successfully!")
except Exception as e:
    print(f"Error loading model: {e}")
    classifier = None

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    if not classifier:
        return jsonify({"error": "Classifier model is not initialized."}), 500
    
    data = request.get_json()
    headline = data.get("headline", "").strip()
    if not headline:
        return jsonify({"error": "Please enter a valid news headline."}), 400
        
    try:
        # Run inference using Hugging Face pipeline
        result = classifier(headline)[0]
        label_raw = result["label"]
        score = result["score"]
        
        # Mapping model labels: LABEL_0 is Fake, LABEL_1 is Real
        if label_raw == "LABEL_0":
            label = "Fake"
            fake_prob = score * 100
            real_prob = (1.0 - score) * 100
        else:
            label = "Real"
            real_prob = score * 100
            fake_prob = (1.0 - score) * 100
            
        return jsonify({
            "headline": headline,
            "prediction": label,
            "confidence": f"{score * 100:.2f}%",
            "real_prob": f"{real_prob:.2f}%",
            "fake_prob": f"{fake_prob:.2f}%"
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, port=5000)
