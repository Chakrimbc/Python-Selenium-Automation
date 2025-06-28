items = [1,2,"chakri",4,"Me"]
print(items[2])
print(items[-1])
print(items[-1:])
print(items.index("Me"))
items.insert(2,"gonthini")
print(items)
# How to add the values in the list
items.append("The End")
print(items)
#How to update the values
items[3] = "Chakradhar"
print(items)
#How to delete the value in list with index
del items[4]
print(items)
#How to remove specific value from the list
items.remove(2)
print(items)
