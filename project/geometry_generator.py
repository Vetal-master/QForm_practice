import sys
from sys import path as path_sys
from os import path as path_os

module_path_excel = path_os.abspath(path_os.join(path_os.dirname(__file__), 'Excel'))
path_sys.append(module_path_excel)

module_path_configs = path_os.abspath(path_os.join(path_os.dirname(__file__), 'configs'))
path_sys.append(module_path_configs)

module_path_SC = path_os.abspath(path_os.join(path_os.dirname(__file__), 'SpaceClaim'))
path_sys.append(module_path_SC)

import geometry_conf as global_conf
import porosity_generator as porosity
# import SP_cube as SC_base

import global_utils as utils


def run_create_geometry_set(path=global_conf.path_tmp_data_geometry):
    geometry_set = open(path, "r")
    lines_models = geometry_set.readlines()

    for line_model in lines_models:
        # cube = {"O1": global_conf.edge_length__ / 2, "O2": global_conf.edge_length__ / 2, "O3": global_conf.edge_length__ / 2}
        # center = {"O1": global_conf.edge_length__ / 4, "O2": global_conf.edge_length__ / 4}
        # SC_cube.extrude_cube(global_conf.cube_plane__,  cube, config.name_base_object__, center)
        # SC_utils.visibility()

        model_data = line_model.split(" ", 5)

        type_object = model_data[0]
        percent_porosity = model_data[1]

        if type_object == global_conf.Ellipse:
            parameters = {
                "relative_OX": float(model_data[2]),
                "relative_OY": float(model_data[3]),
                "relative_OZ": float(model_data[4].replace('\n', ''))
            }

            result = porosity.create(type_object, float(percent_porosity.replace('\n', '')),
                                     global_conf.edge_length__, parameters)
        else:
            result = porosity.create(type_object, float(percent_porosity),
                                     global_conf.edge_length__)

        if result:
            utils.output_red_text(global_conf.error_geometry)
            exit(-1)

    utils.output_green_text(global_conf.success_geometry)
