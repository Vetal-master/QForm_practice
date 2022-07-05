from tqdm import tqdm
import time

import porosity

from Excel import geometry_data_input
from project.configs import pandas as excel_conf
from project.configs import main as global_conf

import utils

from SpaceClaim import utils as SC_utils
from SpaceClaim import cube as SC_cube


def run_create_geometry_set():
    dataset = geometry_data_input.load_geometry_params(excel_conf.path_data_geometry, excel_conf.cols_geometry__)

    count_geometry_set = len(dataset)

    for i in tqdm(range(count_geometry_set), colour='blue', desc='Create 3D objects', ncols=80):
        # SC_cube.extrude_cube(config.cube_plane__, config.edge_length__ / 2, config.name_base_object__)
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

        time.sleep(0.05)

    utils.output_green_text(global_conf.success_geometry)

