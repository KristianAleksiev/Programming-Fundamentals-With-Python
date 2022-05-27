number_of_signs = int(input())
total_ascii_sum = 0

for signs in range(number_of_signs):
    char = input()
    total_ascii_sum += ord(char)

print(f"The sum equals: {total_ascii_sum}")

# ord(char) => Номер в ASCII таблицата на знака
# chr(integer) => Char съответстващ на номера в таблицата