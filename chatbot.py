from chatterbot import ChatBot
import spacy
from chatterbot.tagging import PosLemmaTagger

# Monkey patch to override the model load
def patched_init(self, language):
    self.language = language
    self.nlp = spacy.load("en_core_web_sm")

PosLemmaTagger.__init__ = patched_init

# Initialize the spaCy model
nlp = spacy.load("en_core_web_sm")
doc = nlp("This is a sentence.")

# Initialize the ChatBot
bot = ChatBot(
    "Math",
    logic_adapters=["chatterbot.logic.MathematicalEvaluation"],
    storage_adapter="chatterbot.storage.SQLStorageAdapter"
)

print("============== Math ChatBot ==============")

while True:
    user_text = input("Type the math equation that you want to solve: ")
    response = bot.get_response(user_text)
    print("Chatbot:", response)
