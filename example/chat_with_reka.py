from webscout import REKA

def chat_with_reka(prompt, api_key=""):
    reka = REKA(is_conversation=True, max_tokens=8000, timeout=30, api_key=api_key)
    response = reka.chat(prompt)
    return response

def main():
    prompt = "tell me about india"
    response = chat_with_reka(prompt)
    print(response)

if __name__ == "__main__":
    main()
