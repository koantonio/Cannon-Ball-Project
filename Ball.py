from Vector import *
from OpenGL.GL import *
from OpenGL.GLUT import *
import random

global damping
damping = 0.95
global collisionDamping
collisionDamping = 0.3

class Ball:
    def __init__(self):
        self.center = Vector3d(0,0,0)
        self.velocity = Vector3d(0,0,0)
        self.accel = Vector3d(0,0,0)
        self.color = Vector3d(0.3,0.2,0.8)

    def SetValues(self, _radius, _center, _vel, _accel,  _bbx):
        self.radius = _radius
        self.center = _center
        self.velocity = _vel
        self.accel = _accel
        self.bbx = _bbx
    def SetRandomColor(self):
        self.color.SetX(random.random())
        self.color.SetY(random.random())
        self.color.SetZ(random.random())
    def IsMoving(self):
        vel = self.velocity.norm()
        if( vel < 0.2 ):
            return True
        else:
            return False

    def Update(self, dt):
        self.center.operator_d(self.center.sadd(self.velocity.smul(dt)))
        oldVelocity = self.velocity
        self.velocity.operator_d(self.center.sadd(self.accel.smul(dt)))
        oldAccelY = self.accel.GetY()
        oldAccelY -= 9.8
        self.accel.SetY(oldAccelY)
#        self.accel *= damping
        self.accel.smul(damping)

        self.ResolveCollision()
        if(self.accel.norm() < 0.5 ):
            self.accel.SetAll(0,0,0)
        if(self.velocity.norm() < 0.5):
            self.velocity.SetAll(0,0,0)


    def ResolveCollision(self):
        if(self.center.GetX()-self.radius < self.bbx[0]):
            oldCenterX = self.center.GetX()
            self.center.SetX(self.bbx[0]+self.radius)
            self.velocity.SetX( -1*self.velocity.GetX() )
            self.velocity.smul(collisionDamping)
            self.accel.smul(collisionDamping)

        if( self.center.GetX()+self.radius > self.bbx[1] ):
            oldCenterX = self.center.GetX()
            self.center.SetX(self.bbx[1]-self.radius)
            self.velocity.SetX( -1*self.velocity.GetX() )
            self.velocity.smul(collisionDamping)
            self.accel.smul(collisionDamping)

        if( self.center.GetY()-self.radius < self.bbx[2] ):
            oldCenterY = self.center.GetY()
            self.center.SetY(self.bbx[2]+self.radius)
            self.velocity.SetY( -1*self.velocity.GetY() )
            self.velocity.smul(collisionDamping)
            self.accel.smul(collisionDamping)

        if( self.center.GetY()+self.radius > self.bbx[3] ):
            oldCenterY = self.center.GetY()
            self.center.SetY(self.bbx[3]-self.radius)
            self.velocity.SetY( -1*self.velocity.GetY() )
            self.velocity.smul(collisionDamping)
            self.accel.smul(collisionDamping)

        if( self.center.GetZ()-self.radius < self.bbx[4] ):
            oldCenterZ = self.center.GetZ()
            self.center.SetZ(self.bbx[4]+self.radius)
            self.velocity.SetZ( -1*self.velocity.GetZ() )
            self.velocity.smul(collisionDamping)
            self.accel.smul(collisionDamping)

        if( self.center.GetZ()+self.radius > self.bbx[5] ):
            oldCenterZ = self.center.GetZ()
            self.center.SetZ(self.bbx[5]-self.radius)
            self.velocity.SetZ( -1*self.velocity.GetZ() )
            self.velocity.smul(collisionDamping)
            self.accel.smul(collisionDamping)

    def GetCenter(self):
        return self.center

    def Draw(self):
        glColor3f(self.color.GetX(),self.color.GetY(),self.color.GetZ())
        glPushMatrix();
        glTranslated(self.center.GetX(),self.center.GetY(),self.center.GetZ())
        glutSolidSphere(self.radius,10,10);
        glPopMatrix();
