from tqdm import tqdm
import time

import porosity
from Excel import geometry_data_input
import config
import utils

from SpaceClaim import utils as SC_utils
from SpaceClaim import cube as SC_cube


def run_work__test():
    dataset = geometry_data_input.load_geometry_params(config.path_data_geometry, config.cols_geometry__)

    count_experiments = len(dataset["type_object"])

    for i in tqdm(range(count_experiments), colour='blue', desc='Process', ncols=80):
        # SC_cube.extrude_cube(config.cube_plane__, config.edge_length__ / 2, config.name_base_object__)
        # SC_utils.visibility()

        if dataset["additional_parameter_1"][i] is None:
            result = porosity.create(dataset["type_object"][i], dataset["percent_porosity"][i], config.edge_length__)
        else:
            parameters = {
                "relative_OX": dataset["additional_parameter_1"][i],
                "relative_OY": dataset["additional_parameter_2"][i],
                "relative_OZ": dataset["additional_parameter_3"][i]
            }

            result = porosity.create(dataset["type_object"][i], dataset["percent_porosity"][i], config.edge_length__, parameters)

        if result:
            utils.output_red_text(config.Error)
            exit(-1)

        time.sleep(0.005)

    utils.output_green_text(config.Success)


run_work__test()
