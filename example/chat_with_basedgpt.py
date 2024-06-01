from webscout import BasedGPT

def chat_with_basedgpt(prompt):
    basedgpt = BasedGPT(is_conversation=True, max_tokens=800, timeout=30)
    response = basedgpt.chat(prompt)
    return response

def main():
    prompt = "What is the capital of France?"
    response = chat_with_basedgpt(prompt)
    print(response)

if __name__ == "__main__":
    main()
