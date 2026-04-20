import mysql.connector
import json

class DataSalle:

    def get_connection(self):
        with open("data/config.json") as f:
            config = json.load(f)

        return mysql.connector.connect(
            host=config["host"],
            user=config["user"],
            password=config["password"],
            database=config["database"]
        )

    def insert_salle(self, code, description, categorie, capacite):
        conn = self.get_connection()
        cursor = conn.cursor()

        query = "INSERT INTO salle VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (code, description, categorie, capacite))

        conn.commit()
        conn.close()

    def update_salle(self, salle):
        conn = self.get_connection()
        cursor = conn.cursor()

        query = "UPDATE salle SET description=%s, categorie=%s, capacite=%s WHERE code=%s"
        cursor.execute(query, (salle.description, salle.categorie, salle.capacite, salle.code))

        conn.commit()
        conn.close()

    def delete_salle(self, code):
        conn = self.get_connection()
        cursor = conn.cursor()

        cursor.execute("DELETE FROM salle WHERE code=%s", (code,))
        conn.commit()
        conn.close()

    def get_salle(self, code):
        conn = self.get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM salle WHERE code=%s", (code,))
        result = cursor.fetchone()

        conn.close()
        return result

    def get_all_salles(self):
        conn = self.get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM salle")
        results = cursor.fetchall()

        conn.close()
        return results