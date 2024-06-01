from webscout import POE

def chat_with_poe(prompt):
    poe = POE(is_conversation=True, max_tokens=800, timeout=30)
    response = poe.chat(prompt)
    return response

def main():
    prompt = "What is the capital of France?"
    response = chat_with_poe(prompt)
    print(response)

if __name__ == "__main__":
    main()
