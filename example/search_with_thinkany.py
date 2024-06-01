from webscout import ThinkAnyAI

def search_with_thinkany(prompt):
    ai = ThinkAnyAI(
        is_conversation=True,
        max_tokens=800,
        timeout=30,
        intro=None,
        filepath=None,
        update_file=True,
        proxies={},
        history_offset=10250,
        act=None,
        web_search=False,
    )
    response = ai.ask(prompt)
    message = ai.get_message(response)
    return message

def main():
    prompt = "what is meaning of life"
    response = search_with_thinkany(prompt)
    print(response)

if __name__ == "__main__":
    main()
