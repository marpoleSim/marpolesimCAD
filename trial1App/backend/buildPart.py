from cadquery import exporters
import trial1App.backend.partlib.partlib as pl

def savePartVtp(obj, partName, vtpPath):

    filename = str(vtpPath) + '/' + partName + ".vtp"
    exporters.export(obj, filename)

    return filename

def savePartStl(obj, partName, stlPath):

    filename = str(stlPath) + '/' + partName + ".stl"
    exporters.export(obj, filename)

    return filename

def buildPart(partName, functionName, arg, mediaPath):

    # function name is used here for select function
    flag = True
    try:
       obj = getattr(pl, functionName)( arg )
    except:
       flag = False

    # all model should be saved in vtp format for review
    if flag:
        savePartVtp(obj, partName, mediaPath)
        #savePartStl(obj, partName, mediaPath)

    return flag 

