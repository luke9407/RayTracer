from base import *
from util.ray import *
from util.vector import *
from util.intersection import *


class Plane(Base):
    def __init__(self, t, phong, diffuse, ambient, refract, texture, point, normal):
        super(Plane, self).__init__(t, phong, diffuse, ambient, refract, texture)
        self.point = point
        self.normal = normal

    def intersect(self, ray):
        d = ray.direction.inner(self.normal)

        if -self.EPS <= d <= self.EPS:
            return Intersection.no()

        d = (self.point - ray.origin).inner(self.normal) / d

        if d <= self.EPS:
            return Intersection.no()

        point = ray.origin + ray.direction.scale(d)
        normal = self.normal

        return Intersection(point, normal, d, self)
