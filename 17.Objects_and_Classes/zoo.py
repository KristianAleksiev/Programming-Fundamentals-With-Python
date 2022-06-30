class Zoo:
    __animals = 0

    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, name):
        """Adding a new animal to the zoo"""
        if species == "mammal":
            self.mammals.append(name)

        elif species == "fish":
            self.fishes.append(name)

        elif species == "bird":
            self.birds.append(name)
        Zoo.__animals += 1

    def get_info(self, species):
        """Creating the information output based on species and total animals"""
        info = ""
        if species == "mammal":
            info += f"Mammals in {self.name}: {', '.join(self.mammals)}\n"
        elif species == "fish":
            info += f"Fishes in {self.name}: {', '.join(self.fishes)}\n"
        elif species == "bird":
            info += f"Birds in {self.name}: {', '.join(self.birds)}\n"

        info += f"Total animals: {Zoo.__animals}"
        return info


zoo_name = input()
zoo = Zoo(zoo_name)
number_of_animals = int(input())

for animal_num in range(number_of_animals):
    current_animal = input().split()
    species = current_animal[0]
    name_of_animal = current_animal[1]
    zoo.add_animal(species, name_of_animal)

info_keyword = input()
result = zoo.get_info(info_keyword)

print(result)
