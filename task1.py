# Creating a list
my_list = [1, 2, 3, 4, 5]
print("Initial list:", my_list)

# Adding elements to the list
my_list.append(6)
print("List after appending 6:", my_list)

# Removing elements from the list
my_list.remove(2)
print("List after removing 2:", my_list)

# Modifying elements in the list
my_list[2] = 10  # changing the third element to 10
print("List after modifying the third element to 10:", my_list)


# Creating a dictionary
my_dict = {'a': 1, 'b': 2, 'c': 3}
print("\nInitial dictionary:", my_dict)

# Adding elements to the dictionary
my_dict['d'] = 4
print("Dictionary after adding 'd': 4:", my_dict)

# Removing elements from the dictionary
del my_dict['b']
print("Dictionary after deleting 'b':", my_dict)

# Modifying elements in the dictionary
my_dict['c'] = 10  # changing the value of 'c' to 10
print("Dictionary after modifying 'c' to 10:", my_dict)


# Creating a set
my_set = {1, 2, 3, 4, 5}
print("\nInitial set:", my_set)

# Adding elements to the set
my_set.add(6)
print("Set after adding 6:", my_set)

# Removing elements from the set
my_set.remove(2)
print("Set after removing 2:", my_set)

# Modifying elements in a set (since sets are unordered and unindexed, we cannot modify elements directly,
# we can remove and add the new element to achieve a similar effect)
my_set.discard(3)  # removing element 3
my_set.add(10)     # adding element 10
print("Set after replacing 3 with 10:", my_set)
