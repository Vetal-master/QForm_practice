import math
import config
import utils

import handlers.cube as cube_handler
import handlers.sphere as sphere_handler
import handlers.ellipse as ellipse_handler

# List results
SUCCESS = 1
ERROR_CLASSIFICATION_TYPE = -1


def create(type_3D_object, porosity_percent, base_size, object_parameters=None):
    base_volume = math.pow(2 * base_size, 3)

    porosity_coefficient = porosity_percent / 100

    porosity_volume = porosity_coefficient * base_volume

    if type_3D_object == config.Cube:
        cube_handler.work_cube(porosity_volume)

    elif type_3D_object == config.Sphere:
        sphere_handler.work_sphere(porosity_volume)

    elif type_3D_object == config.Ellipse:
        ellipse_handler.work_ellipse(porosity_volume, object_parameters)

    else:
        utils.output_red_text("Not such type 3D object")

        return ERROR_CLASSIFICATION_TYPE

    utils.output_green_text("SUCCESS")

    return SUCCESS
