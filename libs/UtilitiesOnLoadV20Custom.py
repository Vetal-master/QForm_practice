import math
import clr
import sys

clr.AddReference("System.Drawing")
from System.Drawing import Color
from System import String
from System.Collections.Generic import List
from System.Collections.Generic import Dictionary

sys.path.append('\libs\SpaceClaim')

import SpaceClaim
from SpaceClaim.Api.V20 import *

from SpaceClaim.Api.V20.Modeler import *

from SpaceClaim.Api.V20.Geometry import *

from SpaceClaim.Api.V20.Scripting.Commands import *

from SpaceClaim.Api.V20.Scripting.Helpers import *
from SpaceClaim.Api.V20.Scripting.Helpers.Units import *

from SpaceClaim.Api.V20.Scripting.Managers import *

from SpaceClaim.Api.V20.Scripting import ScriptTool
from SpaceClaim.Api.V20.Scripting import MeshBuilder

from SpaceClaim.Api.V20.Scripting.Selection import *
from SpaceClaim.Api.V20.Scripting.PersistenceMaps import *
from SpaceClaim.Api.V20.Scripting.PowerSelection import *
from SpaceClaim.Api.V20.Scripting.Commands import *
from SpaceClaim.Api.V20.Scripting.Commands.CommandOptions import *
from SpaceClaim.Api.V20.Scripting.Commands.CommandResults import *
from SpaceClaim.Api.V20.Scripting.Commands.CommandData import *
from SpaceClaim.Api.V20.Scripting.Commands.ProblemAreas import *
from SpaceClaim.Api.V20.Scripting.Internal import SpaceClaimTesting
from SpaceClaim.Api.V20.Scripting.Internal import ValidationExecption
from SpaceClaim.Api.V20.Scripting.ReplayBlocks import ReplayBlockHelper
from SpaceClaim.Api.V20.Scripting.Internal.ReplayBlocks import ReplayInputHelper

clr.ImportExtensions(SpaceClaim.Api.V20.Scripting.Extensions.DesignEdgeExtensions)
clr.ImportExtensions(SpaceClaim.Api.V20.Scripting.Extensions.DesignFaceExtensions)
clr.ImportExtensions(SpaceClaim.Api.V20.Scripting.Extensions.DesignCurveExtensions)
clr.ImportExtensions(SpaceClaim.Api.V20.Scripting.Extensions.PartExtensions)
clr.ImportExtensions(SpaceClaim.Api.V20.Scripting.Extensions.MidsurfaceAspectExtensions)
clr.ImportExtensions(SpaceClaim.Api.V20.Scripting.Extensions.ComponentExtensions)
clr.ImportExtensions(SpaceClaim.Api.V20.Scripting.Extensions.DesignMeshExtensions)
clr.ImportExtensions(SpaceClaim.Api.V20.Scripting.Extensions.DesignBodyExtensions)
clr.ImportExtensions(SpaceClaim.Api.V20.Scripting.Extensions.DocObjectExtensions)
clr.ImportExtensions(SpaceClaim.Api.V20.Scripting.Extensions.HasNameExtensions)


def GetID(object):
    monstr = object.Moniker.ToString()
    s = monstr.split(":")
    t = s[1].split('"')
    return t[0]


def GetObject(id):
    entity = GetPart().Find(id)
    if entity is None:
        return None

    return entity


def GetActiveWindow():
    window = Window.ActiveWindow
    if window is None:
        return None

    return window


def GetRootPart():
    ''' '''
    return DocumentHelper.GetRootPart()


def GetActivePart():
    ''' '''
    return DocumentHelper.GetActivePart()


def CloseWindow():
    Window.ActiveWindow.Close()


def SelectionDebug(sel):
    objects = sel.GetDocObjects()
    for ob in objects:
        ObjectDebug(ob)


def ObjectDebug(object):
    print(type(object))
    print("	ID = " + str(GetID(object)))
    if type(object) is DesignBody:
        print("	Body Name: " + object.Name)
        print("	Faces = " + str(object.Faces.Count))
        print("	Edges = " + str(object.Edges.Count))
    elif type(object) is DesignFace:
        surface = object.Shape.Geometry
        if type(surface) is Cylinder:
            print("	Cylinder")
        elif type(surface) is Sphere:
            print("	Sphere")
        elif type(surface) is Torus:
            print("	Torus")
        elif type(surface) is Plane:
            print("	Plane")
        else:
            print("	Unknown Surface Type")
        print("	Edges = " + str(object.Edges.Count))
    elif type(object) is DesignEdge:
        edge = object.Shape.Geometry
        if type(edge) is Line:
            print("	Line")
        if type(edge) is Circle:
            print("	Circle")
        if type(edge) is Ellipse:
            print("	Ellipse")
        print("	Smooth = " + str(object.Shape.IsSmooth))
        print("	Concave = " + str(object.Shape.IsConcave))
        print("	Precision = " + str(object.Shape.Precision))
        print("	Faces = " + str(object.Faces.Count))


def ClearAll():
    part = GetRootPart()
    ComponentHelper.SetRootActive()
    part.ClearAllPartData()


def ClearTypes(type):
    part = GetRootPart()
    part.ClearPartData(type)
