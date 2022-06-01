number = int(input())
keyword = input()
keyword_list = []
string_list = []

for _ in range(number):
    current_string = input()
    string_list.append(current_string)
    if keyword in current_string:
        keyword_list.append(current_string)

print(string_list)
print(keyword_list)