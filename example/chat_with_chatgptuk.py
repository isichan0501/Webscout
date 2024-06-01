from webscout import ChatGPTUK

def chat_with_chatgptuk(prompt):
    ai = ChatGPTUK(
        is_conversation=True,
        max_tokens=800,
        timeout=30,
        intro=None,
        filepath=None,
        update_file=True,
        proxies={},
        history_offset=10250,
        act=None,
    )
    response = ai.chat(prompt)
    return response

def main():
    prompt = "Explain the concept of recursion in simple terms."
    response = chat_with_chatgptuk(prompt)
    print(response)

if __name__ == "__main__":
    main()
