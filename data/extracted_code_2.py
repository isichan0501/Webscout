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


