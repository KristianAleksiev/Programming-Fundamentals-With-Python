countries = input().split(", ")
capitals = input().split(", ")

country_info = {countries[index]: capitals[index] for index in range(len(countries))}

for key, value in country_info.items():
    print(f"{key} -> {value}")

# for country, capital in zip(countries, capitals):
#     print(f"{country} -> {capital}")

#country_info = dict(zip(countries, capitals))