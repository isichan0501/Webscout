from webscout import OPENGPT

opengpt = OPENGPT(is_conversation=True, max_tokens=8000, timeout=30, assistant_id="bca37014-6f97-4f2b-8928-81ea8d478d88")
while True:
    # Prompt the user for input
    prompt = input("Enter your prompt: ")
    # Send the prompt to the OPENGPT model and print the response
    response_str = opengpt.chat(prompt)
    print(response_str)

