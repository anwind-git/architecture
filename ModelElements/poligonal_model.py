from .poligon import Poligon
from .texture import Texture


class PoligonalModel:
    def __init__(self, poligons: Poligon, textures: Texture):
        self.poligons = poligons
        self.textures = textures