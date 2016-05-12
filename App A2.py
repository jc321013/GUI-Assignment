from kivy.app import App
from kivy.lang import Builder
from Assignment1 import loading_items


class ExperimentHire(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def build(self):
        self.title = "Experiment Hire"
        self.root = Builder.load_file('GUI A2.kv')
        file = 'items.csv'
        in_file = open(file, 'r', encoding='utf-8')
        items = in_file.readlines()
        in_file.close()
        for line in items:
            section = line.split(',')
            print(section)
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

    def item_rustyBucket(self):
        label_display = 'Rusty Bucket(40L bucket-quite rusty), $0.00 is in'
        self.root.ids.rusty_bucket.text = 'Rusty Bucket'
        self.root.ids.action_label.text = str(label_display)
        return label_display

    def item_thermomix(self):
        label_display = 'Thermomix(TM-31), $25.5 is out'
        self.root.ids.thermo_mix.text = 'Thermomix'
        self.root.ids.action_label.text = str(label_display)
        return label_display

    def item_golfCart(self):
        label_display = 'Golf Cart(Tesla powered 250 turbo), $195 is out'
        self.root.ids.golf_cart.text = 'Golf Cart'
        self.root.ids.action_label.text = str(label_display)
        return label_display

    def item_AeroPress(self):
        label_display = 'AeroPress(great coffee maker), $5 is in'
        self.root.ids.aero_press.text = 'Aero Press'
        self.root.ids.action_label.text = str(label_display)
        return label_display

    def item_Guitar(self):
        label_display = 'Guitar(JTV-59), $12.95 is in'
        self.root.ids.guitar.text = 'Guitar'
        self.root.ids.action_label.text = str(label_display)
        return label_display



# create and start the App running
ExperimentHire().run()
