import csv


class Item:
    def __init__(self, name, description, price, stock):
        self.name = name
        self.description = description
        self.price = price
        self.stock = stock

    def __str__(self):
        return "{} ({}), ${} is {}".format(self.name, self.description, self.price, self.stock)
