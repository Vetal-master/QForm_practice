import math
import SpaceClaim.ellipse as SC


def calculate_ellipse(volume, object_parameters):
    relative_coefficient = object_parameters["relative_OX"] * object_parameters["relative_OY"] * object_parameters[
        "relative_OZ"]

    scale = 3 * volume / (4 * math.pi * relative_coefficient)

    ellipse_parameters = {
        "real_OX": object_parameters["relative_OX"] * scale,
        "real_OY": object_parameters["relative_OY"] * scale,
        "real_OZ": object_parameters["relative_OZ"] * scale,
    }

    return ellipse_parameters


def work_ellipse(volume, object_parameters):
    ellipse = calculate_ellipse(volume, object_parameters)
