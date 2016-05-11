from kivy.app  import App
from kivy.lang import Builder


class ExperimentHire(App):
    def build(self):
        self.title = "Experiment Hire"
        self.root = Builder.load_file('assignment.kv')
        return self.root

    def item_rustyBucket(self):
        rusty_bucket = str(self.root.ids.rusty_bucket.text)
        name = 'Rusty Bucket(40L bucket-quite rusty), $0.00 is in'
        self.root.ids.action_label.text = str(rusty_bucket)
        return name


    def item_thermomix(self):
        Thermomix = str(self.root.ids.thermo_mix.text)
        self.root.ids.action_label.text = str(Thermomix)


    def item_golfCart(self):
        rusty_bucket = str(self.root.ids.golf_cart.text)
        self.root.ids.action_label.text = str(rusty_bucket)

    def item_AeroPress(self):
        rusty_bucket = str(self.root.ids.aero_press.text)
        self.root.ids.action_label.text = str(rusty_bucket)

    def item_Guitar(self):
        rusty_bucket = str(self.root.ids.guitar.text)
        self.root.ids.action_label.text = str(rusty_bucket)



# create and start the App running
ExperimentHire().run()
