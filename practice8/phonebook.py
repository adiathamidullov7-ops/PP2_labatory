import psycopg2
from connect import get_connection


def execute_sql_file(filename):
    conn = get_connection()
    cur = conn.cursor()
    try:
        with open(filename, "r", encoding="utf-8") as file:
            sql = file.read()
            cur.execute(sql)
        conn.commit()
        print(f"{filename} executed successfully.")
    except Exception as e:
        conn.rollback()
        print(f"Error executing {filename}: {e}")
    finally:
        cur.close()
        conn.close()


def setup_database():
    execute_sql_file("functions.sql")
    execute_sql_file("procedures.sql")


def upsert_contact():
    name = input("Enter name: ").strip()
    phone = input("Enter phone: ").strip()

    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute("CALL upsert_contact(%s, %s);", (name, phone))
        conn.commit()
        print("Contact inserted/updated successfully.")
    except Exception as e:
        conn.rollback()
        print("Error:", e)
    finally:
        cur.close()
        conn.close()


def search_contacts():
    pattern = input("Enter search pattern: ").strip()

    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute("SELECT * FROM search_contacts(%s);", (pattern,))
        rows = cur.fetchall()

        if rows:
            print("\nSearch results:")
            for row in rows:
                print(f"ID: {row[0]}, Name: {row[1]}, Phone: {row[2]}")
        else:
            print("No matching contacts found.")
    except Exception as e:
        print("Error:", e)
    finally:
        cur.close()
        conn.close()


def insert_many_contacts():
    n = int(input("How many contacts do you want to insert? "))
    names = []
    phones = []

    for i in range(n):
        print(f"\nContact #{i + 1}")
        name = input("Enter name: ").strip()
        phone = input("Enter phone: ").strip()
        names.append(name)
        phones.append(phone)

    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute("CALL insert_many_contacts(%s, %s);", (names, phones))
        conn.commit()
        print("Bulk insert completed.")
        print("Check NOTICE messages in PostgreSQL output for incorrect data.")
    except Exception as e:
        conn.rollback()
        print("Error:", e)
    finally:
        cur.close()
        conn.close()


def get_paginated_contacts():
    limit_count = int(input("Enter LIMIT: "))
    offset_count = int(input("Enter OFFSET: "))

    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute(
            "SELECT * FROM get_contacts_paginated(%s, %s);",
            (limit_count, offset_count)
        )
        rows = cur.fetchall()

        if rows:
            print("\nPaginated contacts:")
            for row in rows:
                print(f"ID: {row[0]}, Name: {row[1]}, Phone: {row[2]}")
        else:
            print("No contacts found for this page.")
    except Exception as e:
        print("Error:", e)
    finally:
        cur.close()
        conn.close()


def delete_contact():
    value = input("Enter username or phone to delete: ").strip()

    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute("CALL delete_contact(%s);", (value,))
        conn.commit()
        print("Contact(s) deleted if matched.")
    except Exception as e:
        conn.rollback()
        print("Error:", e)
    finally:
        cur.close()
        conn.close()


def show_menu():
    while True:
        print("\n--- PHONEBOOK MENU ---")
        print("1. Setup database objects")
        print("2. Insert or update contact")
        print("3. Search contacts by pattern")
        print("4. Insert many contacts")
        print("5. Show contacts with pagination")
        print("6. Delete contact by username or phone")
        print("0. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            setup_database()
        elif choice == "2":
            upsert_contact()
        elif choice == "3":
            search_contacts()
        elif choice == "4":
            insert_many_contacts()
        elif choice == "5":
            get_paginated_contacts()
        elif choice == "6":
            delete_contact()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    show_menu()