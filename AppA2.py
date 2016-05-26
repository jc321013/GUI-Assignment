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

LIST_MODE = 0
HIRE_MODE = 1
RETURN_MODE = 2
ADD_MODE = 3


class ExperimentHire(App):

    action_label = StringProperty()

    def __init__(self, **kwargs):
        super(ExperimentHire, self).__init__(**kwargs)

    def build(self):
        self.mode = LIST_MODE
        self.item_list = ItemList()
        temp_list = load_items()
        self.selected_items = []
        self.item_list.store_items(temp_list)
        self.action_label = "Select a mode on the left side, then select items on the right"
        self.title = 'Experiment Hire'
        self.root = Builder.load_file('GUI A2.kv')
        self.create_entry_buttons()
        return self.root

    def listing_items(self):
        self.mode = LIST_MODE
        self.selected_items = []
        self.action_label = "Select a mode on the left side, then select items on the right"
        self.root.ids.listItems.state = 'down'
        self.root.ids.hireItem.state = 'normal'
        self.root.ids.addButton.state = 'normal'
        self.root.ids.itemConfirm.state = 'normal'
        self.root.ids.returnItem.state = 'normal'

    def hiring_item(self):
        self.mode = HIRE_MODE
        self.selected_items = []
        self.action_label = 'Select Available Items to Hire'
        self.root.ids.listItems.state = 'normal'
        self.root.ids.hireItem.state = 'down'
        self.root.ids.addButton.state = 'normal'
        self.root.ids.itemConfirm.state = 'normal'
        self.root.ids.returnItem.state = 'normal'

    def return_item(self):
        self.mode = RETURN_MODE
        self.selected_items = []
        self.action_label = 'Select available items to return'
        self.root.ids.listItems.state = 'normal'
        self.root.ids.hireItem.state = 'normal'
        self.root.ids.addButton.state = 'normal'
        self.root.ids.itemConfirm.state = 'normal'
        self.root.ids.returnItem.state = 'down'

    def confirm_item(self):
        if self.mode == HIRE_MODE:
            for item in self.selected_items:
                item.stock = "out"
                self.set_button_to_normal()
            self.listing_items()

        elif self.mode == RETURN_MODE:
            for item in self.selected_items:
                item.stock = "in"
                self.set_button_to_normal()
            self.listing_items()

    def create_entry_buttons(self):
        for item in self.item_list.items:
            temp_button = Button(text=item.name)
            temp_button.bind(on_release=self.press_entry)
            self.root.ids.newItem.add_widget(temp_button)

    def button_status(self,status):
        while status != 'in' or 'out':
            if status == 'in':
                pass
            elif status == 'out':
                pass

    def press_entry(self, instance):
        item = self.item_list.get_item(instance.text)
        if self.mode == LIST_MODE:
            self.action_label = str(item)
        elif self.mode == HIRE_MODE:
            if item.stock == 'in':
                if item not in self.selected_items:
                    self.selected_items.append(item)
                    instance.state = 'down'
                    running_total = 0
                    names = []
                    for item in self.selected_items:
                        running_total += item.price
                        names.append(item.name)
                    self.action_label = "Hiring: {} for ${}".format(', '.join(names), running_total)
        elif self.mode == RETURN_MODE:
            if item.stock == 'out':
                if item not in self.selected_items:
                    self.selected_items.append(item)
                    instance.state = 'down'
                    names = []
                    for item in self.selected_items:
                        names.append(item.name)
                    self.action_label = "Returning: {}".format(', '.join(names))
        elif self.mode == ADD_MODE:
            pass



    def set_button_to_normal(self):
        for button in self.root.ids.newItem.children:
            button.state = 'normal'
            self.selected_items = []

    def press_add(self):
        self.mode = ADD_MODE
        self.selected_items = []
        self.action_label = ''
        self.root.ids.listItems.state = 'normal'
        self.root.ids.hireItem.state = 'normal'
        self.root.ids.addButton.state = 'down'
        self.root.ids.itemConfirm.state = 'normal'
        self.root.ids.returnItem.state = 'normal'
        self.action_label = "Enter Details For New Item"
        self.root.ids.popup.open()
        pass

    def clear_fields(self):
        self.root.ids.addedName.text = ""
        self.root.ids.addedDescription.text = ""
        self.root.ids.addedPrice.text = ""

    def press_cancel(self):
        self.root.ids.popup.dismiss()
        self.clear_fields()
        self.action_label = ""

    def press_save(self, added_name, added_description, added_price):

        try:
            self.item_list.add_item(added_name, added_description, float(added_price), 'in')
            self.root.ids.newItem.cols = len(self.item_list.items) // 5 + 1
            new_button = Button(text=added_name)
            new_button.bind(on_release=self.press_entry)
            self.root.ids.newItem.add_widget(new_button)
            self.root.ids.popup.dismiss()
            self.clear_fields()
        except ValueError:
            self.root.ids.addedPrice.text = ''

        if added_name == "" and added_description == "" and added_price == "":
            self.root.ids.popup_label.text = "All Fields Must Be Completed"
    

    def on_stop(self):
        save_items(self.item_list.get_items_as_list())


# main_program()
ExperimentHire().run()
