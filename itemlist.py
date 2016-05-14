# from Assignment1 import loading_items


class ItemList():
    def list_items(self):
        label_display = 'Choose action from the left menu, then select items on the right'
        self.root.ids.list_items.text = "List Items"
        self.root.ids.action_label.text = str(label_display)
        return label_display

    # def load_item(self):
    #     file = 'items.csv'
    #     in_file = open(file, 'r', encoding='utf-8')
    #     items = in_file.readlines()
    #     in_file.close()
    #     for line in items:
    #         section = line.split(',')
    #         print(section)
