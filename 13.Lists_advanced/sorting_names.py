# nums = ["one", "two", "four", "three"]
# nums.sorted(nums, key=len)

#.sort() changes the list
#.sorted() doesn't

names = input().split(", ")
result = sorted(names, key=lambda item: (-len(item), item))

print(result)
