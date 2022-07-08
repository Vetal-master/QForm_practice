import math

from System.Collections.Generic import List
from System.Collections.Generic import ICollection
import SpaceClaim.Api.V19.Unsupported

# Global message
error_geometry = "-------------------------------ERROR CREATE GEOMETRY---------------------------"
success_geometry = "------------------------------END CREATE GEOMETRY------------------------------"

# Base Cube Parameters
edge_length__ = 0.1 * 2  # (м)
cube_plane__ = Plane.PlaneXY
name_base_object__ = "base_cube"

# Set 3D objects
Cube__ = "cube"
Sphere__ = "sphere"
Ellipse__ = "ellipse"

# Path save models
path_save__ = r"C:\Users\Andeo\Desktop\Практика\Задачи\Модель пористости\tmp"
path_geometry_data__ = r"C:\GitHub\QForm_practice\tmp_data_log\geometry.txt"


def visibility():
    mode = InteractionMode.Solid

    ViewHelper.SetViewMode(mode, None)


def save_model(name, path=path_save__):
    options = ExportOptions.Create()

    DocumentSave.Execute(path + "\\" + name + ".stp", options)


def remove_model():
    selection = BodySelection.Create(GetRootPart().Bodies[0])

    result = Delete.Execute(selection)


def extrude_cube(cube_plane, cube, name_3D_object, center_coordinate={"O1": 0, "O2": 0}, angle_cube_plane=0):
    center = PointUV.Create(center_coordinate["O1"], center_coordinate["O2"])

    profile = SpaceClaim.Api.V19.Geometry.RectangleProfile(cube_plane__, cube["O1"], cube["O2"],
                                                           center,
                                                           angle_cube_plane)

    cube = Body.ExtrudeProfile(profile, cube["O3"])

    DesignBody.Create(Window.ActiveWindow.Document.MainPart, name_3D_object, cube)


def execute_cube(cube_plane, cube, name_3D_object, center_coordinate={"O1": 0, "O2": 0}, angle_cube_plane=0):
    extrude_cube(cube_plane, cube, name_3D_object, center_coordinate)

    targets = BodySelection.Create(GetRootPart().Bodies[0])

    tools = BodySelection.Create(GetRootPart().Bodies[1])

    options = MakeSolidsOptions()

    result = Combine.Intersect(targets, tools, options)

    selection = BodySelection.Create(GetRootPart().Bodies[2])

    result = Combine.RemoveRegions(selection)

    selection = BodySelection.Create(GetRootPart().Bodies[1])

    result = Delete.Execute(selection)


def extrude_sphere(radius, center_coordinate={"OX": 0, "OY": 0, "OZ": 0}):
    begin = Point.Create(M(center_coordinate["OX"]), M(center_coordinate["OY"]), M(center_coordinate["OZ"]))

    radius_coordinate = {
        "OX": radius,
        "OY": 0,
        "OZ": 0
    }

    end = Point.Create(M(radius_coordinate["OX"]), M(radius_coordinate["OY"]), M(radius_coordinate["OZ"]))

    SphereBody.Create(begin, end, ExtrudeType.ForceIndependent)


def execute_sphere(radius, center_coordinate={"OX": 0, "OY": 0, "OZ": 0}):
    begin = Point.Create(M(center_coordinate["OX"]), M(center_coordinate["OY"]), M(center_coordinate["OZ"]))

    radius_coordinate = {
        "OX": radius,
        "OY": 0,
        "OZ": 0
    }

    end = Point.Create(M(radius_coordinate["OX"]), M(radius_coordinate["OY"]), M(radius_coordinate["OZ"]))

    SphereBody.Create(begin, end, ExtrudeType.Cut)


def extrude_ellipse(a, b, c, name_3D_object, center_coordinate={"OX": 0, "OY": 0, "OZ": 0}):
    center = Point.Create(center_coordinate["OX"], center_coordinate["OY"], center_coordinate["OZ"])

    c1 = CurveSegment.Create(Ellipse.Create(Frame.Create(center, Direction.DirX, Direction.DirY), a, b),
                             Interval.Create(0, math.pi))
    c2 = CurveSegment.Create(Ellipse.Create(Frame.Create(center, Direction.DirX, Direction.DirZ), a, c),
                             Interval.Create(0, math.pi))
    c3 = CurveSegment.Create(Ellipse.Create(Frame.Create(center, Direction.DirY, Direction.DirZ), b, c),
                             Interval.Create(0, math.pi / 2))

    pt = Window.ActiveWindow.Document.MainPart

    profile1 = List[ITrimmedCurve]([c1])
    profile2 = List[ITrimmedCurve]([c2])
    guides = List[ITrimmedCurve]([c3])
    profiles = List[ICollection[ITrimmedCurve]]([profile1, profile2])
    b = Body.LoftProfiles(None, profiles, None, guides)

    matrixXZ = SpaceClaim.Api.V19.Unsupported.MatrixMethods.GetMirror(
        Plane.Create(Frame.Create(center, Direction.DirX, Direction.DirZ)))
    matrixXY = SpaceClaim.Api.V19.Unsupported.MatrixMethods.GetMirror(
        Plane.Create(Frame.Create(center, Direction.DirX, Direction.DirY)))

    b2 = b.Copy()
    b2.Transform(matrixXZ)
    b.Unite(List[Body]([b2]))
    b2 = b.Copy()
    b2.Transform(matrixXY)
    b.Unite(List[Body]([b2]))

    DesignBody.Create(pt, name_3D_object, b)


def execute_ellipse(a, b, c, center_coordinate={"OX": 0, "OY": 0, "OZ": 0}):
    extrude_ellipse(a, b, c, "execute", center_coordinate)

    targets = BodySelection.Create(GetRootPart().Bodies[0])

    tools = BodySelection.Create(GetRootPart().Bodies[1])

    options = MakeSolidsOptions()

    result = Combine.Intersect(targets, tools, options)

    selection = BodySelection.Create(GetRootPart().Bodies[2])

    result = Combine.RemoveRegions(selection)

    selection = BodySelection.Create(GetRootPart().Bodies[1])

    result = Delete.Execute(selection)


def run_create_geometry_set(path):
    geometry_set = open(path, "r")
    lines_models = geometry_set.readlines()

    for line_model in lines_models:
        cube = {"O1": edge_length__ / 2.0, "O2": edge_length__ / 2.0, "O3": edge_length__ / 2.0}
        center = {"O1": edge_length__ / 4.0, "O2": edge_length__ / 4.0}
        extrude_cube(cube_plane__, cube, name_base_object__, center)
        visibility()

        model_data = line_model.split(" ", 5)

        type_object = model_data[0]
        percent_porosity = model_data[1]

        if type_object == Ellipse__:
            parameters = {
                "relative_OX": float(model_data[2]),
                "relative_OY": float(model_data[3]),
                "relative_OZ": float(model_data[4].replace('\n', ''))
            }

            result = create_por(type_object, float(percent_porosity.replace('\n', '')),
                                edge_length__, parameters)
        else:
            result = create_por(type_object, float(percent_porosity),
                                edge_length__)

        if result:
            print(error_geometry)
            exit(-1)

    print(success_geometry)


# List results create
SUCCESS = 0
ERROR_CLASSIFICATION_TYPE = -1
ERROR_POROSITY_PERCENT_OUT_OF_RANGE = -2
ERROR_BASE_SIZE_OUT_OF_RANGE = -3
ERROR_ELLIPSE_PARAMS = -4


def create_por(type_3D_object, porosity_percent, base_size, object_parameters=None):
    if (porosity_percent > 100 or porosity_percent <= 0):
        print("Incorrect porosity percent")

        return ERROR_POROSITY_PERCENT_OUT_OF_RANGE

    if (base_size <= 0):
        print("Incorrect base size")

        return ERROR_BASE_SIZE_OUT_OF_RANGE

    base_volume = math.pow(base_size, 3)

    porosity_coefficient = porosity_percent / 100

    porosity_volume = porosity_coefficient * base_volume

    if type_3D_object == Ellipse__:
        name_model = type_3D_object + "_" + \
                     str(porosity_percent) + "_" + \
                     str(object_parameters["relative_OX"]) + "_" + \
                     str(object_parameters["relative_OY"]) + "_" + \
                     str(object_parameters["relative_OZ"])
    else:
        name_model = type_3D_object + "_" + str(porosity_percent)

    if type_3D_object == Cube__:
        work_cube(porosity_volume, name_model)

    elif type_3D_object == Sphere__:
        work_sphere(porosity_volume, name_model)

    elif type_3D_object == Ellipse__:
        if len(object_parameters) < 3:
            print("Incorrect additional parameters. Must be 3 parameters for ellipse")

            return ERROR_ELLIPSE_PARAMS

        work_ellipse(porosity_volume, object_parameters, name_model)

    else:
        print("Not such type 3D object")

        return ERROR_CLASSIFICATION_TYPE

    print(name_model + " DONE")

    return SUCCESS


def calculate_cube(volume):
    return math.pow(volume, 1.0 / 3.0)


def work_cube(volume, name="cube"):
    edge = calculate_cube(volume) / 2.0

    execute_cube(cube_plane__, {"O1": edge, "O2": edge, "O3": edge}, "execute", {"O1": edge / 2.0, "O2": edge / 2.0})

    save_model(name)

    remove_model()


def calculate_ellipse(volume, object_parameters, data=0):
    relative_coefficient = object_parameters["relative_OX"] * object_parameters["relative_OY"] * object_parameters[
        "relative_OZ"]

    scale = math.pow((3.0 * volume) / (4.0 * math.pi * relative_coefficient), 1.0 / 3.0)

    ellipse_parameters = {
        "OX": object_parameters["relative_OX"] * scale,
        "OY": object_parameters["relative_OY"] * scale,
        "OZ": object_parameters["relative_OZ"] * scale
    }

    return ellipse_parameters


def work_ellipse(volume, object_parameters, name="ellipse"):
    ellipse = calculate_ellipse(volume, object_parameters)

    execute_ellipse(ellipse["OX"], ellipse["OY"], ellipse["OZ"])

    save_model(name)

    remove_model()


def calculate_sphere(volume):
    return math.pow(3.0 * volume / (4.0 * math.pi), 1.0 / 3.0)


def work_sphere(volume, name="sphere"):
    radius = calculate_sphere(volume)

    execute_sphere(radius)

    save_model(name)

    remove_model()


def run_work():
    run_create_geometry_set(path_geometry_data__)


run_work()
