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
# from itemlist import ItemList


# from Assignment1 import loading_items


class ExperimentHire(App, Item):
    action_label = StringProperty()

    def __init__(self, **kwargs):
        """Constructs main app"""
        super(ExperimentHire, self).__init__(**kwargs)
        self.experimentHire = {}

    def build(self):
        """Builds the Kivy Gui and references to the root Kivy Widget"""
        self.title = "Experiment Hire"
        self.root = Builder.load_file('GUI A2.kv')
        self.create_entry_buttons()
        return self.root

    def list_items(self):
        label_display = 'Choose action from the left menu, then select items on the right'
        self.root.ids.list_items.text = "List Items"
        self.root.ids.action_label.text = str(label_display)
        return label_display

    def hiring_item(self):
        label_display = 'Select available items to hire'
        self.root.ids.hire_item.text = 'Hire Items'
        self.root.ids.action_label.text = str(label_display)
        temp_button = Button(text="Rusty Bucket")
        if temp_button.bind(on_release=self.root.ids.rusty_bucket):
            return label_display


    def create_entry_buttons(self):
        """Constructs the entry buttons and allows the GUI to access them"""
        for name in self.experimentHire:
            temp_button = Button(text=name)
            temp_button.bind(on_release=self.press_entry)
            #  using the add_widget it adds the button to the ""newItems""
            self.root.ids.newItem.add_widget(temp_button)

    def press_entry(self, instance):
        """handles the pressing of entry buttons"""
        name = instance.text
        self.root.ids.action_label.text = "{} ${} Per Day".format(name, self.experimentHire[name])
        # set button state
        # print(instance.state)
        instance.state = 'down'

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
        # this controls the opening of the popup
        self.root.ids.popup.open()

    def press_save(self, added_name, added_description, added_price):
        """Saves the new entry to the front page of the GUI, and controls the pressing of the save button """
        label_display = "All fields must be completed"
        price_label = "Must be a valid number"
        if added_name == "" or added_description == "" or added_price == "" :
            self.root.ids.popup_label.text = label_display
            return label_display

        # if added_price  < 0:
        #     self.root.ids.popup_label.text = price_label
        #     return price_label

        self.experimentHire[added_name] = added_description, added_price
        # Number columns is depended upon the number of entries
        self.root.ids.newItem.cols = len(self.experimentHire) // 5 + 1
        # same function as in function above(create_entry_buttons), new entry button
        temp_button = Button(text=added_name)
        temp_button.bind(on_release=self.press_entry)
        self.root.ids.newItem.add_widget(temp_button)
        # dismisses the popup closing it
        self.root.ids.popup.dismiss()
        # Clears the fields
        self.clear_fields()

    def clear_fields(self):
        """ Puts empty string in the text input fields from add entry"""
        self.root.ids.addedName.text = ""
        self.root.ids.addedDescription.text = ""

    def press_cancel(self):
        """ handles the pressing for the cancel in the add entry"""
        self.root.ids.popup.dismiss()
        self.clear_fields()
        self.action_label = ""




# create and start the App running
ExperimentHire().run()
