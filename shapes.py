from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# bu fonk sorulur
def set_material(diffuse, specular, shininess):
    glMaterialfv(GL_FRONT, GL_AMBIENT_AND_DIFFUSE, diffuse)
    glMaterialfv(GL_FRONT, GL_SPECULAR, specular)
    glMaterialf(GL_FRONT, GL_SHININESS, shininess)

def gradient_color(start_color, end_color, factor):
    return [
        start_color[i] + (end_color[i] - start_color[i]) * factor
        for i in range(3)
    ]
def draw_cube():
    set_material((0.8, 0.6, 0.9, 1.0), (0.9, 0.7, 1.0, 1.0), 128)
    for i in range(20):
        factor = i / 20.0
        glColor3fv(gradient_color([0.7, 0.5, 0.8], [0.8, 0.6, 0.9], factor))
        glutSolidCube(0.5)


def draw_sphere():
    set_material((0.9, 0.3, 0.6, 1.0), (1.0, 0.5, 0.8, 1.0), 128)
    for i in range(20):
        factor = i / 20.0
        glColor3fv(gradient_color([0.8, 0.2, 0.5], [0.9, 0.3, 0.6], factor))
        glutSolidSphere(0.3, 64, 64)


def draw_cylinder():
    set_material((0.6, 0.8, 1.0, 0.4), (0.9, 1.0, 1.0, 0.6), 64)  # Şeffaf cam efekti için malzeme
    quad = gluNewQuadric()
    for i in range(20):
        factor = i / 20.0
        glColor4f(0.6 + factor * 0.2, 0.8 + factor * 0.1, 1.0, 0.2 + factor * 0.1)
        gluCylinder(quad, 0.2, 0.2, 0.5, 64, 64)

def draw_pyramid():
    set_material((0.9, 0.7, 0.4, 1.0), (1.0, 1.0, 0.8, 1.0), 128)  # Parlak yüzey ve ışık yansıtıcı malzeme özellikleri
    glBegin(GL_TRIANGLES)

    glColor3fv([0.9, 0.6, 0.3])  # Ön yüz rengi
    glVertex3f(0, 0.5, 0)
    glVertex3f(-0.5, -0.5, 0.5)
    glVertex3f(0.5, -0.5, 0.5)

    glColor3fv([0.8, 0.5, 0.3])  # Sağ yüz rengi
    glVertex3f(0, 0.5, 0)
    glVertex3f(0.5, -0.5, 0.5)
    glVertex3f(0.5, -0.5, -0.5)

    glColor3fv([0.8, 0.4, 0.2])  # Sol yüz rengi
    glVertex3f(0, 0.5, 0)
    glVertex3f(-0.5, -0.5, -0.5)
    glVertex3f(-0.5, -0.5, 0.5)

    glColor3fv([0.7, 0.4, 0.2])  # Arka yüz rengi
    glVertex3f(0, 0.5, 0)
    glVertex3f(0.5, -0.5, -0.5)
    glVertex3f(-0.5, -0.5, -0.5)

    glEnd()