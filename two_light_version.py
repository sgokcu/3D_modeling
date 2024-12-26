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

    # --- Işıklandırma ayarları ---
    glEnable(GL_LIGHTING)  # Aydınlatmayı etkinleştir
    glEnable(GL_LIGHT0)    # İlk ışık kaynağını etkinleştir
    glEnable(GL_LIGHT1)    # İkinci ışık kaynağını etkinleştir
    glEnable(GL_NORMALIZE) # Yüzey normallerini normalize et
    glEnable(GL_COLOR_MATERIAL)  # Malzeme renk özelliklerini etkinleştir

    # Sağdan yukarıdan gelen ışık kaynağı özellikleri
    light0_position = [3.0, 3.0, -2.0, 1.0]  # Sağ üstten gelen ışık
    light0_ambient = [0.2, 0.2, 0.2, 1.0]    # Ortam ışığı
    light0_diffuse = [0.8, 0.8, 0.8, 1.0]    # Yayılma ışığı
    light0_specular = [1.0, 1.0, 1.0, 1.0]   # Yansıma ışığı

    glLightfv(GL_LIGHT0, GL_POSITION, light0_position)
    glLightfv(GL_LIGHT0, GL_AMBIENT, light0_ambient)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, light0_diffuse)
    glLightfv(GL_LIGHT0, GL_SPECULAR, light0_specular)

    # Soldan yukarıdan gelen ikinci ışık kaynağı özellikleri
    light1_position = [-3.0, 3.0, -2.0, 1.0]  # Soldan üstten gelen ışık
    light1_ambient = [0.1, 0.1, 0.3, 1.0]    # Ortam ışığı (hafif mavi tonlu)
    light1_diffuse = [0.5, 0.5, 0.9, 1.0]    # Yayılma ışığı (mavi tonlu)
    light1_specular = [0.7, 0.7, 1.0, 1.0]   # Yansıma ışığı (parlak mavi)

    glLightfv(GL_LIGHT1, GL_POSITION, light1_position)
    glLightfv(GL_LIGHT1, GL_AMBIENT, light1_ambient)
    glLightfv(GL_LIGHT1, GL_DIFFUSE, light1_diffuse)
    glLightfv(GL_LIGHT1, GL_SPECULAR, light1_specular)

def gradient_color(start_color, end_color, factor):
    return [
        start_color[i] + (end_color[i] - start_color[i]) * factor
        for i in range(3)
    ]

def draw_cube():
    set_material((0.8, 0.6, 0.9, 1.0), (0.9, 0.7, 1.0, 1.0), 128)  # Açık lila yüzey
    for i in range(20):
        factor = i / 20.0
        glColor3fv(gradient_color([0.7, 0.5, 0.8], [0.8, 0.6, 0.9], factor))
        glutSolidCube(0.5)

def draw_sphere():
    set_material((0.9, 0.3, 0.6, 1.0), (1.0, 0.5, 0.8, 1.0), 128)  # Parlak pembe tonlu yüzey
    for i in range(20):
        factor = i / 20.0
        glColor3fv(gradient_color([0.8, 0.2, 0.5], [0.9, 0.3, 0.6], factor))
        glutSolidSphere(0.3, 64, 64)

def draw_cylinder():
    set_material((0.6, 0.8, 1.0, 0.4), (0.9, 1.0, 1.0, 0.6), 64)  # Şeffaf cam efekti için malzeme
    quad = gluNewQuadric()
    for i in range(20):
        factor = i / 20.0
        glColor4f(0.6 + factor * 0.2, 0.8 + factor * 0.1, 1.0, 0.4 + factor * 0.1)  # Şeffaf renk
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

def draw_shadow():
    """
    Zemin üzerinde her şekil için gölge projeksiyonu oluşturur.
    """
    light_position = [2.0, 2.0, -2.0, 1.0]  # Sağ üstten ışık
    ground_plane = [0, 1, 0, 0]  # Zemin düzlemi (yukarı doğru normalli)
    shadow_matrix = create_shadow_matrix(light_position, ground_plane)

    glDisable(GL_LIGHTING)  # Gölgeyi aydınlatmasız çiz
    glEnable(GL_BLEND)      # Şeffaf gölgeler için karışımı etkinleştir
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

    glPushMatrix()
    glMultMatrixf(shadow_matrix)
    glColor4f(0.0, 0.0, 0.0, 0.5)  # Hafif şeffaf siyah gölge

    # Gölgeyi her şekil için ayrı ayrı çiz
    glPushMatrix()
    glTranslatef(-1, -0.5, -2.5)  # Küpün gölgesi
    draw_cube()
    glPopMatrix()

    glPushMatrix()
    glTranslatef(0.25, -0.5, -3.5)  # Kürenin gölgesi
    draw_sphere()
    glPopMatrix()

    glPushMatrix()
    glTranslatef(-0.25, -0.5, -2)  # Silindirin gölgesi
    glRotatef(-90, 1, 0, 0)
    draw_cylinder()
    glPopMatrix()

    glPushMatrix()
    glTranslatef(1.022, -0.5, -3.25)  # Piramidin gölgesi
    glScalef(0.8, 0.8, 0.8)
    draw_pyramid()
    glPopMatrix()

    glPopMatrix()

    glDisable(GL_BLEND)  # Şeffaflığı devre dışı bırak
    glEnable(GL_LIGHTING)  # Aydınlatmayı geri getir

def create_shadow_matrix(light_pos, plane):
    """
    Gölge projeksiyonu matrisi oluşturur.
    """
    dot = sum(plane[i] * light_pos[i] for i in range(4))
    shadow_matrix = []
    for i in range(4):
        for j in range(4):
            if i == j:
                shadow_matrix.append(dot - light_pos[j] * plane[i])
            else:
                shadow_matrix.append(-light_pos[j] * plane[i])
    return shadow_matrix

def draw_shapes():
    glPushMatrix()
    glTranslatef(-1, -0.5, -2.5)  # Küpü biraz öne al
    set_material((1.0, 1.0, 0.9, 1), (1, 1, 1, 1), 50)
    draw_cube()
    glPopMatrix()

    glPushMatrix()
    glTranslatef(0.25, -0.5, -3.5)
    set_material((0.5, 0.0, 0.5, 1), (1, 1, 1, 1), 50)
    draw_sphere()
    glPopMatrix()

    glPushMatrix()
    glTranslatef(-0.25, -0.5, -2)
    glRotatef(-90, 1, 0, 0)
    set_material((0.7, 0.5, 1.0, 1), (1, 1, 1, 1), 50)
    draw_cylinder()
    glPopMatrix()

    glPushMatrix()
    glTranslatef(1.022, -0.5, -3.25)
    glScalef(0.8, 0.8, 0.8)
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

def set_material(diffuse, specular, shininess):
    glMaterialfv(GL_FRONT, GL_AMBIENT_AND_DIFFUSE, diffuse)
    glMaterialfv(GL_FRONT, GL_SPECULAR, specular)
    glMaterialf(GL_FRONT, GL_SHININESS, shininess)

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    gluLookAt(0, 0, 0, 0, 0, -1, 0, 1, 0)

    draw_room()
    draw_shadow()
    draw_shapes()

    glutSwapBuffers()

def reshape(w, h):
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, w / h, 1, 100)
    glMatrixMode(GL_MODELVIEW)

def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH | GLUT_MULTISAMPLE)
    glutInitWindowSize(width, height)
    glutCreateWindow(b"3D Room with Lighting and Shadows")
    init()
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutIdleFunc(display)
    glutMainLoop()

if __name__ == "__main__":
    main()
