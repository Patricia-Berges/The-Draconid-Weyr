import sqlite3


def create_db():
    conn = sqlite3.connect("draconids.db")
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS draconids(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    species TEXT NOT NULL,
    sex TEXT NOT NULL,
    age INTEGER NOT NULL
    )
    ''')
    conn.commit()
    conn.close()


def save_draconid(draconid):
    conn = sqlite3.connect("draconids.db")
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO draconids (name, species, sex, age) VALUES (?, ?, ?, ?)",
        (draconid.name, draconid.species, draconid.sex, draconid.age)
    )
    conn.commit()
    conn.close()
    print("Saved draconid")


def fetch_draconid(draconid_id):
    conn = sqlite3.connect("draconids.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM draconids WHERE id=?", (draconid_id,))
    draconid = cursor.fetchone()
    conn.close()
    return draconid


def delete_draconid(draconid_id):
    conn = sqlite3.connect("draconids.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM draconids WHERE id=?", (draconid_id,))
    conn.commit()
    conn.close()
    print("Deleted draconid")


def fetch_all_draconids_names():
    conn = sqlite3.connect("draconids.db")
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM draconids")
    draconid_list = cursor.fetchall()
    conn.close()
    names = [name[0] for name in draconid_list]
    return names


def fetch_all_draconids():
    conn = sqlite3.connect("draconids.db")
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM draconids")
    draconid_list = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return draconid_list


def delete_table():
    conn = sqlite3.connect("draconids.db")
    cursor = conn.cursor()
    cursor.execute("DROP TABLE draconids")
    conn.commit()
    conn.close()


def delete_all_draconids():
    conn = sqlite3.connect("draconids.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM draconids")
    conn.commit()
    conn.close()
