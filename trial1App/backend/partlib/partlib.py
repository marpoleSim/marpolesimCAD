import cadquery as cq

def rectanglePlate( arg ):

    length = arg[0]     # Length of the block
    height = arg[1]     # Height of the block
    thickness = arg[2]  # Thickness of the block
   
    obj = (
           cq.Workplane("XY")
           .box(length, height, thickness)
          )

    return obj

   
