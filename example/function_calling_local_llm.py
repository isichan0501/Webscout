from webscout.Local import Model, Thread, formats
from webscout import DeepWEBS
from webscout.Local.utils import download_model
from webscout.Local.model import Model
from webscout.Local.thread import Thread
from webscout.Local.samplers import SamplerSettings

def deepwebs_search(query, max_results=5):
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
    for result in search_results[0]:
        formatted_results.append(f"Title: {result['title']}\nURL: {result['url']}\n")
    return "\n".join(formatted_results)

def function_calling_local_llm(repo_id, filename, system_prompt):
    model_path = download_model(repo_id, filename, token='')
    model = Model(model_path, n_gpu_layers=10)
    sampler = SamplerSettings(temp=0.7, top_p=0.9)
    custom_chatml = formats.chatml.copy()
    custom_chatml['system_content'] = system_prompt
    thread = Thread(model, custom_chatml, sampler=sampler)
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
    while True:
        user_input = input("You: ")
        response = thread.send(user_input)
        print("Bot: ", response)

def main():
    repo_id = "OEvortex/HelpingAI-9B"
    filename = "helpingai-9b.Q4_0.gguf"
    system_prompt = "You are a helpful AI assistant. Respond to user queries concisely. If a user asks for information that requires a web search, use the `deepwebs_search` tool. Do not call the tool if it is not necessary."
    function_calling_local_llm(repo_id, filename, system_prompt)

if __name__ == "__main__":
    main()
