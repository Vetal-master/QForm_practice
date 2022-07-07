# from tqdm import tqdm
from sys import path as path_sys
from os import path as path_os

module_path_excel = path_os.abspath(path_os.join(path_os.dirname(__file__), 'Excel'))
path_sys.append(module_path_excel)

lib_path_configs = path_os.abspath(path_os.join(path_os.dirname(__file__), 'configs'))
path_sys.append(lib_path_configs)

import geometry_data_reader as reader
import pandas_geometry_conf as excel_conf
import geometry_conf as global_conf
import porosity_generator as porosity

import global_utils as utils


def run_create_geometry_set():
    dataset = reader.load_geometry_params(excel_conf.path_data_geometry, excel_conf.cols_geometry__)

    count_geometry_set = len(dataset)

    # for i in tqdm(range(count_geometry_set), colour='blue', desc='Create 3D objects', ncols=80):
    for i in range(count_geometry_set):
        # cube = {"O1": global_conf.edge_length__ / 2, "O2": global_conf.edge_length__ / 2, "O3": global_conf.edge_length__ / 2}
        # center = {"O1": global_conf.edge_length__ / 4, "O2": global_conf.edge_length__ / 4}
        # SC_cube.extrude_cube(global_conf.cube_plane__,  cube, config.name_base_object__, center)
        # SC_utils.visibility()

        if dataset[i]["type_object"] == global_conf.Cube or dataset[i]["type_object"] == global_conf.Sphere:
            result = porosity.create(dataset[i]["type_object"], dataset[i]["percent_porosity"], global_conf.edge_length__)
        else:
            parameters = {
                "relative_OX": dataset[i]["additional_parameter_1"],
                "relative_OY": dataset[i]["additional_parameter_2"],
                "relative_OZ": dataset[i]["additional_parameter_3"]
            }

            result = porosity.create(dataset[i]["type_object"], dataset[i]["percent_porosity"], global_conf.edge_length__, parameters)

        if result:
            utils.output_red_text(global_conf.error_geometry)
            exit(-1)

    utils.output_green_text(global_conf.success_geometry)

