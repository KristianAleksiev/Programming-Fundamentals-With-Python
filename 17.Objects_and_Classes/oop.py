class Person:

    hair_color = "black"

    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name
        self.age = 20

    def say_hello(self):
        return f"Hello {self.first_name}"

    def __str__(self):
        return f"Object with name {self.first_name} from class Person with available methods: say_hello"


georgi = Person("Georgi", "Georgiev")
print(georgi.hair_color)
print(georgi.age)
print(georgi.say_hello())
print(Person)
print(georgi)


# Dynamic addition
georgi.eye_color = "brown"
print(georgi.eye_color)
# print(help(georgi))

########################
class Test:
    value = 52

    def __init__(self): #, value=42
        self.value += 10


print(Test.value)

obj = Test()
print(obj.value)

#########################

# Protected members - Can be reached outside class
# Private members -  Can't be reached outside class

# Protected
class Test:
    _pi = 3.14

    def __init__(self):
        pass


test = Test()
test._pi += 10
print(test._pi)

# Private - Cannot be changed
class Test:
    __pi = 3.14

    def __init__(self):
        pass


# test = Test()
# test.__pi += 10
# print(test.__pi)

