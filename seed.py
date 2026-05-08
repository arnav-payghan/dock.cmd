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
            "minecraft",
            "Chill session of Minecraft.",
            json.dumps({
                "actions": [
                    {"type": "app", "value": "C:\\Users\\arnav\\AppData\\Roaming\\.tlauncher\\legacy\\Minecraft\\LL.exe"},
                    {"type": "app", "value": "C:\\Users\\arnav\\AppData\\Local\\Discord\\app-1.0.9236\\Discord.exe"}
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