from services.service_salle import ServiceSalle
from models.salle import Salle

service = ServiceSalle()

# afficher salles
print("Liste des salles :")
for s in service.recuperer_salles():
    print(s)

# ajouter
s1 = Salle("S500", "Salle test service", "Classe", 20)
print(service.ajouter_salle(s1))

# modifier
s2 = Salle("S500", "Salle modifiée service", "Labo", 40)
print(service.modifier_salle(s2))

# rechercher
print("Recherche :", service.rechercher_salle("S500"))

# supprimer
print(service.supprimer_salle("S500"))
#afficher liste des salles
print("Liste des salles :")
print(service.recuperer_salles())
