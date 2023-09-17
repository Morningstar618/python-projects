import pandas

data = pandas.read_csv('nato_phonetic_alphabet.csv')
data_dict = {row.letter:row.code for (index,row) in data.iterrows()}

name = input("Enter name: ").upper()
name_phonetics = [data_dict[char] for char in name]

print(name_phonetics)

