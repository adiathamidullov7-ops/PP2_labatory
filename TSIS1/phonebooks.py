import csv
import json
import psycopg2
from connect import get_connection


# =========================
# PRINT HELPERS
# =========================

def print_contacts(rows):
    if not rows:
        print("  (no contacts found)")
        return

    print("-" * 70)
    for r in rows:
        print(f"[{r[0]}] {r[1]} {r[2]}")
        print(f"  Email: {r[3]}")
        print(f"  Birthday: {r[4]}")
        print(f"  Group: {r[5]}")
    print("-" * 70)


def print_contacts_full(rows):
    if not rows:
        print("  (no contacts found)")
        return

    print("-" * 70)
    seen = set()

    for r in rows:
        cid, fn, ln, email, bd, grp, phone, ptype = r

        if cid not in seen:
            print(f"[{cid}] {fn} {ln}")
            print(f"  Email: {email}")
            print(f"  Birthday: {bd}")
            print(f"  Group: {grp}")
            seen.add(cid)

        if phone:
            print(f"   -> {phone} ({ptype})")

    print("-" * 70)


# =========================
# SCHEMA SETUP
# =========================

def setup_schema():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
    DROP TABLE IF EXISTS phones CASCADE;
    DROP TABLE IF EXISTS contacts CASCADE;
    DROP TABLE IF EXISTS groups CASCADE;

    CREATE TABLE groups (
        id SERIAL PRIMARY KEY,
        name VARCHAR(50) UNIQUE NOT NULL
    );

    CREATE TABLE contacts (
        id SERIAL PRIMARY KEY,
        first_name VARCHAR(50),
        last_name VARCHAR(50),
        email VARCHAR(100),
        birthday DATE,
        group_id INTEGER REFERENCES groups(id)
    );

    CREATE TABLE phones (
        id SERIAL PRIMARY KEY,
        contact_id INTEGER REFERENCES contacts(id) ON DELETE CASCADE,
        phone VARCHAR(20),
        type VARCHAR(10)
    );

    INSERT INTO groups (name)
    VALUES ('Family'), ('Work'), ('Friend'), ('Other')
    ON CONFLICT DO NOTHING;
    """)

    conn.commit()
    cur.close()
    conn.close()

    print("Schema updated successfully")


# =========================
# ADD CONTACT
# =========================

def add_contact():
    print("\n--- Add Contact ---")

    first = input("First name: ").strip()
    last = input("Last name: ").strip() or None
    email = input("Email: ").strip() or None
    birthday = input("Birthday YYYY-MM-DD: ").strip() or None

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT id, name FROM groups ORDER BY id")
    groups = cur.fetchall()

    print("Groups:")
    for g in groups:
        print(f"{g[0]}. {g[1]}")

    group_id = input("Group id: ").strip()
    group_id = int(group_id) if group_id.isdigit() else None

    phone = input("Main phone: ").strip() or None

    cur.execute("""
        INSERT INTO contacts (first_name, last_name, email, birthday, group_id)
        VALUES (%s,%s,%s,%s,%s)
        RETURNING id
    """, (first, last, email, birthday, group_id))

    cid = cur.fetchone()[0]

    if phone:
        cur.execute("""
            INSERT INTO phones (contact_id, phone, type)
            VALUES (%s,%s,'mobile')
        """, (cid, phone))

    conn.commit()
    cur.close()
    conn.close()

    print("Contact added")


# =========================
# FILTER BY GROUP
# =========================

def filter_by_group():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT id, name FROM groups")
    groups = cur.fetchall()

    for g in groups:
        print(f"{g[0]}. {g[1]}")

    gid = input("Group id: ")

    cur.execute("""
        SELECT c.id, c.first_name, c.last_name, c.email, c.birthday, g.name
        FROM contacts c
        LEFT JOIN groups g ON g.id = c.group_id
        WHERE c.group_id = %s
    """, (gid,))

    print_contacts(cur.fetchall())

    cur.close()
    conn.close()


# =========================
# SEARCH BY EMAIL
# =========================

def search_by_email():
    q = input("Email search: ")

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT c.id, c.first_name, c.last_name, c.email, c.birthday, g.name
        FROM contacts c
        LEFT JOIN groups g ON g.id = c.group_id
        WHERE c.email ILIKE %s
    """, (f"%{q}%",))

    print_contacts(cur.fetchall())

    cur.close()
    conn.close()


# =========================
# LIST SORTED
# =========================

def list_contacts():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT c.id, c.first_name, c.last_name, c.email, c.birthday, g.name
        FROM contacts c
        LEFT JOIN groups g ON g.id = c.group_id
        ORDER BY c.first_name
    """)

    print_contacts(cur.fetchall())

    cur.close()
    conn.close()


# =========================
# PAGINATION (DB FUNCTION OR PYTHON)
# =========================

def paginated_view():
    limit = int(input("Limit: "))
    offset = int(input("Offset: "))

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT c.id, c.first_name, c.last_name, c.email, c.birthday, g.name
        FROM contacts c
        LEFT JOIN groups g ON g.id = c.group_id
        LIMIT %s OFFSET %s
    """, (limit, offset))

    print_contacts(cur.fetchall())

    cur.close()
    conn.close()


# =========================
# SEARCH ALL FIELDS
# =========================

def search_all():
    q = input("Search: ")

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT c.id, c.first_name, c.last_name, c.email, c.birthday,
               g.name, p.phone, p.type
        FROM contacts c
        LEFT JOIN groups g ON g.id = c.group_id
        LEFT JOIN phones p ON p.contact_id = c.id
        WHERE c.first_name ILIKE %s
           OR c.last_name ILIKE %s
           OR c.email ILIKE %s
           OR p.phone ILIKE %s
    """, (f"%{q}%",)*4)

    print_contacts_full(cur.fetchall())

    cur.close()
    conn.close()


# =========================
# ADD PHONE
# =========================

def add_phone():
    name = input("Contact name: ")
    phone = input("Phone: ")

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT id FROM contacts WHERE first_name ILIKE %s", (name,))
    c = cur.fetchone()

    if c:
        cur.execute("""
            INSERT INTO phones (contact_id, phone, type)
            VALUES (%s,%s,'mobile')
        """, (c[0], phone))

        conn.commit()

    cur.close()
    conn.close()


# =========================
# MOVE GROUP
# =========================

def move_group():
    name = input("Contact: ")
    group = input("Group: ")

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT id FROM contacts WHERE first_name ILIKE %s", (name,))
    c = cur.fetchone()

    cur.execute("SELECT id FROM groups WHERE name ILIKE %s", (group,))
    g = cur.fetchone()

    if c and g:
        cur.execute("UPDATE contacts SET group_id=%s WHERE id=%s", (g[0], c[0]))
        conn.commit()

    cur.close()
    conn.close()


# =========================
# EXPORT JSON
# =========================

def export_json():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT c.id, c.first_name, c.last_name, c.email, c.birthday, g.name
        FROM contacts c
        LEFT JOIN groups g ON g.id = c.group_id
    """)

    result = []

    for r in cur.fetchall():
        cid, fn, ln, email, bd, grp = r

        cur.execute("SELECT phone, type FROM phones WHERE contact_id=%s", (cid,))
        phones = [{"phone": p[0], "type": p[1]} for p in cur.fetchall()]

        result.append({
            "first_name": fn,
            "last_name": ln,
            "email": email,
            "birthday": str(bd),
            "group": grp,
            "phones": phones
        })

    with open("contacts.json", "w") as f:
        json.dump(result, f, indent=2)

    cur.close()
    conn.close()

    print("Export done")


# =========================
# IMPORT JSON
# =========================

def import_json():
    file = input("JSON file: ") or "contacts.json"

    with open(file, "r") as f:
        data = json.load(f)

    conn = get_connection()
    cur = conn.cursor()

    for item in data:
        cur.execute("""
            INSERT INTO contacts (first_name, last_name, email, birthday, group_id)
            VALUES (%s,%s,%s,%s,NULL)
        """, (item["first_name"], item["last_name"], item["email"], item["birthday"]))

    conn.commit()
    cur.close()
    conn.close()

    print("Import done")
    
def import_csv():
    filename = input("CSV filename (default contacts.csv): ").strip() or "contacts.csv"

    conn = get_connection()
    cur = conn.cursor()

    added = 0

    with open(rf"c:/Users/adiat/Music/pp2_adia/TSIS1/{filename}", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)

        for row in reader:
            first = row.get("first_name") or row.get("name")
            last = row.get("last_name")
            email = row.get("email")
            birthday = row.get("birthday")
            phone = row.get("phone")

            if not first:
                continue

            cur.execute("""
                INSERT INTO contacts (first_name, last_name, email, birthday, group_id)
                VALUES (%s,%s,%s,%s,NULL)
                RETURNING id
            """, (first, last, email, birthday))

            cid = cur.fetchone()[0]

            if phone:
                cur.execute("""
                    INSERT INTO phones (contact_id, phone, type)
                    VALUES (%s,%s,'mobile')
                """, (cid, phone))

            added += 1

    conn.commit()
    cur.close()
    conn.close()

    print(f"CSV import done. Added: {added}")

# =========================
# MENU
# =========================

def main():
    while True:
        print("""
1. Add contact
2. Filter group
3. Search email
4. List
5. Pagination
6. Search all
7. Add phone
8. Move group
9. Export JSON
10. Import JSON
11. Import csv
12. Setup schema
0. Exit
""")

        c = input("Choice: ")

        if c == "1":
            add_contact()
        elif c == "2":
            filter_by_group()
        elif c == "3":
            search_by_email()
        elif c == "4":
            list_contacts()
        elif c == "5":
            paginated_view()
        elif c == "6":
            search_all()
        elif c == "7":
            add_phone()
        elif c == "8":
            move_group()
        elif c == "9":
            export_json()
        elif c == "10":
            import_json()
        elif c == "11":
            import_csv() 
        elif c == "12":
            setup_schema()
        elif c == "0":
            break


if __name__ == "__main__":
    main()