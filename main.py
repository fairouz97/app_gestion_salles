from data.dao_salle import get_connection

try:
    conn = get_connection()
    print("Connexion réussie ")
    conn.close()
except Exception as e:
    print("Erreur :", e)
from data.dao_salle import insert_salle

insert_salle("S2", "Salle test", "Classe", 30)
print("Salle ajoutée")
from data.dao_salle import delete_salle

delete_salle("S2")
print("Salle supprimée")