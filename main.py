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
from data.dao_salle import update_salle

###insert_salle("S3", "Salle test", "Classe", 30)

update_salle("S3", "Salle modifiée", "Labo", 50)
print("Salle mise à jour")
from data.dao_salle import get_all_salles

salles = get_all_salles()

for salle in salles:
    print(salle)
from data.dao_salle import get_salle

salle = get_salle("S3")
print("Salle trouvée :", salle)