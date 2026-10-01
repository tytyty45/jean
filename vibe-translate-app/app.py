from flask import Flask, render_template, request, jsonify
import os
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.json
    api_key = os.environ.get("GEMINI_API_KEY")
    
    # ลองใช้โมเดลเวอร์ชัน latest เพื่อป้องกันปัญหา URL ไม่แมตช์
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent?key={api_key}"
    
    headers = {"Content-Type": "application/json"}
    response = requests.post(url, headers=headers, json=data)
    
    # === ระบบดักจับและปริ้นต์ Error จาก Google ลงใน Logs ===
    if response.status_code != 200:
        print("====================================")
        print("GOOGLE ERROR CODE:", response.status_code)
        print("GOOGLE ERROR MESSAGE:", response.text)
        print("====================================")
    
    return jsonify(response.json()), response.status_code

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
