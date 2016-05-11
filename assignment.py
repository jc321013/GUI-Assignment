__JaredMarcolongo__ = 'jc321013'

""" CP1404 Assignment 1 - 2016
    Items for Hire - a console-based item hiring program
    Jared Marcolongo
    21/03/2016
    https://github.com/jc321013/Cp1404-Assignment-1 """

""" Pseudocode:

function main()
    display title of document and name
    display how many items loaded from items.csv
    open csv file of in stock items
    close csv file
    display items
    display menu
    get choice
    while choice is not 'Q'
        if choice is 'L'
            display items
        else if choice is 'H'
            call hiring_an_item()
        else if choice is 'R'
            return item
        else if choice is 'A'
            call loading_an_item()
        else
            display invalid choice message
        display menu
        get choice
    print farewell message


function loading_an_item()
    get item name, description and price to add
    open items.csv as fileout for writing
    for each item in items
        write item to fileout
        write newline to fileout
    close fileout
    add item to csv file
        display the new item added


function hiring_an_item()
    display available item
    get item choice
        display item chosen
    chosen item returns an * for unavailable
        display available items
    if no items available
        display unavailable message
    display menu    """

import csv

Menu = "\nMenu:\n(L)ist all items\n(H)ire an item\n(R)eturn an item\n(A)dd new item to stock\n(Q)uit"


def main():
    print("Items for Hire- by Jared Marcolongo")
    print("3 items loaded from items.csv")


    # reads from csv file and displays lines in file
    in_file = open("items.csv", "r", encoding='utf-8')
    reader = csv.reader(in_file.readlines())
    in_file.close()
    for rows in reader:
        print(rows)

    print(Menu)
    # .upper allows user to input both lower and upper case letters
    choice = input("Choice: ").upper()
    while choice != "Q":
        if choice == "L":
            print("All items on file(* indicated item is currently out):")
            print(Items)
        elif choice == "H":
            hiring_an_item()
        elif choice == "R":
            return_item = input("Number of an item to return: ")
            print(return_item, "returned")
        elif choice == "A":
            loading_items()
        else:
            print("Invalid menu choice.")
        print(Menu)
        choice = input("Enter your choice: ").upper()

    print("5 items saved to items.csv\n" "Have a nice day")


def loading_items():
        # empty list ofitems, function adds new items to that list
        add_item = []
        item = 'item_name', 'item_description', 'item_price'
        item_name = input("Item name: ")
        item_description = input("Description: ")
        item_price = input("Price per day: ")
        print(item_name, (item_description), "$", item_price)
        print(item)
        for item in add_item:
            # adds item to add_item
            add_item.append(item)
            # writes to file items.csv with the added item
            out_file = open("items.csv", "a")
            out_file.write(add_item)
            out_file.close()


def hiring_an_item():
    # function loads items and allows user to choose available stock
    print("All items on file(* indicates item is currently out)\n", Items)
    hiring_choice = input("Enter the number of an item to hire: ")
    while hiring_choice != "":
        if hiring_choice == "0":
            print("Rusty Bucket hired for $0.00")
        elif hiring_choice == "1":
            print("Golf cart currently out of stock")
        elif hiring_choice == "2":
            print("Thermomix currently out of stock")
        elif hiring_choice == "3":
            print("AeroPress hired for $5")
        elif hiring_choice == "4":
            print("Guitar hired for $12.95")
    else:
        print("Invalid item choice")
    print(Items)
    hiring_choice = input("Enter the number of an item to hire: ")



main()
