from System.Collections.Generic import List
from System.Collections.Generic import ICollection
import SpaceClaim.Api.V19.Unsupported

import time

# Cube Parameters
edge_length__ = 0.1
cube_plane__ = Plane.PlaneXY
name_base_object__ = "Cube__"

# Path
path_save = r"C:\Users\Andeo\Desktop\Практика\Задачи\Модель пористости\tmp"


def visibility():
    mode = InteractionMode.Solid

    ViewHelper.SetViewMode(mode, None)


def save_model(name, path=path_save):
    options = ExportOptions.Create()
    DocumentSave.Execute(path + "\\" + name + ".stp", options)


def remove_model():
    selection = BodySelection.Create(GetRootPart().Bodies[0])
    result = Delete.Execute(selection)


def extrude_cube(cube_plane, cube, name_3D_object, center_coordinate={"O1": 0, "O2": 0}, angle_cube_plane=0):
    center = PointUV.Create(center_coordinate["O1"], center_coordinate["O2"])

    profile = SpaceClaim.Api.V19.Geometry.RectangleProfile(cube_plane, cube["O1"], cube["O2"],
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


def run_work():
    extrude_cube(cube_plane__, {"O1": edge_length__, "O2": edge_length__, "O3": edge_length__}, name_base_object__,
                 {"O1": edge_length__ / 2, "O2": edge_length__ / 2})
    execute_cube(cube_plane__, {"O1": edge_length__ / 2, "O2": edge_length__ / 2, "O3": edge_length__ / 2}, "execute",
                 {"O1": edge_length__ / 4, "O2": edge_length__ / 4})
    save_model("cube")
    time.sleep(5)
    remove_model()

    extrude_cube(cube_plane__, {"O1": edge_length__, "O2": edge_length__, "O3": edge_length__}, name_base_object__,
                 {"O1": edge_length__ / 2, "O2": edge_length__ / 2})
    execute_sphere(edge_length__ / 2)
    save_model("sphere")
    time.sleep(5)
    remove_model()

    extrude_cube(cube_plane__, {"O1": edge_length__, "O2": edge_length__, "O3": edge_length__}, name_base_object__,
                 {"O1": edge_length__ / 2, "O2": edge_length__ / 2})
    execute_ellipse(0.01, 0.04, 0.06)
    save_model("ellipse")
    time.sleep(5)
    remove_model()


run_work()