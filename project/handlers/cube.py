import math
from SpaceClaim import cube as SC
from project import config


def calculate_cube(volume):
    return math.pow(volume, 1 / 3)


def work_cube(volume):
    edge = calculate_cube(volume) / 2

    # SC.execute_cube(config.cube_plane, edge, "execute")
