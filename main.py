from data.dao_salle import get_connection

try:
    conn = get_connection()
    print("Connexion réussie ")
    conn.close()
except Exception as e:
    print("Erreur :", e)