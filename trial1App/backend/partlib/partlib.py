import cadquery as cq
from math import sin, cos, pi, floor
import math

def box(arg):

    length = arg[0]     # Length of the block, in x
    width  = arg[1]     # width of the block, in y
    height = arg[2]     # Height of the block, in z
   
    obj = (
           cq.Workplane("XY")
           .box(length, width, height)
          )

    return obj

def sphere(arg):

    radius = arg[0]

    obj = (
           cq.Workplane("XY")
           .sphere(radius)
          )

    return obj

def plateWithHole(arg):

    length = arg[0]
    height = arg[1]
    thickness = arg[2]
    center_hole_dia = arg[3]
    
    # Create a box and add a center hole
    obj = (
        cq.Workplane("XY")
        .box(length, height, thickness)
        .faces(">Z")
        .workplane()
        .hole(center_hole_dia)
    )

    return obj

def tee(arg):

    diameter = arg[0]
    length = arg[1]

    obj = (
        cq.Workplane("front")
        .circle(diameter)
        .extrude(length)
        .copyWorkplane(
            cq.Workplane("right", origin=(-length/2.0, 0, 0))
        )
        .circle(diameter)
        .extrude(length)
    )

    return obj

def boxWithFillet(arg):
  
    length = arg[0]
    width  = arg[1]
    height = arg[2]
    filletRadius = arg[3] 

    obj = (
        cq.Workplane("XY")
        .box(length, width, height)
        .edges("|Z")
        .fillet(filletRadius)
    )

    return obj
  
def bearingPillowBlock(arg):

    length     = arg[0]
    height     = arg[1]
    bearingDia = arg[2]
    thickness  = arg[3]
    padding    = arg[4]

    obj = (
        cq.Workplane("XY")
        .box(length, height, thickness)
        .faces(">Z")
        .workplane()
        .hole(bearingDia)
        .faces(">Z")
        .workplane()
        .rect(length - padding, height - padding, forConstruction=True)
        .vertices()
        .cboreHole(2.4, 4.4, 2.1)
    )

    return obj

# define the generating function
def hypocycloid(t, r1, r2):
    return (
        (r1 - r2) * cos(t) + r2 * cos(r1 / r2 * t - t),
        (r1 - r2) * sin(t) + r2 * sin(-(r1 / r2 * t - t)),
    )


def epicycloid(t, r1, r2):
    return (
        (r1 + r2) * cos(t) - r2 * cos(r1 / r2 * t + t),
        (r1 + r2) * sin(t) - r2 * sin(r1 / r2 * t + t),
    )


def gear(t, r1=4, r2=1):
    if (-1) ** (1 + floor(t / 2 / pi * (r1 / r2))) < 0:
        return epicycloid(t, r1, r2)
    else:
        return hypocycloid(t, r1, r2)

def cycloidalGear(arg): 

    length = arg[0]
    para1  = arg[1]
    para2  = arg[2]
    para3  = arg[3]
    angle  = arg[4] 
 
    # create the gear profile and extrude it
    obj = (
        cq.Workplane("XY")
        .parametricCurve(lambda t: gear(t * para1 * pi, para2, para3))
        .twistExtrude(length, angle)
        .faces(">Z")
        .workplane()
        .circle(2)
        .cutThruAll()
    )
    
    return obj

def lego(arg):

    #####
    # Inputs
    ######
    lbumps = int(arg[0])  # number of bumps long
    wbumps = int(arg[1])  # number of bumps wide
    thin = True  # True for thin, False for thick
    
    #
    # Lego Brick Constants-- these make a Lego brick a Lego :)
    #
    pitch = 8.0
    clearance = 0.1
    bumpDiam = 4.8
    bumpHeight = 1.8
    if thin:
        height = 3.2
    else:
        height = 9.6
    
    t = (pitch - (2 * clearance) - bumpDiam) / 2.0
    postDiam = pitch - t  # works out to 6.5
    total_length = lbumps * pitch - 2.0 * clearance
    total_width = wbumps * pitch - 2.0 * clearance
    
    # make the base
    s = cq.Workplane("XY").box(total_length, total_width, height)
    
    # shell inwards not outwards
    s = s.faces("<Z").shell(-1.0 * t)
    
    # make the bumps on the top
    s = (
        s.faces(">Z")
        .workplane()
        .rarray(pitch, pitch, lbumps, wbumps, True)
        .circle(bumpDiam / 2.0)
        .extrude(bumpHeight)
    )
    
    # add posts on the bottom. posts are different diameter depending on geometry
    # solid studs for 1 bump, tubes for multiple, none for 1x1
    tmp = s.faces("<Z").workplane(invert=True)
    
    if lbumps > 1 and wbumps > 1:
        tmp = (
            tmp.rarray(pitch, pitch, lbumps - 1, wbumps - 1, center=True)
            .circle(postDiam / 2.0)
            .circle(bumpDiam / 2.0)
            .extrude(height - t)
        )
    elif lbumps > 1:
        tmp = (
            tmp.rarray(pitch, pitch, lbumps - 1, 1, center=True)
            .circle(t)
            .extrude(height - t)
        )
    elif wbumps > 1:
        tmp = (
            tmp.rarray(pitch, pitch, 1, wbumps - 1, center=True)
            .circle(t)
            .extrude(height - t)
        )
    else:
        tmp = s

    return tmp

def gearbox(arg):

    # Diameter of the circle at which a gear meets it's neighbor gear
    # Use this to space out your gears correctly
    def pitchCircle(mod, toothCount): return mod*toothCount
    
    # Length of an arc between the same point on neighboring teeth
    def circularPitch(mod): return mod*math.pi
    
    # Outer circle of a gear
    def addendumCircle(pitchCircle, mod): return pitchCircle+(2*mod)
    
    # Radius difference from pitch circle to the base of each tooth
    # 1.25 typically used such that the root is 25% depper than the meshing gear's tooth tops
    # for tooth clearance
    def dedendum(mod): return 1.25*mod
    
    # Diameter of a circle intersecting with the base of each tooth
    def rootCircle(pitchCircle, dedendum): return pitchCircle-(2*dedendum)
    
    # Height of each tooth
    def wholeDepth(mod, dedendum): return mod+dedendum
    
    # Lowest point at which a mating tooth should reach towards our root
    def clearanceCircle(pitchCircle, mod): return pitchCircle-(2*mod)
    
    # The circle that we draw our involute curves from
    def baseCircle(pitchCircle, pressureAngle): return pitchCircle*math.cos(math.radians(pressureAngle))
    
    def angleBetweenTeeth(toothCount): return 360/toothCount
    def herringbone (helix=20): return [-helix, -helix, -helix, -helix, 0, helix, helix, helix, helix]
    def circumferencePerTooth(c1rcle, teeth): return (math.pi*c1rcle)/teeth
    
    def angle(p1, p2, p3):
        a = distanceBetweenTwo2dPoints(p1, p2)
        b = distanceBetweenTwo2dPoints(p2, p3)
        c = distanceBetweenTwo2dPoints(p3, p1)
    
        return math.degrees(math.acos((a**2 + b**2 - c**2)/(2*a*b)))
    
    # TODO pull from utility library?
    def distanceBetweenTwo2dPoints(p1, p2): return math.sqrt(((p2[0]-p1[0])**2)+((p2[1]-p1[1])**2))
    
    # As degrees
    def toothWidthAtBaseCircle(baseCircleRadius, pitchCircleRadius, toothCount, backlashDegrees):
        p1     = involuteAtRadius(baseCircleRadius, pitchCircleRadius, -1, 0)
        p2     = involuteAtRadius(baseCircleRadius, pitchCircleRadius, 1, 0)
        mangle = angle(p1, [0,0], p2)
    
        return mangle+(angleBetweenTeeth(toothCount)/2)-backlashDegrees
    
    
    def rotateVect(v, a): 
        newVect = []
        for i in v:
            newVect.append([(i[0]*cos(a))-(i[1]*sin(a)),
                            (i[0]*sin(a))+(i[1]*cos(a))])
    
        return newVect;
    
    def involuteX(baseCircleRadius, t, off): 
        return baseCircleRadius*(math.cos(math.radians(t))+(math.radians(t-off)*math.sin(math.radians(t))))
    
    def involuteY(baseCircleRadius, t, off): 
        return baseCircleRadius*(math.sin(math.radians(t))-(math.radians(t-off)*math.cos(math.radians(t))))
    
    def involuteAtRadius(baseCircleRadius, targetRadius, direction=1, off=0):
      t = math.degrees(math.sqrt(((targetRadius/baseCircleRadius)**2)-1))
    
      return [involuteX(baseCircleRadius,(t*direction)+off,off),
              involuteY(baseCircleRadius,(t*direction)+off,off)]
    
    def helixTrack(height, teeth, gearModule, helixAngle):
        zMove = height
        circumferenceToTravel = math.tan(math.radians(-helixAngle))*zMove
        gearCircumference = (pitchCircle(gearModule, teeth)*math.pi)
        circumferenceMMPerDegree = 360/gearCircumference
    
        return circumferenceMMPerDegree*circumferenceToTravel
    
    def gearProfile(
            profile,
            teeth=10,
            mod=1,
            pressureAngle=20,
            gearRes=4,
            backlash=0.1,
            addendumOffset=0,
            dedendumOffset=0):
    
        mpitchCircle       = pitchCircle(mod, teeth)
        addendumCircleR    = (addendumCircle(mpitchCircle, mod)/2)+addendumOffset
        mdedendum          = dedendum(mod)+dedendumOffset
        rootCircleR        = rootCircle(mpitchCircle, mdedendum)/2
        baseCircleR        = baseCircle(mpitchCircle, pressureAngle)/2
        mangleBetweenTeeth = angleBetweenTeeth(teeth)
    
        backlashDegrees = 360*(backlash/(mpitchCircle*math.pi))
        htwabc = (toothWidthAtBaseCircle(baseCircleR, mpitchCircle/2, teeth, backlashDegrees)/2)
    
        leadingPoints=1
        trailingPoints=1
    
        invStartRadius = baseCircleR if (baseCircleR > rootCircleR) else rootCircleR;
        vertexCount = ((gearRes+1)*2)+leadingPoints+trailingPoints
    
        step = ((addendumCircleR)-invStartRadius)/gearRes
    
        profile = profile.moveTo(math.cos(math.radians(-htwabc))*rootCircleR,math.sin(math.radians(-htwabc))*rootCircleR)
    
        for i in range(teeth):
            a = mangleBetweenTeeth*i
            for j in range(leadingPoints):
                if (i > 0):
                    profile = profile.lineTo(math.cos(math.radians(-htwabc+a))*rootCircleR,
                                             math.sin(math.radians(-htwabc+a))*rootCircleR)
    
    
            xy = involuteAtRadius(baseCircleR, (invStartRadius), 1, -htwabc+a)
            profile = profile.lineTo(xy[0],xy[1])
    
            splinePts = []
            for j in range(gearRes+1):
                xy = involuteAtRadius(baseCircleR, (invStartRadius)+(step*j), 1, -htwabc+a)
                splinePts.append(xy)
    
            profile = profile.spline(splinePts, includeCurrent=False)
    
            xy = involuteAtRadius(baseCircleR, addendumCircleR, -1, htwabc+a)
            profile = profile.lineTo(xy[0],xy[1])
    
            splinePts = []
            for j in range(1,gearRes+1):
                xy = involuteAtRadius(baseCircleR, (addendumCircleR)-(step*j), -1, htwabc+a)
                splinePts.append(xy)
            profile = profile.spline(splinePts, includeCurrent=True)
            for j in range(trailingPoints):
                profile = profile.lineTo(math.cos(math.radians(htwabc+a))*rootCircleR, math.sin(math.radians(htwabc+a))*rootCircleR) 
    
        profile = profile.close()
    
        return profile
   
    para1 = arg[0]
    para2 = arg[1]
 
    points = cq.Workplane("XY")
    gearProfile(profile=points);
    
    p1 = cq.Workplane("XY",origin=(0,0,0)).polyline(([0,0,0],[0,0,para2]))
    p2 = cq.Workplane("XY",origin=(0,para1,0)).polyline(([0,0,0],[para1,0,para1],[0,0,para2]))
    
    p = points.wire().sweep(p1, auxSpine=p2)

    return p 

