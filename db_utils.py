import json

from database import get_connection


# Show all the commands in the database
def show_commands():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT id, command, description
        FROM commands
    """)

    rows = cur.fetchall()

    print("\nAvailable Commands:\n")

    for row in rows:
        print(f"ID: {row[0]} | Command: {row[1]} | Description: {row[2]}")

    conn.close()

# Commands deletion 
def delete_command(command_id):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "DELETE FROM commands WHERE id = ?",
        (command_id,)
    )

    conn.commit()

    if cur.rowcount > 0:
        print(f"\nDeleted command with ID {command_id}")
    else:
        print(f"\nNo command found with ID {command_id}")

    conn.close()

# Dropping a db table (use with caution)
def drop_table(table_name):
    allowed_tables = ["commands", "command_history"]

    if table_name not in allowed_tables:
        print("Invalid table name.")
        return

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(f"DROP TABLE {table_name}")

    conn.commit()
    conn.close()

    print(f"{table_name} table dropped.")

# Update Command/Description/Payload by ID
def update_command(command_id):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT command, description, payload
        FROM commands
        WHERE id = ?
    """, (command_id,))

    row = cur.fetchone()

    if not row:
        print("Command not found.")
        conn.close()
        return

    current_command, current_description, current_payload = row

    print(f"\nCurrent command: {current_command}")
    print(f"Current description: {current_description}")
    print(f"Current payload: {current_payload}")

    new_command = input(
        "\nEnter new command name "
        "(leave blank to keep current): "
    ).strip()

    new_description = input(
        "Enter new description "
        "(leave blank to keep current): "
    ).strip()

    print(
        "\nEnter new payload JSON "
        "(leave blank to keep current)"
    )

    new_payload = input("Payload: ").strip()

    updated_command = (
        new_command if new_command else current_command
    )

    updated_description = (
        new_description
        if new_description
        else current_description
    )

    updated_payload = (
        new_payload if new_payload else current_payload
    )

    # validate JSON before updating
    try:
        json.loads(updated_payload)
    except json.JSONDecodeError:
        print("Invalid JSON payload format.")
        conn.close()
        return

    cur.execute("""
        UPDATE commands
        SET command = ?, description = ?, payload = ?
        WHERE id = ?
    """, (
        updated_command,
        updated_description,
        updated_payload,
        command_id
    ))

    conn.commit()
    conn.close()

    print(
        f"\nCommand ID {command_id} updated successfully."
    )

if __name__ == "__main__":
    print("\nDatabase Utilities")
    print("1. Delete command by ID")
    print("2. Update command")
    print("3. Drop table")

    choice = input("\nChoose an option: ")

    match choice:
        case "1":
            show_commands()

            try:
                command_id = int(
                    input("\nEnter command ID to delete: ")
                )
                delete_command(command_id)

            except ValueError:
                print("Invalid ID")

        case "2":
            show_commands()

            try:
                command_id = int(
                    input("\nEnter command ID to update: ")
                )
                update_command(command_id)

            except ValueError:
                print("Invalid ID")

        case "3":
            print(
                "Warning: This action is irreversible."
            )

            table_name = input(
                "\nEnter table name to drop: "
            ).strip()

            drop_table(table_name)

        case _:
            print("Invalid option selected.")