from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route("/")
def home():
    return "API is running"

@app.route("/translate")
def translate():
    text = request.args.get("text")
    target = request.args.get("target", "ur")

    if not text:
        return jsonify({"error": "Text required"})

    url = "https://libretranslate.de/translate"
    data = {
        "q": text,
        "source": "auto",
        "target": target,
        "format": "text"
    }

    r = requests.post(url, data=data)
    return jsonify(r.json())
