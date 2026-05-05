from database import init_db
from command_parser import handle_input
from rich.console import Console

console = Console()

def main():
    init_db()
    console.print("[bold green]"-"[/bold green]" * 40)
    console.print("[bold green]Welcome to the Command Shell![/bold green]")
    console.print("[bold green]"-"[/bold green]" * 40)
    console.print("\nType [bold cyan]help[/bold cyan] to see available commands.")

    while True:
        user_input = console.input("[bold yellow]> [/bold yellow]")
        try:
            handle_input(user_input)
        except SystemExit:
            console.print("[bold red]Goodbye![/bold red]")
            break

if __name__ == "__main__":
    main()