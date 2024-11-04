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