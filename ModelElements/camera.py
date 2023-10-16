from .point_3d import Point3D
from .angle_3d import Angle3D


class Camera:
    def __init__(self, location: Point3D, angle: Angle3D):
        self.location = location
        self.angle = angle

    def rotate(self: Angle3D):
        pass

    def move(self: Point3D):
        pass