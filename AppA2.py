""" CP1404 Assignment 2 - 2016
    ExperimentHire - a GUI kivy app based hiring program
    Jared Marcolongo
    27/05/2016
    https://github.com/jc321013/GUI-Assignment"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.properties import StringProperty
from item import Item
from itemlist import ItemList
from Assignment1 import loading_items
from Assignment1 import saving_items

List_Items = 0
Hire_Items = 1
Return_Items = 2
Add_Items = 3


class ExperimentHire(App):
    action_label = StringProperty()

    def __init__(self, **kwargs):
        """Constructs main app"""
        super(ExperimentHire, self).__init__(**kwargs)



    def build(self):
        """Builds the Kivy Gui and references to the root Kivy Widget"""
        self.title = "Experiment Hire"
        self.root = Builder.load_file('GUI A2.kv')
        self.mode = List_Items
        self.create_entry_buttons()
        labelButton = "Choose Action From The left, then Select Items From the Right"
        self.action_label = str(labelButton)
        self.item_listing = []
        self.list_item = ItemList()
        item_store = loading_items()
        self.list_item.save_item(item_store)
        return self.root

    def button_status(self, status):
        while status != 'in' or 'out':
            if status == 'in':
                pass
            elif status == 'out':
                pass

    def list_items(self, items_avaliable):
        items_avaliable = self.list_item


    def listing_items(self):
        label_display = 'Choose action from the left menu, then select items on the right'
        self.root.ids.listItems.text = "List Items"
        self.root.ids.action_label.text = str(label_display)
        self.mode = List_Items
        self.item_listing = []
        self.root.ids.listItems.state = 'down'
        self.root.ids.hireItem.state = 'normal'
        self.root.ids.addButton.state = 'normal'
        self.root.ids.itemConfirm.state = 'normal'
        self.root.ids.returnItem.state = 'normal'
        return label_display

    def hiring_item(self):
        label_display = 'Select available items to hire'
        self.root.ids.hireItem.text = 'Hire Items'
        self.root.ids.action_label.text = str(label_display)
        self.mode = Hire_Items
        self.item_listing = []
        self.root.ids.listItems.state = 'normal'
        self.root.ids.hireItem.state = 'down'
        self.root.ids.addButton.state = 'normal'
        self.root.ids.itemConfirm.state = 'normal'
        self.root.ids.returnItem.state = 'normal'
        self.action_label = ""
        return label_display

    def confirm_item(self):
        if self.mode == Hire_Items:
            for item in self.item_listing:
                item.stock = "out"
                self.set_button_to_normal()
            self.listing_items()
        elif self.mode == Return_Items:
            for item in self.item_listing:
                item.stock = "out"
                self.set_button_to_normal()
            self.listing_items()

        self.root.ids.listItems.state = 'normal'
        self.root.ids.hireItem.state = 'normal'
        self.root.ids.addButton.state = 'normal'
        self.root.ids.itemConfirm.state = 'down'
        self.root.ids.returnItem.state = 'normal'


    def return_item(self):
        label_display = 'Select Items To Return'
        self.root.ids.returnItem.text = 'Return Item'
        self.root.ids.action_label.text = str(label_display)
        self.mode = Return_Items
        self.item_listing = []
        self.root.ids.listItems.state = 'normal'
        self.root.ids.hireItem.state = 'normal'
        self.root.ids.addButton.state = 'normal'
        self.root.ids.itemConfirm.state = 'normal'
        self.root.ids.returnItem.state = 'down'
        return label_display

    def set_button_to_normal(self):
        for button in self.root.ids.experiment_hire.children:
            button.state = 'normal'
            self.item_listing = []

    def create_entry_buttons(self):
        """Constructs the entry buttons and allows the GUI to access them"""
        for item in self.list_item.items:
            temp_button = Button(text=item.name)
            temp_button.bind(on_release=self.press_entry)
            #  using the add_widget it adds the button to the ""newItems""
            self.root.ids.newItem.add_widget(temp_button)

    def press_entry(self, instance):
        """handles the pressing of entry buttons"""
        item = self.list_item.display_item_list(instance.text)
        if self.mode == List_Items:
            self.action_label = str(item)
        elif self.mode == Hire_Items:
            if item.stock == 'in':
                if item not in self.item_listing:
                    self.item_listing.append(item)
                    instance.state = 'down'
                    total = 0
                    name = []
                    for item in self.item_listing:
                        total += item.price
                        name.append(item.name)
                    self.action_label = "Hiring: {} for ${}".format(', '.join(name), total)
        elif self.mode == Return_Items:
            if item.stock == 'out':
                if item not in self.item_listing:
                    self.item_listing.append(item)
                    instance.state = 'down'
                    names = []
                    for item in self.item_listing:
                        names.append(item.name)
                    self.action_label = "Returning: {}".format(', '.join(names))

        elif self.mode == Add_Items:
            pass
        self.action_label = "{}, {}, {}".format(item[0], self.experimentHire[item][1], self.experimentHire[item][2])


    def item_add(self):
        """
        Clear any buttons that have been selected (visually) and reset status text
        :return: None
        """
        # use the .children attribute to access all widgets that are "in" another widget
        for instance in self.root.ids.newItem.children:
            instance.state = 'normal'
        self.action_label = ""

    def press_add(self):
        """Handles the pressing of the add buttons, and the display of the label"""
        self.root.ids.popup_label.text = "Enter details for new Item"
        self.mode = Add_Items
        self.item_listing = []
        self.root.ids.listItems.state = 'normal'
        self.root.ids.hireItem.state = 'normal'
        self.root.ids.addButton.state = 'down'
        self.root.ids.itemConfirm.state = 'normal'
        self.root.ids.returnItem.state = 'normal'
        # this controls the opening of the popup
        self.root.ids.popup.open()

    # Saves the new entry to the front page of the GUI, and controls the pressing of the save button
    def press_save(self, added_name, added_description, added_price):
        try:
            self.list_item.add_to_list(added_name, added_description, float(added_price), 'in')
            # self.experimentHire.append(receive_object(added_name, added_description, added_price))

            label_display = "All fields must be completed"
            price_label = "Must be a valid number"
            if added_name == "" or added_description == "" or added_price == "":
                self.root.ids.popup_label.text = label_display
                return label_display

            # while not added_price < 0:
            #     try:
            #         while added_price < 0:
            #             self.root.ids.popup_label = str(price_label)
            #             return price_label
            #     except ValueError:
            #         self.root.ids.popup_label = str(price_label)
            #         return price_label

            # self.experimentHire[added_name] = added_description, added_price
            # Number columns is depended upon the number of entries
            self.root.ids.newItem.cols = len(self.list_item.items)
            temp_button = Button(text=added_name)
            temp_button.bind(on_release=self.press_entry)
            self.root.ids.newItem.add_widget(temp_button)
            # dismisses the popup closing it
            self.root.ids.popup.dismiss()
            # Clears the fields
            self.clear_fields()
        except ValueError:
            self.root.ids.addedPrice.text = ''

    def clear_fields(self):
        """ Puts empty string in the text input fields from add entry"""
        self.root.ids.addedName.text = ""
        self.root.ids.addedDescription.text = ""
        self.root.ids.addedPrice.text = ""

    def press_cancel(self):
        """ handles the pressing for the cancel in the add entry"""
        self.root.ids.popup.dismiss()
        self.clear_fields()
        self.action_label = ""

    def GUI_finish(self):
        saving_items(self.root.list_item.display_item_as_list())
        return








"""create and start the App running"""
ExperimentHire().run()
