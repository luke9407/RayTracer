from util.vector import *
from util.parser import *
from objects.sphere import *
from objects.triangle import *

import os

objs = []

phong = {'ka': Vector(1.0, 1.0, 1.0), 'kd': Vector(1.0, 1.0, 1.0), 'ks': Vector(1.0, 1.0, 1.0), 'shininess': 4}
objs.append(
    Sphere(
        'REFLECTIVE_AND_REFRACTIVE', phong, Vector(255, 0, 0), Vector(52, 0, 0), 1.9, 'texture/sphere.jpg',
        Vector(-5, -3, -10), 2
    )
)

phong = {'ka': Vector(1.0, 1.0, 1.0), 'kd': Vector(1.0, 1.0, 1.0), 'ks': Vector(1.0, 1.0, 1.0), 'shininess': 4}
objs.append(
    Sphere(
        'MATT', phong, Vector(255, 0, 0), Vector(52, 0, 0), None, 'texture/sphere.jpg',
        Vector(5, 0, -10), 2
    )
)

phong = {'ka': Vector(1.0, 1.0, 1.0), 'kd': Vector(1.0, 1.0, 1.0), 'ks': Vector(1.0, 1.0, 1.0), 'shininess': 4}
objs.append(
    Sphere(
        'MATT', phong, Vector(255, 0, 0), Vector(52, 0, 0), None, None,
        Vector(0, -4.5, -5), 0.5
    )
)

phong = {'ka': Vector(0.0, 0.0, 0.0), 'kd': Vector(0.0, 0.0, 0.0), 'ks': Vector(1.0, 1.0, 1.0), 'shininess': 4}
objs.append(
    Triangle(
        'REFLECTIVE', phong, Vector(0, 255, 0), Vector(0, 52, 0), None, None,
        [Vector(0, -5, -7), Vector(2, -5, -5), Vector(2, -3, -5)],
        [],
        []
    )
)
objs.append(
    Triangle(
        'REFLECTIVE', phong, Vector(0, 255, 0), Vector(0, 52, 0), None, None,
        [Vector(0, -5, -7), Vector(2, -3, -5), Vector(0, -3, -7)],
        [],
        []
    )
)

objs.append(
    Triangle(
        'REFLECTIVE', phong, Vector(0, 255, 0), Vector(0, 52, 0), None, None,
        [Vector(0, -5, -7), Vector(-2, -3, -5), Vector(-2, -5, -5)],
        [],
        []
    )
)
objs.append(
    Triangle(
        'REFLECTIVE', phong, Vector(0, 255, 0), Vector(0, 52, 0), None, None,
        [Vector(0, -5, -7), Vector(0, -3, -7), Vector(-2, -3, -5)],
        [],
        []
    )
)

phong = {'ka': Vector(1.0, 1.0, 1.0), 'kd': Vector(1.0, 1.0, 1.0), 'ks': Vector(1.0, 1.0, 1.0), 'shininess': 16}
# Bottom
objs.append(
    Triangle(
        'MATT', phong, Vector(0, 0, 255), Vector(0, 0, 52), None, 'texture/plane.jpg',
        [Vector(9, -5, 0), Vector(-9, -5, -20), Vector(-9, -5, 0)],
        [(1, 1), (0, 0), (0, 1)],
        [Vector(0, 1, 0), Vector(0, 1, 0), Vector(0, 1, 0)]
    )
)
objs.append(
    Triangle(
        'MATT', phong, Vector(0, 0, 255), Vector(0, 0, 52), None, 'texture/plane.jpg',
        [Vector(9, -5, 0), Vector(9, -5, -20), Vector(-9, -5, -20)],
        [(1, 1), (1, 0), (0, 0)],
        [Vector(0, 1, 0), Vector(0, 1, 0), Vector(0, 1, 0)]
    )
)
# Top
objs.append(
    Triangle(
        'MATT', phong, Vector(224, 224, 224), Vector(22, 22, 22), None, None,
        [Vector(9, 5, 0), Vector(-9, 5, 0), Vector(-9, 5, -20)],
        [(1, 0), (0, 0), (0, 1)],
        [Vector(0, -1, 0), Vector(0, -1, 0), Vector(0, -1, 0)]
    )
)
objs.append(
    Triangle(
        'MATT', phong, Vector(224, 224, 224), Vector(22, 22, 22), None, None,
        [Vector(9, 5, 0), Vector(-9, 5, -20), Vector(9, 5, -20)],
        [(1, 0), (0, 1), (1, 1)],
        [Vector(0, -1, 0), Vector(0, -1, 0), Vector(0, -1, 0)]
    )
)
# Right
objs.append(
    Triangle(
        'MATT', phong, Vector(224, 224, 224), Vector(22, 22, 22), None, None,
        [Vector(9, -5, 0), Vector(9, 5, 0), Vector(9, 5, -20)],
        [(1, 1), (1, 0), (0, 0)],
        [Vector(-1, 0, 0), Vector(-1, 0, 0), Vector(-1, 0, 0)]
    )
)
objs.append(
    Triangle(
        'MATT', phong, Vector(224, 224, 224), Vector(22, 22, 22), None, None,
        [Vector(9, -5, 0), Vector(9, 5, -20), Vector(9, -5, -20)],
        [(1, 1), (0, 0), (0, 1)],
        [Vector(-1, 0, 0), Vector(-1, 0, 0), Vector(-1, 0, 0)]
    )
)
# Left
objs.append(
    Triangle(
        'MATT', phong, Vector(224, 224, 224), Vector(22, 22, 22), None, None,
        [Vector(-9, -5, 0), Vector(-9, 5, -20), Vector(-9, 5, 0)],
        [(0, 1), (1, 0), (0, 0)],
        [Vector(1, 0, 0), Vector(1, 0, 0), Vector(1, 0, 0)]
    )
)
objs.append(
    Triangle(
        'MATT', phong, Vector(224, 224, 224), Vector(22, 22, 22), None, None,
        [Vector(-9, -5, 0), Vector(-9, -5, -20), Vector(-9, 5, -20)],
        [(0, 1), (1, 1), (1, 0)],
        [Vector(1, 0, 0), Vector(1, 0, 0), Vector(1, 0, 0)]
    )
)
# Back
objs.append(
    Triangle(
        'MATT', phong, Vector(224, 224, 224), Vector(22, 22, 22), None, None,
        [Vector(9, -5, -20), Vector(9, 5, -20), Vector(-9, 5, -20)],
        [(1, 1), (1, 0), (0, 0)],
        [Vector(0, 0, 1), Vector(0, 0, 1), Vector(0, 0, 1)]
    )
)
objs.append(
    Triangle(
        'MATT', phong, Vector(224, 224, 224), Vector(22, 22, 22), None, None,
        [Vector(9, -5, -20), Vector(-9, 5, -20), Vector(-9, -5, -20)],
        [(1, 1), (0, 0), (0, 1)],
        [Vector(0, 0, 1), Vector(0, 0, 1), Vector(0, 0, 1)]
    )
)

objs += Parser(
    os.path.join(
        os.path.dirname(__file__),
        '../obj/estrellica.obj'
    ),
    [1, 0, 0], 1.57, 0.3
).parse()
