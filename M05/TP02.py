# Anagrammes
def is_sentence(str):
    str_to_list = str.split()
    if 1 < len(str_to_list):
        return True
    return False

def str_to_dict(text):
    str_to_list = list(text)
    dict_each_letter_number_occurance = {}
    for char in str_to_list:
        if char not in dict_each_letter_number_occurance:
            dict_each_letter_number_occurance[char] = 1
        else:
            dict_each_letter_number_occurance[char] = dict_each_letter_number_occurance[char] + 1
    return dict_each_letter_number_occurance

def are_anagrammes(str1, str2):
    str1 = str1.lower()
    str1 = str1.replace(" ", "")
    str2 = str2.lower()
    str2 = str2.replace(" ", "")

    str1_to_dict = str_to_dict(str1)
    str2_to_dict = str_to_dict(str2)

    return str1_to_dict == str2_to_dict

print(are_anagrammes("Chien", "Niche")) # True
print(are_anagrammes("Pablo Picasso", "Pascal Obispo")) # True
print(are_anagrammes("Pablo Picasso", "Pascal Obispooo")) # False
print(are_anagrammes("Léonard de Vinci", "Créa le don divin")) # True
print(are_anagrammes("Léonard de Vinci", "Crëa le don divin")) # False