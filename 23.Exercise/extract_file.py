path = input().split("\\")  # Escaping "\"
file_name, extension = path[-1].split(".")
print(f"File name: {file_name}")
print(f"File extension: {extension}")

