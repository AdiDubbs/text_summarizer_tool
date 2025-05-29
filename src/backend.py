from flask import Flask, request, jsonify
from flask_cors import CORS
from transformers import pipeline

app = Flask(__name__)
CORS(app)

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")


@app.route('/summarize', methods=['POST'])
def summarize():
    data = request.json
    text = data.get('text', '')
    if not text.strip():
        return jsonify({'error': 'No text provided'}), 400

    summary = summarizer(text, max_length=250, min_length=75, do_sample=False)[0]['summary_text']
    return jsonify({'summary': summary})


if __name__ == "__main__":
    app.run(debug=True)
