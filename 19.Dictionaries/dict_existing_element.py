# Existence in Dictionaries
#key in new_dict - Checking for keys
#value in new_dict.values() - Checking for values
new_dict = {
    "one": 1,
    "two": 2,
    "three": 3,
}
if "one" in new_dict:
    print("The key exists in the dictionary 'new_dict'")
if 1 in new_dict.values():
    print("The value exists in the dictionary 'new_dict'")