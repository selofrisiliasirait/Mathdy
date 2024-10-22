import re
import math
import random

# Manual conversation handling
def handle_conversation(user_text):
    user_text = user_text.lower()
    if "hello" in user_text or "halo" in user_text or "hai" in user_text or "hi" in user_text or "Hello" in user_text or "Halo" in user_text or "Hai" in user_text or "Hi" in user_text:
        return "Haiii!! Ada yang bisa aku bantu?"
    elif "aku pusing banget" in user_text or "gangerti mtk" in user_text or "bantu pliss" in user_text:
        return "Butuh bantuan apaaa aku bisa kokk semoga."
    elif "Kamu siapa?" in user_text or "kamu siapa" in user_text or "kamu siapa?" in user_text:
        return "Aku math bot yang bisa membantu kamu dalam perhitungan dasar. Mungkin kamu mengira kan ada kalkulator, buat apasi Math Bot ini? Jadi kehadiran kami membuat kamu merasakan sesuatu yang lebih interaktif."
    elif "byee" in user_text or "thank youu" in user_text or "Terimakasih" in user_text or "thanks" in user_text:
        return "Byee sama- sama!!"
    else:
        return "Sorry aku cuman bisa menyelesaikan soal matematika.."

# Function to check if input is a math expression (allow modulo %, sqrt, and power **)
def is_math_expression(user_text):
    # Regular expression to match math expressions with +, -, *, /, %, **, sqrt()
    math_pattern = r'^[0-9\+\-\/%\s\(\)\.\\*sqrt]+$'
    return re.match(math_pattern, user_text.strip())

# Safely evaluate math expressions using eval
def solve_math_expression(user_text):
    try:
        # Replace 'sqrt(' with 'math.sqrt(' to ensure correct evaluation
        user_text = user_text.replace("sqrt(", "math.sqrt(")
        # Evaluate the math expression
        result = eval(user_text)
        return f"{result}"
    except Exception as e:
        return f"Error solving math expression: {str(e)}"

# Daftar jokes yang akan diberikan oleh chatbot
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

def chatbot_response(input_text):
    # Jika input adalah permintaan jokes, maka pilih random dari jokes_list
    if "joke" in input_text.lower() or "jokes" in input_text.lower():
        return random.choice(jokes_list)
    else:
        return "I'm sorry, I don't understand. Try asking for a joke or math help."

print("============== Math, Chat, and Jokes ChatBot ==============")

while True:
    user_text = input("You: ")
    
    if user_text.lower() == "exit":
        print("Chatbot: Goodbye! See you next time!")
        break
    
    # Check if input is a math expression
    if is_math_expression(user_text):
        # Solve the math equation using Python's eval
        math_response = solve_math_expression(user_text)
        print("Chatbot (Math):", math_response)
    else:
        # Handle jokes or conversation manually
        response = chatbot_response(user_text)
        if response == "I'm sorry, I don't understand. Try asking for a joke or math help.":
            response = handle_conversation(user_text)
        print("Chatbot:", response)
