start_index = int(input())
end_index = int(input())
final_string = ""

for index in range(start_index, end_index + 1):
    final_string += chr(index) + " "

print(final_string)
