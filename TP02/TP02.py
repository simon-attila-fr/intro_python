class Cheques:
    def __init__(self):
        self.cheque_list = []

    def addCheque(self, cheque):
        self.cheque_list.append(cheque)

    def getNbCheques(self):
        return len(self.cheque_list)

    def get_montant_total(self):
        total = 0
        for c in self.cheque_list:
            total += c.getMontant()
        return total

    def get_montant_moyenne(self):
        return self.get_montant_total() / self.getNbCheques()

    def get_nb_total_inferieure_a(self, limite):
        nb_total = 0
        montant_total = 0
        for c in self.cheque_list:
            if c.getMontant() < int(limite):
                nb_total += 1
                montant_total += c.getMontant()
        msg_nb_total = "Il y a " + str(nb_total) + " chèques dont le montant est inferieure à " + str(limite) + ". "
        msg_montant_total = "Leur montant total est de " + str(montant_total) + "."
        return msg_nb_total + msg_montant_total

    def get_nb_total_superieure_ou_egale__a(self, limite):
        nb_total = 0
        montant_total = 0
        for c in self.cheque_list:
            if int(limite) < c.getMontant():
                nb_total += 1
                montant_total += c.getMontant()
        msg_nb_total = "Il y a " + str(nb_total) + " chèques dont le montant est supérieure ou égale à " + str(limite) + ". "
        msg_montant_total = "Leur montant total est de " + str(montant_total) + "."
        return msg_nb_total + msg_montant_total

    def get_min_cheque(self):
        min_cheque = [self.cheque_list[0].getIdCheque()]
        min_montant = self.cheque_list[0].getMontant()
        for index, c in enumerate(self.cheque_list, start = 1):
            if c.getMontant() < min_montant:
                min_montant = c.getMontant()
                min_cheque.clear()
                min_cheque.append(c.getIdCheque())
            elif c.getMontant() == min_montant:
                min_cheque.append(c.getIdCheque())
        msg = "Le(s) chèque(s) avec le montant le moins élevé : "
        for id in min_cheque:
            msg += str(id) + ", "
        msg += " où le montant est " + str(min_montant) + "."
        return msg

cheques = Cheques()

class Cheque:
    def __init__(self, id_cheque, montant):
        self.id_cheque = int(id_cheque)
        self.montant= int(montant)

    def getIdCheque(self):
        return self.id_cheque

    def getMontant(self):
        return self.montant

id_cheque = int(input("Numéro de chèque: "))

while id_cheque != 0:
    if id_cheque < 0:
        print("Le numéro de cheque doit être un chiffre positif.")
        id_cheque = int(input("Numéro de chèque: "))
    montant = input("Montant : ")
    cheques.addCheque(Cheque(id_cheque, montant))
    id_cheque = int(input("Numéro de chèque: "))

# ------------
# | CALCULES |
# ------------
print("Nombre de chèques introduits : ")
print(cheques.getNbCheques())
print("Le montant total des chèques : ")
print(cheques.get_montant_total())
print("Moyenne de montants : ")
print(cheques.get_montant_moyenne())
print(cheques.get_nb_total_inferieure_a(200))
print(cheques.get_nb_total_superieure_ou_egale__a(200))
print(cheques.get_min_cheque())
