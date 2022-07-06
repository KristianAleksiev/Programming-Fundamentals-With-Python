data = [("Peter", 22), ("Amy", 18), ("George", 35)]
dictionary = {key: value for (key, value) in data}
print(dictionary)


example_dict = {"a": 10, "b": 20, "c": 30}
comprehension_dict = {key: value + 10 for (key, value) in example_dict.items()}
print(comprehension_dict)

