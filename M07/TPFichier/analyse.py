# Pingouins
from datetime import date


class PenguinParser:
    headers = ["penguin_id", "species", "island", "bill_length_mm", "bill_depth_mm", "flipper_length_", "body_mass_g", "sex", "year"]
    no_info = "NA"
    def __init__(self, data_source, analyse_output):
        self.__data_source = data_source
        self.analyse_output = analyse_output
        self.species_dict = {}
        self.island_dict = {}
        self.sex_dict = {}
        self.bill_length_list = []
        self.bill_depth_list = []
        self.age_set = set()
        self.penguin_dict = self.open_data_source()


    # This method allows to get the data source's content and tranform it to a dictionary.
    # Key: id of pinguin.
    def open_data_source(self):
        result = {}

        with open(self.__data_source, "r") as file:
            for line in file:
                row = {}
                # Clear new lines
                _line = line.strip('\r\n')
                list_row_split = _line.split(",")
                p_id = int(list_row_split[0])

                for index, column in enumerate(list_row_split):
                    row[PenguinParser.headers[index]] = list_row_split[index]

                    # Species
                    if PenguinParser.headers[index] == "species":
                        if list_row_split[index] in self.species_dict:
                            self.species_dict[list_row_split[index]] += 1
                        else:
                            self.species_dict[list_row_split[index]] = 1

                    # Island
                    if PenguinParser.headers[index] == "island":
                        if list_row_split[index] in self.island_dict:
                            self.island_dict[list_row_split[index]] += 1
                        else:
                            self.island_dict[list_row_split[index]] = 1

                    # Sex
                    if PenguinParser.headers[index] == "sex":
                        if list_row_split[index] in self.sex_dict:
                            self.sex_dict[list_row_split[index]] += 1
                        else:
                            self.sex_dict[list_row_split[index]] = 1

                    # Bills > length
                    if PenguinParser.headers[index] == "bill_length_mm":
                        if list_row_split[index] != PenguinParser.no_info:
                            self.bill_length_list.append(float(list_row_split[index]))

                    # Bills > depth
                    if PenguinParser.headers[index] == "bill_depth_mm":
                        if list_row_split[index] != PenguinParser.no_info:
                            self.bill_depth_list.append(float(list_row_split[index]))

                    # Age
                    if PenguinParser.headers[index] == "year":
                        if list_row_split[index] != PenguinParser.no_info:
                            current_year = date.today().year
                            self.age_set.add(current_year - int(list_row_split[index]))

                result[p_id] = row
        return result

    def get_pinguin_by_id(self, p_id):
        return self.penguin_dict[p_id]

    @staticmethod
    def get_col_number(header_str):
        return PenguinParser.headers.index(header_str)

    def nb_total_pinguins(self):
        return len(self.penguin_dict)

    def get_species_dict(self):
        return self.species_dict

    def get_island_dict(self):
        return self.island_dict

    def get_sex_dict(self):
        return self.sex_dict

    def get_bill_length_list(self):
        return self.bill_length_list

    def get_bill_depth_list(self):
        return self.bill_depth_list

    def get_age_set(self):
        return self.age_set

    def write_answers_to_file(self):
        with open(self.analyse_output, "w", encoding="utf-8") as file:
            lines = []
            q1 = f"Nb totale de pingouins : {len(pinguins1.penguin_dict)}\n"
            lines.append(q1)
            q2 = f"Nb individu par espece : {self.get_species_dict()}\n"
            lines.append(q2)
            q3 = f"Nb especes : {len(pinguins1.get_species_dict())}\n"
            lines.append(q3)
            q4 = f"Nb individu par île : {self.get_island_dict()}\n"
            lines.append(q4)
            q5 = f"Nb îles : {len(self.get_island_dict())}\n"
            lines.append(q5)
            q6 = f"Longueur moyenne des becs : {sum(pinguins1.get_bill_length_list()) / len(pinguins1.get_bill_length_list())}\n"
            lines.append(q6)
            q7 = f"la plus grande profondeur de bec: {max(pinguins1.get_bill_depth_list())}\n"
            lines.append(q7)
            q8 = f"Nb individu par sex : {pinguins1.get_sex_dict()}\n"
            lines.append(q8)
            q9 = f"l’âge du plus jeune pingouin : {min(pinguins1.get_age_set())}\n"
            lines.append(q9)
            q10 = f"l’âge du pingouin le plus âgé : {max(pinguins1.get_age_set())}\n"
            lines.append(q10)
            file.writelines(lines)

pinguins1 = PenguinParser("D:/Projects/TP/M07/TPFichier/data/pingouins_1.txt", "D:/Projects/TP/M07/TPFichier/data/results.txt")
pinguins1.write_answers_to_file()

