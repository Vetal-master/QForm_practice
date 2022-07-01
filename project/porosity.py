import math
import config
import utils

import work_3D_objects.cube as Cube_
import work_3D_objects.sphere as Sphere_
import work_3D_objects.ellipse as Ellipse_

# List results
SUCCESS = 1
ERROR_CLASSIFICATION_TYPE = -1


def create(name_3D_object, porosity_percent, base_size, object_parameters=None):
    base_volume = math.pow(2 * base_size, 3)

    porosity_coefficient = porosity_percent / 100

    porosity_volume = porosity_coefficient * base_volume

    if name_3D_object == config.Cube:
        Cube_.work_cube(porosity_volume)

    elif name_3D_object == config.Sphere:
        Sphere_.work_sphere(porosity_volume)

    elif name_3D_object == config.Ellipse:
        Ellipse_.work_ellipse(porosity_volume, object_parameters)

    else:
        utils.output_red_text("Not such type 3D object")

        return ERROR_CLASSIFICATION_TYPE

    utils.output_green_text("SUCCESS")

    return SUCCESS
