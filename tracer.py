from PIL import Image
from math import pow

from util.vector import *
from util.ray import *
from util.light import *

from objects.sphere import *
from objects.plane import *
from objects.triangle import *

import scene.objs
import os


def check_intersection(ray, objs):
    ret = Intersection.no()

    for obj in objs:
        intersect = obj.intersect(ray)
        if ret.obj is None:
            ret = intersect
        elif intersect.obj is not None and intersect.near < ret.near:
            ret = intersect

    return ret


def cast(ray, objs, lights, depth, default_color):
    if depth >= 5:  # Limit the depth of recursion
        return default_color

    hit = check_intersection(ray, objs)
    if hit.obj is None:
        return default_color

    if hit.obj.t == 'REFLECTIVE_AND_REFRACTIVE':
        reflected = (-ray.direction).reflect(hit.normal)
        reflected_ray = Ray(hit.point + hit.normal.scale(0.0001), reflected)

        color = cast(reflected_ray, objs, lights, depth + 1, default_color).scale(0.1)

        refracted = ray.direction.refract(hit.normal, hit.obj.refract)
        if refracted is not None:
            if refracted.inner(hit.normal) < 0:
                ray_point = hit.point - hit.normal.scale(0.0001)
            else:
                ray_point = hit.point + hit.normal.scale(0.0001)
            refracted_ray = Ray(ray_point, refracted)

            color += cast(refracted_ray, objs, lights, depth + 1, default_color).scale(0.9)
    elif hit.obj.t == 'REFLECTIVE':
        reflected = (-ray.direction).reflect(hit.normal)
        reflected_ray = Ray(hit.point + hit.normal.scale(0.0001), reflected)

        color = cast(reflected_ray, objs, lights, depth + 1, default_color)

        if color == default_color:
            view = (ray.origin - hit.point).normalize()
            color = calculate_color(hit, view, objs, lights)
        elif depth == 1:
            color = color.scale(0.8)
    else:  # MATT
        view = (ray.origin - hit.point).normalize()
        color = calculate_color(hit, view, objs, lights)

    return color


def calculate_color(hit, view, objs, lights):
    diffuse_coefficient = 0.0
    specular_color = Vector(0, 0, 0)

    for light in lights:
        light_direction = (light.pos - hit.point).normalize()
        shadow_ray = Ray(hit.point, light_direction)

        shadow_hit = check_intersection(shadow_ray, objs)

        if shadow_hit.obj is None or shadow_hit.obj == hit.obj:
            normal = hit.normal
            light_reflected = light_direction.reflect(normal)
            light_distance = (light.pos - hit.point).size()
            light_attenuated = light.intensity / light_distance

            diffuse_coefficient += max(light_direction.inner(normal), 0.0) * light_attenuated
            specular_color += hit.obj.phong['ks'].scale(pow(
                max(light_reflected.inner(view), 0.0), hit.obj.phong['shininess']
            ) * light_attenuated) * light.specular

    uv = None if hit.obj.texture is None else hit.obj.get_uv(hit.point)
    color = hit.obj.get_color(diffuse_coefficient, uv) + specular_color

    return color


def normalize_color(color):
    ret = tuple(map(lambda x: min(int(x), 255), color.to_list()))
    return ret


def main():
    lights = []
    lights.append(Light(Vector(0, 0.5, 1), 10.0, Vector(255, 255, 255)))
    # lights.append(Light(Vector(50, 50, 10), 10.0, Vector(255, 255, 255)))
    # lights.append(Light(Vector(-50, -50, 10), 10.0, Vector(255, 255, 255)))

    camera = Vector(0, 1, 5)
    width = 700
    height = 500

    img = Image.new('RGB', (width, height))
    ratio = float(width) / float(height)

    default_color = Vector(153, 204, 255)

    for i in range(width):
        print 'Width {0}'.format(i)
        for j in range(height):
            x = (2 * ((i + 0.5) / float(width)) - 1) * ratio * 5
            y = (1 - 2 * ((j + 0.5) / float(height))) * 5

            ray = Ray(camera, (Vector(x, y, -5) - camera).normalize())
            color = normalize_color(cast(ray, scene.objs.objs, lights, 1, default_color))

            img.putpixel((i, j), color)
        if i > 0 and i % 100 == 0:
            progress = open('progress/result_{0}.png'.format(i), 'wb')
            img.save(progress, 'PNG')
            progress.flush()
            os.fsync(progress)
            progress.close()

    img.save('result/result.png', 'PNG')


if __name__ == '__main__':
    main()
