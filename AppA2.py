from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.properties import StringProperty
from item import Item
# from Assignment1 import loading_items


class ExperimentHire(App, Item):
    status_text = StringProperty()

    def __init__(self, **kwargs):
        super(ExperimentHire, self).__init__(**kwargs)
        self.experimentHire = {}

    def build(self):
        self.title = "Experiment Hire"
        self.root = Builder.load_file('GUI A2.kv')
        self.create_entry_buttons()
        # file = 'items.csv'
        # in_file = open(file, 'r', encoding='utf-8')
        # items = in_file.readlines()
        # in_file.close()
        # for line in items:
        #     section = line.split(',')
        #     print(section)
        return self.root

    def list_items(self):
        label_display = 'Choose action from the left menu, then select items on the right'
        self.root.ids.list_items.text = "List Items"
        self.root.ids.action_label.text = str(label_display)
        return label_display

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
            # self.root.ids.entriesBox.add_widget(temp_button)

    def press_entry(self, instence):
        name = instence.text
        self.status_text = "{}'s number is {}".format(name, self.phonebook[name])

    def press_add(self):
        self.status_text = "Enter details for new Item"
        self.root.ids.popup.open()

    def press_save(self, added_name, added_number):
        self.phonebook[added_name] = added_number
        self.root.ids.entriesBox.cols = len(self.phonebook) // 5 + 1
        temp_button = Button(text=added_name)
        temp_button.bind(on_release=self.press_entry)
        self.root.ids.entriesBox.add_widget(temp_button)
        self.root.ids.popup.dismiss()
        self.clear_fields()

    def clear_fields(self):
        self.root.ids.addedName.text = ""
        self.root.ids.addedNumber.text = ""

    def press_cancel(self):
        self.root.ids.popup.dismiss()
        self.clear_fields()
        self.status_text = ""







# create and start the App running
ExperimentHire().run()
