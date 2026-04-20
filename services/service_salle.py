from data.dao_salle import DataSalle

class ServiceSalle:

    def __init__(self):
        self.dao_salle = DataSalle()

    def ajouter_salle(self, salle):
        if not salle.code or not salle.description or not salle.categorie or not salle.capacite:
            return False, "Champs manquants"

        if salle.capacite < 1:
            return False, "Capacité invalide"

        self.dao_salle.insert_salle(
            salle.code,
            salle.description,
            salle.categorie,
            salle.capacite
        )

        return True, "Salle ajoutée"

    def modifier_salle(self, salle):
        if salle.capacite < 1:
            return False, "Capacité invalide"

        self.dao_salle.update_salle(salle)
        return True, "Salle modifiée"

    def supprimer_salle(self, code):
        self.dao_salle.delete_salle(code)
        return True, "Salle supprimée"

    def rechercher_salle(self, code):
        return self.dao_salle.get_salle(code)

    def recuperer_salles(self):
        return self.dao_salle.get_all_salles()