from chatterbot import chatbot
from chatterbot.trainers import ListTrainer

# Create a new chat bot named Teana
chatbot = ChatBot('FireBot')

trainer = ListTrainer(chatbot)

trainer.train(['hi', 'Hello', 'How are you?', 'I am fine and you?', 'Great', 'What are you Doing?', 'nothing just roaming around.'])

while True:
    input_data = input("You- ")
    response = chatbot.get_response(input_data)
    print("fireBot- ",response)