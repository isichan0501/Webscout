from webscout import Berlin4h

def chat_with_berlin4h(prompt):
    ai = Berlin4h(
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
    response = chat_with_berlin4h(prompt)
    print(response)

if __name__ == "__main__":
    main()
