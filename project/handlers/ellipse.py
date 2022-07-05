import math
from SpaceClaim import ellipse as SC
from SpaceClaim import utils as SC_utils


def calculate_ellipse(volume, object_parameters):
    relative_coefficient = object_parameters["relative_OX"] * object_parameters["relative_OY"] * object_parameters[
        "relative_OZ"]

    scale = 3 * volume / (4 * math.pi * relative_coefficient)

    ellipse_parameters = {
        "OX": object_parameters["relative_OX"] * scale,
        "OY": object_parameters["relative_OY"] * scale,
        "OZ": object_parameters["relative_OZ"] * scale,
    }

    return ellipse_parameters


def work_ellipse(volume, object_parameters, name="ellipse"):
    ellipse = calculate_ellipse(volume, object_parameters)

    # SC.execute_ellipse(ellipse["OX"], ellipse["OY"], ellipse["OZ"], "execute")

    # SC_utils.save_model(name)

    # SC_utils.remove_model()
