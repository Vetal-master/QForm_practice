from sys import path as path_sys
from os import path as path_os

module_path_excel = path_os.abspath(path_os.join(path_os.dirname(__file__), 'Excel'))
path_sys.append(module_path_excel)

module_path_configs = path_os.abspath(path_os.join(path_os.dirname(__file__), 'configs'))
path_sys.append(module_path_configs)

import geometry_data_reader as reader
import pandas_geometry_conf as excel_conf

reader.load_geometry_params(excel_conf.path_data_geometry, excel_conf.cols_geometry__)
