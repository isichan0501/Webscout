from webscout import YEPCHAT

def chat_with_yepchat(prompt):
    YEPCHAT = YEPCHAT()
    response = YEPCHAT.chat(prompt)
    return response

def main():
    prompt = "What is the capital of France?"
    response = chat_with_yepchat(prompt)
    print(response)

if __name__ == "__main__":
    main()
