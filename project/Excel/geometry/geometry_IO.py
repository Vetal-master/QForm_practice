import pandas
import geometry_IO_conf as global_conf, pandas_geometry_conf as excel_conf

# List results create
ERROR_EMPTY_DATASET = -1


def check_equal_geometry_params(left, right):
    if left["type_object"] == right["type_object"] and left["percent_porosity"] == right["percent_porosity"]:
        if left["type_object"] == global_conf.Ellipse__:
            if (left["additional_parameter_1"] == right["additional_parameter_1"] and
                    left["additional_parameter_2"] == right["additional_parameter_2"] and
                    left["additional_parameter_3"] == right["additional_parameter_3"]):
                return True
            return False
        return True
    return False


def load_geometry_params(path=global_conf.path_dataset, cols_geometry=excel_conf.cols_geometry__, path_save=global_conf.path_geometry_data__IO):
    dataset_df = pandas.read_excel(path, usecols=cols_geometry)

    count_geometry_set = len(dataset_df)

    if count_geometry_set == 0:
        print("Empty dataset")

        return ERROR_EMPTY_DATASET

    list_geometry_set = []

    for i in range(count_geometry_set):
        row = dataset_df.iloc[i]

        model = {
            "type_object": row[excel_conf.geometry],
            "percent_porosity": row[excel_conf.porosity_percent]
        }

        if model["type_object"] == global_conf.Ellipse__:
            model["additional_parameter_1"] = row[excel_conf.additional_parameter_1]
            model["additional_parameter_2"] = row[excel_conf.additional_parameter_2]
            model["additional_parameter_3"] = row[excel_conf.additional_parameter_3]

        if i != 0:
            if check_equal_geometry_params(list_geometry_set[-1], model) is False:
                list_geometry_set.append(model)
        else:
            list_geometry_set.append(model)

    with open(path_save, 'w+') as out:
         for model in list_geometry_set:
             result = ' '.join([f'{value}' for key, value in model.items()])
             out.write('{}\n'.format(result))

    print(global_conf.success_geometry_IO)

    return list_geometry_set


load_geometry_params()