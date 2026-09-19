print("======================================")
print("       🤖 Rule-Based AI Chatbot")
print("======================================")
print("Type 'bye' or 'exit' to end the chat.\n")
responses = {
    "hello": "Hi there! How can I help you?",
    "hi": "Hello! Nice to meet you.",
    "hey": "Hey! How are you doing?",
    
    "how are you": "I'm doing great! Thanks for asking.",
    "what is your name": "I am a Rule-Based AI Chatbot.",
    
    "what is ai": "AI stands for Artificial Intelligence. It enables machines to perform intelligent tasks.",
    
    "help": "Sure! You can ask me about AI, my name, or say hello.",
    
    "thank you": "You're welcome!",
    "thanks": "You're welcome!"
}

while True:
    user_input = input("You: ")

    user_input = user_input.lower().strip()

    if user_input == "bye" or user_input == "exit":
        print("Bot: Goodbye! Have a great day! 👋")
        break

    if user_input in responses:
        print("Bot:", responses[user_input])

    else:
        print("Bot: Sorry, I don't understand that. Please try another question.")
