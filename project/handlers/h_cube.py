import math


def calculate_cube(volume):
    return math.pow(volume, 1 / 3)


def work_cube(volume, name="cube"):
    edge = calculate_cube(volume) / 2

    # SC.execute_cube(config.cube_plane, edge, "execute")

    # SC_utils.save_model(name)

    # SC_utils.remove_model()
