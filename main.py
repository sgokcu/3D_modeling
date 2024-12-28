from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from pygame.locals import *
from math import sin, cos
from shapes import *
from rotating import Rotation
from controls import Control

width, height = 800, 600

def init():
    glEnable(GL_DEPTH_TEST)
    glClearColor(0.5, 0.5, 0.5, 1.0)  # Arka plan rengi
    glEnable(GL_LIGHTING)  # Aydınlatmayı etkinleştir
    glEnable(GL_NORMALIZE)  # Normalleri normalize et
    glShadeModel(GL_SMOOTH)  # Düzgün gölgelendirme etkin
    glEnable(GL_COLOR_MATERIAL)  # Malzeme renklerini etkinleştir


def draw_shapes():
    glPushMatrix()
    glTranslatef(-1.2, -0.5, -2.5)
    glRotatef(Rotation.angle_cube, 1, 1, 0)
    set_material((1.0, 1.0, 0.9, 1), (1, 1, 1, 1), 50)
    draw_cube()
    glPopMatrix()

    glPushMatrix()
    glTranslatef(0.25, -0.5, -2.5)
    glRotatef(Rotation.angle_sphere, 0, 1, 0)
    set_material((0.5, 0.0, 0.5, 1), (1, 1, 1, 1), 50)
    draw_sphere()
    glPopMatrix()

    glPushMatrix()
    glTranslatef(-0.30, -0.5, -1.75)
    glRotatef(-90, 1, 0, 0)
    glRotatef(Rotation.angle_cylinder, 0, 0, 1)    
    set_material((0.7, 0.5, 1.0, 1), (1, 1, 1, 1), 50)
    draw_cylinder()
    glPopMatrix()

    glPushMatrix()
    glTranslatef(1.3, 0.3, -3.25)
    glScalef(0.8, 0.8, 0.8)
    glRotatef(Rotation.angle_pyramid, 0, 1, 1)
    set_material((0.5, 0.0, 0.5, 1), (1, 1, 1, 1), 50)
    draw_pyramid()
    glPopMatrix()

def draw_room():
    glBegin(GL_QUADS)

    for i in range(10):
        factor = i / 10.0
        glColor3fv(gradient_color([0.6, 0.3, 0.3], [0.5, 0.2, 0.2], factor))
        glVertex3f(-2 + i * 0.4, -1, -5)
        glVertex3f(-1.6 + i * 0.4, -1, -5)
        glVertex3f(-1.6 + i * 0.4, -1, -1)
        glVertex3f(-2 + i * 0.4, -1, -1)

    for i in range(10):
        factor = i / 10.0
        glColor3fv(gradient_color([0.6, 0.3, 0.3], [0.5, 0.2, 0.2], factor))
        glVertex3f(-2 + i * 0.4, 1, -5)
        glVertex3f(-1.6 + i * 0.4, 1, -5)
        glVertex3f(-1.6 + i * 0.4, 1, -1)
        glVertex3f(-2 + i * 0.4, 1, -1)

    for i in range(10):
        factor = i / 10.0
        glColor3fv(gradient_color([0.2, 0.1, 0.1], [0.0, 0.0, 0.0], factor))
        glVertex3f(-2 + i * 0.4, -1, -5)
        glVertex3f(-1.6 + i * 0.4, -1, -5)
        glVertex3f(-1.6 + i * 0.4, 1, -5)
        glVertex3f(-2 + i * 0.4, 1, -5)

    for i in range(10):
        factor = i / 10.0
        glColor3fv(gradient_color([0.2, 0.1, 0.1], [0.0, 0.0, 0.0], factor))
        glVertex3f(-2, -1 + i * 0.2, -5)
        glVertex3f(-2, -0.8 + i * 0.2, -5)
        glVertex3f(-2, -0.8 + i * 0.2, -1)
        glVertex3f(-2, -1 + i * 0.2, -1)

    for i in range(10):
        factor = i / 10.0
        glColor3fv(gradient_color([0.2, 0.1, 0.1], [0.0, 0.0, 0.0], factor))
        glVertex3f(2, -1 + i * 0.2, -5)
        glVertex3f(2, -0.8 + i * 0.2, -5)
        glVertex3f(2, -0.8 + i * 0.2, -1)
        glVertex3f(2, -1 + i * 0.2, -1)

    glEnd()

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    gluLookAt(
        Control.camera_x,
        Control.camera_y,
        Control.camera_z + Control.camera_distance,
        Control.camera_x + sin(Control.camera_y),
        Control.camera_y + sin(Control.camera_x),
        Control.camera_z - cos(Control.camera_y),
        0, 1, 0
    )
    Rotation.update()
    draw_room()
    # draw_shadow()
    draw_shapes()
    glutSwapBuffers()


# bu belki sorulur
def reshape(w, h):
    global width, height
    width, height = w, h
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, w/h, 1, 100)
    glMatrixMode(GL_MODELVIEW)


# bu kesin
def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(width, height)
    glutCreateWindow(b"3D room")
    init()

    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutKeyboardFunc(Control.keyboard)
    glutSpecialFunc(Control.special_keys)
    glutIdleFunc(display)
    glutMainLoop()

if __name__ == "__main__":
    main()
