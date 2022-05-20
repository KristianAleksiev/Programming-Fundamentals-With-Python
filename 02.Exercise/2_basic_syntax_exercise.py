### Basic syntax, conditional statements and loops - Exercise


### Enumerate function
number = "123545678"

# for current_digit in range(0, len(number)):
#     print(current_digit)
#     if int(number[current_digit]) % 2 == 0:
#         print(number[current_digit])
#
#
# for current_digit in number:
#     if int(current_digit) % 2 ==0:
#         print(current_digit)

#for index, value in enumerate(number): #Едновременно използване на две стойности през итерациите
#    print(index, value)

### Slicing

random_string = "Goshoepich"
new_string = random_string[::-1] #[start:end:step]
print(new_string)

#endswith() startswith() - Дали започва или съответно завършва с нещо

some_string = "https:/tradingview.com/apIjemqI"
if some_string.startswith("https"):
    print("This site has SSL Certificate")
else:
    print("It has no SSL Certificate ")


