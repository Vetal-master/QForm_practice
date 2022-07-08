# List results create
SUCCESS = 0
ERROR_CLASSIFICATION_TYPE = -1
ERROR_POROSITY_PERCENT_OUT_OF_RANGE = -2
ERROR_BASE_SIZE_OUT_OF_RANGE = -3
ERROR_ELLIPSE_PARAMS = -4


def create_por(type_3D_object, porosity_percent, base_size, object_parameters=None):
    if (porosity_percent > 100 or porosity_percent <= 0):
        print("Incorrect porosity percent")

        return ERROR_POROSITY_PERCENT_OUT_OF_RANGE

    if (base_size <= 0):
        print("Incorrect base size")

        return ERROR_BASE_SIZE_OUT_OF_RANGE

    base_volume = math.pow(base_size, 3)

    porosity_coefficient = porosity_percent / 100

    porosity_volume = porosity_coefficient * base_volume

    if type_3D_object == Ellipse__:
        name_model = type_3D_object + "_" + \
                     str(porosity_percent) + "_" + \
                     str(object_parameters["relative_OX"]) + "_" + \
                     str(object_parameters["relative_OY"]) + "_" + \
                     str(object_parameters["relative_OZ"])
    else:
        name_model = type_3D_object + "_" + str(porosity_percent)

    if type_3D_object == Cube__:
        work_cube(porosity_volume, name_model)

    elif type_3D_object == Sphere__:
        work_sphere(porosity_volume, name_model)

    elif type_3D_object == Ellipse__:
        if len(object_parameters) < 3:
            print("Incorrect additional parameters. Must be 3 parameters for ellipse")

            return ERROR_ELLIPSE_PARAMS

        work_ellipse(porosity_volume, object_parameters, name_model)

    else:
        print("Not such type 3D object")

        return ERROR_CLASSIFICATION_TYPE

    print(name_model + " DONE")

    return SUCCESS
