from webscout.LLM import LLM

def chat_with_llm(user_input, model="microsoft/WizardLM-2-8x22B", system_message=""):
    llm = LLM(model=model, system_message=system_message)
    messages = [{"role": "user", "content": user_input}]
    response = llm.chat(messages)
    return response

def main():
    user_input = input("User: ")
    response = chat_with_llm(user_input)
    print("AI: ", response)

if __name__ == "__main__":
    main()
