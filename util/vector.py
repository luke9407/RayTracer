from math import sqrt, atan2


class Vector:
    def __init__(self, x, y, z):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)

    def __str__(self):
        return 'x : {0}, y : {1}, z : {2}, size : {3}'.format(self.x, self.y, self.z, self.size())

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __ne__(self, other):
        return self.x != other.x or self.y != other.y or self.z != other.z

    def __neg__(self):
        return Vector(-self.x, -self.y, -self.z)

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other):
        return Vector(self.x * other.x, self.y * other.y, self.z * other.z)

    def to_list(self):
        return [self.x, self.y, self.z]

    @staticmethod
    def from_list(v):
        return Vector(v[0], v[1], v[2])

    def scale(self, mul):
        return Vector(self.x * mul, self.y * mul, self.z * mul)

    def divide(self, div):
        return Vector(self.x / float(div), self.y / float(div), self.z / float(div))

    def normalize(self):
        s = self.size()
        if s == 0:
            return Vector(0, 0, 0)

        x = self.x / s
        y = self.y / s
        z = self.z / s

        return Vector(x, y, z)

    def size(self):
        return sqrt(self.x * self.x + self.y * self.y + self.z * self.z)

    def inner(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z

    def outer(self, other):
        x = self.y * other.z - self.z * other.y
        y = self.z * other.x - self.x * other.z
        z = self.x * other.y - self.y * other.x

        return Vector(x, y, z)

    def angle(self, other):
        y = (other - self).size()
        x = self.size()
        return atan2(y, x)

    def calculate_normal(self, p0, p1, p2):
        v_p0 = Vector.from_list(p0)
        v_p1 = Vector.from_list(p1)
        v_p2 = Vector.from_list(p2)

        v1 = v_p1 - v_p0
        v2 = v_p2 - v_p0

        normal = v1.outer(v2)
        if normal.inner(v_p0 - self) > 0:
            normal = -normal

        return normal.to_list()

    def reflect(self, normal):
        return (normal.scale(2 * self.inner(normal)) - self).normalize()

    def refract(self, normal, out_refract):
        in_refract = 1.0

        c = (-normal).inner(self)
        if c <= 0:
            in_refract, out_refract = out_refract, in_refract
            normal = -normal
            c = -c

        r = in_refract / out_refract
        d = 1.0 - r * r * (1 - c * c)
        if d < 0.0001:
            return Vector(0, 0, 0)

        d = max(0.0, d)
        return (self.scale(r) + normal.scale(r * c - sqrt(d))).normalize()
