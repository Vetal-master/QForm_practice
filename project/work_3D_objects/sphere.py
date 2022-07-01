import math
import SpaceClaim.cube_geometry as SC


def work_sphere(volume):
    radius = math.pow(3 * volume / (4 * math.pi), 1 / 3)
