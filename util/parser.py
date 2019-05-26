from objects.triangle import *


class Parser:
    def __init__(self, f):
        self.f = f

    def parse(self):
        objs = []

        v = []
        vt = []
        vn = []

        phong = {'ka': Vector(1.0, 1.0, 1.0), 'kd': Vector(1.0, 1.0, 1.0), 'ks': Vector(0.0, 0.0, 0.0), 'shininess': 4}

        with open(self.f, 'r') as f:
            for line in f:
                tmp = line.partition('#')[0].strip().split()
                if not tmp:
                    continue

                if tmp[0] == 'v':
                    tmp[3] = float(tmp[3]) - 20.0
                    v.append(tmp[1:])
                elif tmp[0] == 'vt':
                    vt.append(tmp[1:])
                elif tmp[0] == 'vn':
                    vn.append(tmp[1:])
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
                        t_vt = map(lambda x: Vector.from_list(x), [vt[p_0[1] - 1], vt[p_1[1] - 1], vt[p_2[1] - 1]])
                    t_vn = []
                    if len(p_0) >= 3 and p_0[2] != '':
                        t_vn = map(lambda x: Vector.from_list(x), [vn[p_0[2] - 1], vn[p_1[2] - 1], vn[p_2[2] - 1]])

                    objs.append(
                        Triangle(
                            'MATT', phong, Vector(255, 0, 0), Vector(52, 0, 0), None, None,
                            t_v, t_vt, t_vn
                        )
                    )

        return objs
