from webscout import WEBS as w

def chat_with_duckchat(prompt, model='claude-3-haiku'):
    R = w().chat(prompt, model=model)
    return R

def main():
    prompt = "hello"
    response = chat_with_duckchat(prompt)
    print(response)

if __name__ == "__main__":
    main()
