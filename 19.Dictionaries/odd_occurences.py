# 1)
# from collections import defaultdict
# words = input().split()
# counter_of_words = dafaultdict(int)
#
# for word in words:
#     counter_of_words[word.lower()] +=1
#
# print(" ".join([word for word, count in counter_of_words.items() if count % 2 != 0]))
#


# 2)
words = input().split()
dict = {}
for word in words:
    word_lower = word.lower()
    if word_lower not in dict:
        dict[word_lower] = 0
    dict[word_lower] += 1

for key, value in dict.items():
    if value % 2 != 0:
        print(key, end=" ")
