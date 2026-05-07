import json
from database import get_connection


def seed_commands():
    conn = get_connection()
    cur = conn.cursor()

    commands = [
        # (
        #     "practice",
        #     "Open coding practice websites",
        #     json.dumps({
        #         "actions": [
        #             {"type": "url", "value": "https://www.youtube.com"},
        #             {"type": "url", "value": "https://www.leetcode.com"}
        #         ]
        #     })
        # ),
        (
            "chill",
            "Need a break? Chill out with some entertainment.",
            json.dumps({
                "actions": [
                    {"type": "url", "value": "https://www.youtube.com"},
                    {"type": "url", "value": "https://www.netflix.com"},
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