import pandas

import QForm_IO_conf as excel_conf


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
