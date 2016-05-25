from Assignment1 import loading_items
from item import Item
import csv


class ItemList:
    def __init__(self):
        Item()
        loading_items()
        self.item_list = []
        pass

    def loading_items(self):
        with open('items.csv', 'rt') as in_file:
            reader = csv.reader(in_file)
            items = list(reader)
            for item in items:
                temp_item = item(item[0], item[1], item[2], item[3])
                self.item_list.append(temp_item)
            print(self.item_list)
        print("{} items loaded from items.csv".format(len(items)))
        return self.item_list

    def saving_items(self, items):
        with open('items.csv', 'w', newline='') as out_file:
            writer = csv.writer(out_file, delimiter=',')
            writer.writerows(items)
        count = len(items)
        print("{} items saved to items.csv\nHave a nice day :)".format(count))
