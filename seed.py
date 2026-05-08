import json
from database import get_connection


def seed_commands():
    conn = get_connection()
    cur = conn.cursor()

    commands = [
        # (
        #     "command_name",
        #     "description of the command",
        #     json.dumps({
        #         "actions": [
        #             {"type": "app", "value": "file_path"},
        #             {"type": "url", "value": "https://www.website.com"}
        #         ]
        #     })
        # ),
        # Type required data below

        (
            "youtube",
            "Just wanna screen some random videos, eh?",
            json.dumps({
                "actions": [
                    {"type": "url", "value": "https://www.youtube.com"}
                ]
            })
        ),
        (
            "whatsapp",
            "work or socialize, you decide.",
            json.dumps({
                "actions": [
                    {"type": "url", "value": "https://web.whatsapp.com"}
                ]
            })
        ),
        (
            "github",
            "why? but alright! here's your coding hub.",
            json.dumps({
                "actions": [
                    {"type": "url", "value": "https://www.github.com"}
                ]
            })
        )
    ]

    for cmd in commands:
        try:
            cur.execute(
                "INSERT INTO commands (command, description, payload) VALUES (?, ?, ?)",
                cmd
            )
        except:
            pass
    
    conn.commit()
    conn.close()

if __name__ == "__main__": 
    seed_commands()