from item import Item
import csv


class ItemList:
    def __init__(self):
        self.items = []

    def display_item_list(self, name):
        for item in self.items:
            if item.name == name:
                return item
        return None


    def save_item(self, items):
        for item in items:
            store_item = Item(item[0], item[1], float(item[2]), item[3].strip())
            self.items.append(store_item)

    def display_item_as_list(self):
        item_store = []
        for item in self.items:
            item_store.append([item.name, item.description, item.price, item.stock])
            return item_store

    def add_to_list(self, added_name, added_description, added_price, added_stock):
        self.items.append(Item(added_name, added_description, added_price, added_stock))
