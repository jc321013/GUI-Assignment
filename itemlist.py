from item import Item
import csv


class ItemList:
    def __init__(self, Item, saving_items, loading_items):
        self.item_list = []

    def display_item_list(self, name):
        for items in self.item_list:
            if items.name == name:
                return items
        return None


    def save_item(self, items):
        for item in items:
            store_item = Item(item[0], item[1], float(item[2]), item[3].strip())
            self.item_list.append(store_item)

    def display_item_as_list(self):
        item_store = []
        for item in self.item_list:
            item_store.append([item.name, item.description, item.price, item.stock])
            return item_store

    def add_to_list(self, name, description, price, stock):
        self.item_list.append(Item(name, description, price, stock))
