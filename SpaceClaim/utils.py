def visibility():
    mode = InteractionMode.Solid

    ViewHelper.SetViewMode(mode, None)


def center_coordinate(edge_length):
    return PointUV.Create(edge_length / 2, edge_length / 2)
