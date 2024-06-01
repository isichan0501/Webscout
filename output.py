"""webscoutのサンプルコード"""



from rich.console import Console
from webscout import tempid

def main():
    console = Console()
    phone = tempid.TemporaryPhoneNumber()

    try:
        # Get a temporary phone number for a specific country (or random)
        number = phone.get_number(country="Finland")
        console.print(f"Your temporary phone number: [bold cyan]{number}[/bold cyan]")

        # Pause execution briefly (replace with your actual logic)
        # import time module
        import time
        time.sleep(30)  # Adjust the waiting time as needed

        # Retrieve and print messages
        messages = phone.get_messages(number)
        if messages:
            # Access individual messages using indexing:
            console.print(f"[bold green]{messages[0].frm}:[/] {messages[0].content}")
            # (Add more lines if you expect multiple messages)
        else:
            console.print("No messages received.")

    except Exception as e:
        console.print(f"[bold red]An error occurred: {e}")

if __name__ == "__main__":
    main()


import asyncio
from rich.console import Console
from rich.table import Table
from rich.text import Text
from webscout import tempid

async def main() -> None:
    console = Console()
    client = tempid.Client()
    
    try:
        domains = await client.get_domains()
        if not domains:
            console.print("[bold red]No domains available. Please try again later.")
            return

        email = await client.create_email(domain=domains[0].name)
        console.print(f"Your temporary email: [bold cyan]{email.email}[/bold cyan]")
        console.print(f"Token for accessing the email: [bold cyan]{email.token}[/bold cyan]")

        while True:
            messages = await client.get_messages(email.email)
            if messages is not None:
                break

        if messages:
            table = Table(show_header=True, header_style="bold magenta")
            table.add_column("From", style="bold cyan")
            table.add_column("Subject", style="bold yellow")
            table.add_column("Body", style="bold green")
            for message in messages:
                body_preview = Text(message.body_text if message.body_text else "No body")
                table.add_row(message.email_from or "Unknown", message.subject or "No Subject", body_preview)
            console.print(table)
        else:
            console.print("No messages found.")
    
    except Exception as e:
        console.print(f"[bold red]An error occurred: {e}")
    
    finally:
        await client.close()

if __name__ == '__main__':
    asyncio.run(main())

import sys
from webscout import transcriber

def extract_transcript(video_id):
    """Extracts the transcript from a YouTube video."""
    try:
        transcript_list = transcriber.list_transcripts(video_id)
        for transcript in transcript_list:
            transcript_data_list = transcript.fetch()
            lang = transcript.language
            transcript_text = ""
            if transcript.language_code == 'en':
                for line in transcript_data_list:
                    start_time = line['start']
                    end_time = start_time + line['duration']
                    formatted_line = f"{start_time:.2f} - {end_time:.2f}: {line['text']}\n"
                    transcript_text += formatted_line
                return transcript_text
            elif transcript.is_translatable:
                english_transcript_list = transcript.translate('en').fetch()
                for line in english_transcript_list:
                    start_time = line['start']
                    end_time = start_time + line['duration']
                    formatted_line = f"{start_time:.2f} - {end_time:.2f}: {line['text']}\n"
                    transcript_text += formatted_line
                return transcript_text
        print("Transcript extraction failed. Please check the video URL.")
    except Exception as e:
        print(f"Error: {e}")

def main():
    video_url = input("Enter the video link: ")

    if video_url:
        video_id = video_url.split("=")[1]
        print("Video URL:", video_url)
        submit = input("Press 'Enter' to get the transcript or type 'exit' to quit: ")
        if submit == '':
            print("Extracting Transcript...")
            transcript = extract_transcript(video_id)
            print('Transcript:')
            print(transcript)
            print("__________________________________________________________________________________")
        elif submit.lower() == 'exit':
            print("Exiting...")
            sys.exit()
        else:
            print("Invalid input. Please try again.")

if __name__ == "__main__":
    main()

from webscout import DeepWEBS

def perform_web_search(query):
    # Initialize the DeepWEBS class
    D = DeepWEBS()
    
    # Set up the search parameters
    search_params = D.DeepSearch(
        queries=[query], # Query to search
        result_num=5, # Number of search results
        safe=True, # Enable SafeSearch
        types=["web"], # Search type: web
        extract_webpage=True, # True for extracting webpages
        overwrite_query_html=False,
        overwrite_webpage_html=False,
    )
    
    # Execute the search and retrieve results
    results = D.queries_to_search_results(search_params)
    
    return results

def print_search_results(results):
    """
    Print the search results.
    
    Args:
    - search_results (list): List of search results to print.
    """
    if results:
        for index, result in enumerate(results, start=1):
            print(f"Result {index}: {result}")
    else:
        print("No search results found.")

def main():
    # Prompt the user for a search query
    query = input("Enter your search query: ")
    
    # Perform the web search
    results = perform_web_search(query)
    
    # Print the search results
    print_search_results(results)

if __name__ == "__main__":
    main()


from webscout import play_audio

message = "This is an example of text-to-speech."
audio_content = play_audio(message, voice="Brian")

# Save the audio to a file
with open("output.mp3", "wb") as f:
    f.write(audio_content)

from webscout import WEBS

# Text search for 'live free or die' using DuckDuckGo.com 
with WEBS() as WEBS:
    for r in WEBS.text('live free or die', region='wt-wt', safesearch='off', timelimit='y', max_results=10):
        print(r)

    for r in WEBS.text('live free or die', region='wt-wt', safesearch='off', timelimit='y', max_results=10):
        print(r)

from webscout import WEBS

# Instant answers for the query "sun" using DuckDuckGo.com 
with WEBS() as WEBS:
    for r in WEBS.answers("sun"):
        print(r)

from webscout import WEBS

# Image search for the keyword 'butterfly' using DuckDuckGo.com 
with WEBS() as WEBS:
    keywords = 'butterfly'
    WEBS_images_gen = WEBS.images(
      keywords,
      region="wt-wt",
      safesearch="off",
      size=None,
      type_image=None,
      layout=None,
      license_image=None,
      max_results=10,
    )
    for r in WEBS_images_gen:
        print(r)

from webscout import WEBS

# Video search for the keyword 'tesla' using DuckDuckGo.com 
with WEBS() as WEBS:
    keywords = 'tesla'
    WEBS_videos_gen = WEBS.videos(
      keywords,
      region="wt-wt",
      safesearch="off",
      timelimit="w",
      resolution="high",
      duration="medium",
      max_results=10,
    )
    for r in WEBS_videos_gen:
        print(r)

from webscout import WEBS
import datetime

def fetch_news(keywords, timelimit):
    news_list = []
    with WEBS() as webs_instance:
        WEBS_news_gen = webs_instance.news(
            keywords,
            region="wt-wt",
            safesearch="off",
            timelimit=timelimit,
            max_results=20
        )
        for r in WEBS_news_gen:
            # Convert the date to a human-readable format using datetime
            r['date'] = datetime.datetime.fromisoformat(r['date']).strftime('%B %d, %Y')
            news_list.append(r)
    return news_list

def _format_headlines(news_list, max_headlines: int = 100):
    headlines = []
    for idx, news_item in enumerate(news_list):
        if idx >= max_headlines:
            break
        new_headline = f"{idx + 1}. {news_item['title'].strip()} "
        new_headline += f"(URL: {news_item['url'].strip()}) "
        new_headline += f"{news_item['body'].strip()}"
        new_headline += "\n"
        headlines.append(new_headline)

    headlines = "\n".join(headlines)
    return headlines

# Example usage
keywords = 'latest AI news'
timelimit = 'd'
news_list = fetch_news(keywords, timelimit)

# Format and print the headlines
formatted_headlines = _format_headlines(news_list)
print(formatted_headlines)


from webscout import WEBS

# Map search for the keyword 'school' in 'anantnag' using DuckDuckGo.com
with WEBS() as WEBS:
    for r in WEBS.maps("school", place="anantnag", max_results=50):
        print(r)

from webscout import WEBS

# Translation of the keyword 'school' to German ('hi') using DuckDuckGo.com
with WEBS() as WEBS:
    keywords = 'school'
    r = WEBS.translate(keywords, to="hi")
    print(r)

from webscout import WEBS

# Suggestions for the keyword 'fly' using DuckDuckGo.com
with WEBS() as WEBS:
    for r in WEBS.suggestions("fly"):
        print(r)

from webscout import WEBS as w
R = w().chat("hello", model='claude-3-haiku') # GPT-3.5 Turbo
print(R)

from webscout import PhindSearch

# Create an instance of the PHIND class
ph = PhindSearch()

# Define a prompt to send to the AI
prompt = "write a essay on phind"

# Use the 'ask' method to send the prompt and receive a response
response = ph.ask(prompt)

# Extract and print the message from the response
message = ph.get_message(response)
print(message)

from webscout import YEPCHAT

# Instantiate the YEPCHAT class with default parameters
YEPCHAT = YEPCHAT()

# Define a prompt to send to the AI
prompt = "What is the capital of France?"

# Use the 'cha' method to get a response from the AI
r = YEPCHAT.chat(prompt)
print(r)



from webscout import YouChat
from rich import print

ai = YouChat(
    is_conversation=True,
    max_tokens=800,
    timeout=30,
    intro=None,
    filepath=None,
    update_file=True,
    proxies={},
    history_offset=10250,
    act=None,
)

prompt = "what is meaning of life"

response = ai.ask(prompt)

# Extract and print the message from the response
message = ai.get_message(response)
print(message)

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

from webscout import Berlin4h
# Create an instance of the PERPLEXITY class
ai = Berlin4h(
    is_conversation=True,
    max_tokens=800,
    timeout=30,
    intro=None,
    filepath=None,
    update_file=True,
    proxies={},
    history_offset=10250,
    act=None,
)

# Example usage:
prompt = "Explain the concept of recursion in simple terms."
response = ai.chat(prompt)
print(response)

from webscout import BLACKBOXAI
from rich import print

ai = BLACKBOXAI(
    is_conversation=True,
    max_tokens=800,
    timeout=30,
    intro=None,
    filepath=None,
    update_file=True,
    proxies={},
    history_offset=10250,
    act=None,
    model=None # You can specify a model if needed
)

# Start an infinite loop for continuous interaction
while True:
    # Define a prompt to send to the AI
    prompt = input("Enter your prompt: ")
    
    # Check if the user wants to exit the loop
    if prompt.lower() == "exit":
        break
    
    # Use the 'chat' method to send the prompt and receive a response
    r = ai.chat(prompt)
    print(r)

from webscout import PERPLEXITY
# Create an instance of the PERPLEXITY class
perplexity = PERPLEXITY()

# Example usage:
prompt = "Explain the concept of recursion in simple terms."
response = perplexity.chat(prompt)
print(response)

from webscout import OPENGPT

opengpt = OPENGPT(is_conversation=True, max_tokens=8000, timeout=30, assistant_id="bca37014-6f97-4f2b-8928-81ea8d478d88")
while True:
    # Prompt the user for input
    prompt = input("Enter your prompt: ")
    # Send the prompt to the OPENGPT model and print the response
    response_str = opengpt.chat(prompt)
    print(response_str)

from webscout import KOBOLDAI

# Instantiate the KOBOLDAI class with default parameters
koboldai = KOBOLDAI()

# Define a prompt to send to the AI
prompt = "What is the capital of France?"

# Use the 'ask' method to get a response from the AI
response = koboldai.ask(prompt)

# Extract and print the message from the response
message = koboldai.get_message(response)
print(message)


from webscout import REKA

a = REKA(is_conversation=True, max_tokens=8000, timeout=30,api_key="")

prompt = "tell me about india"
response_str = a.chat(prompt)
print(response_str)

from webscout import Cohere

a = Cohere(is_conversation=True, max_tokens=8000, timeout=30,api_key="")

prompt = "tell me about india"
response_str = a.chat(prompt)
print(response_str)

from webscout import Xjai
from rich import print

ai = Xjai(
    is_conversation=True,
    max_tokens=800,
    timeout=30,
    intro=None,
    filepath=None,
    update_file=True,
    proxies={},
    history_offset=10250,
    act=None,
)

prompt = "Tell me about india"

response = ai.chat(prompt)
print(response)

from webscout import ThinkAnyAI

ai = ThinkAnyAI(
    is_conversation=True,
    max_tokens=800,
    timeout=30,
    intro=None,
    filepath=None,
    update_file=True,
    proxies={},
    history_offset=10250,
    act=None,
    web_search=False,
)

prompt = "what is meaning of life"

response = ai.ask(prompt)

# Extract and print the message from the response
message = ai.get_message(response)
print(message)

from webscout import ChatGPTUK
# Create an instance of the PERPLEXITY class
ai = ChatGPTUK(
    is_conversation=True,
    max_tokens=800,
    timeout=30,
    intro=None,
    filepath=None,
    update_file=True,
    proxies={},
    history_offset=10250,
    act=None,
)

# Example usage:
prompt = "Explain the concept of recursion in simple terms."
response = ai.chat(prompt)
print(response)


from webscout.LLM import LLM

# Read the system message from the file
with open('system.txt', 'r') as file:
    system_message = file.read()

# Initialize the LLM class with the model name and system message
llm = LLM(model="microsoft/WizardLM-2-8x22B", system_message=system_message)

while True:
    # Get the user input
    user_input = input("User: ")

    # Define the messages to be sent
    messages = [
        {"role": "user", "content": user_input}
    ]

    # Use the mistral_chat method to get the response
    response = llm.chat(messages)

    # Print the response
    print("AI: ", response)

from webscout.Local.utils import download_model
from webscout.Local.model import Model
from webscout.Local.thread import Thread
from webscout.Local import formats
# 1. Download the model
repo_id = "microsoft/Phi-3-mini-4k-instruct-gguf"  # Replace with the desired Hugging Face repo
filename = "Phi-3-mini-4k-instruct-q4.gguf" # Replace with the correct filename
model_path = download_model(repo_id, filename)

# 2. Load the model 
model = Model(model_path, n_gpu_layers=4)  

# 3. Create a Thread for conversation
thread = Thread(model, formats.phi3)

# 4. Start interacting with the model
thread.interact()

from webscout.Local import Model, Thread, formats
from webscout import DeepWEBS
from webscout.Local.utils import download_model
from webscout.Local.model import Model
from webscout.Local.thread import Thread
from webscout.Local import formats
from webscout.Local.samplers import SamplerSettings
def deepwebs_search(query, max_results=5):
    """Performs a web search using DeepWEBS and returns results as JSON."""
    deepwebs = DeepWEBS()
    search_config = DeepWEBS.DeepSearch(
        queries=[query],
        max_results=max_results,
        extract_webpage=False,
        safe=False,
        types=["web"],
        overwrite_query_html=True,
        overwrite_webpage_html=True,
    )
    search_results = deepwebs.queries_to_search_results(search_config)
    formatted_results = []
    for result in search_results[0]:  # Assuming only one query
        formatted_results.append(f"Title: {result['title']}\nURL: {result['url']}\n")
    return "\n".join(formatted_results)

# Load your model
repo_id = "OEvortex/HelpingAI-9B" 
filename = "helpingai-9b.Q4_0.gguf"
model_path = download_model(repo_id, filename, token='')

# 2. Load the model 
model = Model(model_path, n_gpu_layers=10)

# Create a Thread
system_prompt = "You are a helpful AI assistant. Respond to user queries concisely. If a user asks for information that requires a web search, use the `deepwebs_search` tool. Do not call the tool if it is not necessary."
sampler = SamplerSettings(temp=0.7, top_p=0.9)  # Adjust these values as needed
# 4. Create a custom chatml format with your system prompt
custom_chatml = formats.chatml.copy()
custom_chatml['system_content'] = system_prompt
thread = Thread(model, custom_chatml, sampler=sampler)
# Add the deepwebs_search tool
thread.add_tool({
    "type": "function",
    "function": {
        "name": "deepwebs_search",
        "description": "Performs a web search using DeepWEBS and returns the title and URLs of the results.",
        "execute": deepwebs_search,
        "parameters": {
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": "The query to search on the web",
                },
                "max_results": {
                    "type": "integer",
                    "description": "Maximum number of search results (default: 5)",
                },
            },
            "required": ["query"],
        },
    },
})

# Start interacting with the model
while True:
    user_input = input("You: ")
    response = thread.send(user_input)
    print("Bot: ", response) 

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

# Ignore the specific UserWarning
warnings.filterwarnings("ignore", category=UserWarning, module="curl_cffio", lineno=205)
LLM = LLM(model="mistralai/Mixtral-8x22B-Instruct-v0.1", system_message=system_message)


def chat(
    user_input: str, webs: WEBS, max_results: int = 10
) -> Optional[str]:
    """
    Chat function to perform a web search based on the user input and generate a response using the LLM model.

    Parameters
    ----------
    user_input : str
        The user input to be used for the web search
    webs : WEBS
        The web search instance to be used to perform the search
    max_results : int, optional
        The maximum number of search results to include in the response, by default 10

    Returns
    -------
    Optional[str]
        The response generated by the LLM model, or None if there is no response
    """
    # Perform a web search based on the user input
    search_results: List[str] = []
    for r in webs.text(
        user_input, region="wt-wt", safesearch="off", timelimit="y", max_results=max_results
    ):
        search_results.append(str(r))  # Convert each result to a string

    # Define the messages to be sent, including the user input, search results, and system message
    messages = [
        {"role": "user", "content": user_input + "\n" + "websearch results are:" + "\n".join(search_results)},
    ]

    # Use the chat method to get the response
    response = LLM.chat(messages)

    return response


if __name__ == "__main__":
    while True:
        # Get the user input
        user_input = input("User: ")

        # Perform a web search based on the user input
        with WEBS() as webs:
            response = chat(user_input, webs)

        # Print the response
        if response:
            print("AI:", response)
        else:
            print("No response")

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

# Ignore the specific UserWarning
warnings.filterwarnings("ignore", category=UserWarning, module="curl_cffio", lineno=205)

LLM = LLM(model="mistralai/Mixtral-8x22B-Instruct-v0.1", system_message=system_message)

def perform_web_search(query):
    # Initialize the DeepWEBS class
    D = DeepWEBS()

    # Set up the search parameters
    search_params = D.DeepSearch(
        queries=[query],  # Query to search
        result_num=10,  # Number of search results
        safe=True,  # Enable SafeSearch
        types=["web"],  # Search type: web
        extract_webpage=True,  # True for extracting webpages
        overwrite_query_html=True,
        overwrite_webpage_html=True,
    )

    # Execute the search and retrieve results
    results = D.queries_to_search_results(search_params)
    return results

def chat(user_input: str, result_num: int = 10) -> Optional[str]:
    """
    Chat function to perform a web search based on the user input and generate a response using the LLM model.

    Parameters
    ----------
    user_input : str
        The user input to be used for the web search
    max_results : int, optional
        The maximum number of search results to include in the response, by default 10

    Returns
    -------
    Optional[str]
        The response generated by the LLM model, or None if there is no response
    """
    # Perform a web search based on the user input
    search_results = perform_web_search(user_input)

    # Extract URLs from search results
    url_results = []
    for result in search_results[0]['query_results']:
        url_results.append(f"{result['title']} ({result['site']}): {result['url']}")

    # Format search results
    formatted_results = "\n".join(url_results)

    # Define the messages to be sent, including the user input, search results, and system message
    messages = [
        {"role": "user", "content": f"User question is:\n{user_input}\nwebsearch results are:\n{formatted_results}"},
    ]

    # Use the chat method to get the response
    response = LLM.chat(messages)
    return response

if __name__ == "__main__":
    while True:
        # Get the user input
        user_input = input("User: ")

        # Perform a web search based on the user input
        response = chat(user_input)

        # Print the response
        if response:
            print("AI:", response)
        else:
            print("No response")

import time
import uuid
from typing import Dict, Any, Optional, AsyncGenerator
from rich.console import Console
from rich.markdown import Markdown
from rich.panel import Panel
from rich.style import Style
import webscout
import webscout.AIutel
import g4f
from webscout.g4f import *
from webscout.async_providers import mapper as async_provider_map

class TaskExecutor:
    """
    Manages an interactive chat session, handling user input, AI responses, 
    and optional features like web search, code execution, and text-to-speech.
    """

    def __init__(self) -> None:
        """Initializes the conversational assistant with default settings."""
        self._console: Console = Console()

        # Session configuration
        self._selected_provider: str = "phind"
        self._selected_model: str = "Phind Model"
        self._conversation_enabled: bool = True
        self._max_tokens: int = 600
        self._temperature: float = 0.2
        self._top_k: int = -1
        self._top_p: float = 0.999
        self._timeout: int = 30
        self._auth_token: str = None  # API key, if required
        self._chat_completion_enabled: bool = True  # g4fauto
        self._ignore_working: bool = False  # Ignore working status of providers
        self._proxy_path: str = None  # Path to proxy configuration

        # History Management
        self._history_filepath: str = None
        self._update_history_file: bool = True
        self._history_offset: int = 10250

        # Prompt Engineering
        self._initial_prompt: str = None
        self._awesome_prompt_content: str = None 

        # Optional Features
        self._web_search_enabled: bool = False  # Enable web search
        self._rawdog_enabled: bool = True
        self._internal_script_execution_enabled: bool = False
        self._script_confirmation_required: bool = False
        self._selected_interpreter: str = "python"
        self._selected_optimizer: str = "code"
        self._suppress_output: bool = False  # Suppress verbose output

        # AI provider mapping
        self._ai_provider_mapping: Dict[str, Any] = {
            "phind": webscout.PhindSearch,
            "opengpt": webscout.OPENGPT,
            "koboldai": webscout.KOBOLDAI,
            "blackboxai": webscout.BLACKBOXAI,
            "llama2": webscout.LLAMA2,
            "yepchat": webscout.YEPCHAT,
            "leo": webscout.LEO,
            "groq": webscout.GROQ,
            "openai": webscout.OPENAI,
            "perplexity": webscout.PERPLEXITY,
            "you": webscout.YouChat,
            "xjai": webscout.Xjai,
            "cohere": webscout.Cohere,
            "reka": webscout.REKA,
            "thinkany": webscout.ThinkAnyAI,
            "gemini": webscout.GEMINI, 
            "berlin4h": webscout.Berlin4h,
            "chatgptuk": webscout.ChatGPTUK,
            "poe": webscout.POE,
            "basedgpt": webscout.BasedGPT,
        }

        # Initialize Rawdog if enabled
        if self._rawdog_enabled:
            self._rawdog_instance: webscout.AIutel.RawDog = webscout.AIutel.RawDog(
                quiet=self._suppress_output,
                internal_exec=self._internal_script_execution_enabled,
                confirm_script=self._script_confirmation_required,
                interpreter=self._selected_interpreter,
            )

            self._initial_prompt = self._rawdog_instance.intro_prompt

        # Initialize the selected AI model 
        self._ai_model = self._get_ai_model()

    def _get_ai_model(self):
        """
        Determines the appropriate AI model based on the selected provider, 
        including automatic provider selection and g4fauto support.
        """
        if self._selected_provider == "g4fauto":
            # Automatically select the best provider from g4f
            test = TestProviders(quiet=self._suppress_output, timeout=self._timeout)
            g4fauto = test.best if not self._ignore_working else test.auto
            if isinstance(g4fauto, str):
                self._selected_provider = "g4fauto+" + g4fauto
                self._ai_model = self._create_g4f_model(g4fauto)
            else:
                raise Exception(
                    "No working g4f provider found. "
                    "Consider running 'webscout.webai gpt4free test -y' first"
                )
        else:
            # Use the specified provider
            self._ai_model = self._ai_provider_mapping[self._selected_provider](
                is_conversation=self._conversation_enabled,
                max_tokens=self._max_tokens,
                timeout=self._timeout,
                intro=self._initial_prompt,
                filepath=self._history_filepath,
                update_file=self._update_history_file,
                proxies={},  # Load proxies from config if needed
                history_offset=self._history_offset,
                act=self._awesome_prompt_content, 
                model=self._selected_model,
                quiet=self._suppress_output,
                # auth=self._auth_token,  # Pass API key if required
            )
        return self._ai_model

    def _create_g4f_model(self, provider: str):
        """
        Creates a g4f model instance using the provided provider and webscout.WEBS for web search.
        """
        return webscout.g4f.GPT4FREE(
            provider=provider,
            auth=self._auth_token,
            max_tokens=self._max_tokens,
            chat_completion=self._chat_completion_enabled,
            ignore_working=self._ignore_working,
            timeout=self._timeout,
            intro=self._initial_prompt,
            filepath=self._history_filepath,
            update_file=self._update_history_file,
            proxies={},  # Load proxies from config if needed
            history_offset=self._history_offset,
            act=self._awesome_prompt_content, 
        )

    def process_query(self, query: str) -> None:
        """
        Processes a user query, potentially enhancing it with web search results, 
        passing it to the AI model, and handling the response.

        Args:
            query: The user's text input.

        Returns:
            None
        """
        if self._web_search_enabled:
            query = self._augment_query_with_web_search(query)

        # Apply code optimization if configured
        if self._selected_optimizer == "code":
            query = webscout.AIutel.Optimizers.code(query)

        try:
            response: str = self._ai_model.chat(query)
        except webscout.exceptions.FailedToGenerateResponseError as e:
            self._console.print(Markdown(f"LLM: [red]{e}[/red]"))
            return

        # Handle Rawdog responses if enabled
        if self._rawdog_enabled:
            self._handle_rawdog_response(response)
        else:
            self._console.print(Markdown(f"LLM: {response}"))

    def _augment_query_with_web_search(self, query: str) -> str:
        """Performs a web search and appends the results to the query.

        Args:
            query: The user's text input.

        Returns:
            str: The augmented query with web search results.
        """
        web_search_results = webscout.WEBS().text(query, max_results=3)
        if web_search_results:
            formatted_results = "\n".join(
                f"{i+1}. {result['title']} - {result['href']}\n\nBody: {result['body']}"
                for i, result in enumerate(web_search_results)
            )
            query += f"\n\n## Web Search Results are:\n\n{formatted_results}"
        return query

    def _handle_rawdog_response(self, response: str) -> None:
        """Handles AI responses, potentially executing them as code with Rawdog.

        Args:
            response: The AI model's response.

        Returns:
            None
        """
        try:
            is_feedback = self._rawdog_instance.main(response)
        except Exception as e:
            self._console.print(Markdown(f"LLM: [red]Error: {e}[/red]"))
            return
        if is_feedback:
            self._console.print(Markdown(f"LLM: {is_feedback}"))
        else:
            self._console.print(Markdown("LLM: (Script executed successfully)"))

    async def process_async_query(self, query: str) -> None:
        """
        Asynchronously processes a user query, potentially enhancing it with web search results, 
        passing it to the AI model, and handling the response.

        Args:
            query: The user's text input.

        Returns:
            None
        """
        if self._web_search_enabled:
            query = self._augment_query_with_web_search(query)

        # Apply code optimization if configured
        if self._selected_optimizer == "code":
            query = webscout.AIutel.Optimizers.code(query)

        async_model = self._get_async_ai_model()

        try:
            async for response in async_model.chat(query, stream=True):
                self._console.print(Markdown(f"LLM: {response}"), end="")
        except webscout.exceptions.FailedToGenerateResponseError as e:
            self._console.print(Markdown(f"LLM: [red]{e}[/red]"))
            return

        # Handle Rawdog responses if enabled
        if self._rawdog_enabled:
            self._handle_rawdog_response(response)
        else:
            self._console.print(Markdown(f"LLM: {response}"))

    def _get_async_ai_model(self):
        """
        Determines the appropriate asynchronous AI model based on the selected provider.
        """
        if self._selected_provider == "g4fauto":
            # Automatically select the best provider from g4f
            test = TestProviders(quiet=self._suppress_output, timeout=self._timeout)
            g4fauto = test.best if not self._ignore_working else test.auto
            if isinstance(g4fauto, str):
                self._selected_provider = "g4fauto+" + g4fauto
                self._ai_model = self._create_async_g4f_model(g4fauto)
            else:
                raise Exception(
                    "No working g4f provider found. "
                    "Consider running 'webscout gpt4free test -y' first"
                )
        else:
            # Use the specified provider
            if self._selected_provider in async_provider_map:
                self._ai_model = async_provider_map[self._selected_provider](
                    is_conversation=self._conversation_enabled,
                    max_tokens=self._max_tokens,
                    timeout=self._timeout,
                    intro=self._initial_prompt,
                    filepath=self._history_filepath,
                    update_file=self._update_history_file,
                    proxies={},  # Load proxies from config if needed
                    history_offset=self._history_offset,
                    act=self._awesome_prompt_content, 
                    model=self._selected_model,
                    quiet=self._suppress_output,
                    auth=self._auth_token,  # Pass API key if required
                )
            else:
                raise Exception(
                    f"Asynchronous provider '{self._selected_provider}' is not yet supported"
                )
        return self._ai_model

    def _create_async_g4f_model(self, provider: str):
        """
        Creates an asynchronous g4f model instance using the provided provider and webscout.WEBS for web search.
        """
        return webscout.g4f.AsyncGPT4FREE(
            provider=provider,
            auth=self._auth_token,
            max_tokens=self._max_tokens,
            chat_completion=self._chat_completion_enabled,
            ignore_working=self._ignore_working,
            timeout=self._timeout,
            intro=self._initial_prompt,
            filepath=self._history_filepath,
            update_file=self._update_history_file,
            proxies={},  # Load proxies from config if needed
            history_offset=self._history_offset,
            act=self._awesome_prompt_content,
        )

if __name__ == "__main__":
    assistant = TaskExecutor()
    while True:
        input_query = input("Enter your query: ")
        assistant.process_query(input_query)


