import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import math

def Cylinder():
    radius = 1.0
    height = 2.0
    slices = 50

    # Alt yüzey
    glBegin(GL_TRIANGLE_FAN)
    glColor3f(1, 0, 0)  # Kırmızı
    glVertex3f(0, 0, -height / 2)
    for i in range(slices + 1):
        angle = 2 * math.pi * i / slices
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        glVertex3f(x, y, -height / 2)
    glEnd()

    # Üst yüzey
    glBegin(GL_TRIANGLE_FAN)
    glColor3f(0, 1, 0)  # Yeşil
    glVertex3f(0, 0, height / 2)
    for i in range(slices + 1):
        angle = 2 * math.pi * i / slices
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        glVertex3f(x, y, height / 2)
    glEnd()

    # Yan yüzeyler
    glBegin(GL_QUAD_STRIP)
    glColor3f(0, 0, 1)  # Mavi
    for i in range(slices + 1):
        angle = 2 * math.pi * i / slices
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        glVertex3f(x, y, -height / 2)
        glVertex3f(x, y, height / 2)
    glEnd()

def Pyramid():
    vertices = (
        (0, 1, 0),     # Tepe noktası
        (-1, -1, -1),  # Sol alt arka
        (1, -1, -1),   # Sağ alt arka
        (1, -1, 1),    # Sağ alt ön
        (-1, -1, 1),   # Sol alt ön
    )

    glBegin(GL_TRIANGLES)
    glColor3f(1, 0, 0)  # Kırmızı
    for i in range(1, 5):
        glVertex3fv(vertices[0])
        glVertex3fv(vertices[i])
        glVertex3fv(vertices[1 if i == 4 else i + 1])
    glEnd()

    glBegin(GL_QUADS)
    glColor3f(0, 1, 0)  # Yeşil
    for i in range(1, 5):
        glVertex3fv(vertices[i])
    glEnd()

def Cube():
    vertices = (
        (1, 1, -1),
        (1, -1, -1),
        (-1, -1, -1),
        (-1, 1, -1),
        (1, 1, 1),
        (1, -1, 1),
        (-1, -1, 1),
        (-1, 1, 1),
    )

    faces = (
        (0, 1, 2, 3),
        (4, 5, 6, 7),
        (0, 4, 7, 3),
        (1, 5, 6, 2),
        (0, 1, 5, 4),
        (3, 2, 6, 7),
    )

    glBegin(GL_QUADS)
    glColor3f(0, 0, 1)  # Mavi
    for face in faces:
        for vertex in face:
            glVertex3fv(vertices[vertex])
    glEnd()

def Sphere():
    sphere = gluNewQuadric()
    glColor3f(1, 1, 0)  # Sarı
    gluQuadricDrawStyle(sphere, GLU_FILL)
    gluSphere(sphere, 1, 32, 32)

def main():
    pygame.init()
    display = (1280, 720)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0, 0, -10)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # Küp
        glPushMatrix()
        glTranslatef(-4, 0, 0)
        Cube()
        glPopMatrix()

        # Silindir (Dik Konumda)
        glPushMatrix()
        glTranslatef(-1.5, 0, 0)
        glRotatef(90, 1, 0, 0)  # X ekseni etrafında 90 derece döndür
        Cylinder()
        glPopMatrix()

        # Piramit
        glPushMatrix()
        glTranslatef(1.5, 0, 0)
        Pyramid()
        glPopMatrix()

        # Küre
        glPushMatrix()
        glTranslatef(4, 0, 0)
        Sphere()
        glPopMatrix()

        pygame.display.flip()
        pygame.time.wait(10)

main()
