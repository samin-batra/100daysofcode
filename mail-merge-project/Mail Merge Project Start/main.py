
with open("Input/Letters/starting_letter.txt", "r") as f:
    letter = f.readlines()

with open("Input/Names/invited_names.txt", "r") as f:
    names_list = f.readlines()


for name in names_list:
    letter_to_send = letter.copy()
    opening_line = letter_to_send[0].strip()
    name = name.strip("\n")
    filename = "Output/ReadyToSend/" + name + ".txt"
    with open(filename, "w") as out_file:
        opening_line = opening_line.replace("[name]", name)
        letter_to_send[0] = opening_line
        out_file.writelines(letter_to_send)
