# Global message
Error = "---------------------------------ERROR TESTING---------------------------------"
Success = "--------------------------------SUCCESS TESTING--------------------------------"

# Base Cube Parameters
edge_length__ = 0.1 * 2             # (м)
# cube_plane__ = Plane.PlaneXY
name_base_object__ = "base_cube"

# Заглушки
cube_plane__ = 2

# Set 3D objects
Cube = "куб"
Sphere = "сфера"
Ellipse = "эллипс"

# Excel reader params for geometry data
path_data_geometry = "C:\GitHub\QForm_practice\\tests\Модель_пористости.xlsx"
cols_geometry__ = [0, 1, 9, 10, 11]
col_type_object = 0
col_percent_porosity = 1
col_additional_parameter_1 = 2
col_additional_parameter_2 = 3
col_additional_parameter_3 = 4

# Excel reader params for qform data
path_data_geometry = "C:\GitHub\QForm_practice\\tests\Модель_пористости.xlsx"
cols_qform__ = [2, 3, 4]
col_VX = 0
col_VY = 1
col_VZ = 2
