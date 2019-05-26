from math import pow, sqrt, atan2, pi
from util.intersection import *
from util.ray import *
from util.vector import *
from base import *


class Sphere(Base):
    def __init__(self, t, phong, diffuse, ambient, refract, texture, center, radius):
        super(Sphere, self).__init__(t, phong, diffuse, ambient, refract, texture)
        self.center = center
        self.radius = radius

    def intersect(self, ray):
        d = pow(ray.direction.inner(ray.origin - self.center), 2) \
          - pow((ray.origin - self.center).size(), 2) \
          + pow(self.radius, 2)

        if d < 0:
            return Intersection.no()

        base = -(ray.direction.inner(ray.origin - self.center))
        d1 = base + sqrt(d)
        d2 = base - sqrt(d)

        near = min(d1, d2) if d1 > 0 and d2 > 0 else max(d1, d2)

        if near <= self.EPS:
            return Intersection.no()

        point = ray.origin + ray.direction.scale(near)
        normal = (point - self.center).normalize()

        return Intersection(point, normal, near, self)

    def get_uv(self, point):
        n = (point - self.center).normalize()
        u = atan2(n.x, n.z) / (2 * pi) + 0.5
        v = n.y * 0.5 + 0.5

        return u, v
