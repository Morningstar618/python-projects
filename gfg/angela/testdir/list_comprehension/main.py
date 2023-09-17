numbers = [1, 2, 3]

new_numbers = [n + 1 for n in numbers]
print(new_numbers)

name = "ayush"
print([letter for letter in name])

print([n * 2 for n in range(1, 5)])

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
print([name for name in names if len(name) < 5])
print([name.upper() for name in names if len(name) > 5])
