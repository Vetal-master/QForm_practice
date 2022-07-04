from tqdm import tqdm
import time

import porosity
from Excel import excel_IO
import config
import utils


def run_work():
    base_object.create_cube(cube_plane, edge_length, center_coordinate, angle_cube_plane, name_3D_object)


# run_work()

def run_work__test():
    dataset = excel_IO.load_geometry_params(config.path_data_geometry, config.cols_geometry_)

    count_experiments = len(dataset["type_object"])

    for i in tqdm(range(count_experiments), colour='blue', desc='Process', ncols=80):
        if dataset["additional_parameter_1"][i] is None:
            result = porosity.create(dataset["type_object"][i], dataset["percent_porosity"][i], config.edge_length)
        else:
            parameters = {
                "relative_OX": dataset["additional_parameter_1"][i],
                "relative_OY": dataset["additional_parameter_2"][i],
                "relative_OZ": dataset["additional_parameter_3"][i]
            }

            result = porosity.create(dataset["type_object"][i], dataset["percent_porosity"][i], config.edge_length, parameters)

        if result:
            utils.output_red_text(config.Error)
            exit(-1)

        time.sleep(0.005)

    utils.output_green_text(config.Success)


run_work__test()
