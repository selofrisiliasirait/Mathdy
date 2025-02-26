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
    elif "tips belajar" in user_text or "tips and trick belajar mtk" in user_text:
        return """
            <ul>
            Tips Belajar Matematika ala Mathdy:
                <li>Pahami konsep dasar materi</li>
                <li>Belajar dari berbagai sumber</li>
                <li>Rajin latihan soal</li>
                <li>Belajar secara berkelompok</li>
                <li>Buat jadwal belajar rutin</li>
            </ul>
        """
    elif "list materi" in user_text or "materi" in user_text:
        return """
            <ul>
            List Materi Matematika Dasar:
                <li>Bilangan dan Operasi Bilangan</li>
                <li>Pecahan, Desimal, dan Persen</li>
                <li>Aljabar</li>
                <li>Eksponen dan Logaritma</li>
                <li>Perbandingan</li>
                <li>Pengukuran Panjang, Berat, dan Volume</li>
                <li>Bangun Datar dan Bangun Ruang</li>
                <li>Sistem Persamaan dan Pertdaksamaan Linear</li>
                <li>Persamaan dan Pertdaksamaan Kuadrat</li>
                <li>Fungsi Komposisi dan Invers</li>
            </ul>
        """
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
    "Kamu itu seperti konstanta Pi, tak terhingga dan selalu bikin aku terpana.",
    "Hubungan kita kayak garis paralel, selalu sejajar dan nggak akan pernah berpisah.",
    "Kalau kamu jadi variabel X, aku bakal jadi Y, biar kita selalu ada dalam persamaan yang sama.",
    "Kamu seperti akar dari -1, nggak nyata tapi selalu ada dalam pikiranku.",
    "Aku boleh nggak jadi turunanmu? Biar aku selalu mengejar perubahan kecil dalam hidupmu.",
    "Kalau kamu sudut, aku pasti 90 derajat, karena aku jatuh tegak lurus mencintaimu.",
    "Aku dan kamu bagaikan himpunan, selalu saling melengkapi dan tak terpisahkan.",
    "Kamu seperti eksponensial, semakin lama semakin membuat hati ini berdegup lebih cepat.",
    "Jangan jadi irasional, biarkan kita jadi satu pasangan sempurna.",
    "Kita itu kayak limit, semakin dekat tanpa batas, walaupun nggak pernah benar-benar bertemu.",
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
