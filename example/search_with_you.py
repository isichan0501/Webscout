from webscout import YouChat
from rich import print

def search_with_you(prompt):
    ai = YouChat(
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
    response = ai.ask(prompt)
    message = ai.get_message(response)
    return message

def main():
    prompt = "what is meaning of life"
    response = search_with_you(prompt)
    print(response)

if __name__ == "__main__":
    main()
