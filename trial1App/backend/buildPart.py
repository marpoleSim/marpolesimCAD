import trial1App.backend.partlib.partlib as pl
from cadquery import exporters

def savePartVtp(obj, partName, vtpPath):

    filename = str(vtpPath) + '/' + partName + ".vtp"
    exporters.export(obj, filename)

    return filename

def buildPart(partName, functionName, arg, vtpPath):

    # function name is used here for select function
    obj = pl.rectanglePlate( arg )

    # all model should be saved in vtp format for review
    filename = savePartVtp(obj, partName, vtpPath)

    return filename

