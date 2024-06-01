from __future__ import annotations
from typing import List, Optional
from webscout.LLM import LLM
from webscout import DeepWEBS
import warnings

system_message: str = (
    "As an AI assistant, I have been designed with advanced capabilities, including real-time access to online resources. This enables me to enrich our conversations and provide you with informed and accurate responses, drawing from a vast array of information. With each interaction, my goal is to create a seamless and meaningful connection, offering insights and sharing relevant content."
    "My directives emphasize the importance of respect, impartiality, and intellectual integrity. I am here to provide unbiased responses, ensuring an ethical and respectful exchange. I will respect your privacy and refrain from sharing any personal information that may be obtained during our conversations or through web searches, only utilizing web search functionality when necessary to provide the most accurate and up-to-date information."
    "Together, let's explore a diverse range of topics, creating an enjoyable and informative experience, all while maintaining the highest standards of privacy and respect"
)

warnings.filterwarnings("ignore", category=UserWarning, module="curl_cffio", lineno=205)
LLM = LLM(model="mistralai/Mixtral-8x22B-Instruct-v0.1", system_message=system_message)

def perform_web_search(query):
    D = DeepWEBS()
    search_params = D.DeepSearch(
        queries=[query],
        result_num=10,
        safe=True,
        types=["web"],
        extract_webpage=True,
        overwrite_query_html=True,
        overwrite_webpage_html=True,
    )
    results = D.queries_to_search_results(search_params)
    return results

def chat(user_input: str, result_num: int = 10) -> Optional[str]:
    search_results = perform_web_search(user_input)
    url_results = []
    for result in search_results[0]['query_results']:
        url_results.append(f"{result['title']} ({result['site']}): {result['url']}")
    formatted_results = "\n".join(url_results)
    messages = [
        {"role": "user", "content": f"User question is:\n{user_input}\nwebsearch results are:\n{formatted_results}"},
    ]
    response = LLM.chat(messages)
    return response

def main():
    while True:
        user_input = input("User: ")
        response = chat(user_input)
        if response:
            print("AI:", response)
        else:
            print("No response")

if __name__ == "__main__":
    main()
