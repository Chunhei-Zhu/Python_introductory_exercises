# =============================================================================
# This code follows the tutorials by Paul McWhorter (TopTechBoy.com).
# I wrote this to practice Python syntax and VPython 3D library.
# =============================================================================

from vpython import *
import numpy as np
import time

# =============================================================================
# Python 3D Graphics Tutorials (1-21)
# =============================================================================

def Python_3D_Graphics_Tutorial_1():
    try:
        floor = box(pos = vector(0,-5,0),color = color.white, length = 10,height = .1,width = 10)
        ceiling  = box(pos = vector(0,5,0),color = color.white, length = 10,height = .1,width = 10)
        while True:
           pass
    except: pass

def Python_3D_Graphics_Tutorial_2():
    try:
        floor = box(pos = vector(0,-5,0),color = color.white,size = vector(10,.1,10))
        ceiling  = box(pos = vector(0,5,0),color = color.white,size = vector(10,.1,10))
        backwall = box(pos = vector(0,0,-5),size = vector(10,10,.1),color = color.white)
        leftwall = box(pos = vector(-5,0,0),size = vector(.1,10,10),color = color.white)
        rightwall = box(pos = vector(5,0,0),size = vector(.1,10,10),color = color.white)
        marble = sphere(radius = .75,color = color.red)
        deltaX = .1
        xPos = 0
        while True:
           rate(50)
           xPos = xPos + deltaX
           if (xPos > 5 or xPos < -5):
               deltaX = deltaX*(-1)
           marble.pos = vector(xPos,0,0)
    except: pass

def Python_3D_Graphics_Tutorial_3():
    try:
        mRadius = .75
        wallThickness = .1
        roomWidth = 10
        roomDepth = 5
        roomHeight = 10
        floor = box(pos = vector(0,-roomHeight/2,0),color = color.white,size = vector(roomWidth,wallThickness,roomDepth))
        ceiling  = box(pos = vector(0,roomHeight/2.0,0),color = color.white,size = vector(roomWidth,wallThickness,roomDepth))
        backwall = box(pos = vector(0,0,-roomDepth/2),size = vector(roomWidth,roomHeight,wallThickness),color = color.white)
        leftwall = box(pos = vector(-roomWidth/2,0,0),size = vector(wallThickness,roomHeight,roomDepth),color = color.white)
        rightwall = box(pos = vector(roomWidth/2,0,0),size = vector(wallThickness,roomHeight,roomDepth),color = color.white)
        marble = sphere(radius = mRadius,color = color.red)
        deltaX = .1
        xPos = 0
        while True:
           rate(10)
           xPos = xPos + deltaX
           if (xPos > roomWidth/2 or xPos < -roomWidth/2):
               deltaX = deltaX*(-1)
           marble.pos = vector(xPos,0,0)
    except: pass

def Python_3D_Graphics_Tutorial_4():
    try:
        mRadius = 2
        wallThickness = 1
        roomWidth = 15
        roomDepth = 12
        roomHeight = 8
        floor = box(pos = vector(0,-roomHeight/2,0),color = color.white,size = vector(roomWidth,wallThickness,roomDepth))
        ceiling  = box(pos = vector(0,roomHeight/2.0,0),color = color.white,size = vector(roomWidth,wallThickness,roomDepth))
        backwall = box(pos = vector(0,0,-roomDepth/2),size = vector(roomWidth,roomHeight,wallThickness),color = color.white)
        leftwall = box(pos = vector(-roomWidth/2,0,0),size = vector(wallThickness,roomHeight,roomDepth),color = color.white)
        rightwall = box(pos = vector(roomWidth/2,0,0),size = vector(wallThickness,roomHeight,roomDepth),color = color.white)
        marble = sphere(radius = mRadius,color = color.red)
        deltaX = .1
        xPos = 0
        while True:
           rate(10)
           xPos = xPos + deltaX
           Xrme = xPos + mRadius
           Xlme = xPos - mRadius
           Rwe = roomWidth/2 - wallThickness/2
           Lwe =- roomWidth/2 + wallThickness/2
           if (Xrme >= Rwe or Xlme < Lwe):
               deltaX = deltaX*(-1)
           marble.pos = vector(xPos,0,0)
    except: pass

def Python_3D_Graphics_Tutorial_5():
    try:
        mRadius = .5
        wallThickness = .1
        roomWidth = 12
        roomDepth = 20
        roomHeight = 2
        floor = box(pos = vector(0,-roomHeight/2,0),color = color.white,size = vector(roomWidth,wallThickness,roomDepth))
        ceiling  = box(pos = vector(0,roomHeight/2.0,0),color = color.white,size = vector(roomWidth,wallThickness,roomDepth))
        backwall = box(pos = vector(0,0,-roomDepth/2),size = vector(roomWidth,roomHeight,wallThickness),color = color.white)
        leftwall = box(pos = vector(-roomWidth/2,0,0),size = vector(wallThickness,roomHeight,roomDepth),color = color.white)
        rightwall = box(pos = vector(roomWidth/2,0,0),size = vector(wallThickness,roomHeight,roomDepth),color = color.white)
        marble = sphere(radius = mRadius,color = color.red)
        deltaX = .1
        deltaY = .1
        deltaZ = .1
        xPos = 0
        yPos = 0
        zPos = 0
        while True:
           rate(25)
           xPos = xPos + deltaX
           yPos = yPos + deltaY
           zPos = zPos + deltaZ
           Xrme = xPos + mRadius
           Xlme = xPos - mRadius
           Ytme = yPos + mRadius
           Ybme = yPos - mRadius
           Zbme = zPos - mRadius
           Zfme = zPos + mRadius
           Rwe = roomWidth/2 - wallThickness/2
           Lwe = -roomWidth/2 + wallThickness/2
           Cwe = roomHeight/2 - wallThickness/2
           Floorwe = -roomHeight/2 + wallThickness/2
           Bwe = -roomDepth/2 + wallThickness/2
           Fwe = roomDepth/2 - wallThickness/2
           if (Xrme >= Rwe or Xlme <= Lwe):
               deltaX = deltaX*(-1)
           if (Ytme >= Cwe or Ybme <= Floorwe):
               deltaY = deltaY*(-1)
           if (Zfme >= Fwe or Zbme <= Bwe):
               deltaZ = deltaZ*(-1)
           marble.pos = vector(xPos,yPos,zPos)
    except: pass

def Python_3D_Graphics_Tutorial_6():
    try:
        Piston1 = sphere(radius = 1,color = color.red,opacity = .5)
        while True:
           for myRadius in np.linspace(.1,1,1000):
               rate(250)
               Piston1.radius = myRadius
           for myRadius in np.linspace(1,.1,1000):
               rate(250)
               Piston1.radius = myRadius
    except: pass

def Python_3D_Graphics_Tutorial_7():
    try:
        glassBulb = sphere(radius = 1.25,color = color.white,opacity = .5)
        glassCyl = cylinder(radius = .65,length = 6,color = color.white,opacity = .5)
        mercSphere = sphere(radius = 1,color = color.red)
        mercColumn = cylinder(radius = .45,length = 6,color = color.red)
        for tick in np.linspace(1,6,15):
           box(size = vector(.05,.5,.25),color = color.white,pos = vector(tick,0,.5))
        while True:
           for myTemp in np.linspace(1,6,100):
               rate(100)
               mercColumn.length = myTemp
           for myTemp in np.linspace(6,1,100):
               rate(100)
               mercColumn.length = myTemp
    except: pass

def Python_3D_Graphics_Tutorial_8():
    try:
        myCylOrange = cylinder(radius = 1,color = color.orange,length = 6)
        myCylCyan = cylinder(radius = 1, length = 6, color = color.cyan,pos = vector(0,3,0))
        myCylOrangeLength = 1
        myCylCyanLength = 1
        myCylOrangeDelta = .01
        myCylCyanDelta = .02
        while True:
           rate(50)
           myCylOrangeLength = myCylOrangeLength + myCylOrangeDelta
           myCylCyanLength = myCylCyanLength + myCylCyanDelta
           myCylOrange.length = myCylOrangeLength
           myCylCyan.length = myCylCyanLength
           if myCylOrangeLength >= 6 or myCylOrangeLength <= .1:
               myCylOrangeDelta = myCylOrangeDelta*(-1)
           if myCylCyanLength >= 6 or myCylCyanLength <= .1:
               myCylCyanDelta = myCylCyanDelta*(-1)
    except: pass

def Python_3D_Graphics_Tutorial_9():
    try:
        mySphere = sphere(radius = 1,color = vector(.7,0,1))
        while True:
           pass
    except: pass

def Python_3D_Graphics_Tutorial_10():
    try:
        myOrb = sphere(radius = 1,color = color.white)
        rChan = 0
        gChan = 0
        bChan = 0
        rInc = .001
        gInc = .002
        bInc = .015
        while True:
           rate(500)
           rChan = rChan + rInc
           gChan = gChan + gInc
           bChan = bChan + bInc
           myOrb.color = vector(rChan,gChan,bChan)
           if rChan >= 1 or rChan <= 0:
               rInc = rInc*(-1)
           if gChan >= 1 or gChan <= 0:
               gInc = gInc*(-1)
           if bChan >= 1 or bChan <= 0:
               bInc = bInc*(-1)
    except: pass

def Python_3D_Graphics_Tutorial_11():
    try:
        myOrb = sphere(radius = 1,color = vector(1,1,0))
        rChan = 1
        gChan = 1
        bChan = 0
        rInc = .001
        gInc = -.001
        bInc = .001
        while True:
           rate(100)
           rChan = rChan + rInc
           gChan = gChan + gInc
           bChan = bChan + bInc
           if rChan <= 1:
               rApply = rChan
           if rChan > 1:
               rApply = 1
           if gChan <= 1:
               gApply = gChan
           if gChan > 1:
               gApply = 1
           if bChan <= 1:
               bApply = bChan
           if bChan > 1:
               bApply = 1
           myOrb.color = vector(rApply,gApply,bApply)
           if rChan >= 1.5 or rChan <= 0:
               rInc = rInc*(-1)
           if gChan >= 1.5 or gChan <= 0:
               gInc = gInc*(-1)
           if bChan >= 1.5 or bChan <= 0:
               bInc = bInc*(-1)
           print(rApply + gApply + bApply)
    except: pass

def Python_3D_Graphics_Tutorial_12():
    try:
        arrowL = 2
        arrowT = .02
        pntT = .04
        theta = 0
        Xarrow = arrow(axis = vector(1,0,0),color = color.red,length = arrowL,shaftwidth = arrowT)
        Yarrow = arrow(axis = vector(0,1,0),color = color.green,length = arrowL,shaftwidth = arrowT)
        Zarrow = arrow(axis = vector(0,0,1),color = color.blue,length = arrowL,shaftwidth = arrowT)
        pntArrow = arrow(axis = vector(arrowL*np.cos(theta),arrowL*np.sin(theta),0),color = color.orange,length = arrowL,shaftwidth = pntT)
        while True:
           for myAngle in np.linspace(0,2*np.pi,1000):
               rate(50)
               pntArrow.axis = vector(arrowL*np.cos(myAngle),arrowL*np.sin(myAngle),0)
               pntArrow.length = arrowL
    except: pass

def Python_3D_Graphics_Tutorial_13():
    try:
        arrowL = 2
        arrowT = .02
        pntT = .04
        bRadius = .05
        Xarrow = arrow(axis = vector(1,0,0),color = color.red,length = arrowL,shaftwidth = arrowT)
        Yarrow = arrow(axis = vector(0,1,0),color = color.green,length = arrowL,shaftwidth = arrowT)
        Zarrow = arrow(axis = vector(0,0,1),color = color.blue,length = arrowL,shaftwidth = arrowT)
        Parrow = arrow(axis = vector(1,0,0),color = color.orange,length = arrowL,shaftwidth = pntT)
        myBall = sphere(make_trail = True,trail_color = color.cyan,radius = bRadius,color = color.red,pos = vector(arrowL,0,0))
        while True:
           for myAngle in np.linspace(0,2*np.pi,1000):
               rate(50)
               Parrow.axis = vector(arrowL*np.cos(myAngle),arrowL*np.sin(myAngle),0)
               Parrow.length = arrowL
               myBall.pos = vector(arrowL*np.cos(myAngle),arrowL*np.sin(myAngle),0)
           for myAngle in np.linspace(0,5*np.pi/2,1000):
               rate(50)
               Parrow.axis = vector(arrowL*np.cos(myAngle),0,arrowL*np.sin(myAngle))
               Parrow.length = arrowL
               myBall.pos = vector(arrowL*np.cos(myAngle),0,arrowL*np.sin(myAngle))
           for myAngle in np.linspace(0,2*np.pi,1000):
               rate(50)
               Parrow.axis = vector(0,arrowL*np.sin(myAngle),arrowL*np.cos(myAngle))
               Parrow.length = arrowL
               myBall.pos = vector(0,arrowL*np.sin(myAngle),arrowL*np.cos(myAngle))
           for myAngle in np.linspace(np.pi/2,2*np.pi/2,1000):
               rate(50)
               Parrow.axis = vector(0,arrowL*np.sin(myAngle),arrowL*np.cos(myAngle))
               Parrow.length = arrowL
               myBall.pos = vector(0,arrowL*np.sin(myAngle),arrowL*np.cos(myAngle))
    except: pass

def Python_3D_Graphics_Tutorial_14():
    try:
        clockR = 2
        clockT = clockR/10
        majorTickL = clockR/7
        majorTickT = 2*np.pi*clockR/400
        majorTickW = clockT*1.2
        manorTickL = clockR/12
        manorTickT = 2*np.pi*clockR/600
        manorTickW = clockT*1.2
        for theta in np.linspace(0,2*np.pi,13):
           majorTick = box(axis = vector(clockR*np.cos(theta),clockR*np.sin(theta),0),color = color.black,length = majorTickL,width = majorTickW,height = majorTickT,pos = vector((clockR-majorTickL/2)*np.cos(theta),(clockR-majorTickL/2)*np.sin(theta),0))
        for theta in np.linspace(0,2*np.pi,61):
           manorTick = box(axis = vector(clockR*np.cos(theta),clockR*np.sin(theta),0),color = color.black,length = manorTickL,width = manorTickW,height = manorTickT,pos = vector((clockR-manorTickL/2)*np.cos(theta),(clockR-manorTickL/2)*np.sin(theta),0))
        clockFace = cylinder(axis = vector(0,0,1),color = vector(0,1,.8),length = clockT,radius = clockR,pos = vector(0,0,-clockT/2))
        while True:
           pass
    except: pass

def Python_3D_Graphics_Tutorial_15():
    try:
        clockR = 2
        clockT = clockR/10
        majorTickL = clockR/7
        majorTickT = 2*np.pi*clockR/400
        majorTickW = clockT*1.2
        manorTickL = clockR/12
        manorTickT = 2*np.pi*clockR/600
        manorTickW = clockT*1.2
        minuteHandL = clockR-majorTickL
        minuteHandT = minuteHandL/25
        mniuteHandOffset = clockT/2 + minuteHandT
        hubRadius = clockT/2
        hourHandL = .75*minuteHandL
        hourHandT = minuteHandT*1.25
        hourHandOffset = clockT/2 + hourHandT
        hourRadius = clockT/2
        hourAngle = np.pi/2
        minuteAngle = np.pi/2
        minInc = .01
        hourInc = minInc/12
        for theta in np.linspace(0,2*np.pi,13):
           majorTick = box(axis = vector(clockR*np.cos(theta),clockR*np.sin(theta),0),color = color.black,length = majorTickL,width = majorTickW,height = majorTickT,pos = vector((clockR-majorTickL/2)*np.cos(theta),(clockR-majorTickL/2)*np.sin(theta),0))
        for theta in np.linspace(0,2*np.pi,61):
           manorTick = box(axis = vector(clockR*np.cos(theta),clockR*np.sin(theta),0),color = color.black,length = manorTickL,width = manorTickW,height = manorTickT,pos = vector((clockR-manorTickL/2)*np.cos(theta),(clockR-manorTickL/2)*np.sin(theta),0))
        clockFace = cylinder(axis = vector(0,0,1),color = vector(0,1,.8),length = clockT,radius = clockR,pos = vector(0,0,-clockT/2))
        minuteHand = arrow(axis = vector(1,0,0),color = color.red,shaftwidth = minuteHandT,length = minuteHandL,pos = vector(0,0,mniuteHandOffset))
        hourHand = arrow(axis = vector(0,1,0),color = color.red,shaftwidth = hourHandT,length = hourHandL,pos = vector(0,0,hourHandOffset))
        hub = cylinder(axis = vector(0,0,1),color = color.red,radius = hubRadius,length = 2*clockT)
        while True:
           rate(50)
           hourAngle = hourAngle - hourInc
           minuteAngle = minuteAngle - minInc
           hourHand.axis = vector(hourHandL*np.cos(hourAngle),hourHandL*np.sin(hourAngle),0)
           minuteHand.axis = vector(minuteHandL*np.cos(minuteAngle),minuteHandL*np.sin(minuteAngle),0)
    except: pass

def Python_3D_Graphics_Tutorial_16():
    try:
        clockR = 2
        clockT = clockR/10
        majorTickL = clockR/7
        majorTickT = 2*np.pi*clockR/400
        majorTickW = clockT*1.2
        manorTickL = clockR/12
        manorTickT = 2*np.pi*clockR/600
        manorTickW = clockT*1.2
        minuteHandL = clockR-majorTickL
        minuteHandT = minuteHandL/25
        mniuteHandOffset = clockT/2 + minuteHandT
        hubRadius = clockT/2
        hourHandL = .75*minuteHandL
        hourHandT = minuteHandT*1.25
        hourHandOffset = clockT/2 + hourHandT
        hourRadius = clockT/2
        hourAngle = np.pi/2
        minuteAngle = np.pi/2
        minInc = .0001
        hourInc = minInc/12
        secondHandL = clockR - majorTickL/2
        secondHandT = minuteHandL/50
        secondHandOffset = clockT*1.5 + minuteHandT
        secondAngle = np.pi/2
        secondInc = minInc*60
        for theta in np.linspace(0,2*np.pi,13):
           majorTick = box(axis = vector(clockR*np.cos(theta),clockR*np.sin(theta),0),color = color.black,length = majorTickL,width = majorTickW,height = majorTickT,pos = vector((clockR-majorTickL/2)*np.cos(theta),(clockR-majorTickL/2)*np.sin(theta),0))
        for theta in np.linspace(0,2*np.pi,61):
           manorTick = box(axis = vector(clockR*np.cos(theta),clockR*np.sin(theta),0),color = color.black,length = manorTickL,width = manorTickW,height = manorTickT,pos = vector((clockR-manorTickL/2)*np.cos(theta),(clockR-manorTickL/2)*np.sin(theta),0))
        clockFace = cylinder(axis = vector(0,0,1),color = vector(0,1,.8),length = clockT,radius = clockR,pos = vector(0,0,-clockT/2))
        minuteHand = arrow(axis = vector(0,1,0),color = color.red,shaftwidth = minuteHandT,length = minuteHandL,pos = vector(0,0,mniuteHandOffset))
        hourHand = arrow(axis = vector(0,1,0),color = color.red,shaftwidth = hourHandT,length = hourHandL,pos = vector(0,0,hourHandOffset))
        hub = cylinder(axis = vector(0,0,1),color = color.red,radius = hubRadius,length = 2*clockT)
        secondHand = arrow(axis = vector(0,1,0),color = color.red,shaftwidth = secondHandT,length = secondHandL,pos = vector(0,0,secondHandOffset))
        while True:
           rate(18)
           hourAngle = hourAngle - hourInc
           minuteAngle = minuteAngle - minInc
           secondAngle = secondAngle - secondInc
           hourHand.axis = vector(hourHandL*np.cos(hourAngle),hourHandL*np.sin(hourAngle),0)
           minuteHand.axis = vector(minuteHandL*np.cos(minuteAngle),minuteHandL*np.sin(minuteAngle),0)
           secondHand.axis = vector(secondHandL*np.cos(secondAngle),secondHandL*np.sin(secondAngle),0)
    except: pass

def Python_3D_Graphics_Tutorial_17():
    try:
        clockR = 2
        clockT = clockR/10
        majorTickL = clockR/7
        majorTickT = 2*np.pi*clockR/400
        majorTickW = clockT*1.2
        manorTickL = clockR/12
        manorTickT = 2*np.pi*clockR/600
        manorTickW = clockT*1.2
        minuteHandL = clockR-majorTickL
        minuteHandT = minuteHandL/25
        mniuteHandOffset = clockT/2 + minuteHandT
        hubRadius = clockT/2
        hourHandL = .75*minuteHandL
        hourHandT = minuteHandT*1.25
        hourHandOffset = clockT/2 + hourHandT
        hourRadius = clockT/2
        hourAngle = np.pi/2
        minuteAngle = np.pi/2
        minInc = .0001
        hourInc = minInc/12
        secondHandL = clockR - majorTickL/2
        secondHandT = minuteHandL/50
        secondHandOffset = clockT*1.5 + minuteHandT
        secondAngle = np.pi/2
        secondInc = minInc*60
        for theta in np.linspace(0,2*np.pi,13):
           majorTick = box(axis = vector(clockR*np.cos(theta),clockR*np.sin(theta),0),color = color.black,length = majorTickL,width = majorTickW,height = majorTickT,pos = vector((clockR-majorTickL/2)*np.cos(theta),(clockR-majorTickL/2)*np.sin(theta),0))
        for theta in np.linspace(0,2*np.pi,61):
           manorTick = box(axis = vector(clockR*np.cos(theta),clockR*np.sin(theta),0),color = color.black,length = manorTickL,width = manorTickW,height = manorTickT,pos = vector((clockR-manorTickL/2)*np.cos(theta),(clockR-manorTickL/2)*np.sin(theta),0))
        clockFace = cylinder(axis = vector(0,0,1),color = vector(0,1,.8),length = clockT,radius = clockR,pos = vector(0,0,-clockT/2))
        minuteHand = arrow(axis = vector(0,1,0),color = color.red,shaftwidth = minuteHandT,length = minuteHandL,pos = vector(0,0,mniuteHandOffset))
        hourHand = arrow(axis = vector(0,1,0),color = color.red,shaftwidth = hourHandT,length = hourHandL,pos = vector(0,0,hourHandOffset))
        hub = cylinder(axis = vector(0,0,1),color = color.red,radius = hubRadius,length = 2*clockT)
        secondHand = arrow(axis = vector(0,1,0),color = color.red,shaftwidth = secondHandT,length = secondHandL,pos = vector(0,0,secondHandOffset))
        while True:
           rate(5000)
           hour = time.localtime(time.time())[3]
           if hour>12:
               hour - hour-12
           minute = time.localtime(time.time())[4]
           second = time.localtime(time.time())[5]
           hourAngle = -(hour/12)*2*np.pi + np.pi/2
           minuteAngle = -(minute/60)*2*np.pi + np.pi/2
           secondAngle = -(second/60)*2*np.pi + np.pi/2
           # print(second)
           hourHand.axis = vector(hourHandL*np.cos(hourAngle),hourHandL*np.sin(hourAngle),0)
           minuteHand.axis = vector(minuteHandL*np.cos(minuteAngle),minuteHandL*np.sin(minuteAngle),0)
           secondHand.axis = vector(secondHandL*np.cos(secondAngle),secondHandL*np.sin(secondAngle),0)
    except: pass

def Python_3D_Graphics_Tutorial_18():
    try:
        clockR = 2
        clockT = clockR/10
        majorTickL = clockR/7
        majorTickT = 2*np.pi*clockR/400
        majorTickW = clockT*1.2
        manorTickL = clockR/12
        manorTickT = 2*np.pi*clockR/600
        manorTickW = clockT*1.2
        minuteHandL = clockR-majorTickL
        minuteHandT = minuteHandL/25
        mniuteHandOffset = clockT/2 + minuteHandT
        hubRadius = clockT/2
        hourHandL = .75*minuteHandL
        hourHandT = minuteHandT*1.25
        hourHandOffset = clockT/2 + hourHandT
        hourRadius = clockT/2
        hourAngle = np.pi/2
        minuteAngle = np.pi/2
        minInc = .0001
        hourInc = minInc/12
        secondHandL = clockR - majorTickL/2
        secondHandT = minuteHandL/50
        secondHandOffset = clockT*1.5 + minuteHandT
        secondAngle = np.pi/2
        secondInc = minInc*60

        for theta in np.linspace(0,2*np.pi,13):
            majorTick = box(axis = vector(clockR*np.cos(theta),clockR*np.sin(theta),0),
                            color = color.black,length = majorTickL,width = majorTickW,
                            height = majorTickT,pos = vector((clockR-majorTickL/2)*np.cos(theta),(clockR-majorTickL/2)*np.sin(theta),0))
        for theta in np.linspace(0,2*np.pi,61):
            manorTick = box(axis = vector(clockR*np.cos(theta),clockR*np.sin(theta),0),
                            color = color.black,length = manorTickL,width = manorTickW,height = manorTickT,
                            pos = vector((clockR-manorTickL/2)*np.cos(theta),(clockR-manorTickL/2)*np.sin(theta),0))
        clockFace = cylinder(axis = vector(0,0,1),color = vector(0,1,.8),length = clockT,radius = clockR,pos = vector(0,0,-clockT/2))
        minuteHand = arrow(axis = vector(0,1,0),color = color.red,shaftwidth = minuteHandT,
                          length = minuteHandL,pos = vector(0,0,mniuteHandOffset))
        hourHand = arrow(axis = vector(0,1,0),color = color.red,shaftwidth = hourHandT,
                        length = hourHandL,pos = vector(0,0,hourHandOffset))
        hub = cylinder(axis = vector(0,0,1),color = color.red,radius = hubRadius,length = 2*clockT)
        secondHand = arrow(axis = vector(0,1,0),color = color.red,shaftwidth = secondHandT,
                          length = secondHandL,pos = vector(0,0,secondHandOffset))
        while True:
            rate(5000)
            hour = time.localtime(time.time())[3]
            if hour>12:
                hour - hour-12
            minute = time.localtime(time.time())[4]
            second = time.localtime(time.time())[5]
            hourAngle = -((hour+minute/60)/12)*2*np.pi + np.pi/2
            minuteAngle = -((minute+second/60)/60)*2*np.pi + np.pi/2
            secondAngle = -(second/60)*2*np.pi + np.pi/2
            # print(second)
            hourHand.axis = vector(hourHandL*np.cos(hourAngle),hourHandL*np.sin(hourAngle),0)
            minuteHand.axis = vector(minuteHandL*np.cos(minuteAngle),minuteHandL*np.sin(minuteAngle),0)
            secondHand.axis = vector(secondHandL*np.cos(secondAngle),secondHandL*np.sin(secondAngle),0)
    except: pass

def Python_3D_Graphics_Tutorial_19():
    try:
        clockR = 2
        clockT = clockR/10
        majorTickL = clockR/7
        majorTickT = 2*np.pi*clockR/400
        majorTickW = clockT*1.2
        manorTickL = clockR/12
        manorTickT = 2*np.pi*clockR/600
        manorTickW = clockT*1.2
        minuteHandL = clockR-majorTickL
        minuteHandT = minuteHandL/25
        mniuteHandOffset = clockT/2 + minuteHandT
        hubRadius = clockT/2
        hourHandL = .75*minuteHandL
        hourHandT = minuteHandT*1.25
        hourHandOffset = clockT/2 + hourHandT
        hourRadius = clockT/2
        hourAngle = np.pi/2
        minuteAngle = np.pi/2
        minInc = .0001
        hourInc = minInc/12
        secondHandL = clockR - majorTickL/2
        secondHandT = minuteHandL/50
        secondHandOffset = clockT*1.5 + minuteHandT
        secondAngle = np.pi/2
        secondInc = minInc*60

        for theta in np.linspace(0,2*np.pi,13):
            majorTick = box(axis = vector(clockR*np.cos(theta),clockR*np.sin(theta),0),
                            color = color.black,length = majorTickL,width = majorTickW,
                            height = majorTickT,pos = vector((clockR-majorTickL/2)*np.cos(theta),(clockR-majorTickL/2)*np.sin(theta),0))
        for theta in np.linspace(0,2*np.pi,61):
            manorTick = box(axis = vector(clockR*np.cos(theta),clockR*np.sin(theta),0),
                            color = color.black,length = manorTickL,width = manorTickW,height = manorTickT,
                            pos = vector((clockR-manorTickL/2)*np.cos(theta),(clockR-manorTickL/2)*np.sin(theta),0))
        clockFace = cylinder(axis = vector(0,0,1),color = vector(0,1,.8),length = clockT,radius = clockR,pos = vector(0,0,-clockT/2))
        minuteHand = arrow(axis = vector(0,1,0),color = color.red,shaftwidth = minuteHandT,
                          length = minuteHandL,pos = vector(0,0,mniuteHandOffset))
        hourHand = arrow(axis = vector(0,1,0),color = color.red,shaftwidth = hourHandT,
                        length = hourHandL,pos = vector(0,0,hourHandOffset))
        hub = cylinder(axis = vector(0,0,1),color = color.red,radius = hubRadius,length = 2*clockT)
        secondHand = arrow(axis = vector(0,1,0),color = color.red,shaftwidth = secondHandT,
                          length = secondHandL,pos = vector(0,0,secondHandOffset))
        textH = clockR/4
        myLabel = text(text = 'Texas Time',align = 'center',color = color.orange,height = textH,pos = vector(0,1.1*clockR,-clockT/2),depth = clockT)
        while True:
            rate(5000)
            hour = time.localtime(time.time())[3]
            if hour>12:
                hour - hour-12
            minute = time.localtime(time.time())[4]
            second = time.localtime(time.time())[5]
            hourAngle = -((hour+minute/60)/12)*2*np.pi + np.pi/2
            minuteAngle = -((minute+second/60)/60)*2*np.pi + np.pi/2
            secondAngle = -(second/60)*2*np.pi + np.pi/2
            # print(second)
            hourHand.axis = vector(hourHandL*np.cos(hourAngle),hourHandL*np.sin(hourAngle),0)
            minuteHand.axis = vector(minuteHandL*np.cos(minuteAngle),minuteHandL*np.sin(minuteAngle),0)
            secondHand.axis = vector(secondHandL*np.cos(secondAngle),secondHandL*np.sin(secondAngle),0)
    except: pass

def Python_3D_Graphics_Tutorial_20():
    try:
        clockR = 2
        clockT = clockR/10
        majorTickL = clockR/7
        majorTickT = 2*np.pi*clockR/400
        majorTickW = clockT*1.2
        manorTickL = clockR/12
        manorTickT = 2*np.pi*clockR/600
        manorTickW = clockT*1.2
        minuteHandL = clockR - majorTickL
        minuteHandT = minuteHandL/25
        mniuteHandOffset = clockT/2 + minuteHandT
        hubRadius = clockT/2
        hourHandL = .75*minuteHandL
        hourHandT = minuteHandT*1.25
        hourHandOffset = clockT/2 + hourHandT
        hourRadius = clockT/2
        hourAngle = np.pi/2
        minuteAngle = np.pi/2
        minInc = .0001
        hourInc = minInc/12
        secondHandL = clockR - majorTickL/2
        secondHandT = minuteHandL/50
        secondHandOffset = clockT*1.5 + minuteHandT
        secondAngle = np.pi/2
        secondInc = minInc*60
        
        for theta in np.linspace(0,2*np.pi,13):
           majorTick = box(axis = vector(clockR*np.cos(theta),clockR*np.sin(theta),0),
                           color = color.black,length = majorTickL,width = majorTickW,
                           height = majorTickT,pos = vector((clockR-majorTickL/2)*np.cos(theta),(clockR-majorTickL/2)*np.sin(theta),0))
        for theta in np.linspace(0,2*np.pi,61):
           manorTick = box(axis = vector(clockR*np.cos(theta),clockR*np.sin(theta),0),
                           color = color.black,length = manorTickL,width = manorTickW,height = manorTickT,
                           pos = vector((clockR-manorTickL/2)*np.cos(theta),(clockR-manorTickL/2)*np.sin(theta),0))
        clockFace = cylinder(axis = vector(0,0,1),color = vector(0,1,.8),length = clockT,radius = clockR,pos = vector(0,0,-clockT/2))
        minuteHand = arrow(axis = vector(0,1,0),color = color.red,shaftwidth = minuteHandT,
                           length = minuteHandL,pos = vector(0,0,mniuteHandOffset))
        hourHand = arrow(axis = vector(0,1,0),color = color.red,shaftwidth = hourHandT,
                         length = hourHandL,pos = vector(0,0,hourHandOffset))
        hub = cylinder(axis = vector(0,0,1),color = color.red,radius = hubRadius,length = 2*clockT)
        secondHand = arrow(axis = vector(0,1,0),color = color.red,shaftwidth = secondHandT,
                           length = secondHandL,pos = vector(0,0,secondHandOffset))
        textH = clockR/4
        myLabel = text(text = 'Texas Time',align = 'center',color = color.orange,height = textH,
                       pos = vector(0,1.1*clockR,-clockT/2),depth = clockT)
        Angle = np.pi/2
        AngleInc = -2*np.pi/12
        Angle = Angle + AngleInc
        numH = clockR/6
        for i in range(1,13,1):
           clockNum = text(align = 'center',text = str(i),
                           pos = vector(clockR*.75*np.cos(Angle),clockR*.75*np.sin(Angle) - numH/2,0),
                           height = numH,depth = clockT,color = color.orange)
           Angle = Angle + AngleInc
        while True:
           rate(5000)
           hour = time.localtime(time.time())[3]
           if hour>12:
               hour - hour-12
           minute = time.localtime(time.time())[4]
           second = time.localtime(time.time())[5]
           hourAngle = -((hour+minute/60)/12)*2*np.pi + np.pi/2
           minuteAngle = -((minute+second/60)/60)*2*np.pi + np.pi/2
           secondAngle = -(second/60)*2*np.pi + np.pi/2
           hourHand.axis = vector(hourHandL*np.cos(hourAngle),hourHandL*np.sin(hourAngle),0)
           minuteHand.axis = vector(minuteHandL*np.cos(minuteAngle),minuteHandL*np.sin(minuteAngle),0)
           secondHand.axis = vector(secondHandL*np.cos(secondAngle),secondHandL*np.sin(secondAngle),0)
    except: pass

def Python_3D_Graphics_Tutorial_21():
    try:
        mRadius = .5
        wallThickness = .1
        roomWidth = 12
        roomDepth = 20
        roomHeight = 15
        floor = box(pos = vector(0,-roomHeight/2,0),color = color.white,size = vector(roomWidth,wallThickness,roomDepth))
        ceiling  = box(pos = vector(0,roomHeight/2.0,0),color = color.white,size = vector(roomWidth,wallThickness,roomDepth))
        backwall = box(pos = vector(0,0,-roomDepth/2),size = vector(roomWidth,roomHeight,wallThickness),color = color.white)
        leftwall = box(pos = vector(-roomWidth/2,0,0),size = vector(wallThickness,roomHeight,roomDepth),color = color.white)
        rightwall = box(pos = vector(roomWidth/2,0,0),size = vector(wallThickness,roomHeight,roomDepth),color = color.white)
        marble = sphere(radius = mRadius,color = color.red)
        deltaX = .1
        deltaY = .1
        deltaZ = .1

        xPos = 0
        yPos = 0
        zPos = 0

        run = 0
        mySpeed = 1

        def ballColorRed(x):
           marble.color = color.red
        button(bind = ballColorRed,text = 'Red',color = color.black,background = color.red)
        def ballColorGreen(x):
           marble.color = color.green
        button(bind = ballColorGreen,text = 'Green',color = color.black,background = color.green)
        def ballColorBlue(x):
           marble.color = color.blue
        button(bind = ballColorBlue,text = 'Blue',color = color.black,background = color.blue)
        scene.append_to_caption('\n\n')

        def runRadio(x):
           print(x.checked)
           global run 
           if x.checked == True:
               run = 1
           if x.checked == False:
               run = 0
        radio(bind = runRadio, text = 'Run')
        scene.append_to_caption('\n\n')

        def bigBall(x):
           global mRadius
           if x.checked == True:
               mRadius = mRadius*2
               marble.radius = mRadius
           if x.checked == False:
               mRadius = mRadius/2
               marble.radius = mRadius
        checkbox(bind = bigBall,text = 'Big Ball')
        scene.append_to_caption('\n\n')
        wtext(text = 'Choose Ball Speed')
        scene.append_to_caption('\n\n')
        def speed(x):
           global mySpeed
           if x.selected == '1':
               mySpeed = 1
           if x.selected == '2':
               mySpeed = 2
           if x.selected == '3':
               mySpeed = 3
           if x.selected == '4':
               mySpeed = 4
           if x.selected == '5':
               mySpeed = 5
        menu(bind = speed,choices = ['1','2','3','4','5'])
        scene.append_to_caption('\n\n')
        wtext(text = 'Choose Ball Opacity')
        scene.append_to_caption('\n\n')
        
        def ballOpacity(x):
           op = x.value
           marble.opacity = op
        slider(bind = ballOpacity,vertical = False,min = 0,max = 1,value = 1)

        while True:
          rate(25)
          xPos = xPos + deltaX*run*mySpeed
          yPos = yPos + deltaY*run*mySpeed
          zPos = zPos + deltaZ*run*mySpeed

          Xrme = xPos + mRadius
          Xlme = xPos - mRadius
          Ytme = yPos + mRadius
          Ybme = yPos - mRadius
          Zbme = zPos - mRadius
          Zfme = zPos + mRadius
          Rwe = roomWidth/2 - wallThickness/2
          Lwe = -roomWidth/2 + wallThickness/2
          Cwe = roomHeight/2 - wallThickness/2
          Floorwe = -roomHeight/2 + wallThickness/2
          Bwe = -roomDepth/2 + wallThickness/2
          Fwe = roomDepth/2 - wallThickness/2
          if (Xrme >= Rwe or Xlme <= Lwe):
              deltaX = deltaX*(-1)
          if (Ytme >= Cwe or Ybme <= Floorwe):
              deltaY = deltaY*(-1)
          if (Zfme >= Fwe or Zbme <= Bwe):
              deltaZ = deltaZ*(-1)
          marble.pos = vector(xPos,yPos,zPos)
    except: pass

def Python_3D_Graphics_Tutorial_Homework():
    try:
        clockR = 2
        clockT = clockR/10
        majorTickL = clockR/7
        majorTickT = 2*np.pi*clockR/400
        majorTickW = clockT*1.2
        manorTickL = clockR/12
        manorTickT = 2*np.pi*clockR/600
        manorTickW = clockT*1.2
        minuteHandL = clockR-majorTickL
        minuteHandT = minuteHandL/25
        mniuteHandOffset = clockT/2 + minuteHandT
        hubRadius = clockT/2
        hourHandL = .75*minuteHandL
        hourHandT = minuteHandT*1.25
        hourHandOffset = clockT/2 + hourHandT
        hourRadius = clockT/2
        hourAngle = np.pi/2
        minuteAngle = np.pi/2
        minInc = .0001
        hourInc = minInc/12
        secondHandL = clockR - majorTickL/2
        secondHandT = minuteHandL/50
        secondHandOffset = clockT*1.5 + minuteHandT
        secondAngle = np.pi/2
        secondInc = minInc*60

        cityt = {
            'UTC': 0,
            'New York': -4,
            'London': 0,
            'Berlin': 1,
            'Beijing': 8,
            'Tokyo': 9,
            'Sydney': 10
        }
        bcolor = {
            'white':color.white,
            'black':color.black,
            'blue':color.blue,
            'cyan':color.cyan,
            'green':color.green
        }

        currentcity = 'UTC'
        currentoffset = cityt[currentcity]

        for theta in np.linspace(0,2*np.pi,13):
            majorTick = box(axis = vector(clockR*np.cos(theta),clockR*np.sin(theta),0),
                            color = color.black,length = majorTickL,width = majorTickW,
                            height = majorTickT,pos = vector((clockR-majorTickL/2)*np.cos(theta),(clockR-majorTickL/2)*np.sin(theta),0))
        for theta in np.linspace(0,2*np.pi,61):
            manorTick = box(axis = vector(clockR*np.cos(theta),clockR*np.sin(theta),0),
                            color = color.black,length = manorTickL,width = manorTickW,height = manorTickT,
                            pos = vector((clockR-manorTickL/2)*np.cos(theta),(clockR-manorTickL/2)*np.sin(theta),0))
        clockFace = cylinder(axis = vector(0,0,1),color = vector(0,1,.8),length = clockT,radius = clockR,pos = vector(0,0,-clockT/2))
        minuteHand = arrow(axis = vector(0,1,0),color = color.red,shaftwidth = minuteHandT,
                          length = minuteHandL,pos = vector(0,0,mniuteHandOffset))
        hourHand = arrow(axis = vector(0,1,0),color = color.red,shaftwidth = hourHandT,
                        length = hourHandL,pos = vector(0,0,hourHandOffset))
        hub = cylinder(axis = vector(0,0,1),color = color.red,radius = hubRadius,length = 2*clockT)
        secondHand = arrow(axis = vector(0,1,0),color = color.red,shaftwidth = secondHandT,
                          length = secondHandL,pos = vector(0,0,secondHandOffset))
        myLabel = label(text=f'{currentcity} Time', pos=vector(0,1.3*clockR,0), height=16, box=False, color=color.orange)
        Angle = np.pi/2
        AngleInc = -2*np.pi/12
        Angle = Angle + AngleInc
        numH = clockR/6

        def pickcity(x):
            nonlocal currentcity, currentoffset
            currentcity = x.selected
            currentoffset = cityt[currentcity]
            myLabel.text = f'{currentcity} Time'
            
        def backcolor(x):
            clockFace.color = bcolor[x.selected]
            
        scene.append_to_caption('\n\n')
        wtext(text = 'Choose Font size')
        scene.append_to_caption('\n\n')
        
        def setFontSize(x):
            nonlocal numH
            if x.selected == 'small':
                numH = clockR/9
            elif x.selected == 'medium':
                numH = clockR/6
            elif x.selected == 'large':
                numH = clockR/3
            for i, t in enumerate(clockNums):
                t.height = numH
                
        clockNums = []
        menu(bind = setFontSize,choices = ['small','medium','large'])
        
        scene.append_to_caption('\n\n')
        wtext(text = "Select City Timezone")
        scene.append_to_caption('\n\n')
        menu(bind = pickcity, choices = list(cityt.keys()))
        scene.append_to_caption('\n\n')
        wtext(text = "Select Clock Face Color")
        scene.append_to_caption('\n\n')
        menu(bind = backcolor, choices = list(bcolor.keys()))
        
        myLabel.text = f'{currentcity} Time'
        for i in range(1,13,1):
            clockNum = text(align='center', text=str(i),
                            pos=vector(clockR*.75*np.cos(Angle), clockR*.75*np.sin(Angle) - numH/2, 0),
                            height=numH, depth=clockT, color=color.orange)
            clockNums.append(clockNum)
            Angle = Angle + AngleInc
            
        while True:
            rate(50)
            utc_ts = time.time()
            citytm = time.gmtime(utc_ts + currentoffset*3600)
            hour   = citytm.tm_hour % 12 
            minute = citytm.tm_min
            second = citytm.tm_sec
            hourAngle   = -((hour+minute/60)/12)*2*np.pi + np.pi/2
            minuteAngle = -((minute+second/60)/60)*2*np.pi + np.pi/2
            secondAngle = -(second/60)*2*np.pi + np.pi/2
            hourHand.axis   = vector(hourHandL*np.cos(hourAngle),   hourHandL*np.sin(hourAngle),   0)
            minuteHand.axis = vector(minuteHandL*np.cos(minuteAngle), minuteHandL*np.sin(minuteAngle), 0)
            secondHand.axis = vector(secondHandL*np.cos(secondAngle), secondHandL*np.sin(secondAngle), 0)
    except Exception as e:
        print("Error in 3D Homework:", e)

