import pandas
from project import config


def load_geometry_params(path, cols_geometry):
    dataset_df = pandas.read_excel(path, usecols=cols_geometry)

    type_object = dataset_df.iloc[:, config.col_type_object].values.tolist()

    percent_porosity = dataset_df.iloc[:, config.col_percent_porosity].values.tolist()

    additional_parameter_1 = dataset_df.iloc[:, config.col_additional_parameter_1].values.tolist()

    additional_parameter_2 = dataset_df.iloc[:, config.col_additional_parameter_2].values.tolist()

    additional_parameter_3 = dataset_df.iloc[:, config.col_additional_parameter_3].values.tolist()

    dataset = {
        "type_object": type_object,
        "percent_porosity": percent_porosity,
        "additional_parameter_1": additional_parameter_1,
        "additional_parameter_2": additional_parameter_2,
        "additional_parameter_3": additional_parameter_3
    }

    return dataset
