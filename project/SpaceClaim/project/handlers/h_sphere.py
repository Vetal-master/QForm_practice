def calculate_sphere(volume):
    return math.pow(3.0 * volume / (4.0 * math.pi), 1.0 / 3.0)


def work_sphere(volume, name="sphere"):
    radius = calculate_sphere(volume)

    execute_sphere(radius)

    save_model(name)

    remove_model()
