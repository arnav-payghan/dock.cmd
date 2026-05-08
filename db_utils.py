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


if __name__ == "__main__":
    print("\nDatabase Utilities")
    print("1. Delete command by ID")
    print("2. Drop table")

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
            print("Warning: This action is irreversible.")
            table_name = input(
                "\nEnter table name to drop: "
            ).strip()

            drop_table(table_name)
            print(f"Dropped table successfully : {table_name}")
        case _:
            print("Invalid option selected.")