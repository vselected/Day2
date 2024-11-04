# Create variable that hold a list
my_list = ["String",1,2,3]
print(my_list)
print(len(my_list))
print(my_list[0:2])

# Create variable that hold another list
another_list = ["four", "five", 5]
print(my_list+another_list)

# Create a new variable that hold new list
new_list = ["One", "Two", "Three"]
new_list[0] = "Five"
print(new_list)
new_list.append("Six")
print(new_list)
popped_item = new_list.pop(0)
print(popped_item)
print(new_list)

new_list = ["a","e", "d", "b", "f", "c"]
num_list = [1,7,2,3,6,9,4,8]

new_list.sort()
num_list.sort()

print(new_list)
print(num_list)

num_list.reverse()
print(num_list)

# Exercise
# Lists
# Create a list that contains at least one string, one integer and one float.
# For example:
# [1, 'two', 3.14159]
# Note that the order and number of items doesn't matter.

list = [1, "String", 2.342]

# Dictionaries
# {"key1":"value1", "key2":"value2"}

my_dictionary = {"key1":"value1", "key2":"value2"}
print(my_dictionary["key1"])

prices_lookup = {"apple":2.99, "milk":5, "cheese":2.33}
print(prices_lookup["apple"])
d = {"k1":123, "k2":[2,4,2], "k3":{"kk1":2121, "kk2":"dsa"}}
print(d["k3"]["kk2"].upper())
print(d.keys())
print(d.values())
print(d.items())

# Exercise Dictionaries
# Create a dictionary where all the keys are strings, and all the values are integers.
# For example:
# {'Monday':19, 'Tuesday':20}

dictionary = {"Apple":3, "Milk":2, "Bread":1}