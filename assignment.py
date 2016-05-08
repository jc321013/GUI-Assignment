from kivy.app import App
from kivy.lang import Builder


class ExperimentHire(App):
    def build(self):
        self.title = "Experiment Hire"
        self.root = Builder.load_file('assignment.kv')
        return self.root


# create and start the App running
ExperimentHire().run()
