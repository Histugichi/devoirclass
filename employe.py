class employe :
   
    def __init__(self, nom, prenom, matricule, fonction, departement):
        self.nom= nom
        self.prenom= prenom
        self. matricule=matricule
        self.fonction= fonction
        self.departement= departement

    def get_nom(self):
        return self.nom

    def set_nom(self, value):
        self.nom = value

    def get_prenom(self):
        return self.prenom

    def set_prenom(self, value):
        self.prenom = value

    def get_matricule(self):
        return self.matricule

    def set_matricule(self, value):
        self. matricule = value

    def get_fonction(self):
        return self.fonction

    def set_fonction(self, value):
        self.fonction = value

    def get_departement(self):
        return self.departement

    def set_departement(self, value):
        self.departement = value


