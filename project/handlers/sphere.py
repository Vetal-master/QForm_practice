import math
from SpaceClaim import sphere as SC
from SpaceClaim import utils as SC_utils


def calculate_ellipse(volume):
    return math.pow(3 * volume / (4 * math.pi), 1 / 3)


def work_sphere(volume, name="sphere"):
    radius = calculate_ellipse(volume)

    # SC.execute_sphere(radius)

    # SC_utils.save_model(name)

    # SC_utils.remove_model()