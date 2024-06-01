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

