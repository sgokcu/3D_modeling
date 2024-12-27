from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# Window dimensions
width, height = 800, 600

def init():
    glEnable(GL_DEPTH_TEST)
    glClearColor(0.5, 0.5, 0.5, 1)

# Draw a simple 3D room

def draw_room():
    glBegin(GL_QUADS)

    # Floor
    glColor3f(0.7, 0.7, 0.7)
    glVertex3f(-2, -1, -5)
    glVertex3f(2, -1, -5)
    glVertex3f(2, -1, -1)
    glVertex3f(-2, -1, -1)

    # Ceiling
    glColor3f(0.9, 0.9, 0.9)
    glVertex3f(-2, 1, -5)
    glVertex3f(2, 1, -5)
    glVertex3f(2, 1, -1)
    glVertex3f(-2, 1, -1)

    # Back Wall
    glColor3f(0.5, 0.5, 0.9)
    glVertex3f(-2, -1, -5)
    glVertex3f(2, -1, -5)
    glVertex3f(2, 1, -5)
    glVertex3f(-2, 1, -5)

    # Left Wall
    glColor3f(0.9, 0.5, 0.5)
    glVertex3f(-2, -1, -5)
    glVertex3f(-2, -1, -1)
    glVertex3f(-2, 1, -1)
    glVertex3f(-2, 1, -5)

    # Right Wall
    glColor3f(0.5, 0.9, 0.5)
    glVertex3f(2, -1, -5)
    glVertex3f(2, -1, -1)
    glVertex3f(2, 1, -1)
    glVertex3f(2, 1, -5)

    glEnd()

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    gluLookAt(0, 0, 0, 0, 0, -1, 0, 1, 0)

    draw_room()

    glutSwapBuffers()

def reshape(w, h):
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, w / h, 1, 100)
    glMatrixMode(GL_MODELVIEW)

def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(width, height)
    glutCreateWindow(b"3D Room Perspective")
    init()
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutIdleFunc(display)
    glutMainLoop()

if __name__ == "__main__":
    main()