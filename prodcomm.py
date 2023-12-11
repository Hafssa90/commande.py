class Produit:
    nombre_produits = 0  
    def __init__(self, reference, designation, prix_achat, prix_vente):
        self.reference = reference
        self.designation = designation
        self._prix_achat = prix_achat
        self._prix_vente = prix_vente
        self.stock = 0  
        Produit.nombre_produits += 1  

    @property
    def prix_achat(self):
        return self._prix_achat

    @prix_achat.setter
    def prix_achat(self, nouveau_prix):
        self._prix_achat = nouveau_prix

    @property
    def prix_vente(self):
        return self._prix_vente

    @prix_vente.setter
    def prix_vente(self, nouveau_prix):
        self._prix_vente = nouveau_prix

    def afficher_info_produit(self):
        print(f"""Référence: {self.reference}
Désignation: {self.designation}
Prix d'achat: {self._prix_achat}
Prix de vente: {self._prix_vente}
Stock: {self.stock}""")

    def augmenter_stock(self, quantite):
        self.stock += quantite

    def diminuer_stock(self, quantite):
        if quantite <= self.stock:
            self.stock -= quantite
        else:
            print("Pas assez de stock pour diminuer.")

    def _eq_(self, other):
        if isinstance(other, Produit):
            return self.reference == other.reference
        return False

class Commande:
    def __init__(self, date_creation):
        self.date_creation = date_creation
        self.produits = {}

    def details_commande(self):
        print(f"Date de la commande: {self.date_creation}")
        for produit in self.produits.values():
            produit.afficher_info_produit()

produit1 = Produit('3', 'forever', 10.0, 15.0)
produit1.augmenter_stock(10)
produit2 = Produit('4', 'kiko', 12.0, 18.0)
produit2.augmenter_stock(2)

produit1.afficher_info_produit()
produit2.afficher_info_produit()
print("Nombre de produits:", Produit.nombre_produits)

commande1 = Commande('2000-02-01')

