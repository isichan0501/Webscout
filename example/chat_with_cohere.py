from webscout import Cohere

def chat_with_cohere(prompt, api_key=""):
    cohere = Cohere(is_conversation=True, max_tokens=8000, timeout=30, api_key=api_key)
    response = cohere.chat(prompt)
    return response

def main():
    prompt = "tell me about india"
    response = chat_with_cohere(prompt)
    print(response)

if __name__ == "__main__":
    main()
