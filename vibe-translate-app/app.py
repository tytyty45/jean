from flask import Flask, render_template, request, jsonify
import os
import requests

app = Flask(__name__)

# หน้าแรกให้เสิร์ฟไฟล์ index.html
@app.route('/')
def home():
    return render_template('index.html')

# ตัวกลางสำหรับยิง API ไปหา Gemini
@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.json
    # ดึง API Key จากตัวแปรลับบน Render
    api_key = os.environ.get("GEMINI_API_KEY")
    
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={api_key}"
    
    headers = {"Content-Type": "application/json"}
    response = requests.post(url, headers=headers, json=data)
    
    return jsonify(response.json()), response.status_code

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)