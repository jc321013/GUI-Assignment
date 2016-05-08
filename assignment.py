from kivy.app import App
from kivy.lang import Builder


class ItemsForHire(App):
    def build(self):
        self.title = "Items for Hire"
        self.root = Builder.load_file('assignment.kv')
        return self.root


# create and start the App running
ItemsForHire().run()
