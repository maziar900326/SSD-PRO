from src.models.swing import Swing


class Structure:

    HH = "HH"
    HL = "HL"
    LH = "LH"
    LL = "LL"

    def __init__(self, structure_type, swing):
        self.type = structure_type
        self.swing = swing

    @property
    def price(self):
        return self.swing.price

    @property
    def time(self):
        return self.swing.time

    @property
    def index(self):
        return self.swing.index

    @property
    def is_hh(self):
        return self.type == Structure.HH

    @property
    def is_hl(self):
        return self.type == Structure.HL

    @property
    def is_lh(self):
        return self.type == Structure.LH

    @property
    def is_ll(self):
        return self.type == Structure.LL

    def __str__(self):
        return f"{self.type} | {self.time} | {self.price}"