class Item:
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