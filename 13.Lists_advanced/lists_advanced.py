# List comprehension
# [new_x for x in list] -  Less memory than looping

# [output expression (new_x) for variable(x) in input sequence(list) if optional parameter(x > 0)]

# print(sum([num ** 2 for num in range(1000)]))
# x = [num for num in range(5)]
# print(list(range(11)))


nums = [1, 2, 3, 4, 5, 6]
squares = [num ** 2 for num in nums]
print(squares)
evens = [num ** 2 for num in nums if num % 2 == 0 if num > 4]
print(evens)

# filtered = [True if x % 2 == 0 else False for x in nums]

matrix = [[x for x in range(3)] for _ in range(3)]
print(matrix)


#help(list)

list = [1, 2, 3]
other_list = [4, 5]
list.extend(other_list)
print(list)

# insert

list.insert(1, 5)

# .clear()
# .pop(0) Delete 0 index and return it, pop() last element
# .remove() - by value - first element encountered
# .count(element) - how many times element in list
# .index(element) - index of first encountered element
# .reverse()

# map()
# def square_numbers(n):
#     return n ** 2

# x = list(map(square_numbers, [2, 3, 4, 5, 6, 7]))
# print(x)
#
# str_list = ["1", "2", "3"]
# int_list = list(map(int, str_list)) # Will return everything
# print(int_list)

# filter()
# list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5, 6])) # Only return the elements which return True


## Swapping list elements

lst = ["a", "b", "c"]
lst[0], lst[2] = lst[2], lst[0]

## The set() function
numbers = [1, 2, 3, 4, 5, 6, 6, 6, 6, 3, 3, 2]
unique = list({numbers})
print(unique)
