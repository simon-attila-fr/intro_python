# Écosystème


# class Animal:
#     predator_of
#     prey_of
# class Ecosystem:

# animals = []
# get_center()

# predators = {1:2, 2:3, 3:1}
# add_prey()
# add_predator()

class Animal:
    def __init__(self, species, predator_of, prey_of):
        self.species = species
        self.predator_of = predator_of
        self.prey_of = prey_of

class Ecosystem:
    def __init__(self, dim_x, dim_y, animals, predators):
        self.predators = predators
        self.dim_x = dim_x
        self.dim_y = dim_y
        self.animals = []

    def create_food_chain(self):
        for predator in self.predators.keys():
            self.animals[predator].predator_of = self.predators[predator]

    # def create_ecosystem(self):
    #     for x in range(self.dim_x):
    #         for y in range(self.dim_y):

# animals = [{}; {}; {}]
predators = {1:2, 2:3, 3:1}
ecosystem1 = Ecosystem(3, 3, animals, predators)
print(ecosystem1.animals)