from util.vector import *
from util.parser import *
from objects.sphere import *
from objects.triangle import *

objs = []

# phong = {'ka': Vector(1.0, 1.0, 1.0), 'kd': Vector(1.0, 1.0, 1.0), 'ks': Vector(1.0, 1.0, 1.0), 'shininess': 4}
# objs.append(
#     Sphere(
#         'REFLECTIVE_AND_REFRACTIVE', phong, Vector(255, 0, 0), Vector(52, 0, 0), 1.9, 'texture/sphere.jpg',
#         Vector(0, -4, -10), 1
#     )
# )
#
# phong = {'ka': Vector(1.0, 1.0, 1.0), 'kd': Vector(1.0, 1.0, 1.0), 'ks': Vector(1.0, 1.0, 1.0), 'shininess': 4}
# objs.append(
#     Sphere(
#         'REFLECTIVE_AND_REFRACTIVE', phong, Vector(255, 0, 0), Vector(52, 0, 0), 1.9, 'texture/sphere.jpg',
#         Vector(-3, -4, -10), 1
#     )
# )

# phong = {'ka': Vector(0.0, 0.0, 0.0), 'kd': Vector(0.0, 0.0, 0.0), 'ks': Vector(1.0, 1.0, 1.0), 'shininess': 4}
# objs.append(
#     Triangle(
#         'REFLECTIVE', phong, Vector(0, 255, 0), Vector(0, 52, 0), None, None,
#         [Vector(-0.5, -1.0, -6), Vector(0.5, -1.0, -6), Vector(0.5, -0.3, -6)],
#         [],
#         []
#     )
# )
# objs.append(
#     Triangle(
#         'REFLECTIVE', phong, Vector(0, 255, 0), Vector(0, 52, 0), None, None,
#         [Vector(-0.5, -1.0, -6), Vector(0.5, -0.3, -6), Vector(-0.5, -0.3, -6)],
#         [],
#         []
#     )
# )

# phong = {'ka': Vector(0.0, 0.0, 0.0), 'kd': Vector(0.0, 0.0, 0.0), 'ks': Vector(1.0, 1.0, 1.0), 'shininess': 4}
# objs.append(
#     Triangle(
#         'REFLECTIVE', phong, Vector(0, 255, 0), Vector(0, 52, 0), None, None,
#         [Vector(0, -5, -12), Vector(3, -5, -9), Vector(3, -2, -9)],
#         [],
#         []
#     )
# )
# objs.append(
#     Triangle(
#         'REFLECTIVE', phong, Vector(0, 255, 0), Vector(0, 52, 0), None, None,
#         [Vector(0, -5, -12), Vector(3, -2, -9), Vector(0, -2, -12)],
#         [],
#         []
#     )
# )
#
# objs.append(
#     Triangle(
#         'REFLECTIVE', phong, Vector(0, 255, 0), Vector(0, 52, 0), None, None,
#         [Vector(0, -5, -12), Vector(-3, -2, -9), Vector(-3, -5, -9)],
#         [],
#         []
#     )
# )
# objs.append(
#     Triangle(
#         'REFLECTIVE', phong, Vector(0, 255, 0), Vector(0, 52, 0), None, None,
#         [Vector(0, -5, -12), Vector(0, -2, -12), Vector(-3, -2, -9)],
#         [],
#         []
#     )
# )

# objs.append(Sphere('MATT', phong, Vector(0, 255, 0), Vector(0, 52, 0), None, Vector(1, 0, -20), 1))
# objs.append(Sphere('MATT', phong, Vector(0, 0, 255), Vector(0, 0, 52), None, Vector(0.5, 1, -20), 1))

# phong = {'ka': Vector(1.0, 1.0, 1.0), 'kd': Vector(1.0, 1.0, 1.0), 'ks': Vector(1.0, 1.0, 1.0), 'shininess': 4}
# objs.append(Sphere('REFLECTIVE_AND_REFRACTIVE', phong, Vector(0, 255, 0), Vector(0, 52, 0), 1.333, Vector(0.5, -0.7, -3), 0.3))

# phong = {'ka': Vector(1.0, 1.0, 1.0), 'kd': Vector(1.0, 1.0, 1.0), 'ks': Vector(1.0, 1.0, 1.0), 'shininess': 16}
# objs.append(Plane('MATT', phong, Vector(255, 255, 0), Vector(52, 52, 0), None, Vector(0, -1, 0), Vector(0, 1, 0)))

phong = {'ka': Vector(1.0, 1.0, 1.0), 'kd': Vector(1.0, 1.0, 1.0), 'ks': Vector(1.0, 1.0, 1.0), 'shininess': 16}
# Bottom
objs.append(
    Triangle(
        'MATT', phong, Vector(0, 0, 255), Vector(0, 0, 52), None, None,
        [Vector(9, -5, 0), Vector(-9, -5, -20), Vector(-9, -5, 0)],
        [(1, 1), (0, 0), (0, 1)],
        [Vector(0, 1, 0), Vector(0, 1, 0), Vector(0, 1, 0)]
    )
)
objs.append(
    Triangle(
        'MATT', phong, Vector(255, 0, 255), Vector(52, 0, 52), None, None,
        [Vector(9, -5, 0), Vector(9, -5, -20), Vector(-9, -5, -20)],
        [(1, 1), (1, 0), (0, 0)],
        [Vector(0, 1, 0), Vector(0, 1, 0), Vector(0, 1, 0)]
    )
)
# # Top
# objs.append(
#     Triangle(
#         'MATT', phong, Vector(255, 255, 0), Vector(52, 52, 0), None, None,
#         [Vector(2, 1, 0), Vector(-2, 1, 0), Vector(-2, 1, -7)],
#         [],
#         [Vector(0, -1, 0), Vector(0, -1, 0), Vector(0, -1, 0)]
#     )
# )
# objs.append(
#     Triangle(
#         'MATT', phong, Vector(255, 255, 0), Vector(52, 52, 0), None, None,
#         [Vector(2, 1, 0), Vector(-2, 1, -7), Vector(2, 1, -7)],
#         [],
#         [Vector(0, -1, 0), Vector(0, -1, 0), Vector(0, -1, 0)]
#     )
# )
# # Right
# objs.append(
#     Triangle(
#         'MATT', phong, Vector(255, 0, 255), Vector(52, 0, 52), None, None,
#         [Vector(2, -1, 0), Vector(2, 1, 0), Vector(2, 1, -7)],
#         [],
#         [Vector(-1, 0, 0), Vector(-1, 0, 0), Vector(-1, 0, 0)]
#     )
# )
# objs.append(
#     Triangle(
#         'MATT', phong, Vector(255, 0, 255), Vector(52, 0, 52), None, None,
#         [Vector(2, -1, 0), Vector(2, 1, -7), Vector(2, -1, -7)],
#         [],
#         [Vector(-1, 0, 0), Vector(-1, 0, 0), Vector(-1, 0, 0)]
#     )
# )
# # Left
# objs.append(
#     Triangle(
#         'MATT', phong, Vector(0, 255, 255), Vector(0, 52, 52), None, None,
#         [Vector(-2, -1, 0), Vector(-2, 1, -7), Vector(-2, 1, 0)],
#         [],
#         [Vector(1, 0, 0), Vector(1, 0, 0), Vector(1, 0, 0)]
#     )
# )
# objs.append(
#     Triangle(
#         'MATT', phong, Vector(0, 255, 255), Vector(0, 52, 52), None, None,
#         [Vector(-2, -1, 0), Vector(-2, -1, -7), Vector(-2, 1, -7)],
#         [],
#         [Vector(1, 0, 0), Vector(1, 0, 0), Vector(1, 0, 0)]
#     )
# )
# # Back
# objs.append(
#     Triangle(
#         'MATT', phong, Vector(200, 200, 200), Vector(52, 52, 52), None, None,
#         [Vector(2, -1, -7), Vector(2, 1, -7), Vector(-2, 1, -7)],
#         [],
#         [Vector(0, 0, 1), Vector(0, 0, 1), Vector(0, 0, 1)]
#     )
# )
# objs.append(
#     Triangle(
#         'MATT', phong, Vector(200, 200, 200), Vector(52, 52, 52), None, None,
#         [Vector(2, -1, -7), Vector(-2, 1, -7), Vector(-2, -1, -7)],
#         [],
#         [Vector(0, 0, 1), Vector(0, 0, 1), Vector(0, 0, 1)]
#     )
# )
objs += Parser('obj/humanoid.obj').parse()
