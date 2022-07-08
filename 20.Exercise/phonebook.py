phonebook = {}

while True:
    entry = input()
    if "-" not in entry:
        break
    name, phone = entry.split("-")
    phonebook[name] = phone

for checking in range(int(entry)):
    searched_contact = input()

    if searched_contact in phonebook.keys():
        print(f"{searched_contact} -> {phonebook[searched_contact]}")
    else:
        print(f"Contact {searched_contact} does not exist.")
