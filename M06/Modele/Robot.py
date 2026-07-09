import string
import random
from typing import final


class Robot:
    nb_robot = 0
    orientation_values = ["NORD", "EST", "SUD", "OUEST"]
    statut_dict = {1: "En service", 2: "Hors Service", 3: "En réparation"}
    def __init__(
            self,
            statut=1,
            orientation='NORD',
            robot_type='Générique'
    ):
        self.__numero_serie = Robot.generate_numero_serie(),
        self.statut = statut
        self.orientation = orientation
        self.robot_type = robot_type
        Robot.nb_robot += 1

    @property
    def robot_type(self):
        return self.__robot_type

    @robot_type.setter
    def robot_type(self, robot_type):
        if len(robot_type) < 2:
            print("Le robot type n'est pas valide. Sa valeur par défaut a été affectée.")
            self.__robot_type = "Générique"
        else :
            self.__robot_type = robot_type

    @robot_type.deleter
    def robot_type(self):
        del self.__robot_type

    @final
    @property
    def numero_serie(self):
        return self.__numero_serie

    @numero_serie.setter
    def numero_serie(self, numero_serie):
        self.__numero_serie = numero_serie

    @staticmethod
    def generate_numero_serie():
        # First two letters in uppercase
        n_serie_part1 = random.choices(string.ascii_uppercase, k=2)
        n_serie_part2 = random.choices(("0", "1", "2", "3", "4", "5", "6", "7", "8", "9"), k=10)
        n_serie = n_serie_part1 + n_serie_part2
        return "".join(n_serie)

    @property
    def orientation(self):
        return self.__orientation

    @orientation.setter
    def orientation(self, orientation):
        if orientation not in Robot.orientation_values:
            print(f"Orientation should be in {Robot.orientation_values}. The default NORD value has been set.")
            self.__orientation = "NORD"
        else:
            self.__orientation = orientation

    @property
    def statut(self):
        return Robot.statut_dict[int(self.__statut)]

    @statut.setter
    def statut(self, statut):
        if statut not in Robot.statut_dict.keys():
            print("The statut should be in {Robot.statut_dict.keys().} Default value 1 has been set.")
            self.__statut = 1
        else:
            self.__statut = statut

    def __str__(self):
        presentation = f"Robot {self.__numero_serie[0]} - {self.__robot_type}\n"
        presentation = presentation + f"Statut : {self.__statut}\n"
        presentation = presentation + f"Orientation : {self.__orientation}\n"
        return presentation

    def turn(self, direction):
        valid_directions = [1, -1]
        if direction not in valid_directions:
            print(f"Direction should be in {valid_directions}.")
        else:
            current_orientation_index = Robot.orientation_values.index(self.__orientation)
            if 0 < current_orientation_index and current_orientation_index < len(Robot.orientation_values) - 1:
                self.__orientation = Robot.orientation_values[current_orientation_index + direction]

            elif (current_orientation_index == len(Robot.orientation_values) - 1) and direction == 1:
                self.__orientation = Robot.orientation_values[0]

            elif (current_orientation_index == 0) and direction == -1:
                self.__orientation = Robot.orientation_values[len(Robot.orientation_values) - 1]

            else:
                self.__orientation = Robot.orientation_values[current_orientation_index + direction]

        print(
            f"The robot has turned from {Robot.orientation_values[current_orientation_index]} to {self.__orientation}."
        )


# Initialization with invalid robot_type property
my_robot1 = Robot(1, "SUD", "A")
# Result: "Le robot type n'est pas valide. Sa valeur par défaut a été affectée."
my_robot1.robot_type = "ABC-123"
print(my_robot1.robot_type) # ABC-123
my_robot1.turn(1)
my_robot1.turn(1)
my_robot1.turn(-1)
my_robot1.turn(-1)

# Initialization with invalid orientation property
my_robot2 = Robot(2, "ESTT", "ABC-321")
# Result: "Orientation should be in ['NORD', 'EST', 'SUD', 'OUEST']. The default NORD value has been set."
my_robot2.statut = 3
print(my_robot2.statut)
print(str(my_robot2))
