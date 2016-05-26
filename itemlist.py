from item import Item

# This class has two methods, one for loads and saves the items and another for reutnring the list to the file
class ItemList:

    def __init__(self):
        self.items = []
        pass

    def get_item(self, name):
        for item in self.items:
            if item.name == name:
                return item
        return None

    def save_items(self, items):
        for item in items:
            temp_item = Item(item[0], item[1], float(item[2]), item[3].strip())
            self.items.append(temp_item)

    def get_items_as_list(self):
        temp_list = []
        for item in self.items:
            temp_list.append([item.name, item.description, item.price, item.stock])
        return temp_list

    def add_item(self, name, description, price, stock):
        self.items.append(Item(name, description, price, stock))
