import math
import config
import utils

import handlers.cube as cube_handler
import handlers.sphere as sphere_handler
import handlers.ellipse as ellipse_handler

# List results create
SUCCESS = 0
ERROR_CLASSIFICATION_TYPE = -1
ERROR_POROSITY_PERCENT_OUT_OF_RANGE = -2
ERROR_BASE_SIZE_OUT_OF_RANGE = -3
ERROR_ELLIPSE_PARAMS = -4


def create(type_3D_object, porosity_percent, base_size, object_parameters=None):
    if (porosity_percent > 100 or porosity_percent <= 0):
        utils.output_red_text("Incorrect porosity percent")

        return ERROR_POROSITY_PERCENT_OUT_OF_RANGE

    if (base_size <= 0):
        utils.output_red_text("Incorrect base size")

        return ERROR_BASE_SIZE_OUT_OF_RANGE

    base_volume = math.pow(base_size, 3)

    porosity_coefficient = porosity_percent / 100

    porosity_volume = porosity_coefficient * base_volume

    if type_3D_object == config.Cube:
        cube_handler.work_cube(porosity_volume)

    elif type_3D_object == config.Sphere:
        sphere_handler.work_sphere(porosity_volume)

    elif type_3D_object == config.Ellipse:
        if len(object_parameters) < 3:
            utils.output_red_text("Incorrect additional parameters. Must be 3 parameters for ellipse")

            return ERROR_ELLIPSE_PARAMS

        ellipse_handler.work_ellipse(porosity_volume, object_parameters)

    else:
        utils.output_red_text("Not such type 3D object")

        return ERROR_CLASSIFICATION_TYPE

    return SUCCESS
