import re
import math

# Manual conversation handling
def handle_conversation(user_text):
    user_text = user_text.lower()
    if "hello" in user_text or "hi" in user_text:
        return "Hello! How can I assist you today?"
    elif "your name" in user_text:
        return "I am a chatbot designed to solve math equations, including modulo, square root, and power."
    elif "goodbye" in user_text:
        return "Goodbye! Have a nice day!"
    else:
        return "I can help with math problems. Try asking a math question."

# Function to check if input is a math expression (allow modulo %, sqrt, and power **)
def is_math_expression(user_text):
    # Regular expression to match math expressions with +, -, *, /, %, **, sqrt()
    math_pattern = r'^[0-9\+\-\*/%\s\(\)\.\*\*sqrt]+$'
    return re.match(math_pattern, user_text.strip())

# Safely evaluate math expressions using eval
def solve_math_expression(user_text):
    try:
        # Replace 'sqrt(' with 'math.sqrt(' to ensure correct evaluation
        user_text = user_text.replace("sqrt(", "math.sqrt(")
        # Evaluate the math expression
        result = eval(user_text)
        return f"The result is: {result}"
    except Exception as e:
        return f"Error solving math expression: {str(e)}"

print("============== Math and Chat ChatBot ==============")

while True:
    user_text = input("Type something: ")
    
    # Check if input is a math expression
    if is_math_expression(user_text):
        # Solve the math equation using Python's eval
        math_response = solve_math_expression(user_text)
        print("Chatbot (Math):", math_response)
    else:
        # Handle conversation manually
        response = handle_conversation(user_text)
        print("Chatbot:", response)
