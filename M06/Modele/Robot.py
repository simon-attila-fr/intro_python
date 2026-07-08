class Robot:
    def __init__(
            self,
            numero_serie,
            orientation,
            statut,
            robot_type='Générique'
    ):
        self.numero_serie = numero_serie
        self.orientation = orientation
        self.statut = statut
        self.robot_type = robot_type

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

my_robot = Robot(3321689, "orientation", "stand by", "A")