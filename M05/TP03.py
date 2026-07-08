# Écosystème
import random
import math
from idlelib.run import exit_now


class Cell:
    def __init__(self, x, y, animal):
        self.x = x
        self.y = y
        self.animal = animal
        self.id = str(self.x) + "-" + str(self.y)

# In an ecosystem, there are animals.
# Each animal is a predator of an other animal.
# Each animal is a prey of an other aimal.
class Animal:
    def __init__(self, animal):
        self.id = animal["id"]
        self.species = animal["species"]
        self.predator_of = animal["predator_of"]
        self.prey_of = animal["prey_of"]

class Ecosystem:
    def __init__(self, dim_x, dim_y, animals):
        self.dim_x = dim_x
        self.dim_y = dim_y
        self.animals = animals
        self.grid_dict = {}
        self.create_eco_grid()

    def get_cell_by_id(self, x, y):
        return self.grid_dict[f"{x}-{y}"]

    def get_center_cell(self):
        x = math.ceil(self.dim_x/2)
        y = math.ceil(self.dim_y/2)
        return self.get_cell_by_id(x, y)

    def create_eco_grid(self):
        for x in range(1, self.dim_x + 1):
            for y in range(1, self.dim_y + 1):
                current_animal = random.choice(self.animals)
                self.grid_dict[f"{x}-{y}"] = Cell(x, y, Animal(current_animal))

    def print_eco_grid(self):
        grid = ""
        for x in range(1, self.dim_x + 1):
            for y in range(1, self.dim_y + 1):
                grid += f"{x}-{y}: " + self.get_cell_by_id(x, y).animal.species + " "
                if y == self.dim_y:
                    grid += "\n"
        print(grid)

    def count_predators(self, prey):
        count = 0
        for x in range(1, self.dim_x + 1):
            for y in range(1, self.dim_y + 1):
                current_animal = self.get_cell_by_id(x, y).animal
                if current_animal.predator_of == prey.id:
                    count += 1
        return count

    def count_preys(self, prey):
        count = 0
        for x in range(1, self.dim_x + 1):
            for y in range(1, self.dim_y + 1):
                current_animal = self.get_cell_by_id(x, y).animal
                if current_animal.id == prey.id:
                    count += 1
        return count

    def get_animal_by_id(self, id):
        for animal in self.animals:
            if animal["id"] == id:
                return animal

    def replace_prey(self, predator_id):
        self.get_center_cell().animal = Animal(self.get_animal_by_id(predator_id))

    # The rule of the ecosystem is that an animal in the center is the prey.
    #  If there is a majority of its predators in the ecosystem, the predator replaces the prey.
    def hunting_turn(self, verbose):
        print("---------- Before ----------")
        self.print_eco_grid()
        prey = self.get_center_cell().animal
        predator_id = prey.prey_of
        if verbose : print("PREY: ", prey.species)
        nb_predators = self.count_predators(prey) # Number of predators of the prey
        if verbose : print("Nb predators: ", nb_predators)
        nb_preys = self.count_preys(prey) # Number of preys of the prey
        if verbose : print("Nb preys: ", nb_preys)
        nb_neutral = len(self.grid_dict) - (nb_predators + nb_preys) # Number of animals that are nor predators, nor preys of the prey

        if (nb_predators > nb_preys) or ((nb_predators + nb_neutral) > nb_preys):
            if verbose : print("There are more predators than preys OR there are more predators and neutral animals then preys.")
            self.replace_prey(predator_id)

        elif (nb_predators + nb_preys) > nb_neutral:
            if verbose : print("There are more predators and preys than neutral animals.")
            chance = random.randint(1, 2)
            if chance == 1:
                self.replace_prey(predator_id)
                if verbose : print("The prey has been replaced.")
            else:
                if verbose : print("The prey has not been replaced.")

        elif nb_preys > nb_predators:
            if verbose : print("There are more preys than predators.")
            if verbose : print("No change in the ecosystem.")

        print("---------- After ----------")
        self.print_eco_grid()

    def simulation(self, nb_turns):
        for turn in range(1, nb_turns + 1):
            print(f"TRUN no {turn}:")
            self.hunting_turn(False)

animals = [
    {
        "id": 1,
        "species": "human",
        "predator_of": 2,
        "prey_of": 3
    },
    {
        "id": 2,
        "species": "hen",
        "predator_of": 3,
        "prey_of": 1
    },
    {
        "id": 3,
        "species": "worm",
        "predator_of": 1,
        "prey_of": 2
    }
]

ecosystem1 = Ecosystem(3, 3, animals)
ecosystem1.simulation(5)