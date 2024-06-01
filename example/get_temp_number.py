from rich.console import Console
from webscout import tempid

def get_temp_number(country="Finland"):
    console = Console()
    phone = tempid.TemporaryPhoneNumber()

    try:
        number = phone.get_number(country=country)
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
