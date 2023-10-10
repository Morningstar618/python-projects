import pandas

data = pandas.read_csv('nato_phonetic_alphabet.csv')
data_dict = {row.letter:row.code for (index,row) in data.iterrows()}

def generate_phonetic():
    name = input("Enter name: ").upper()
    try:
        name_phonetics = [data_dict[char] for char in name]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(name_phonetics)

generate_phonetic()
 