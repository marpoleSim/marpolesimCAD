import cadquery as cq
from cadquery import exporters

def simpleBlock(x, y, diameter, vtpROOTPath):

    x = float(x)
    y = float(y)
    diameter = float(diameter)

    length = 80.0     # Length of the block
    height = 60.0     # Height of the block
    thickness = 20.0  # Thickness of the block
   
    result = (
              cq.Workplane("XY")
              .box(length, height, thickness)
              .faces(">Z").workplane()
              .center(x,y)
              .hole(diameter)
    )
    
    filename = str(vtpROOTPath) + '/' + "simpleBlock.vtp"
    cq.exporters.export(result, filename)

    return filename
   
