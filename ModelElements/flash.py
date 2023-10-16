from .point_3d import Point3D
from .angle_3d import Angle3D
from .color import Color


class Flash:
    def __init__(self, location, angle, color, power):
        self.Location = location
        self.Angle = angle
        self.Color = color
        self.Power = power

    def rotate(self: Angle3D):
        pass

    def move(self: Point3D):
        pass