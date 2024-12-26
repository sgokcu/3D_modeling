from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# Pencere boyutları
width, height = 800, 600

def init():
    glEnable(GL_DEPTH_TEST)
    glClearColor(0.5, 0.5, 0.5, 1)  # Arka plan rengi (nötr gri)

# Gradyan rengi hesaplayan fonksiyon
def gradient_color(start_color, end_color, factor):
    return [
        start_color[i] + (end_color[i] - start_color[i]) * factor
        for i in range(3)
    ]

# 3D oda çizimi
def draw_room():
    glBegin(GL_QUADS)

    # Zemin (gradyan: koyu gri - orta gri)
    for i in range(10):
        factor = i / 10.0
        glColor3fv(gradient_color([0.6, 0.3, 0.3], [0.5, 0.2, 0.2], factor))
        glVertex3f(-2 + i * 0.4, -1, -5)
        glVertex3f(-1.6 + i * 0.4, -1, -5)
        glVertex3f(-1.6 + i * 0.4, -1, -1)
        glVertex3f(-2 + i * 0.4, -1, -1)

    # Tavan (gradyan: koyu mavi - açık mavi)
    for i in range(10):
        factor = i / 10.0
        glColor3fv(gradient_color([0.8, 0.6, 0.6], [0.9, 0.7, 0.7], factor))
        glVertex3f(-2 + i * 0.4, 1, -5)
        glVertex3f(-1.6 + i * 0.4, 1, -5)
        glVertex3f(-1.6 + i * 0.4, 1, -1)
        glVertex3f(-2 + i * 0.4, 1, -1)

    glEnd()

# Küp çizimi
def draw_cube():
    glColor3f(1, 0, 0)  # Kırmızı renk
    glutSolidCube(0.5)

# Küre çizimi
def draw_sphere():
    glColor3f(0, 1, 0)  # Yeşil renk
    glutSolidSphere(0.3, 20, 20)

# Silindir çizimi
def draw_cylinder():
    glColor3f(0, 0, 1)  # Mavi renk
    quad = gluNewQuadric()
    gluCylinder(quad, 0.2, 0.2, 0.5, 32, 32)

# Üçgen Pramit çizimi
def draw_pyramid():
    glColor3f(1, 1, 0)  # Sarı renk
    glBegin(GL_TRIANGLES)
    
    # Ön yüz
    glVertex3f(0, 0.5, 0)
    glVertex3f(-0.5, -0.5, 0.5)
    glVertex3f(0.5, -0.5, 0.5)
    
    # Sağ yüz
    glVertex3f(0, 0.5, 0)
    glVertex3f(0.5, -0.5, 0.5)
    glVertex3f(0.5, -0.5, -0.5)
    
    # Sol yüz
    glVertex3f(0, 0.5, 0)
    glVertex3f(-0.5, -0.5, -0.5)
    glVertex3f(-0.5, -0.5, 0.5)
    
    # Arka yüz
    glVertex3f(0, 0.5, 0)
    glVertex3f(0.5, -0.5, -0.5)
    glVertex3f(-0.5, -0.5, -0.5)

    glEnd()

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    gluLookAt(0, 0, 2, 0, 0, -1, 0, 1, 0)

    draw_room()

    # Küp
    glPushMatrix()
    glTranslatef(-1, -0.5, -3)
    draw_cube()
    glPopMatrix() #

    # Küre
    glPushMatrix()
    glTranslatef(1, -0.5, -3)
    draw_sphere()
    glPopMatrix()

    # Silindir
    glPushMatrix()
    glTranslatef(0, -0.5, -4)
    glRotatef(-90, 1, 0, 0)
    draw_cylinder()
    glPopMatrix()

    # Üçgen Pramit
    glPushMatrix()
    glTranslatef(0, 0.5, -3)
    draw_pyramid()
    glPopMatrix()

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
    glutCreateWindow(b"3D Room with Gradient Colors and Shapes")
    init()
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutIdleFunc(display)
    glutMainLoop()

if __name__ == "__main__":
    main()
