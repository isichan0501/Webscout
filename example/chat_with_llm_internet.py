from __future__ import annotations
from typing import List, Optional
from webscout.LLM import LLM
from webscout import WEBS
import warnings

system_message: str = (
    "As an AI assistant, I have been designed with advanced capabilities, including real-time access to online resources. This enables me to enrich our conversations and provide you with informed and accurate responses, drawing from a vast array of information. With each interaction, my goal is to create a seamless and meaningful connection, offering insights and sharing relevant content."
    "My directives emphasize the importance of respect, impartiality, and intellectual integrity. I am here to provide unbiased responses, ensuring an ethical and respectful exchange. I will respect your privacy and refrain from sharing any personal information that may be obtained during our conversations or through web searches, only utilizing web search functionality when necessary to provide the most accurate and up-to-date information."
    "Together, let's explore a diverse range of topics, creating an enjoyable and informative experience, all while maintaining the highest standards of privacy and respect"
)

warnings.filterwarnings("ignore", category=UserWarning, module="curl_cffio", lineno=205)
LLM = LLM(model="mistralai/Mixtral-8x22B-Instruct-v0.1", system_message=system_message)

def chat(user_input: str, webs: WEBS, max_results: int = 10) -> Optional[str]:
    search_results: List[str] = []
    for r in webs.text(
        user_input, region="wt-wt", safesearch="off", timelimit="y", max_results=max_results
    ):
        search_results.append(str(r))
    messages = [
        {"role": "user", "content": user_input + "\n" + "websearch results are:" + "\n".join(search_results)},
    ]
    response = LLM.chat(messages)
    return response

def main():
    while True:
        user_input = input("User: ")
        with WEBS() as webs:
            response = chat(user_input, webs)
        if response:
            print("AI:", response)
        else:
            print("No response")

if __name__ == "__main__":
    main()
