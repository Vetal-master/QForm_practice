import utils


def extrude_cube(cube_plane, edge_length, center_coordinate, type_3D_object, angle_cube_plane=0):
    profile = SpaceClaim.Api.V19.Geometry.RectangleProfile(cube_plane, edge_length, edge_length, center_coordinate,
                                                           angle_cube_plane)

    cube = Body.ExtrudeProfile(profile, edge_length)

    DesignBody.Create(Window.ActiveWindow.Document.MainPart, type_3D_object, cube)

    utils.visibility()


def execute_cube(cube_plane, edge_length, center_coordinate, name_3D_object, angle_cube_plane=0):
    targets = BodySelection.Create(GetRootPart().Bodies[0])
    tools = BodySelection.Create(GetRootPart().Bodies[1])
    options = MakeSolidsOptions()
    result = Combine.Intersect(targets, tools, options)
    selection = BodySelection.Create(GetRootPart().Bodies[2])
    result = Combine.RemoveRegions(selection)
    selection = BodySelection.Create(GetRootPart().Bodies[1])
    result = Delete.Execute(selection)
