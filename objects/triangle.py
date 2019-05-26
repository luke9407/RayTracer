from util.intersection import *
from util.vector import *
from base import *


class Triangle(Base):
    def __init__(self, t, phong, diffuse, ambient, refract, texture, v, vt, vn):
        super(Triangle, self).__init__(t, phong, diffuse, ambient, refract, texture)
        self.v = v
        self.vt = vt
        self.vn = vn

        outer = (v[1] - v[0]).outer(v[2] - v[0])

        if vn:
            self.normal = (vn[0] + vn[1] + vn[2]).divide(3.0).normalize()
        else:
            self.normal = outer.normalize()

        if outer.inner(self.normal) <= self.EPS:
            self.v[1], self.v[2] = self.v[2], self.v[1]
            if self.vt:
                self.vt[1], self.vt[2] = self.vt[2], self.vt[1]
            self.vn[1], self.vn[2] = self.vn[2], self.vn[1]

        self.s = outer.size() / 2.0

    def intersect(self, ray):
        d = ray.direction.inner(self.normal)

        if d == 0:
            return Intersection.no()

        d = (self.v[0] - ray.origin).inner(self.normal) / d

        if d < self.EPS:
            return Intersection.no()

        point = ray.origin + ray.direction.scale(d)
        normal = self.normal

        for i in range(3):
            v_0 = self.v[i]
            v_1 = self.v[(i + 1) % 3]

            if (v_1 - v_0).outer(point - v_0).inner(normal) < self.EPS:
                return Intersection.no()

        return Intersection(point, normal, d, self)

    def get_uv(self, point):
        opposite_0 = (self.v[1] - point).outer(self.v[2] - point).size() / 2.0
        opposite_1 = (self.v[2] - point).outer(self.v[0] - point).size() / 2.0

        co_0 = opposite_0 / self.s
        co_1 = opposite_1 / self.s
        co_2 = 1 - co_0 - co_1

        u = co_0 * self.vt[0][0] + co_1 * self.vt[1][0] + co_2 * self.vt[2][0]
        v = co_0 * self.vt[0][1] + co_1 * self.vt[1][1] + co_2 * self.vt[2][1]

        return u, v
