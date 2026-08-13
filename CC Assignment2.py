# q1
# 1.1
# 1024160130
L = [10, 0, 20, 40, 10, 60, 0, 10, 30, 0]
print(L)

# 1.2
# adding a new number to the end of the list
L.append(100)
print(L)

# inserting a number at a particular index
L.insert(3, 200)
print(L)

# 1.3
# removing the first occurrence of 10 from the list
L.remove(10)
print(L)

# popping the element at index 1
L.pop(1)
print(L)

# 1.4
L.sort()
print(L)
L.sort(reverse=True)
print(L)

# 1.5
print(L[:3])
print(L[-3:])

# 1.6
average = sum(L) / len(L)
print(average)
greater_than_average = [x for x in L if x > average]
print(greater_than_average)


# q2
# 2.1
scores = (10, 0, 20, 40, 10, 60, 0, 10)
highest_score = max(scores)
print(highest_score)
print(scores.index(highest_score))
print(min(scores))
print(scores.count(min(scores)))

# 2.2
scores = list(scores[::-1])
print(scores)
# tuples cannot be reversed in-place because of their immutability, so we convert it to a list

# 2.3
a = int(input("enter a number: "))
if a in scores:
    print("yes, index is:", scores.index(a))
else:
    print("no")

# 2.4
scores = (10, 0, 20, 40, 10, 60, 0, 10)

# scores[0] = 100
error_we_got = "'tuple' object does not support item assignment"
# tuples do not allow modifying elements once created since they are immutable, unlike mutable lists

# 2.5
first, second, *remaining = scores
print("First Score:", first)
print("Second Score:", second)
print("Remaining Scores:", remaining)


# q3
import random
from collections import Counter

# 3.1
random.seed(1024160130)
numbers = []
for i in range(100):
    numbers.append(random.randint(100, 900))
print(numbers)

# 3.2
odd = [x for x in numbers if x % 2 != 0]
print(len(odd))
print(odd)

# 3.3
even = [x for x in numbers if x % 2 == 0]
print(len(even))
print(even)

# 3.4
def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

prime = [x for x in numbers if isPrime(x)]
print(len(prime))
print(prime)

# 3.5
freq = Counter(numbers)
print(freq.most_common(1))


# q4
digits = [1, 0, 2, 4, 1, 6, 0, 1]
print(digits)

A = {digit * 7 for digit in digits}
B = {digit * 9 for digit in digits}
print(A)
print(B)

# 4.1
print(A.union(B))

# 4.2
print(A.intersection(B))

# 4.3
print(A.difference(B))
print(B.difference(A))
# difference gives items present only in the first set, whereas symmetric_difference gives all items from both sets except the common ones

# 4.4
print(A.symmetric_difference(B))

# 4.5
print(A.issubset(B))
print(B.issuperset(A))

# 4.6
x = int(input("Enter value: "))
A.discard(x)
print(A)
# discard is preferred over remove because it won't crash or throw a KeyError if the element isn't in the set


# q5
my_dict = {
    "name": "Bisman Singh Rai",
    "roll_no": "1024160130",
    "branch": "COSE",
    "age": "21",
    "city": "Ludhiana"
}

# i. Rename "city" to "location" using pop()
my_dict["location"] = my_dict.pop("city")
print("\nAfter renaming city to location:")
print(my_dict)

# ii. Add CGPA
my_dict["cgpa"] = 9.1
print("\nAfter adding CGPA:")
print(my_dict)

# iii. Increase age by 1
my_dict["age"] = int(my_dict["age"]) + 1
print("\nAfter increasing age by 1:")
print(my_dict)

# iv. Delete "branch" using pop() and del
# making two distinct shallow copies of the dictionary
dict_pop = my_dict.copy()
dict_del = my_dict.copy()

# Using pop()
removed_value = dict_pop.pop("branch")

# Using del
del dict_del["branch"]

print("\nUsing pop():")
print(dict_pop)

print("\nUsing del:")
print(dict_del)

# pop returns the value of the deleted key, whereas del is a statement that just deletes the key without returning any value
print("\npop() returns the removed value, while del only removes the key-value pair and returns nothing.")

# v. Iterate using items()
print("\nKey-value pairs:")
for key, value in my_dict.items():
    print(key, "→", value)

# vi. Check whether "email" exists
print("\nChecking for email:")
if "email" in my_dict:
    print("Email:", my_dict["email"])
else:
    print("Email key does not exist.")

# vii. Create friend_dict and merge using ** syntax
friend_dict = {
    "name": "Gurman Singh",
    "roll_no": "1024160142",
    "branch": "COSE",
    "age": 21,
    "city": "Chandigarh"
}

merged_dict = {**my_dict, **friend_dict}
print("\nFriend Dictionary:")
print(friend_dict)

print("\nMerged Dictionary:")
print(merged_dict)

# for duplicate keys during merging, the second dictionary's value takes priority and overrides the first
print("\nWhen both dictionaries have the same key, the value from the second dictionary wins.")

# viii. Dictionary comprehension
# filtering the dictionary to retain only the entries where the value is of string type
string_dict = {
    key: value
    for key, value in my_dict.items()
    if isinstance(value, str)
}

print("\nDictionary containing only string values:")
print(string_dict)
