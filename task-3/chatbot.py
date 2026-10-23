#welcome to simple chat bot system
print("Welcome to the Simple Chat Bot System!")
print("=== Basic Chatbot ===")
print("Type 'bye' to exit the chatbot.")

while True:
    user_input = input("You: ").lower()

    if user_input == "hello" or user_input == "hi":
        print("Bot: Hello! How can I help you?")

    elif user_input == "good morning":
        print("Bot: Good morning! Have a great day.")

    elif user_input == "how are you":
        print("Bot: I'm doing great! Thanks for asking.")

    elif user_input == "what is your name":
        print("Bot: I'm a basic Python chatbot.")

    elif user_input == "who created you":
        print("Bot: I was created using Python.")

    elif user_input == "what can you do":
        print("Bot: I can answer some basic questions.")

    elif user_input == "what is python":
        print("Bot: Python is a popular programming language.")

    elif user_input == "what is ai":
        print("Bot: AI means Artificial Intelligence.")

    elif user_input == "thank you" or user_input == "thanks":
        print("Bot: You're welcome!")

    elif user_input == "help":
        print("Bot: You can ask me about Python, AI, my name, or how I am.")

    elif user_input == "bye":
        print("Bot: Goodbye! Have a nice day.")
        break

    else:
        print("Bot: Sorry, I don't understand that.")
        