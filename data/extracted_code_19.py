import webscout
from webscout import GEMINI

# Replace with the path to your bard.google.com.cookies.json file
COOKIE_FILE = "path/to/bard.google.com.cookies.json"

# Optional: Provide proxy details if needed
PROXIES = {
    "http": "http://proxy_server:port",
    "https": "https://proxy_server:port",
}

# Initialize GEMINI with cookie file and optional proxies
gemini = GEMINI(cookie_file=COOKIE_FILE, proxy=PROXIES)

# Ask a question and print the response
response = gemini.chat("What is the meaning of life?")
print(response)

