# Task 1: Function that lets user add items to a list

def addItem(item):
    l.append(item)

# Task 2: Function that lets user remove items from list

def removeItem(item):
    if (item not in l):
        print("You can't remove an item not on the list!")
    else:
        l.remove(item)

# Task 3: Add function that prints out whole list

def printList():
    s = ""
    for i in l:
        s = s + i + "\n"
    print("Shopping List:")
    print(s)

l = []
print("Welcome to you shopping list! Please select and option from below.")
while True:
    user_input = input("\nType add, remove, view, or exit based on how you'd like to adjust your shopping list. ")
    if (user_input == "exit"):
        break
    elif(user_input == "view"):
        printList()
    elif (user_input == "add"):
        new_item = input("What item would like to add to you shopping list? ")
        addItem(new_item)
    elif (user_input == "remove"):
        print(l)
        remove_item = input("What item would you like to remove? ")
        removeItem(remove_item)
    else:
        print("Please select a valid option.")