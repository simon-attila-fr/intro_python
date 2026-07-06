class Viande:
    question_type = "Type de viande :\n1)boeuf\n2)porc\n3)canard\nVeuillez choisir un numero\n"
    question_cuisson = "Type de cuisson :\n1)Bleu\n2)A point\n3)Bien cuit\nVeuillez choisir un numero\n"
    question_poids = "Le poids de votre morceau :\n"
    # Coeff de type de cuisson
    coeffs_cuisson = {"1": 0.8, "2": 1.0, "3": 1.3}

    def __init__(self):
        self.cuisson       = ''
        self.poids_morceau = ''
        self.coeff_cuisson = 0

    def poser_question_type():
        choix = input(Viande.question_type)
        if choix not in ["1", "2", "3"]:
            return input("Options valides 1, 2 et 3. " + Viande.question_type)
        else:
            return choix

    def poser_question_cuisson(self):
        self.coeff_cuisson = self.coeffs_cuisson[input(Viande.question_cuisson)]

    def poser_question_poids(self):
        self.poids_morceau = int(input(Viande.question_poids))

    def calulcule_temps_cuisson(self):
        return (int(self.poids_morceau) / 100) * self.coefficient_viande * self.coeff_cuisson


# Canard
class Canard(Viande):
    def __init__(self, question_cuisson, coefficient_viande):
        super().__init__()
        self.question_cuisson   = question_cuisson
        self.coefficient_viande = coefficient_viande

class Boeuf(Viande):
    def __init__(self, coefficient_viande):
        super().__init__()
        self.coefficient_viande      = coefficient_viande

class Porc(Viande):
    def __init__(self, coefficient_viande):
        super().__init__()
        self.coefficient_viande      = coefficient_viande

choix = Viande.poser_question_type()

if choix == "1":
    ma_viande = Boeuf(2.5)
elif choix == "2":
    ma_viande = Porc(3.5)
elif choix == "3":
    ma_viande = Canard(
        "Type de cuisson :\n1)Rosé\n2)A point\n3)Bien cuit\nVeuillez choisir un numero\n",
        3.0
    )

ma_viande.poser_question_cuisson()
ma_viande.poser_question_poids()
print(ma_viande.calulcule_temps_cuisson())