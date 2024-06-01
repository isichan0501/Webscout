import webscout
from webscout import GEMINI

def search_with_gemini(prompt, cookie_file, proxies=None):
    gemini = GEMINI(cookie_file=cookie_file, proxy=proxies)
    response = gemini.chat(prompt)
    return response

def main():
    COOKIE_FILE = "path/to/bard.google.com.cookies.json"
    PROXIES = {
        "http": "http://proxy_server:port",
        "https": "https://proxy_server:port",
    }
    prompt = "What is the meaning of life?"
    response = search_with_gemini(prompt, COOKIE_FILE, PROXIES)
    print(response)

if __name__ == "__main__":
    main()
