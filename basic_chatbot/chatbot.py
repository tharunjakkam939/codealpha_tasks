def chatbot():
    print("Welcome to ChatBot! (type 'exit' to quit)")
    while True:
        user_input = input("You: ").lower()
        if user_input == "exit":
            print("Bot: Goodbye!")
            break
        elif user_input in ["hello", "hi"]:
            print("Bot: Hi!")
        elif user_input == "how are you":
            print("Bot: I'm fine, thanks!")
        elif user_input == "bye":
            print("Bot: Goodbye!")
            break
        else:
            print("Bot: I don't understand.")

if __name__ == "__main__":
    chatbot()
