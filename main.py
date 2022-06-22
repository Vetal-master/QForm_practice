import sys
sys.path.append('C:\Program Files education\QForm Engineer\SpaceClaim\Scripting')
sys.path.append('C:\Program Files education\QForm Engineer\SpaceClaim\SpaceClaim.Api.V19')

import UtilitiesOnLoadV20Custom

rect = SpaceClaim.Api.V19.Geometry.RectangleProfile(Plane.PlaneXY,0.1,0.1,PointUV.Origin,0.0)
bbody = Body.ExtrudeProfile(rect,0.1)
DesignBody.Create(Window.ActiveWindow.Document.MainPart, "Brick", bbody)


circle_cavity = SpaceClaim.Api.V19.Geometry.CircleProfile(Plane.PlaneXY,0.01,PointUV.Origin,0.0)
bbody = Body.ExtrudeProfile(circle_cavity,0.01)
DesignBody.Create(Window.ActiveWindow.Document.MainPart, "Cylinder", bbody)




########Recorded#########

# Intersect Bodies
targets = Body2
tools = Body3
options = MakeSolidsOptions()
result = Combine.Intersect(targets, tools, options, Info1)
# EndBlock

# Delete Objects
selection = Body4
result = Combine.RemoveRegions(selection, Info2)
# EndBlock

########Recorded#########




selection = Body3
result = Delete.Execute(selection)

DocumentSave.Execute(r"D:deleteeee.stp", FileSettings1)
