import math
import clr

clr.AddReference("System.Drawing")
from System.Drawing import Color
from System import String
from System.Collections.Generic import List
from System.Collections.Generic import Dictionary

import SpaceClaim
from SpaceClaim.Api.V20 import Window
from SpaceClaim.Api.V20 import InteractionMode
from SpaceClaim.Api.V20 import Document
from SpaceClaim.Api.V20 import IDocObject
from SpaceClaim.Api.V20 import DocObject
from SpaceClaim.Api.V20 import ImportOptions
from SpaceClaim.Api.V20 import MixedImportResolution
from SpaceClaim.Api.V20 import AnalysisType
from SpaceClaim.Api.V20 import ExportOptions
from SpaceClaim.Api.V20 import StlExportFormat
from SpaceClaim.Api.V20 import StlFileGranularity
from SpaceClaim.Api.V20 import Part
from SpaceClaim.Api.V20 import IPart
from SpaceClaim.Api.V20 import Component
from SpaceClaim.Api.V20 import IComponent
from SpaceClaim.Api.V20 import Group
from SpaceClaim.Api.V20 import IGroup
from SpaceClaim.Api.V20 import DrawingViewStyle
from SpaceClaim.Api.V20 import MidSurfaceAspect
from SpaceClaim.Api.V20 import CoordinateAxis
from SpaceClaim.Api.V20 import ICoordinateAxis
from SpaceClaim.Api.V20 import CoordinateSystem
from SpaceClaim.Api.V20 import ICoordinateSystem
from SpaceClaim.Api.V20 import DesignBody
from SpaceClaim.Api.V20 import IDesignBody
from SpaceClaim.Api.V20 import DesignFace
from SpaceClaim.Api.V20 import IDesignFace
from SpaceClaim.Api.V20 import DesignEdge
from SpaceClaim.Api.V20 import IDesignEdge
from SpaceClaim.Api.V20 import DesignCurve
from SpaceClaim.Api.V20 import IDesignCurve
from SpaceClaim.Api.V20 import DesignMesh
from SpaceClaim.Api.V20 import IDesignMesh
from SpaceClaim.Api.V20 import DesignMeshRegion
from SpaceClaim.Api.V20 import IDesignMeshRegion
from SpaceClaim.Api.V20 import DesignMeshTopology
from SpaceClaim.Api.V20 import IDesignMeshTopology
from SpaceClaim.Api.V20 import CircularSense
from SpaceClaim.Api.V20 import MixedImportResolution
from SpaceClaim.Api.V20 import AnalysisType
from SpaceClaim.Api.V20 import IDatumLine
from SpaceClaim.Api.V20 import DatumLine
from SpaceClaim.Api.V20 import IDatumPlane
from SpaceClaim.Api.V20 import DatumPlane
from SpaceClaim.Api.V20 import IDatumPoint
from SpaceClaim.Api.V20 import DatumPoint
from SpaceClaim.Api.V20 import IBeam
from SpaceClaim.Api.V20 import ICurvePoint
from SpaceClaim.Api.V20 import CurvePoint
from SpaceClaim.Api.V20 import IDesignAxis
from SpaceClaim.Api.V20 import DesignAxis
from SpaceClaim.Api.V20 import ISectionCurve
from SpaceClaim.Api.V20 import SectionCurve
from SpaceClaim.Api.V20 import IWireCurve
from SpaceClaim.Api.V20 import WireCurve
from SpaceClaim.Api.V20 import IHole
from SpaceClaim.Api.V20 import IFacePoint
from SpaceClaim.Api.V20 import FacePoint
from SpaceClaim.Api.V20 import MidSurfaceOffsetType

from SpaceClaim.Api.V20 import IBlocking
from SpaceClaim.Api.V20 import Blocking
from SpaceClaim.Api.V20 import IBlockVolume
from SpaceClaim.Api.V20 import BlockVolume
from SpaceClaim.Api.V20 import IBlockEdge
from SpaceClaim.Api.V20 import BlockEdge
from SpaceClaim.Api.V20 import IBlockVertex
from SpaceClaim.Api.V20 import BlockVertex
from SpaceClaim.Api.V20 import IBlockFace
from SpaceClaim.Api.V20 import BlockFace
from SpaceClaim.Api.V20 import IBlockMaterial
from SpaceClaim.Api.V20 import BlockMaterial
from SpaceClaim.Api.V20 import IBlockMeshAnalysis
from SpaceClaim.Api.V20 import BlockMeshAnalysis

from SpaceClaim.Api.V20.Modeler import Body
from SpaceClaim.Api.V20.Modeler import Edge
from SpaceClaim.Api.V20.Modeler import Facet
from SpaceClaim.Api.V20.Modeler import MeshFace
from SpaceClaim.Api.V20.Modeler import MeshEdge
from SpaceClaim.Api.V20.Modeler import MeshVertex

from SpaceClaim.Api.V20.Geometry import Direction
from SpaceClaim.Api.V20.Geometry import IBounded
from SpaceClaim.Api.V20.Geometry import Box
from SpaceClaim.Api.V20.Geometry import Curve
from SpaceClaim.Api.V20.Geometry import CurveEvaluation
from SpaceClaim.Api.V20.Geometry import Point
from SpaceClaim.Api.V20.Geometry import PointCurve
from SpaceClaim.Api.V20.Geometry import ProceduralCurve
from SpaceClaim.Api.V20.Geometry import Line
from SpaceClaim.Api.V20.Geometry import Helix
from SpaceClaim.Api.V20.Geometry import Cylinder
from SpaceClaim.Api.V20.Geometry import Sphere
from SpaceClaim.Api.V20.Geometry import Torus
from SpaceClaim.Api.V20.Geometry import Plane
from SpaceClaim.Api.V20.Geometry import Circle
from SpaceClaim.Api.V20.Geometry import Parameterization
from SpaceClaim.Api.V20.Geometry import Geometry
from SpaceClaim.Api.V20.Geometry import NurbsSurface
from SpaceClaim.Api.V20.Geometry import ProceduralSurface
from SpaceClaim.Api.V20.Geometry import Surface
from SpaceClaim.Api.V20.Geometry import SurfaceEvaluation
from SpaceClaim.Api.V20.Geometry import Space
from SpaceClaim.Api.V20.Geometry import ITrimmedSpace
from SpaceClaim.Api.V20.Geometry import Cone
from SpaceClaim.Api.V20.Geometry import Ellipse
from SpaceClaim.Api.V20.Geometry import Polygon
from SpaceClaim.Api.V20.Geometry import ITrimmedCurve
from SpaceClaim.Api.V20.Geometry import ITrimmedSurface
from SpaceClaim.Api.V20.Geometry import CurveSegment
from SpaceClaim.Api.V20.Geometry import LineSegment
from SpaceClaim.Api.V20.Geometry import Profile
from SpaceClaim.Api.V20.Geometry import NurbsCurve
from SpaceClaim.Api.V20.Geometry import Interval
from SpaceClaim.Api.V20.Geometry import Matrix
from SpaceClaim.Api.V20.Geometry import Vector
from SpaceClaim.Api.V20.Geometry import VectorUV
from SpaceClaim.Api.V20.Geometry import Frame
from SpaceClaim.Api.V20.Geometry import BoxUV
from SpaceClaim.Api.V20.Geometry import DirectionUV
from SpaceClaim.Api.V20.Geometry import Accuracy
from SpaceClaim.Api.V20.Geometry import PointUV

from SpaceClaim.Api.V20.Scripting.Commands import Point2D

from SpaceClaim.Api.V20.Scripting.Helpers import WindowHelper
from SpaceClaim.Api.V20.Scripting.Helpers import ComponentHelper
from SpaceClaim.Api.V20.Scripting.Helpers import DocumentHelper
from SpaceClaim.Api.V20.Scripting.Helpers import ViewHelper
from SpaceClaim.Api.V20.Scripting.Helpers import ColorHelper
from SpaceClaim.Api.V20.Scripting.Helpers import Beta
from SpaceClaim.Api.V20.Scripting.Helpers import ApplicationHelper
from SpaceClaim.Api.V20.Scripting.Helpers.Units import *
from SpaceClaim.Api.V20.Scripting.Helpers import *

from SpaceClaim.Api.V20.Scripting.Managers import ScriptEventManager

# from SpaceClaim.Api.V20.Scripting import ScriptTool
# from SpaceClaim.Api.V20.Scripting import MeshBuilder

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
    print (type(object))
    print ("	ID = " + str(GetID(object)))
    if type(object) is DesignBody:
        print ("	Body Name: " + object.Name)
        print ("	Faces = " + str(object.Faces.Count))
        print ("	Edges = " + str(object.Edges.Count))
    elif type(object) is DesignFace:
        surface = object.Shape.Geometry
        if type(surface) is Cylinder:
            print ("	Cylinder")
        elif type(surface) is Sphere:
            print ("	Sphere")
        elif type(surface) is Torus:
            print ("	Torus")
        elif type(surface) is Plane:
            print ("	Plane")
        else:
            print ("	Unknown Surface Type")
        print ("	Edges = " + str(object.Edges.Count))
    elif type(object) is DesignEdge:
        edge = object.Shape.Geometry
        if type(edge) is Line:
            print ("	Line")
        if type(edge) is Circle:
            print ("	Circle")
        if type(edge) is Ellipse:
            print ("	Ellipse")
        print ("	Smooth = " + str(object.Shape.IsSmooth))
        print ("	Concave = " + str(object.Shape.IsConcave))
        print ("	Precision = " + str(object.Shape.Precision))
        print ("	Faces = " + str(object.Faces.Count))


def ClearAll():
    part = GetRootPart()
    ComponentHelper.SetRootActive()
    part.ClearAllPartData()


def ClearTypes(type):
    part = GetRootPart()
    part.ClearPartData(type)
