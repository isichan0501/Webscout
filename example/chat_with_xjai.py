from webscout import Xjai
from rich import print

def chat_with_xjai(prompt):
    ai = Xjai(
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
    prompt = "Tell me about india"
    response = chat_with_xjai(prompt)
    print(response)

if __name__ == "__main__":
    main()
