###Definition and usage
# Collection which is index supported and changeable, allows duplicating items
# Lists can store elements with different data types
# list_example = ["apple", "banana", "cherry"]

### Storing data
#[[], [], []] -> Matrix

### Creating lists
#list = [] /// list()

### Accessing elements
#a = [1, 2, 3, 4, 5, 6]
#print(a[0]) => 1 - accessing with index
#print(a[-1]) => Last element

### List manipulations

## Split()

#some_text = "a b c d"
#my_list = some_text.split(" ") -> Creating a list from a string based on a specific criteria (" ")
# numbers = input().split(" ")
# split(sep=None, maxsplit = -1) => no limit
# a = "1, 2, 3, 4, 5"
# a.split(" ", maxsplit=2) = > Splits the first two elements from the string as a seperate element in the list

## Append()

# empty_list = []
# empty_list.append(Value to be appended)
# empty_list += [value]

## Remove()

# a = [1, 2, 3, 4, 5]
# a.remove(5) => N.B.! Value, not index - If value is in list more than once

## Pop() => Removes the last element in the list

# list.pop()
# list.pop([index]) => Removes the element by Index


## Join() - Only with strings

#test = ["a", "b", "c"]
#print("-".join(test)) => "a-", "b-", "c-"

## Range
#print(list(range(1, 11)))

### Looping through lists
#        FOR
# for element in list:
# my_list = ["dog", "cat", "fish"]
#for element in my_list:
#   print(element)

#for index in range(len(my_list)
#   print(my_list[index])

# for index, value in enumerate(my_list):
#    print(index, value)

#       WHILE
# while i < len(my_list):
#    print(my_list[i], end=" ")

### Searching in lists

# if value in list:
# if value not in list:
