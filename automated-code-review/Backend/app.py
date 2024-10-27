from flask import Flask, request, jsonify, send_from_directory
import requests
import json
from flask_cors import CORS

app = Flask(__name__, static_folder='../Frontend', static_url_path='')
CORS(app)

# API key and URL
api_key = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'  # Replace with your actual API key
url = f'https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent?key={api_key}'

@app.route('/')
def index():
    return send_from_directory('../Frontend', 'index.html')

@app.route('/styles.css')
def styles():
    return send_from_directory('../Frontend', 'styles.css')

@app.route('/review', methods=['POST'])
def review_code():
    data = request.json
    code = data.get('code', '')

    headers = {'Content-Type': 'application/json'}
    payload = {
        "contents": [{"parts": [{"text": code}]}]
    }

    try:
        response = requests.post(url, headers=headers, data=json.dumps(payload))
        response.raise_for_status()
        result = response.json()
        return jsonify(result)
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
