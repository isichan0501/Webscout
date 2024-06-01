from webscout import BLACKBOXAI
from rich import print

def search_with_blackbox(prompt):
    ai = BLACKBOXAI(
        is_conversation=True,
        max_tokens=800,
        timeout=30,
        intro=None,
        filepath=None,
        update_file=True,
        proxies={},
        history_offset=10250,
        act=None,
        model=None
    )
    response = ai.chat(prompt)
    return response

def main():
    while True:
        prompt = input("Enter your prompt: ")
        if prompt.lower() == "exit":
            break
        response = search_with_blackbox(prompt)
        print(response)

if __name__ == "__main__":
    main()
