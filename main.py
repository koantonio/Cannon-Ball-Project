from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from Ball import *
from Vector import *
from Target import *
import sys

global red,blue,green, dt, yPlane, head, ball, target, cannon, curRadius, minRadius, maxRadius, maxAccel, cannonL, maxcannonL, mincannonL, angel1, angel2, bbx
red=float(1.0)
blue=float(1.0)
green=float(1.0)

dt = float(0.065)
yPlane = float(-4)

#singular ball
ball = Ball()
#list of mult balls
allBalls = []
# a singular target
target = Target()
# cannon position
cannon = Vector3d(0,0,0)
# ball radius
curRadius = float(0.6);
minRadius = float(0.2);
maxRadius = float(1.4);
# maximum acceleration
maxAccel = float(850);
# cannon length
cannonL = float(0.5);
maxCannonL = float(1.5);
minCannonL = float(0.25);
# angle1 for rotating cannon
angle1 = float(45.0);
angle2 = float(165.0);


bbx= [-20,20,-4,20,-100,100]


def init():
    mat_specular = [ 1.0, 1.0, 1.0, 0.0 ]
    mat_shininess = [ 10.0 ]
    light_position = [ 1.0, 1.0, 1.0, 0.0 ]
    light_ambient = [ 0.8, 0.8, 0.8, 1.0 ]
    light_diffuse = [ 1.0, 1.0, 1.0, 1.0 ]
    light_specular = [ 0.8, 0.8, 0.8, 1.0 ]
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glShadeModel (GL_SMOOTH);

    glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, mat_specular);
    glMaterialfv(GL_FRONT_AND_BACK, GL_SHININESS, mat_shininess);


    glLightfv(GL_LIGHT0, GL_AMBIENT, light_ambient);
    glLightfv(GL_LIGHT0, GL_DIFFUSE, light_diffuse);
    glLightfv(GL_LIGHT0, GL_SPECULAR, light_specular);
    glLightfv(GL_LIGHT0, GL_POSITION, light_position);

    glEnable(GL_LIGHTING);
    glEnable(GL_LIGHT0);
    glEnable(GL_DEPTH_TEST);

def changeSize(w, h):
    if (h == 0):
        h = 1;
    ratio =  float(w * 1.0 / h)

    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    glViewport(0, 0, w, h);


    gluPerspective(float(45.0), ratio, float(0.1), float(1000.0));

    glMatrixMode(GL_MODELVIEW);

def drawBBX():
    glShadeModel (GL_SMOOTH);
    glNormal3d(1,0,0);
    glColor3f(1,0,0);
    glBegin(GL_QUADS); #left side
    glVertex3d(bbx[0],bbx[2],bbx[4]);
    glVertex3d(bbx[0],bbx[3],bbx[4]);
    glVertex3d(bbx[0],bbx[3],bbx[5]);
    glVertex3d(bbx[0],bbx[2],bbx[5]);
    glEnd();

    glNormal3d(-1,0,0);
    glColor3f(0,0,1);
    glBegin(GL_QUADS); #right side
    glVertex3d(bbx[1],bbx[2],bbx[4]);
    glVertex3d(bbx[1],bbx[3],bbx[4]);
    glVertex3d(bbx[1],bbx[3],bbx[5]);
    glVertex3d(bbx[1],bbx[2],bbx[5]);
    glEnd();

    glNormal3d(0,1,0);
    glColor3f(0.8,0.8,0.8);
    glBegin(GL_QUADS); #bottom side
    glVertex3d(bbx[0],bbx[2],bbx[4]);
    glVertex3d(bbx[0],bbx[2],bbx[5]);
    glVertex3d(bbx[1],bbx[2],bbx[5]);
    glVertex3d(bbx[1],bbx[2],bbx[4]);
    glEnd();

    glNormal3d(0,-1,0);
    glColor3f(0.0,0.8,0.2);
    glBegin(GL_QUADS); #top side
    glVertex3d(bbx[0],bbx[3],bbx[4]);
    glVertex3d(bbx[0],bbx[3],bbx[5]);
    glVertex3d(bbx[1],bbx[3],bbx[5]);
    glVertex3d(bbx[1],bbx[3],bbx[4]);
    glEnd();

  #back
    glNormal3d(0,0,-1);
    glColor3f(0.0,0.8,0.8);
    glBegin(GL_QUADS); #back side
    glVertex3d(bbx[0],bbx[2],bbx[4]);
    glVertex3d(bbx[0],bbx[3],bbx[4]);
    glVertex3d(bbx[1],bbx[3],bbx[4]);
    glVertex3d(bbx[1],bbx[2],bbx[4]);
    glEnd();
  #front
    glNormal3d(0,0,1);
    glColor3f(0.0,0.8,0.8);
    glBegin(GL_QUADS); #front side
    glVertex3d(bbx[0],bbx[2],bbx[5]);
    glVertex3d(bbx[0],bbx[3],bbx[5]);
    glVertex3d(bbx[1],bbx[3],bbx[5]);
    glVertex3d(bbx[1],bbx[2],bbx[5]);
    glEnd();

def getCannonEndPts(ang1, cX, cY):
  cX = cannon.GetX()+cannonL * cosd(ang1);
  cY = cannon.GetY()+cannonL * sind(ang1);

def getCannonEndPts3D(ang1, ang2, cX, cY, cZ):
    cY = cannon.GetY()+ (cannonL * sind(ang1));
    l2 = cannonL * cosd(ang1);
    cX = cannon.GetX()+ (cannonL * sind(ang2));
    cZ = cannon.GetZ()+ (cannonL * cosd(ang2));
    return [cX,cY,cZ]

def DrawAllBalls():
  [i.Draw() for i in allBalls]

def UpdateAllBalls():
  for i in allBalls:
      i.Update(dt)
      print(i.GetCenter().GetX(), i.GetCenter().GetY(), i.GetCenter().GetZ())

def AddBall(_r, stPt, vel, accelVec):
  a = Ball()
  a.SetValues(curRadius,stPt,vel,accelVec,bbx)
  a.SetRandomColor()
  allBalls.append(a)


def renderScene():
    glEnable(GL_DEPTH_TEST);

	# Clear Color and Depth Buffers
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
    glClearColor(0.5, 0.5, 0.5, 1.0);           # background is gray

	# Reset transformations
    glLoadIdentity();

	#Set the camera
    gluLookAt(float(0.0), float(0.0), float(10.0),
			float(0.0), float(0.0),  float(0.0),
			float(0.0), float(1.0),  float(0.0));

    # Enable lighting
    glEnable(GL_LIGHTING);
    glEnable(GL_LIGHT0);
    glEnable(GL_COLOR_MATERIAL);

    # draw bbx
    drawBBX();

	#draw yPlane
    glLineWidth(2);
    glBegin(GL_LINES);  #draw the yPlane
    glVertex3f(float(-4.0),yPlane, float(0.0));
    glVertex3f(float(4.0),yPlane, float(0.0));
    glEnd();


    DrawAllBalls();
    target.Draw();

    cX=0;
    cY=0;
    cZ=0
    myList=getCannonEndPts3D(angle1, angle2,cX, cY, cZ)
    glColor3f(0,0,1);
    glLineWidth(2);
    glBegin(GL_LINES);
    glVertex3f(cannon.GetX(), cannon.GetY(), cannon.GetZ());
    glVertex3f(myList[0], myList[1], myList[2]);
    glEnd();


    UpdateAllBalls()

    target.Update(allBalls);

    glutSwapBuffers();


def processNormalKeys(bkey, x, y):
	global cannonL
	global curRadius

	key = bkey.decode("utf-8")
	if (key=='q'):  #quit
		sys.exit();
	elif(key=='s'):  #shoot
		cX=0
		cY=0
		cZ=0
		myList=getCannonEndPts3D(angle1,angle2,cX,cY,cZ);
		accel = maxAccel * (cannonL/maxCannonL)
		stPt = Vector3d(myList[0],myList[1]+curRadius,myList[2]);
		vel = Vector3d(0,0,0)
		accelVec = Vector3d(myList[0]-cannon.GetX(),myList[1]-cannon.GetY(),myList[2]-cannon.GetZ());
		accelVec.snormalize();
		accelVec.sscale(accel);
		AddBall(curRadius,stPt,vel,accelVec)

	elif(key=='1'):
	  cannonL -= 0.02;
	  if(cannonL<minCannonL):cannonL = minCannonL
	elif(key=='2'):
	  cannonL += 0.02;
	  if(cannonL>maxCannonL):cannonL = maxCannonL;
	elif(key=='9'):
	  curRadius -= 0.2;
	  if(curRadius<minRadius):curRadius = minRadius;
	elif(key=='0'):
	  curRadius += 0.2;
	  if(curRadius>maxRadius):curRadius = maxRadius;
	else: print("unknown key")

def processSpecialKeys(key,x,y):
   global angle1
   global angle2
   if (key == GLUT_KEY_UP):
       angle1 += 1
       if (angle1 >=100):
           angle1 = 100
   elif (key == GLUT_KEY_DOWN):
       angle1 -= 1;
       if (angle1 <= 0): angle1 = 0
   elif (key == GLUT_KEY_LEFT):
       angle2 += 1;
       if (angle2 >= 270): angle2 = 270
   elif (key == GLUT_KEY_RIGHT ):
       angle2 -= 1;
       if (angle2 <= 90): angle2 = 90


    #cannon.SetAll(-4,yPlane,0);
cannon = Vector3d(0,yPlane,0)
	#set the target bbx
target.SetBBX(bbx);

# init GLUT and create window
glutInit();
glutInitDisplayMode(GLUT_DEPTH | GLUT_DOUBLE | GLUT_RGBA);
glutInitWindowPosition(100,100);
glutInitWindowSize(1000,700);
glutCreateWindow("ShootPts");

init();
#	#register callbacks
glutDisplayFunc(renderScene)
glutReshapeFunc(changeSize);
glutIdleFunc(renderScene);

# here are the new entries
glutKeyboardFunc(processNormalKeys);
glutSpecialFunc(processSpecialKeys);

# enter GLUT event processing cycle
glutMainLoop();

