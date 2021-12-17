import math
import sys

global PI
PI = 3.1415926535897
global TWOPI
TWOPI = 6.2831853071794

def myRand():
	return math.rand() / sys.maxsize.__rand__()

def sqr(a):
    return a ** 2
def sign(x):
    if (x >= 0):
        return 1
    else:
        return -1

def degToRad(x):
    return (x*PI)/180
def radToDeg(x):
    return (x*180)/PI

def sind(x):
    return math.sin(degToRad(x))

def cosd(x):
    return math.cos(degToRad(x))

def tand(x):
    return math.tan(degToRad(x))

def asind(x):
    return radToDeg(math.asin(x))

def acosd(x):
    return radToDeg(math.acos(x))

def atand(x):
    return radToDeg(math.atan(x))

def atan2d(x,y):
    return radToDeg(math.atan2(x,y))