def run_create_geometry_set(path):
    geometry_set = open(path, "r")
    lines_models = geometry_set.readlines()

    for line_model in lines_models:
        cube = {"O1": edge_length__ / 2.0, "O2": edge_length__ / 2.0, "O3": edge_length__ / 2.0}
        center = {"O1": edge_length__ / 4.0, "O2": edge_length__ / 4.0}
        extrude_cube(cube_plane__, cube, name_base_object__, center)
        visibility()

        model_data = line_model.split(" ", 5)

        type_object = model_data[0]
        percent_porosity = model_data[1]

        if type_object == Ellipse__:
            parameters = {
                "relative_OX": float(model_data[2]),
                "relative_OY": float(model_data[3]),
                "relative_OZ": float(model_data[4].replace('\n', ''))
            }

            result = create_por(type_object, float(percent_porosity.replace('\n', '')),
                                edge_length__, parameters)
        else:
            result = create_por(type_object, float(percent_porosity),
                                edge_length__)

        if result:
            print(error_geometry)
            exit(-1)

    print(success_geometry)
