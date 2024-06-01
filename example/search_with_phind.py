from webscout import PhindSearch

def search_with_phind(prompt):
    ph = PhindSearch()
    response = ph.ask(prompt)
    message = ph.get_message(response)
    return message

def main():
    prompt = "write an essay on phind"
    response = search_with_phind(prompt)
    print(response)

if __name__ == "__main__":
    main()
