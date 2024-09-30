import re

# Manual conversation handling
def handle_conversation(user_text):
    user_text = user_text.lower()
    if "hello" in user_text or "hi" in user_text:
        return "Hello! How can I assist you today?"
    elif "your name" in user_text:
        return "I am a chatbot designed to solve math equations."
    elif "goodbye" in user_text:
        return "Goodbye! Have a nice day!"
    else:
        return "I can help with math problems. Try asking a math question."

# Function to check if input is a math expression
def is_math_expression(user_text):
    # Regular expression to match simple math expressions (e.g., 3+2, 5*7-1)
    math_pattern = r'^[0-9\+\-\*/\s\(\)]+$'
    return re.match(math_pattern, user_text.strip())

# Safely evaluate math expressions using eval
def solve_math_expression(user_text):
    try:
        # Here we use eval to evaluate the math expression
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
