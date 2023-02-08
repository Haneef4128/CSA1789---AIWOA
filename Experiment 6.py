# Initialize a list
my_list = [1, 2, 3, 4, 5]

# Add items to the list
my_list.append(6)
print("List after appending an item:", my_list)

# Extend the list with another list
my_list.extend([7, 8, 9])
print("List after extending with another list:", my_list)

# Delete items from the list
del my_list[0]
print("List after deleting the first item:", my_list)

my_list.pop(1)
print("List after popping the second item:", my_list)

my_list.remove(5)
print("List after removing the item with value 5:", my_list)
