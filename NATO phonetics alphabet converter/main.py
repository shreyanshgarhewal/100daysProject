import pandas as pd

### reading nato phonetics data in csv and converting it into pandas dataframe and then into a dictionary

phonetics = open("nato_phonetic_alphabet.csv")
phonetics_list = pd.read_csv(phonetics)

nato_dictionary = {value.letter: value.code for (key, value) in phonetics_list.iterrows()}

### taking input as a string and converting each letter in the word in nato code phonetics


def name_converter():
    name = input("Enter anything: ")

    try:
        name_in_phonetics = [nato_dictionary[elements] for elements in name.upper()]
        print(name_in_phonetics)

    except KeyError:
        print("Sorry, enter only in alphabets")
        name_converter()


name_converter()
