import math
import SpaceClaim.cube as SC


def calculate_cube(volume):
    return math.pow(volume, 1 / 3)


def work_cube(volume):
    edge = calculate_cube(volume)
