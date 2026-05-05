from database import init_db
from command_parser import handle_input
from rich.console import Console

console = Console()

def main():
    init_db()
    console.print("[bold green]Welcome to the Command Shell![/bold green]")
    console.print("Type [bold cyan]list[/bold cyan] to see available commands.")
    console.print("Type [bold cyan]run <command_name>[/bold cyan] to execute a command.")
    console.print("Type [bold cyan]exit[/bold cyan] to quit.")

    while True:
        user_input = console.input("[bold yellow]> [/bold yellow]")
        try:
            handle_input(user_input)
        except SystemExit:
            console.print("\n[bold red]Goodbye![/bold red]")
            break

if __name__ == "__main__":
    main()