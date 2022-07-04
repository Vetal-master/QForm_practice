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


def execute_cube(cube_plane, edge_length, name_3D_object, angle_cube_plane=0):
    extrude_cube(cube_plane, edge_length, name_3D_object)

    targets = BodySelection.Create(GetRootPart().Bodies[0])

    tools = BodySelection.Create(GetRootPart().Bodies[1])

    options = MakeSolidsOptions()

    result = Combine.Intersect(targets, tools, options)

    selection = BodySelection.Create(GetRootPart().Bodies[2])

    result = Combine.RemoveRegions(selection)

    selection = BodySelection.Create(GetRootPart().Bodies[1])

    result = Delete.Execute(selection)


def execute_sphere(center_coordinate, radius):
    begin = Point.Create(M(center_coordinate["OX"]), M(center_coordinate["OY"]), M(center_coordinate["OZ"]))

    radius_coordinate = {
        "OX": radius,
        "OY": 0,
        "OZ": 0
    }

    end = Point.Create(M(radius_coordinate["OX"]), M(radius_coordinate["OY"]), M(radius_coordinate["OZ"]))

    SphereBody.Create(begin, end, ExtrudeType.Cut)


def run_work():
    extrude_cube(cube_plane__, edge_length__, name_base_object__)
    visibility()
    execute_sphere({"OX": edge_length / 2, "OY": edge_length / 2, "OZ": 0}, edge_length / 2)


run_work()

    # [a]*Cos([u])*Cos([v])
    # [b]*Cos([v])*Sin([u])
    # [c]*Sin([v])
    # 0
    # 6,28
    # 0
    # 6,28
    # 10
    # 1
    # 2
    # 4
    #
    # # Преобразовать объекты в фасетированные тела.
    # selection = BodySelection.Create(GetRootPart().Bodies[1])
    # result = FacetConvert.Create(selection)
    # result.CreatedMeshes[0].Shape.Vertices[0].Position.X
    # # EndBlock
    #
    # DesignMesh.Create()