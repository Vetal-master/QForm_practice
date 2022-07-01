# Cube Parameters
edge_length = 0.1
center_coordinate = PointUV.Create(edge_length / 2, edge_length / 2)
cube_plane = Plane.PlaneXY
name_3D_object = "Cube"


def create_cube(cube_plane, edge_length, center_coordinate, name_3D_object, angle_cube_plane=0):
    profile = SpaceClaim.Api.V19.Geometry.RectangleProfile(cube_plane, edge_length, edge_length, center_coordinate,
                                                           angle_cube_plane)

    cube = Body.ExtrudeProfile(profile, edge_length)

    DesignBody.Create(Window.ActiveWindow.Document.MainPart, name_3D_object, cube)

    mode = InteractionMode.Solid

    result = ViewHelper.SetViewMode(mode, None)


def run_work():
    create_cube(cube_plane, edge_length, center_coordinate, name_3D_object)


run_work()