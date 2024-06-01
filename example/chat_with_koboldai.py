from webscout import KOBOLDAI

def chat_with_koboldai(prompt):
    koboldai = KOBOLDAI()
    response = koboldai.ask(prompt)
    message = koboldai.get_message(response)
    return message

def main():
    prompt = "What is the capital of France?"
    response = chat_with_koboldai(prompt)
    print(response)

if __name__ == "__main__":
    main()
