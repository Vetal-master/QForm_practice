def extrude_sphere(center_coordinate, radius):
    begin = Point.Create(M(center_coordinate["OX"]), M(center_coordinate["OY"]), M(center_coordinate["OZ"]))

    radius_coordinate = {
        "OX": radius,
        "OY": 0,
        "OZ": 0
    }

    end = Point.Create(M(radius_coordinate["OX"]), M(radius_coordinate["OY"]), M(radius_coordinate["OZ"]))

    SphereBody.Create(begin, end, ExtrudeType.ForceIndependent)


def execute_sphere(center_coordinate, radius):
    begin = Point.Create(M(center_coordinate["OX"]), M(center_coordinate["OY"]), M(center_coordinate["OZ"]))

    radius_coordinate = {
        "OX": radius,
        "OY": 0,
        "OZ": 0
    }

    end = Point.Create(M(radius_coordinate["OX"]), M(radius_coordinate["OY"]), M(radius_coordinate["OZ"]))

    SphereBody.Create(begin, end, ExtrudeType.Cut)
