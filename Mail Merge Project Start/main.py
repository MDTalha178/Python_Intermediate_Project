PLACEHOLDER = "[name]"
with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()
    print(names)

with open("./Input/Letters/starting_letter.txt") as content_file:
    content = content_file.read()
    for name in names:
        strip_name = name.strip()
        new_content = content.replace(PLACEHOLDER, strip_name)
        with open(f"./Output/ReadyToSend/letter_for{strip_name}.txt", mode="w") as complelte_letter:
            complelte_letter.write(new_content)
    