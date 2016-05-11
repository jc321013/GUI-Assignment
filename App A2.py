from kivy.app import App
from kivy.lang import Builder


class ExperimentHire(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def build(self):
        self.title = "Experiment Hire"
        self.root = Builder.load_file('GUI A2.kv')
        in_file = open("items.csv", 'r', encoding='utf-8')
        items = in_file.readlines()
        in_file.close()
        for line in items:
            section = line.split(',')
            print(section)
        return self.root

    def list_items(self):
        self.root.ids.list_items.text = "List Items"

    def item_rustyBucket(self):
        name = 'Rusty Bucket(40L bucket-quite rusty), $0.00 is in'
        self.root.ids.rusty_bucket.text = 'Rusty Bucket'
        self.root.ids.action_label.text = str(name)
        return name

    def item_thermomix(self):
        name = 'Thermomix(TM-31), $25.5 is out'
        self.root.ids.thermo_mix.text = 'Thermomix'
        self.root.ids.action_label.text = str(name)
        return name

    def item_golfCart(self):
        name = 'Golf Cart(Tesla powered 250 turbo), $195 is out'
        self.root.ids.golf_cart.text = 'Golf Cart'
        self.root.ids.action_label.text = str(name)
        return name

    def item_AeroPress(self):
        name = 'AeroPress(great coffee maker), $5 is in'
        self.root.ids.aero_press.text = 'Aero Press'
        self.root.ids.action_label.text = str(name)
        return name

    def item_Guitar(self):
        name = 'Guitar(JTV-59), $12.95 is in'
        self.root.ids.guitar.text = 'Guitar'
        self.root.ids.action_label.text = str(name)
        return name



# create and start the App running
ExperimentHire().run()
