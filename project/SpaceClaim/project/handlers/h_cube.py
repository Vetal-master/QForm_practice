def calculate_cube(volume):
    return math.pow(volume, 1.0 / 3.0)


def work_cube(volume, name="cube"):
    edge = calculate_cube(volume) / 2.0

    execute_cube(cube_plane__, {"O1": edge, "O2": edge, "O3": edge}, "execute", {"O1": edge / 2.0, "O2": edge / 2.0})

    save_model(name)

    remove_model()
