from webscout import YEPCHAT

# Instantiate the YEPCHAT class with default parameters
YEPCHAT = YEPCHAT()

# Define a prompt to send to the AI
prompt = "What is the capital of France?"

# Use the 'cha' method to get a response from the AI
r = YEPCHAT.chat(prompt)
print(r)


