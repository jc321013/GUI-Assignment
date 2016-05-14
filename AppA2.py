from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.properties import StringProperty
from item import Item
from itemlist import ItemList
# from Assignment1 import loading_items


class ExperimentHire(App, Item, ItemList):
    action_label = StringProperty()

    def __init__(self, **kwargs):
        super(ExperimentHire, self).__init__(**kwargs)
        self.experimentHire = {}

    def build(self):
        self.title = "Experiment Hire"
        self.root = Builder.load_file('GUI A2.kv')
        self.create_entry_buttons()
        return self.root



    def hiring_item(self):
        # in_file = open("items.csv", 'r', encoding='utf-8')
        # item = ['Rusty Bucket', 'Golf Cart', 'Thermomix', 'AeroPress', 'Guitar']
        # for item in in_file:
        #     if item in in_file:
        #         item = 'out'
        #     else:
        #         item = 'in'
        label_display = 'Select available items to hire'
        self.root.ids.hire_item.text = 'Hire Items'
        self.root.ids.action_label.text = str(label_display)
        return label_display

    def create_entry_buttons(self):
        for name in self.experimentHire:
            temp_button = Button(text=name)
            temp_button.bind(on_release=self.press.entry)
            self.root.ids.newItem.add_widget(temp_button)

    def press_entry(self, instance):
        name = instance.text
        self.root.ids.action_label.text = "{} $ {} Per Day".format(name, self.experimentHire[name])

    def press_add(self):
        self.action_label = "Enter details for new Item"
        self.root.ids.popup.open()

    def press_save(self, added_name, added_description, added_price):
        self.experimentHire[added_name] = added_description, added_price
        self.root.ids.newItem.cols = len(self.experimentHire)
        temp_button = Button(text=added_name)
        temp_button.bind(on_release=self.press_entry)
        self.root.ids.newItem.add_widget(temp_button)
        self.root.ids.popup.dismiss()
        self.clear_fields()

    def clear_fields(self):
        self.root.ids.addedName.text = ""
        self.root.ids.addedDescription.text = ""

    def press_cancel(self):
        self.root.ids.popup.dismiss()
        self.clear_fields()
        self.action_label = ""







# create and start the App running
ExperimentHire().run()
