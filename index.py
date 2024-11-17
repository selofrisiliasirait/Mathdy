from flask import Flask, render_template, request
import re
import math
import random
import logging

app = Flask(__name__)

# Fungsi percakapan
def handle_conversation(user_text):
    user_text = user_text.lower()
    if "hello" in user_text or "halo" in user_text or "hai" in user_text or "hi" in user_text:
        return "Hai, aku Mathdy! Ada yang bisa aku bantu?"
    elif "terima kasih" in user_text or "thank you" in user_text or "thanks" in user_text:
        return "Sama-sama, senang bisa membantu!"
    else:
        return "Maaf, aku hanya bisa membantu dengan soal matematika dan bercanda!"


# Fungsi untuk memeriksa apakah input adalah ekspresi matematika
def is_math_expression(user_text):
    math_pattern = r'^[0-9\+\-\/%\s\(\)\.\\*sqrt]+$'
    return re.match(math_pattern, user_text.strip()) is not None

# Fungsi untuk evaluasi ekspresi matematika
def solve_math_expression(user_text):
    try:
        user_text = user_text.replace("sqrt(", "math.sqrt(")
        result = eval(user_text)
        return str(result)
    except Exception:
        return "Error solving math expression."

# Daftar jokes
jokes_list = [
    "Kamu itu seperti konstanta pi, tak terhingga dan selalu bikin aku terpana.",
    "Hubungan kita kayak garis paralel, selalu sejajar dan nggak akan pernah berpisah.",
    "Kalau kamu jadi variabel X, aku bakal jadi Y, biar kita selalu ada dalam persamaan yang sama.",
    "Kamu seperti akar dari -1, nggak nyata tapi selalu ada dalam pikiranku.",
    "Kalau kamu sudut, aku pasti 90 derajat, karena aku jatuh tegak lurus mencintaimu.",
]

# Fungsi utama chatbot response
def chatbot_response(user_text):
    if "joke" in user_text.lower() or "jokes" in user_text.lower():
        return random.choice(jokes_list)
    elif is_math_expression(user_text):
        return solve_math_expression(user_text)
    else:
        return handle_conversation(user_text)

# Route untuk halaman utama
@app.route("/")
def main():
    return render_template("index.html")

# Route untuk halaman kedua (chat)
@app.route("/chat")
def chat():
    return render_template("chat.html")

# Route untuk mendapatkan respon chatbot
@app.route("/get")
def get_chatbot_response():
    user_message = request.args.get('userMessage')
    response = chatbot_response(user_message)
    return str(response)

logging.basicConfig(level=logging.DEBUG)

if __name__ == "__main__":
    print("Starting Flask server...")
    app.run(debug=True, host='0.0.0.0', port=5000)
