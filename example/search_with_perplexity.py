from webscout import PERPLEXITY

def search_with_perplexity(prompt):
    perplexity = PERPLEXITY()
    response = perplexity.chat(prompt)
    return response

def main():
    prompt = "Explain the concept of recursion in simple terms."
    response = search_with_perplexity(prompt)
    print(response)

if __name__ == "__main__":
    main()
