import os
from dotenv import load_dotenv
from flask import Flask, request, jsonify
from flask_cors import CORS
# from transformers import pipeline
from google import genai
from google.genai import types

load_dotenv()

API_KEY = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=API_KEY)

app = Flask(__name__)
CORS(app)

# summarizer = pipeline("summarization", model="facebook/bart-large-cnn")


@app.route('/summarize', methods=['POST'])
def summarize():
    data = request.json
    text = data.get('text', '')
    if not text.strip():
        return jsonify({'error': 'No text provided'}), 400
    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=["Summarize the following text in 3-4 lines", text],
        )
        return  jsonify({"summary": response.text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

    # summary = summarizer(text, max_length=250, min_length=75, do_sample=False)[0]['summary_text']
    # return jsonify({'summary': summary})


if __name__ == "__main__":
    app.run(debug=True)
