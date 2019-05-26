class Intersection:
    def __init__(self, point, normal, near, obj=None):
        self.point = point
        self.normal = normal
        self.near = near
        self.obj = obj

    def __str__(self):
        return 'Near : {0}'.format(self.near if self.near is not None else 'none')

    @staticmethod
    def no():
        return Intersection(None, None, None)
