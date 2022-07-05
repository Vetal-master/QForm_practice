from System.Collections.Generic import List
from System.Collections.Generic import ICollection
import SpaceClaim.Api.V19.Unsupported

# Cube Parameters
edge_length__ = 0.1
cube_plane__ = Plane.PlaneXY
name_base_object__ = "Cube__"


def visibility():
    mode = InteractionMode.Solid

    ViewHelper.SetViewMode(mode, None)


def center_coordinate(edge_length):
    return PointUV.Create(edge_length / 2, edge_length / 2)


def extrude_cube(cube_plane, edge_length, type_3D_object, angle_cube_plane=0):
    profile = SpaceClaim.Api.V19.Geometry.RectangleProfile(cube_plane, edge_length, edge_length,
                                                           center_coordinate(edge_length),
                                                           angle_cube_plane)

    cube = Body.ExtrudeProfile(profile, edge_length)

    DesignBody.Create(Window.ActiveWindow.Document.MainPart, type_3D_object, cube)


def extrude_ellipse(a, b, c, center, name_3D_object):
    center = Point.Create(center["OX"], center["OY"], center["OZ"])

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


def execute_ellipse(a, b, c, center):
    extrude_ellipse(a, b, c, center, "execute")

    targets = BodySelection.Create(GetRootPart().Bodies[0])

    tools = BodySelection.Create(GetRootPart().Bodies[1])

    options = MakeSolidsOptions()

    result = Combine.Intersect(targets, tools, options)

    selection = BodySelection.Create(GetRootPart().Bodies[2])

    result = Combine.RemoveRegions(selection)

    selection = BodySelection.Create(GetRootPart().Bodies[1])

    result = Delete.Execute(selection)


def run_work():
    extrude_cube(cube_plane__, edge_length__, name_base_object__)
    execute_ellipse(0.01, 0.04, 0.06, {"OX": 0, "OY": 0, "OZ": 0})


run_work()

# Сохранить файл
options = ExportOptions.Create()
DocumentSave.Execute("C:\Users\Andeo\Desktop\Практика\Задачи\Модель пористости\Конструкция1ЭЖЖЛ.stp", options)
# EndBlock

# Удалить объекты
selection = BodySelection.Create(GetRootPart().Bodies[0])
result = Delete.Execute(selection)
# EndBlock