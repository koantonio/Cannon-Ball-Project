import math
import random
from OpenGL.GLUT import *
from OpenGL.GL import *
from Ball import *
from Vector import *

class Target:
    def __init__(self):
        self.center = Vector3d(0,10,-80);
        self.color = Vector3d(0.8,0.7,0.8);
        self.innerRadius = 1.0;
        self.outerRadius = 4;
        self.isMoving = False;
        self.deltaX = 0.02;
        self.bbx = None

    def Update(self,ballList):
        if self.isMoving is True:
            self.center.SetX( self.center.GetX() + self.deltaX );
        if( self.center.GetX() < self.bbx[0] ):
            self.center.SetX( self.bbx[0] )
            self.deltaX *=-1

        if( self.center.GetX() > self.bbx[1] ):
            self.center.SetX( self.bbx[1] )
            self.deltaX *=-1

        hit=False
        isLast = False
        for i in ballList:
            ballCenter=i.GetCenter()
            total1 = ballCenter.GetX() - self.center.GetX()
            total2 =  ballCenter.GetY() - self.center.GetY()
            total3 = ballCenter.GetZ() - self.center.GetZ()
            v = Vector3d(0,0,0)
            v.SetAll(total1,total2,total3)
            k = v.norm()
            if (k < self.outerRadius):
                 if( math.fabs(ballCenter.GetZ()-self.center.GetZ()) < 1.0 ):
                    hit = True
                    break

        if hit is True:
            self.isMoving = True
            self.color.SetX( random.random() )
            self.color.SetY( random.random() )
            self.color.SetZ( random.random() )
            self.deltaX *=1.05

    def Draw(self):
        glColor3f(self.color.GetX(),self.color.GetY(),self.color.GetZ())
        glPushMatrix();
        glTranslated(self.center.GetX(),self.center.GetY(),self.center.GetZ())
        #pygame.draw.circle(self.innerRadius,self.outerRadius,20,20)
        glutSolidTorus(self.innerRadius,self.outerRadius,20,20);
        glPopMatrix()
    def SetBBX(self,_bbx):
        self.bbx = _bbx
    def GetCenter(self):
        return self.center

