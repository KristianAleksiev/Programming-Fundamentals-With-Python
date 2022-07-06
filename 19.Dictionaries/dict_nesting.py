# Nested dictionaries

nested_dict = {
    "dict_one": {
        "key_one": "Value_one",
        "key_two": "Value_two",
        "key_three": "Value_three"
    },
    "dict_two": {
        "key_four": "Value_four",
        "key_five": "Value_five",
        "key_nested": {
            "key_six": "Value_six",
        }
    }
}

print(nested_dict["dict_one"]["key_one"])
print(nested_dict["dict_two"]["key_nested"]["key_six"])

nested_dict["dict_two"]["key_nested"]["key_seven"] = "Value_seven"
print(nested_dict["dict_two"]["key_nested"]["key_seven"])


for key, value in nested_dict.items():
    for nested_key, nested_value in value.items():
        print(nested_value)
