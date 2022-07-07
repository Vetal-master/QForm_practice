from sys import path as path_sys
from os import path as path_os

module_path_generator = path_os.abspath(path_os.join(path_os.dirname(__file__), ''))
path_sys.append(module_path_generator)

import geometry_generator as geometry

geometry.run_create_geometry_set()
