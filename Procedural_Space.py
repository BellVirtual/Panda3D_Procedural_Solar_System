from math import pi, sin, cos
from direct.showbase.ShowBase import ShowBase
from panda3d.core import NodePath, TextNode
from direct.gui.DirectGui import *
import random
from direct.task import Task
from direct.interval.IntervalGlobal import Sequence
from panda3d.core import Point3
#from Planets import generate




base = ShowBase()
class World(object):
    def __init__(self):
        base.disableMouse()
        # This is the initialization we had before
        self.title = OnscreenText(  # Create the title
            text="Procedural System",
            parent=base.a2dBottomRight, align=TextNode.A_right,
            style=1, fg=(1, 1, 1, 1), pos=(-0.1, 0.1), scale=.07)

        #base.setBackgroundColor(0, 0, 0)  # Set the background to black
        #base.disableMouse()  # disable mouse control of the camera
        #camera.setPos(0, 0, 45)  # Set the camera position (X, Y, Z)
        #camera.setHpr(0, -90, 0)  # Set the camera orientation



        self.sizescale = 0.6


        self.loadPlanets()

    def loadPlanets(self):

        ########SKYBOX######
        self.sky = loader.loadModel("models/solar_sky_sphere")
        self.sky.reparentTo(render)
        self.sky.setScale(40)
        self.sky_tex = loader.loadTexture("adada/stars.jpg")
        self.sky.setTexture(self.sky_tex, 1)




        #####SUN#######
        self.sun = loader.loadModel("models/planet_sphere")
        self.sun.reparentTo(render)
        self.sun_tex = loader.loadTexture("adada/suntex.jpg")
        self.sun.setTexture(self.sun_tex, 1)
        self.sun.setScale(3 * self.sizescale)

        base.taskMgr.add(self.spinCameraTask, "SpinCameraTask")



        #####Planet Generator######
        for p in range(30):
            pxpos = random.randint(-15, 15)
            pypos = random.randint(-15, 15)
            pzpos = random.randint(-15, 15)
            lck = random.randint(1, 4)
            pscale = 0
            if lck == 1:
                tex = "waterworld.jpg"
                pscale = -.5
            if lck == 2:
                tex = "gasgiant.jpg"
                pscale = .5
            if lck == 3:
                tex = "rockytex.jpg"
            if lck == 4:
                tex = "sandworld.jpg"
                pscale -.4

            self.planet = loader.loadModel("models/planet_sphere")
            self.planet.reparentTo(render)
            self.planet_tex = loader.loadTexture("adada/"+tex)
            self.planet.setTexture(self.planet_tex, 1)
            self.planet.setScale((1 + pscale) * self.sizescale)
            self.planet.setPos(pxpos, pypos, pzpos)

    def spinCameraTask(self, task):
        angleDegrees = task.time * 6.0
        angleRadians = angleDegrees * (pi / 180.0)
        base.camera.setPos(20 * sin(angleRadians), -20 * cos(angleRadians), 3)
        base.camera.setHpr(angleDegrees, 0, 0)
        return Task.cont

# instantiate the class
w = World()
#if grid([-1][-1]) != " ":
base.run()