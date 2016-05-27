""" CP1404 Assignment 2 - 2016
    ExperimentHire - a GUI kivy app based hiring program
    Jared Marcolongo
    27/05/2016
    https://github.com/jc321013/GUI-Assignment"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.properties import StringProperty
from itemlist import ItemList
from Assignment1 import saves_items as save_items, loads_items as load_items

List_Items = 0
Hire_Items = 1
Return_Items = 2
Add_Items = 3


class ExperimentHire(App):
    action_label = StringProperty()

    def __init__(self, **kwargs):
        super(ExperimentHire, self).__init__(**kwargs)

    # Builds the GUI Kivy
    def build(self):
        self.mode = List_Items
        self.list_item = ItemList()
        temp_list = load_items()
        self.item_listing = []
        self.list_item.save_items(temp_list)
        self.action_label = "Select a mode on the left side, then select items on the right"
        self.title = 'Experiment Hire'
        self.root = Builder.load_file('GUI A2.kv')
        self.create_entry_buttons()
        return self.root

    # This function controls the status display of the items
    def listing_items(self):
        self.mode = List_Items
        self.item_listing = []
        statusLable = "Select a mode on the left side, then select items on the right"
        self.action_label = str(statusLable)
        self.root.ids.listItems.state = 'down'
        self.root.ids.hireItem.state = 'normal'
        self.root.ids.addButton.state = 'normal'
        self.root.ids.itemConfirm.state = 'normal'
        self.root.ids.returnItem.state = 'normal'

    # This function controls when the user wants to hire out an item, it passes it through the confirm button andthen deselects it from the GUI making it unavailable. It can only hire out items that are available
    def hiring_item(self):
        statusLable = 'Select Available Items to Hire'
        self.root.ids.action_label.text = str(statusLable)
        self.mode = Hire_Items
        self.item_listing = []
        self.root.ids.listItems.state = 'normal'
        self.root.ids.hireItem.state = 'down'
        self.root.ids.addButton.state = 'normal'
        self.root.ids.itemConfirm.state = 'normal'
        self.root.ids.returnItem.state = 'normal'



    # This function controls when the user wants to return out an item, it passes it through the confirm button and then you are able to select unavailable items it from the GUI making them available
    def return_item(self):
        statuslabel = 'Select available items to return'
        self.root.ids.action_label.text = str(statuslabel)
        self.mode = Return_Items
        self.item_listing = []
        self.root.ids.listItems.state = 'normal'
        self.root.ids.hireItem.state = 'normal'
        self.root.ids.addButton.state = 'normal'
        self.root.ids.itemConfirm.state = 'normal'
        self.root.ids.returnItem.state = 'down'


    # This function controls the hiring and return fucntions, if items are 'out' you can return them, if items are 'in' you can hire them
    def confirm_item(self):
        if self.mode == Hire_Items:
            for item in self.item_listing:
                item.stock = "out"
                self.set_button_to_normal()
                self.listing_items()

        elif self.mode == Return_Items:
            for item in self.item_listing:
                item.stock = "in"
                self.set_button_to_normal()
                # self.item_listing.state = 'normal'
            self.listing_items()

        for self.item in self.item_listing:
            if self.item.stock == "in":
                self.item.state = 'down'
                for button in self.root.ids.newItem.children:
                    button.state = 'down'
                    self.item_listing = []
            elif self.item.stock == "in":
                self.item.state = 'normal'
                for button in self.root.ids.newItem.children:
                    button.state = 'normal'
                    self.item_listing = []



    # Creates the entry button and then adds it to the GUI Kivy
    def create_entry_buttons(self):
        # creates a button for each new item entry being added
        for item in self.list_item.items:
            temp_button = Button(text=item.name)
            temp_button.bind(on_release=self.press_entry)
            # adds the button to "newItem" using add.widget
            self.root.ids.newItem.add_widget(temp_button)

    # updates the button status reloading if the button selected is in or out and passes them
    def button_status(self, status):
        while status != 'in' or 'out':
            if status == 'in':
                pass
            elif status == 'out':
                pass

    # Handles the entry buttons pressing and updates the status text
    def press_entry(self, instance):
        item = self.list_item.get_item(instance.text)
        if self.mode == List_Items:
            self.action_label = str(item)
        elif self.mode == Hire_Items:
            if item.stock == 'in':
                if item not in self.item_listing:
                    self.item_listing.append(item)
                    instance.state = 'down'
                    running_total = 0
                    names = []
                    for item in self.item_listing:
                        running_total += item.price
                        names.append(item.name)
                    self.action_label = "Hiring: {} for ${}".format(', '.join(names), running_total)
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

    # Sets the button status back to normal after being selected
    def set_button_to_normal(self):
        # uses the .children attribute to access all widgets that are located in another widget
        for button in self.root.ids.newItem.children:
            button.state = 'normal'
            self.item_listing = []




    # Handles the add button, and opens up the pop up window
    def press_add(self):
        self.mode = Add_Items
        self.item_listing = []
        self.action_label = ''
        self.root.ids.listItems.state = 'normal'
        self.root.ids.hireItem.state = 'normal'
        self.root.ids.addButton.state = 'down'
        self.root.ids.itemConfirm.state = 'normal'
        self.root.ids.returnItem.state = 'normal'
        self.action_label = "Enter Details For New Item"
        self.root.ids.popup.open()
        pass

        # clears any button that has been selected by user and reset the status text

    def clear_fields(self):
        # if this function is not completed, the popup will continue to have text in the fields after submission
        self.root.ids.addedName.text = ""
        self.root.ids.addedDescription.text = ""
        self.root.ids.addedPrice.text = ""

    # handles the cancel button in the popup window
    def press_cancel(self):
        self.root.ids.popup.dismiss()
        self.clear_fields()
        self.action_label = ""

    # handles the save item button in the popup window, saves a new entry to the memory
    def press_save(self, added_name, added_description, added_price):
        # changes the number of columns based on the number of entries
        try:
            if added_name == "" or added_description == "" or added_price == "":
                self.root.ids.popup_label.text = "All Fields Must Be Completed"
            if float(added_price) < 0:
                self.root.ids.popup_label.text = "Must Be a Valid Number"
            self.list_item.add_item(added_name, added_description, float(added_price), 'in')
            # number of entries
            self.root.ids.newItem.cols = len(self.list_item.items) // 5 + 1
            # add button for new entry
            new_button = Button(text=added_name)
            new_button.bind(on_release=self.press_entry)
            self.root.ids.newItem.add_widget(new_button)
            self.root.ids.popup.dismiss()
            self.clear_fields()
        except ValueError:
            self.root.ids.addedPrice.text = ''
        # creates an error check if the fields are empty






    # after the GUI is closed this saves the created items to the list
    def on_stop(self):
        save_items(self.list_item.get_items_as_list())




# runs the main program
ExperimentHire().run()
