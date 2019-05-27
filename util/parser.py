from objects.triangle import *
from util.quaternion import *
import os


class Parser:
    def __init__(self, f, axis, angle, scale):
        self.f = f
        self.scale = scale
        self.q = Quaternion.q(Quaternion.imaginary(axis), angle)
        self.q_inv = self.q.inverse()

    def parse(self):
        objs = []

        v = []
        vt = []
        vn = []

        default_phong = {
            'ka': Vector(1.0, 1.0, 1.0), 'kd': Vector(1.0, 1.0, 1.0), 'ks': Vector(0.0, 0.0, 0.0),
            'shininess': 4
        }
        mtl_info = None
        current_mtl = None

        with open(self.f, 'r') as f:
            for line in f:
                tmp = line.partition('#')[0].strip().split()
                if not tmp:
                    continue

                if tmp[0] == 'mtllib':
                    mtl_path = os.path.join(
                        os.path.dirname(__file__),
                        '../obj/{0}'.format(tmp[1])
                    )
                    mtl_info = self.parse_mtl(mtl_path)
                elif tmp[0] == 'usemtl':
                    current_mtl = mtl_info[tmp[1]]
                elif tmp[0] == 'v':
                    p = Quaternion.imaginary(tmp[1:])
                    p_new = (self.q * p * self.q_inv).scale(self.scale).to_list()
                    p_new[2] -= 10.0

                    v.append(p_new)
                elif tmp[0] == 'vt':
                    vt.append(tmp[1:])
                elif tmp[0] == 'vn':
                    p = Quaternion.imaginary(tmp[1:])
                    p_new = (self.q * p * self.q_inv).to_list()

                    vn.append(p_new)
                elif tmp[0] == 'f':
                    p_0, p_1, p_2 = list(
                        map(
                            lambda x: map(lambda y: int(y) if y != '' else y, x.split('/')),
                            tmp[1:]
                        )
                    )

                    t_v = map(lambda x: Vector.from_list(x), [v[p_0[0] - 1], v[p_1[0] - 1], v[p_2[0] - 1]])
                    t_vt = []
                    if len(p_0) >= 2 and p_0[1] != '':
                        t_vt = map(
                            lambda x: map(float, x),
                            [vt[p_0[1] - 1], vt[p_1[1] - 1], vt[p_2[1] - 1]]
                        )
                    t_vn = []
                    if len(p_0) >= 3 and p_0[2] != '':
                        t_vn = map(
                            lambda x: Vector.from_list(x).normalize(),
                            [vn[p_0[2] - 1], vn[p_1[2] - 1], vn[p_2[2] - 1]]
                        )

                    t = 'MATT' if current_mtl is None else current_mtl['t']
                    phong = default_phong if current_mtl is None else current_mtl['phong']
                    texture = None if current_mtl is None else current_mtl['texture']
                    objs.append(
                        Triangle(
                            t, phong, Vector(255, 0, 0), Vector(52, 0, 0), None, texture,
                            t_v, t_vt, t_vn
                        )
                    )

        return objs

    def parse_mtl(self, mtl_path):
        ret = {}

        with open(mtl_path, 'r') as f:
            current_material = None
            for line in f:
                tmp = line.partition('#')[0].strip().split()
                if not tmp:
                    continue

                if tmp[0] == 'newmtl':
                    ret[tmp[1]] = {
                        't': 'MATT',
                        'phong': {'ka': None, 'kd': None, 'ks': None, 'shininess': None},
                        'texture': None
                    }
                    current_material = tmp[1]

                if current_material is None:
                    continue

                if tmp[0].upper() == 'NS':
                    ret[current_material]['phong']['shininess'] = float(tmp[1])
                elif tmp[0].upper() == 'KA':
                    ret[current_material]['phong']['ka'] = Vector.from_list(tmp[1:])
                elif tmp[0].upper() == 'KD':
                    ret[current_material]['phong']['kd'] = Vector.from_list(tmp[1:])
                elif tmp[0].upper() == 'KS':
                    ret[current_material]['phong']['ks'] = Vector.from_list(tmp[1:])
                elif tmp[0].upper() == 'MAP_KD':
                    ret[current_material]['texture'] = os.path.join(
                        os.path.dirname(__file__),
                        '../texture/{0}'.format(tmp[1])
                    )
                elif tmp[0].upper() == 'ILLUM':
                    if int(tmp[1]) == 0:
                        ret[current_material]['t'] = 'MATT'
                    if int(tmp[1]) == 1:
                        ret[current_material]['t'] = 'REFLECTIVE'
                    if int(tmp[1]) == 2:
                        ret[current_material]['t'] = 'REFLECTIVE_AND_REFRACTIVE'

        return ret
