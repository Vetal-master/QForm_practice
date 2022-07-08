def calculate_ellipse(volume, object_parameters, data=0):
    relative_coefficient = object_parameters["relative_OX"] * object_parameters["relative_OY"] * object_parameters[
        "relative_OZ"]

    scale = math.pow((3.0 * volume) / (4.0 * math.pi * relative_coefficient), 1.0 / 3.0)

    ellipse_parameters = {
        "OX": object_parameters["relative_OX"] * scale,
        "OY": object_parameters["relative_OY"] * scale,
        "OZ": object_parameters["relative_OZ"] * scale
    }

    return ellipse_parameters


def work_ellipse(volume, object_parameters, name="ellipse"):
    ellipse = calculate_ellipse(volume, object_parameters)

    execute_ellipse(ellipse["OX"], ellipse["OY"], ellipse["OZ"])

    save_model(name)

    remove_model()
