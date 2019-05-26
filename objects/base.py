from PIL import Image
from math import pow
from util.vector import *


class Base(object):
    def __init__(self, t, phong, diffuse, ambient, refract, texture):
        self.t = t.upper()  # Object type. One of MATT, REFLECTIVE, REFLECTIVE_AND_REFRACTIVE.
        self.phong = phong  # Phong illumination constants. ex) {'ka': [], 'kd': [], 'ks': [], 'shininess': x}
        self.diffuse = diffuse  # Diffuse color of object
        self.ambient = ambient  # Ambient color of object
        self.refract = float(refract) if refract is not None else None  # Refraction rate
        self.texture = Image.open(texture).convert('RGB') if texture else None
        self.texture_width = 0.0
        self.texture_height = 0.0

        if self.texture:
            self.texture_width, self.texture_height = self.texture.size

        self.EPS = 0.0001

    def get_color(self, diffuse_coefficient, uv):
        ambient = self.phong['ka']
        diffuse = self.phong['kd'].scale(diffuse_coefficient)

        if uv:
            color = Vector.from_list(self.texture.getpixel(
                (uv[0] * self.texture_width, uv[1] * self.texture_height)
            ))
            ret = ambient * color.scale(0.5) + diffuse * color
        else:
            ret = self.ambient * ambient + self.diffuse * diffuse

        return ret
