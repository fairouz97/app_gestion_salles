import mysql.connector
import json

def get_connection():
    with open("data/config.json") as f:
        config = json.load(f)

    return mysql.connector.connect(
        host=config["host"],
        user=config["user"],
        password=config["password"],
        database=config["database"]
    )
def insert_salle(code, description, categorie, capacite):
    conn = get_connection()
    cursor = conn.cursor()

    query = "INSERT INTO salle (code, description, categorie, capacite) VALUES (%s, %s, %s, %s)"
    values = (code, description, categorie, capacite)

    cursor.execute(query, values)
    conn.commit()

    cursor.close()
    conn.close()
def delete_salle(code):
    conn = get_connection()
    cursor = conn.cursor()

    query = "DELETE FROM salle WHERE code = %s"
    cursor.execute(query, (code,))

    conn.commit()

    cursor.close()
    conn.close()