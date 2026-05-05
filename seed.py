import json
from database import get_connection


def seed_commands():
    conn = get_connection()
    cur = conn.cursor()

    commands = [
        (
            "practice",
            "Open coding practice websites",
            json.dumps({
                "actions": [
                    {"type": "url", "value": "https://www.youtube.com"},
                    {"type": "url", "value": "https://www.leetcode.com"}
                ]
            })
        ),
        (
            "develop",
            "Open coding environment",
            json.dumps({
                "actions": [
                    {"type": "url", "value": "https://www.github.com"},
                    {"type": "app", "value": "code"}
                ]
            })
        ),
        (
            "work",
            "Open work based apps like Gmail.",
            json.dumps({
                "actions": [
                    {"type": "url", "value": "https://www.gmail.com"},
                    {"type": "url", "value": "https://calendar.google.com"},
                    {"type": "url", "value": "https://web.whatsapp.com"}
                ]
            })
        ),
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