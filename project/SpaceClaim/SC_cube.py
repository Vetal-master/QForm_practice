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