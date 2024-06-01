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

