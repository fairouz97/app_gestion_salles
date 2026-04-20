import customtkinter as ctk
from tkinter import ttk
from services.service_salle import ServiceSalle

class ViewSalle(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Gestion des salles")
        self.geometry("700x500")

        self.service_salle = ServiceSalle()
        # Cadre Informations Salle
        self.cadreInfo = ctk.CTkFrame(self, corner_radius=10)
        self.cadreInfo.pack(pady=10, padx=10)

        self.labelCode = ctk.CTkLabel(self.cadreInfo, text="Code salle")
        self.labelCode.grid(row=0, column=0, padx=10, pady=5)
        self.entryCode = ctk.CTkEntry(self.cadreInfo)
        self.entryCode.grid(row=0, column=1, padx=10, pady=5)

        self.labelDescription = ctk.CTkLabel(self.cadreInfo, text="Description")
        self.labelDescription.grid(row=1, column=0, padx=10, pady=5)
        self.entryDescription = ctk.CTkEntry(self.cadreInfo)
        self.entryDescription.grid(row=1, column=1, padx=10, pady=5)

        self.labelCategorie = ctk.CTkLabel(self.cadreInfo, text="Catégorie")
        self.labelCategorie.grid(row=2, column=0, padx=10, pady=5)
        self.entryCategorie = ctk.CTkEntry(self.cadreInfo)
        self.entryCategorie.grid(row=2, column=1, padx=10, pady=5)

        self.labelCapacite = ctk.CTkLabel(self.cadreInfo, text="Capacité")
        self.labelCapacite.grid(row=3, column=0, padx=10, pady=5)
        self.entryCapacite = ctk.CTkEntry(self.cadreInfo)
        self.entryCapacite.grid(row=3, column=1, padx=10, pady=5)
        # Cadre Actions
        self.cadreActions = ctk.CTkFrame(self, corner_radius=10)
        self.cadreActions.pack(pady=10, padx=10)

        self.btnAjouter = ctk.CTkButton(
            self.cadreActions,
            text="Ajouter",
            command=self.ajouter_salle
        )
        self.btnAjouter.grid(row=0, column=0, padx=10, pady=10)

        self.btnModifier = ctk.CTkButton(
            self.cadreActions,
            text="Modifier",
            command=self.modifier_salle
        )
        self.btnModifier.grid(row=0, column=1, padx=10, pady=10)

        self.btnSupprimer = ctk.CTkButton(
            self.cadreActions,
            text="Supprimer",
            command=self.supprimer_salle
        )
        self.btnSupprimer.grid(row=0, column=2, padx=10, pady=10)

        self.btnRechercher = ctk.CTkButton(
            self.cadreActions,
            text="Rechercher",
            command=self.rechercher_salle
        )
        self.btnRechercher.grid(row=0, column=3, padx=10, pady=10)
        # Cadre Liste des salles
        self.cadreList = ctk.CTkFrame(self, corner_radius=10)
        self.cadreList.pack(pady=10, padx=10)

        self.treeList = ttk.Treeview(
            self.cadreList,
            columns=("code", "description", "categorie", "capacite"),
            show="headings"
        )

        # En-têtes
        self.treeList.heading("code", text="CODE")
        self.treeList.heading("description", text="Description")
        self.treeList.heading("categorie", text="Catégorie")
        self.treeList.heading("capacite", text="Capacité")

        # Largeur
        self.treeList.column("code", width=80)
        self.treeList.column("description", width=150)
        self.treeList.column("categorie", width=100)
        self.treeList.column("capacite", width=100)

        self.treeList.pack(expand=True, fill="both")
        self.lister_salles()

    def ajouter_salle(self):
        code = self.entryCode.get()
        description = self.entryDescription.get()
        categorie = self.entryCategorie.get()
        capacite = self.entryCapacite.get()

        try:
            capacite = int(capacite)
        except:
            print("Capacité invalide")
            return

        from models.salle import Salle
        salle = Salle(code, description, categorie, capacite)

        result = self.service_salle.ajouter_salle(salle)
        print(result)

    def supprimer_salle(self):
        code = self.entryCode.get()

        if code == "":
            print("Code requis")
            return

        result = self.service_salle.supprimer_salle(code)
        print(result)

    def modifier_salle(self):
        code = self.entryCode.get()
        description = self.entryDescription.get()
        categorie = self.entryCategorie.get()
        capacite = self.entryCapacite.get()

        try:
            capacite = int(capacite)
        except:
            print("Capacité invalide")
            return

        from models.salle import Salle
        salle = Salle(code, description, categorie, capacite)

        result = self.service_salle.modifier_salle(salle)
        print(result)

    def rechercher_salle(self):
        code = self.entryCode.get()

        result = self.service_salle.rechercher_salle(code)

        if result:
            self.entryCode.delete(0, 'end')
            self.entryCode.insert(0, result[0])

            self.entryDescription.delete(0, 'end')
            self.entryDescription.insert(0, result[1])

            self.entryCategorie.delete(0, 'end')
            self.entryCategorie.insert(0, result[2])

            self.entryCapacite.delete(0, 'end')
            self.entryCapacite.insert(0, result[3])
        else:
            print("Salle non trouvée")

    def lister_salles(self):
        self.treeList.delete(*self.treeList.get_children())

        liste = self.service_salle.recuperer_salles()

        for s in liste:
            self.treeList.insert("", "end", values=(s[0], s[1], s[2], s[3]))