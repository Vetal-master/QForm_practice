import pandas
from sys import path as path_sys
from os import path as path_os

lib_path_configs = path_os.abspath(path_os.join(path_os.dirname(__file__), 'configs'))
path_sys.append(lib_path_configs)

import QForm_data_IO_conf as excel_conf


def load_qform_params(path, cols_qform):
    dataset_df = pandas.read_excel(path, usecols=cols_qform)

    VX = dataset_df.iloc[:, excel_conf.col_VX].values.tolist()

    VY = dataset_df.iloc[:, excel_conf.col_VY].values.tolist()

    VZ = dataset_df.iloc[:, excel_conf.col_VZ].values.tolist()

    dataset = {
        "VX": VX,
        "VY": VY,
        "VZ": VZ
    }

    return dataset
