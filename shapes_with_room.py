from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# Pencere boyutları
width, height = 800, 600

def init():
    glEnable(GL_DEPTH_TEST)
    glClearColor(0.5, 0.5, 0.5, 1)  # Arka plan rengi (nötr gri)
    
    # --- Antialiasing (pürüzsüzleştirme) için eklenen ayarlar ---
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    glEnable(GL_LINE_SMOOTH)
    glEnable(GL_POLYGON_SMOOTH)
    glHint(GL_LINE_SMOOTH_HINT, GL_NICEST)
    glHint(GL_POLYGON_SMOOTH_HINT, GL_NICEST)
    glEnable(GL_MULTISAMPLE)  # Çoklu örnekleme ile daha yumuşak kenarlar

# Gradyan rengi hesaplayan fonksiyon
def gradient_color(start_color, end_color, factor):
    return [
        start_color[i] + (end_color[i] - start_color[i]) * factor
        for i in range(3)
    ]

def draw_cube():
    # Pastel sarıdan daha açık sarıya gradyan
    for i in range(20):
        factor = i / 20.0
        glColor3fv(gradient_color([0.4, 0.4, 0.6], [0.3, 0.2, 0.4], factor))  # Pastel sarıdan açık sarıya geçiş
        glutSolidCube(0.5)

def draw_sphere():
    # Mor tonları gradyanı
    for i in range(20):
        factor = i / 20.0
        glColor3fv(gradient_color([0.5, 0.0, 0.5], [0.8, 0.2, 0.8], factor))  # Mordan pembeye geçiş
        # --- Küre segment/slice sayısı artırıldı (20,20 -> 64,64) ---
        glutSolidSphere(0.3, 64, 64)

def draw_cylinder():
    # Lila tonları gradyanı
    quad = gluNewQuadric()
    for i in range(20):
        factor = i / 20.0
        glColor3fv(gradient_color([0.7, 0.5, 1.0], [0.9, 0.7, 1.0], factor))  # Liladan açık lilaya geçiş
        gluCylinder(quad, 0.2, 0.2, 0.5, 64, 64)

def draw_pyramid():
    # Cam göbeği tonları
    glBegin(GL_TRIANGLES)
    
    # Ön yüz
    for i in range(20):
        factor = i / 20.0
        glColor3fv(gradient_color([0.7, 0.3, 0.4], [0.5, 0.2, 0.2], factor))
        glVertex3f(0, 0.5, 0)
        glVertex3f(-0.5, -0.5, 0.5)
        glVertex3f(0.5, -0.5, 0.5)
    
    # Sağ yüz
    for i in range(20):
        factor = i / 20.0
        glColor3fv(gradient_color([0.7, 0.3, 0.4], [0.5, 0.2, 0.2], factor))
        glVertex3f(0, 0.5, 0)
        glVertex3f(0.5, -0.5, 0.5)
        glVertex3f(0.5, -0.5, -0.5)
    
    # Sol yüz
    for i in range(20):
        factor = i / 20.0
        glColor3fv(gradient_color([0.7, 0.3, 0.4], [0.5, 0.2, 0.2], factor))
        glVertex3f(0, 0.5, 0)
        glVertex3f(-0.5, -0.5, -0.5)
        glVertex3f(-0.5, -0.5, 0.5)
    
    # Arka yüz
    for i in range(20):
        factor = i / 20.0
        glColor3fv(gradient_color([0.7, 0.3, 0.4], [0.5, 0.2, 0.2], factor))
        glVertex3f(0, 0.5, 0)
        glVertex3f(0.5, -0.5, -0.5)
        glVertex3f(-0.5, -0.5, -0.5)

    glEnd()

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

    # Arka duvar (gradyan: açık mavi - daha açık mavi)
    for i in range(10):
        factor = i / 10.0
        glColor3fv(gradient_color([0.8, 0.6, 0.6], [0.9, 0.7, 0.7], factor))
        glVertex3f(-2 + i * 0.4, -1, -5)
        glVertex3f(-1.6 + i * 0.4, -1, -5)
        glVertex3f(-1.6 + i * 0.4, 1, -5)
        glVertex3f(-2 + i * 0.4, 1, -5)

    # Sol duvar (gradyan: koyu mavi - açık mavi)
    for i in range(10):
        factor = i / 10.0
        glColor3fv(gradient_color([0.8, 0.6, 0.6], [0.9, 0.7, 0.7], factor))
        glVertex3f(-2, -1 + i * 0.2, -5)
        glVertex3f(-2, -0.8 + i * 0.2, -5)
        glVertex3f(-2, -0.8 + i * 0.2, -1)
        glVertex3f(-2, -1 + i * 0.2, -1)

    # Sağ duvar (gradyan: koyu mavi - açık mavi)
    for i in range(10):
        factor = i / 10.0
        glColor3fv(gradient_color([0.8, 0.6, 0.6], [0.9, 0.7, 0.7], factor))
        glVertex3f(2, -1 + i * 0.2, -5)
        glVertex3f(2, -0.8 + i * 0.2, -5)
        glVertex3f(2, -0.8 + i * 0.2, -1)
        glVertex3f(2, -1 + i * 0.2, -1)

    glEnd()

def set_material(diffuse, specular, shininess):
    glMaterialfv(GL_FRONT, GL_AMBIENT_AND_DIFFUSE, diffuse)  # Yayılma ve ortam ışığı
    glMaterialfv(GL_FRONT, GL_SPECULAR, specular)            # Yansıtıcı ışık
    glMaterialf(GL_FRONT, GL_SHININESS, shininess)           # Parlaklık

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    gluLookAt(0, 0, 0, 0, 0, -1, 0, 1, 0)

    draw_room()

    # Cube
    glPushMatrix()
    glTranslatef(-1, -0.5, -3)
    glScalef(0.9, 0.9, 0.9)
    set_material((1.0, 1.0, 0.9, 1), (1, 1, 1, 1), 50)
    draw_cube()
    glPopMatrix()

    # Sphere
    glPushMatrix()
    glTranslatef(0.25, -0.5, -3)
    glScalef(0.9, 0.9, 0.9)
    set_material((0.5, 0.0, 0.5, 1), (1, 1, 1, 1), 50)
    draw_sphere()
    glPopMatrix()

    # Cylinder
    glPushMatrix()
    glTranslatef(-0.25, -0.5, -2)
    glRotatef(-90, 1, 0, 0)
    glScalef(0.8, 0.8, 0.8)
    set_material((0.7, 0.5, 1.0, 1), (1, 1, 1, 1), 50)
    draw_cylinder()
    glPopMatrix()

    # Pyramid
    glPushMatrix()
    glTranslatef(1.022, -0.5, -3.25)
    glScalef(0.6, 0.6, 0.6)
    set_material((0.0, 1.0, 1.0, 1), (1, 1, 1, 1), 5)
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
    # Yalnızca MULTISAMPLE ekleyerek antialiasing'i etkinleştirdik
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH | GLUT_MULTISAMPLE)
    glutInitWindowSize(width, height)
    glutCreateWindow(b"3D Room with Gradient Colors")
    init()
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutIdleFunc(display)
    glutMainLoop()

if __name__ == "__main__":
    main()
