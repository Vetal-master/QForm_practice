import porosity


def run_work():
    base_object.create_cube(cube_plane, edge_length, center_coordinate, angle_cube_plane, name_3D_object)


# run_work()

def run_work__test():
    porosity.create("куб", 1, 0.1)
    porosity.create("сфера", 1, 0.1)
    porosity.create("эллипс", 1, 0.1, {"relative_OX": 1, "relative_OY": 2, "relative_OZ": 4})


run_work__test()
