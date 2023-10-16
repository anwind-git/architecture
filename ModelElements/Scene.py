from .poligonal_model import PoligonalModel
from .flash import Flash


class Scene:
    def __init__(self, id: int, models: PoligonalModel, flashes: Flash):
        self.id = id
        self.Models = models
        self.Flashes = flashes

    def method_1(self: None):
        pass

    def method_2(metod1: None, metod2: None):
        pass