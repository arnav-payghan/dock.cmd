from database import init_db
from command_parser import handle_input
from rich.console import Console

console = Console()

def main():
    init_db()
    console.clear()
    console.print("[bold green]*[/bold green]", "[bold green]=[/bold green]" * 70, "[bold green]*[/bold green]")
    console.print("""
        [bold green]
    ██████╗  ██████╗  ██████╗██╗  ██╗    ██████╗███╗   ███╗██████╗
    ██╔══██╗██╔═══██╗██╔════╝██║ ██╔╝   ██╔════╝████╗ ████║██╔══██╗
    ██║  ██║██║   ██║██║     █████╔╝    ██║     ██╔████╔██║██║  ██║
    ██║  ██║██║   ██║██║     ██╔═██╗    ██║     ██║╚██╔╝██║██║  ██║
    ██████╔╝╚██████╔╝╚██████╗██║  ██╗██╗╚██████╗██║ ╚═╝ ██║██████╔╝
    ╚═════╝  ╚═════╝  ╚═════╝╚═╝  ╚═╝╚═╝ ╚═════╝╚═╝     ╚═╝╚═════╝
        [/bold green]
        """)
    console.print("[bold green]*[/bold green]", "[bold green]=[/bold green]" * 70, "[bold green]*[/bold green]")
    console.print("\nType [bold cyan]help[/bold cyan] to check the available commands.")
    console.print("Or type [bold red]exit[/bold red] to leave the terminal.\n")

    while True:
        user_input = console.input("[bold yellow]> [/bold yellow]")
        try:
            handle_input(user_input)
        except SystemExit:
            console.print("[bold red]Goodbye![/bold red]")
            break

if __name__ == "__main__":
    main()