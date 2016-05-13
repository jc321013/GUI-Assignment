from kivy.app import App
from kivy.lang import Builder
from item import Item
# from Assignment1 import loading_items


class ExperimentHire(App, Item):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def build(self):
        self.title = "Experiment Hire"
        self.root = Builder.load_file('GUI A2.kv')
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




# create and start the App running
ExperimentHire().run()
