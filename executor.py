import subprocess
import webbrowser
import json
from database import get_connection
from rich.console import Console


console = Console()

def execute_command(command_name):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "SELECT payload FROM commands WHERE command = ?",
        (command_name,)
    )

    result = cur.fetchone()

    if not result:
        console.print("[bold red]E404:[/bold red] Command not found.\n")
        return

    payload = json.loads(result[0])

    for action in payload["actions"]:
        if action["type"] == "url":
            webbrowser.open(action["value"])

        elif action["type"] == "app":
            try:
                subprocess.Popen(
                    action["value"],
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.DEVNULL,
                    stdin=subprocess.DEVNULL,
                    creationflags=subprocess.DETACHED_PROCESS
                )
            except Exception as e:
                conn.close()
                return f"E500: Failed to open app - {str(e)}"
            
    cur.execute(
        "INSERT INTO command_history (command_name, status) VALUES (?, ?)",
        (command_name, "success")
    )

    console.print("[bold dark_green]S000:[/bold dark_green] Command executed successfully. \n")

    conn.commit()
    conn.close()