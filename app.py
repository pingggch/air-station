from flask import Flask, request, jsonify, render_template
import json

app = Flask(__name__)

# ตัวแปรเก็บค่า (รอรับ PMS7003)
current_data = {
    "temp": 0,
    "humi": 0,
    "pres": 0,
    "ver": "Station Offline",
    "pm1": "Wait...",
    "pm25": "Wait...",
    "pm10": "Wait..."
}

# 1. หน้าแรก (เปลี่ยนมาใช้ render_template เพื่อเรียกไฟล์ html)
@app.route('/')
def index():
    return render_template('index.html')

# 2. รับค่าจาก ESP8266
@app.route('/update', methods=['POST'])
def update_data():
    global current_data
    try:
        data = request.json
        current_data.update(data)
        print(f"📥 Received: {data}")
        return "OK", 200
    except Exception as e:
        print(f"Error: {e}")
        return "Error", 400

# 3. ส่งค่าให้หน้าเว็บ (JS)
@app.route('/api/data')
def get_data():
    return jsonify(current_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)