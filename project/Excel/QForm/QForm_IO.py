import pandas

from project.Excel.QForm.configs import pandas_QForm_conf as excel_conf, QForm_IO_conf as conf
from project.Excel import global_excel_conf as global_excel_conf_
from project import global_conf as global_conf_

# List results create
ERROR_EMPTY_DATASET = -1


def get_name_model(type_3D_object, porosity_percent, object_parameters):
    if type_3D_object == global_conf_.Ellipse__:
        name_model = type_3D_object + "_" + \
                     str(porosity_percent) + "_" + \
                     str(object_parameters["additional_parameter_1"]) + "_" + \
                     str(object_parameters["additional_parameter_2"]) + "_" + \
                     str(object_parameters["additional_parameter_3"]) + ".stp"
    else:
        name_model = type_3D_object + "_" + str(porosity_percent) + ".stp"

    return name_model


def load_qform_params(path=global_excel_conf_.path_dataset, cols_qform=excel_conf.cols_qform_input_):
    dataset_df = pandas.read_excel(path, usecols=cols_qform)

    count_qfrom_set = len(dataset_df)

    if count_qfrom_set == 0:
        print("Empty dataset")

        return ERROR_EMPTY_DATASET

    list_QForm_set = []

    for i in range(count_qfrom_set):
        row = dataset_df.iloc[i]

        model_params = {
            "additional_parameter_1": float(row[global_excel_conf_.additional_parameter_1]),
            "additional_parameter_2": float(row[global_excel_conf_.additional_parameter_2]),
            "additional_parameter_3": float(row[global_excel_conf_.additional_parameter_3]),
        }

        name = get_name_model(row[global_excel_conf_.type_object], float(row[global_excel_conf_.porosity_percent]),
                              model_params)

        qform_params = {
            "VX": float(row[excel_conf.col_VX]),
            "VY": float(row[excel_conf.col_VY]),
            "VZ": float(row[excel_conf.col_VZ]),
            "name_model": name
        }

        list_QForm_set.append(qform_params)

    print(conf.success_QForm_IO)

    return list_QForm_set


def get_results_qform(dataset, path=global_excel_conf_.path_dataset, cols_qform=excel_conf.cols_qform_output_):
    dataset_df = pandas.DataFrame({global_excel_conf_.P1: dataset["tool_1_PZ"],
                                   global_excel_conf_.P2: dataset["tool_2_PY"],
                                   global_excel_conf_.P3: dataset["tool_3_PX"],
                                   global_excel_conf_.medium_stresses: dataset["mean_stress_equal"]})

    with pandas.ExcelWriter(path, mode='a', if_sheet_exists='overlay') as writer:
        dataset_df.to_excel(writer, index=False, header=False, startrow=1, startcol=cols_qform[0],
                            sheet_name=global_excel_conf_.sheet_name)

    print(conf.success_QForm_IO)
