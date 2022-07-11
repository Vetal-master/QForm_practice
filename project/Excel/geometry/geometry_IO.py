import pandas

from project.Excel.geometry.configs import pandas_geometry_conf as excel_conf, geometry_IO_conf as conf
from project.Excel import global_excel_conf as global_excel_conf_
from project import global_conf as global_conf_

# List results create
ERROR_EMPTY_DATASET = -1


def check_equal_geometry_params(left, right):
    if left["type_object"] == right["type_object"] and left["percent_porosity"] == right["percent_porosity"]:
        if left["type_object"] == global_conf_.Ellipse__:
            if (left["additional_parameter_1"] == right["additional_parameter_1"] and
                    left["additional_parameter_2"] == right["additional_parameter_2"] and
                    left["additional_parameter_3"] == right["additional_parameter_3"]):
                return True
            return False
        return True
    return False


def load_geometry_params(path=global_excel_conf_.path_dataset, cols_geometry=excel_conf.cols_geometry__, path_save=conf.path_geometry_data__IO):
    dataset_df = pandas.read_excel(path, usecols=cols_geometry)

    count_geometry_set = len(dataset_df)

    if count_geometry_set == 0:
        print("Empty dataset")

        return ERROR_EMPTY_DATASET

    list_geometry_set = []

    for i in range(count_geometry_set):
        row = dataset_df.iloc[i]

        model = {
            "type_object": row[global_excel_conf_.type_object],
            "percent_porosity": row[global_excel_conf_.porosity_percent]
        }

        if model["type_object"] == global_conf_.Ellipse__:
            model["additional_parameter_1"] = row[global_excel_conf_.additional_parameter_1]
            model["additional_parameter_2"] = row[global_excel_conf_.additional_parameter_2]
            model["additional_parameter_3"] = row[global_excel_conf_.additional_parameter_3]

        if i != 0:
            if check_equal_geometry_params(list_geometry_set[-1], model) is False:
                list_geometry_set.append(model)
        else:
            list_geometry_set.append(model)

    with open(path_save, 'w+') as out:
         for model in list_geometry_set:
             result = ' '.join([f'{value}' for key, value in model.items()])
             out.write('{}\n'.format(result))

    print(conf.success_geometry_IO)

    return list_geometry_set


load_geometry_params()
