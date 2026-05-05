from executor import execute_command
from database import get_connection
from rich.console import Console


console = Console()

def handle_input(user_input):
    parts = user_input.split()

    if not parts:
        return
    
    command = parts[0]

    if command == "run":
        if len(parts) < 2:
            # print("Usage: run <command_name>")
            return
        
        execute_command(parts[1])

    elif command == "list":
        conn = get_connection()
        cur = conn.cursor()

        cur.execute("SELECT command, description FROM commands")
        rows = cur.fetchall()
        
        for row in rows:
            console.print(f"[bold turquoise4]{row[0]}[/bold turquoise4]: {row[1]}")
            console.print("-" * 40)
        
        conn.close()
    
    elif command == "exit":
        raise SystemExit
    
    elif command == "cls":
        console.clear()

    elif command == "help":
        console.print("[bold cyan]Available commands:[/bold cyan]")
        console.print("\n[bold dodger_blue1]run <command_name>[/bold dodger_blue1] - Execute a command")
        console.print("[bold dodger_blue1]list[/bold dodger_blue1] - List all available commands")
        console.print("[bold dodger_blue1]exit[/bold dodger_blue1] - Exit the application")
        console.print("[bold dodger_blue1]cls[/bold dodger_blue1] - Clear the screen")
        console.print("[bold dodger_blue1]help[/bold dodger_blue1] - Show this help message\n")
    
    else:
        console.print("[bold red]E400:[/bold red] Unknown command. Available commands: run, list, exit.")