from sys import path as path_sys
from os import path as path_os

module_path_generator = path_os.abspath(path_os.join(path_os.dirname(__file__), ''))
path_sys.append(module_path_generator)

module_path_configs = path_os.abspath(path_os.join(path_os.dirname(__file__), 'configs'))
path_sys.append(module_path_configs)

import geometry_generator as geometry
from geometry_conf import *

import math

print(math.pow(0.2, 3))
print(math.pow(0.2, 3) * 0.01)
print(math.pow(math.pow(0.2, 3) * 0.01, 1 / 3))

geometry.run_create_geometry_set(path_geometry_data__)
