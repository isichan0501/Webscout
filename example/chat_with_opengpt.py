from webscout import OPENGPT

def chat_with_opengpt(prompt):
    opengpt = OPENGPT(is_conversation=True, max_tokens=8000, timeout=30, assistant_id="bca37014-6f97-4f2b-8928-81ea8d478d88")
    response = opengpt.chat(prompt)
    return response

def main():
    while True:
        prompt = input("Enter your prompt: ")
        if prompt.lower() == "exit":
            break
        response = chat_with_opengpt(prompt)
        print(response)

if __name__ == "__main__":
    main()
