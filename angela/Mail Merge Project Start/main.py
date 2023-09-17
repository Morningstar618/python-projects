name_file = open('Input/Names/invited_names.txt')
start_file = 'Input/Letters/starting_letter.txt'

for data in name_file.readlines():
    name = data.strip('\n')
    with open(start_file) as lines:
        for line in lines.readlines():
            with open(f'Output/ReadyToSend/letter_to_{name}.txt', mode='a') as file:
                if '[name]' in line:
                    file.write(line.replace('[name]', name))
                else:
                    file.write(line)


name_file.close()


