# Global message
Error = "-------------------------------------ERROR-------------------------------------"
Success = "-------------------------------------SUCCESS-------------------------------------"

# Base Cube Parameters
edge_length = 0.1 * 2                                                           # (м)
# center_coordinate = PointUV.Create(edge_length / 2, edge_length / 2)
# cube_plane = Plane.PlaneXY
name_base_object = "base_cube"

# Set 3D objects
Cube = "куб"
Sphere = "сфера"
Ellipse = "эллипс"

# Excel reader params for geometry
path_data_geometry = "C:\GitHub\QForm_practice\\tests\Модель_пористости.xlsx"
cols_geometry_ = [0, 1, 9, 10, 11]
col_type_object = 0
col_percent_porosity = 1
col_additional_parameter_1 = 2
col_additional_parameter_2 = 3
col_additional_parameter_3 = 4
