"""以下は、[README.md](file:///c%3A/Users/sibuy/anaconda3/envs/mygpt/Scripts/Webscout/README.md#1%2C1-1%2C1) から抽出されたPythonコードを関数として整理し、それぞれの関数を個別のPythonファイルとして [example](file:///c%3A/Users/sibuy/anaconda3/envs/mygpt/Scripts/Webscout/README.md#45%2C30-45%2C30) フォルダに保存するための手順です。"""


### 1. Temp Number Function
```python:example/temp_number.py
from rich.console import Console
from webscout import tempid

def get_temp_number():
    console = Console()
    phone = tempid.TemporaryPhoneNumber()

    try:
        number = phone.get_number(country="Finland")
        console.print(f"Your temporary phone number: [bold cyan]{number}[/bold cyan]")
        import time
        time.sleep(30)  # Adjust the waiting time as needed

        messages = phone.get_messages(number)
        if messages:
            console.print(f"[bold green]{messages[0].frm}:[/] {messages[0].content}")
        else:
            console.print("No messages received.")

    except Exception as e:
        console.print(f"[bold red]An error occurred: {e}")

if __name__ == "__main__":
    get_temp_number()
```
