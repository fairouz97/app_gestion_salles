from data.dao_salle import DataSalle

class ServiceSalle:
    def __init__(self):
        self.dao_salle = DataSalle()
    def ajouter_salle(self, salle):
        if salle.code == "" or salle.description == "" or salle.categorie == "":
             return False, "Il manque des informations"

        if salle.capacite < 1:
             return False, "Capacité doit être >= 1"
        self.dao_salle.insert_salle(
        salle.code,
        salle.description,
        salle.categorie,
        salle.capacite
    )

        return True, "Salle ajoutée avec succès"
    def modifier_salle(self, salle):
        # vérifier capacité
        if salle.capacite < 1:
            return False, "Capacité invalide"

        # mise à jour
        self.dao_salle.update_salle(
            salle.code,
            salle.description,
            salle.categorie,
            salle.capacite
        )

        return True, "Salle modifiée"
    def supprimer_salle(self, code):
        self.dao_salle.delete_salle(code)
        return True, "Salle supprimée"
    def rechercher_salle(self, code):
        return self.dao_salle.get_salle(code)