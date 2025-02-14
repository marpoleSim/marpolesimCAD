from cadquery import exporters
import trial1App.backend.partlib.partlib as pl

def savePartVtp(obj, partName, vtpPath):

    filename = str(vtpPath) + '/' + partName + ".vtp"
    exporters.export(obj, filename)

    return filename

def savePartStl(obj, orderId, stlPath):

    filename = str(stlPath) + '/stl/A' + orderId + ".stl"
    exporters.export(obj, filename)

    return filename

def buildPart(orderId, partName, functionName, arg, mediaPath):

    # function name is used here for select function
    flag = True
    try:
       obj = getattr(pl, functionName)( arg )
    except:
       flag = False

    # all model should be saved in vtp format for review
    if flag:
        savePartVtp(obj, partName, mediaPath)
        if orderId != None:
            savePartStl(obj, orderId, mediaPath)

    return flag 

