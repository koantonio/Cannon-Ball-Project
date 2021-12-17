import math
import sys
from Basic import *

class Vector3d():
    def __init__(self,_x, _y, _z):
        self.x = _x
        self.y = _y
        self.z = _z

    def operator(self, _x, _y, _z):
        self.x = _x
        self.y = _y
        self.z = _z
        return self

    def operator_d(self, _d):
        self.x = _d.GetX()
        self.y = _d.GetY()
        self.z = _d.GetZ()
        return self

    def GetX(self):
        return self.x
    def GetY(self):
        return self.y
    def GetZ(self):
        return self.z
    def SetX(self, d):
        self.x = d
    def SetY(self, d):
         self.y = d
    def SetZ(self, d):
        self.z = d

    def SetAll(self, d1, d2, d3):
        self.x = d1
        self.y = d2
        self.z = d3

    def print_vect(self):
        print(self.x, self.y, self.z)

    def reset(self):
        self.x = 0
        self.y = 0
        self.z = 0

    def op(self, **kwargs): #experiment
        self.x = kwargs.get('a')
        self.y = kwargs.get('b')
        self.z = kwargs.get('c')


    def bol(self, a):
        if (self.x == a.GetX() and self.y == a.GetY() and self.z == a.GetZ()):
            return True
        else:
            return False

    #add another vector
    def sadd(self,a):
        self.x += a.GetX()
        self.y += a.GetY()
        self.z += a.GetZ()
        return self

    #substract another vector from this vector
    def ssub(self, a):
         self.x -= a.GetX()
         self.y -= a.GetY()
         self.z -= a.GetZ()
         return self

    #scalar multiplication
    def smul(self, _d):
        self.x *= _d
        self.y *= _d
        self.z *= _d
        return self

    #scalar division
    def sdiv(self, _d):
        self.x /= _d
        self.y /= _d
        self.z /= _d
        return self

     #component multiplication
    def scom(self, a):
        self.x *= a.GetX()
        self.y *= a.GetY()
        self.z *= a.GetZ()
        return self

    #self cross product
    def scp(self, a):
        v0 = self.x
        v1 = self.y
        v2 = self.z
        self.x = v1 * a.GetZ() - v2 * a.GetY()
        self.y = v2 * a.GetX() - v0 * a.GetZ()
        self.z = v0 * a.GetY() - v1 * a.GetX()
        return self

    def neg(self):
        return Vector3d(-self.x, -self.y, -self.z)


    def add(self, a):
        return Vector3d(self.x + a.GetX(), self.y + a.GetY(), self.z + a.GetZ())
    def sub(self,a):
        return Vector3d(self.x - a.GetX(), self.y - a.GetY(), self.z - a.GetZ())
    def mul(self,_d):
        return Vector3d(self.x * _d, self.y * _d, self.z * _d)
    def div(self,_d):
        return Vector3d(self.x / _d, self.y / _d, self.z / _d)
    #component *
    def com(self, a):
        return Vector3d(self.x * a.GetX(), self.y * a.GetY(), self.z * a.GetZ())

    #Cross Product
    def cp(self, _v):
        a = Vector3d(self.x,self.y,self.z)
        return a.scp(_v)

    def dot(self,a):
        return self.x*a.GetX() + self.y*a.GetY() + self.z*a.GetZ()

    def normsqr(self):
        return self.x ** 2 + self.y ** 2 + self.z ** 2



    def norm(self):
        return math.sqrt(self.normsqr())


    def normalize(self):
        n = self.norm()
        if (n < sys.float_info.epsilon):
            return Vector3d(0,0,0)
        self.x = self.x/n
        self.y = self.y/n
        self.z = self.z/n
        return self


    def snormalize(self):
        n = self.norm()
        if (n < sys.float_info.epsilon):
            return self.reset()
        self.x = self.x/n
        self.y = self.y/n
        self.z = self.z/n
        return self


    def comp(self,a):
        a.normalize()
        self.x *= a.GetX()
        self.y *= a.GetY()
        self.z *= a.GetZ()
        return self
    def scale(self,_1):
        n = self.norm()
        if (n < sys.float_info.epsilon):
            return Vector3d(0,0,0)
        self.x *= (_1/n)
        self.y *= (_1/n)
        self.z *= (_1/n)
        return self

    def sscale(self,_1):
        n = self.norm()
        if (n < sys.float_info.epsilon):
            return self.reset()
        self.x *= (_1/n)
        self.y *= (_1/n)
        self.z *= (_1/n)
        return self


    def rotateX(self,_rad):
        c = math.cos(_rad)
        s = math.sin(_rad)
        return self.operator(self.x, self.y*c - self.z*s, self.y*s + self.z*c)

    def rotateXd(self, _deg):
        return self.rotateX(degToRad(_deg))

    def rotateY(self, _rad):
        c = math.cos(_rad)
        s = math.sin(_rad)
        return self.operator(self.x*c + self.z*s, self.y, -self.x*s + self.z*c)

    def rotateYd(self, _deg):
        return self.rotateY(degToRad(_deg))

    def rotateZ(self, _rad):
        c = math.cos(_rad)
        s = math.sin(_rad)
        return self.operator(self.x*c - self.y*s, self.x*s + self.y*c, self.z)

    def rotateZd(self, _deg):
        return self.rotateZ(degToRad(_deg))
