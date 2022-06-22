# Python Script, API Version = V19
# Cube Parameters
center_coordinate = PointUV.Create(0.05, 0.05)
edge_langth = 0.1
cube_plane = Plane.PlaneXY
angle_cube_plane = 0
name_3D_object = "Cube"


def create_cube(cube_plane, edge_langth, center_coordinate, angle_cube_plane, name_3D_object):
    profile = SpaceClaim.Api.V19.Geometry.RectangleProfile(cube_plane, edge_langth, edge_langth, center_coordinate, angle_cube_plane)
    cube = Body.ExtrudeProfile(profile, edge_langth)
    DesignBody.Create(Window.ActiveWindow.Document.MainPart, name_3D_object, cube)


def run_work():
    create_cube(cube_plane, edge_langth, center_coordinate, angle_cube_plane, name_3D_object)


run_work()