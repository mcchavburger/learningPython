#lists are arrays
lists = []

#to add to a list
lists.append("My Added item")

print(lists)

#to remove from a list
lists.remove("My Added item")

#can also use the index if unaware of the item name
lists = ["Item1"]
del lists[0]

#check item in array
word = "Item 1"
lists = ["Item 1", "Item 2", "Item 3"]

if word in lists:
    print(word + " is in the list")
else:
    print(word + ' is not in the list')

for item in lists:
    print(item)