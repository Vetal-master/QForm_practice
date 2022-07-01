import math
import SpaceClaim.sphere as SC


def calculate_ellipse(volume):
    return math.pow(3 * volume / (4 * math.pi), 1 / 3)


def work_sphere(volume):
    radius = calculate_ellipse(volume)
