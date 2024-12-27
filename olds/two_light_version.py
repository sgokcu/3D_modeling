from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import pygame
from pygame.locals import *
from math import sin, cos

width, height = 800, 600
camera_angle_x = 0
camera_angle_y = 0
camera_distance = 1.10
rotation_angle_cube = 0.0
rotation_angle_pyramid = 0.0
camera_position_x = 0.0
camera_position_y = 0.0
camera_position_z = 0.0
is_rotating = True

def toggle_rotation():
    """
    Döndürme işlemini başlat veya durdur.
    """
    global is_rotating
    is_rotating = not is_rotating

def update_rotation():
    """
    Dönüş açılarını güncelle.
    """
    global rotation_angle_cube, rotation_angle_pyramid

    if is_rotating:
        rotation_angle_cube += 1.0
        rotation_angle_pyramid += 1.5

    rotation_angle_cube %= 360
    rotation_angle_pyramid %= 360

    glutPostRedisplay()

def f_light_position():
    light0_position = [3.0, 3.0, -2.0, 1.0]
    light0_ambient = [0.2, 0.2, 0.2, 1.0]
    light0_diffuse = [0.8, 0.8, 0.8, 1.0]
    light0_specular = [1.0, 1.0, 1.0, 1.0]

    glLightfv(GL_LIGHT0, GL_POSITION, light0_position)
    glLightfv(GL_LIGHT0, GL_AMBIENT, light0_ambient)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, light0_diffuse)
    glLightfv(GL_LIGHT0, GL_SPECULAR, light0_specular)

def s_light_position():
    light1_position = [-3.0, 3.0, -2.0, 1.0]
    light1_ambient = [0.1, 0.1, 0.3, 1.0]
    light1_diffuse = [0.5, 0.5, 0.9, 1.0]
    light1_specular = [0.7, 0.7, 1.0, 1.0]

    glLightfv(GL_LIGHT1, GL_POSITION, light1_position)
    glLightfv(GL_LIGHT1, GL_AMBIENT, light1_ambient)
    glLightfv(GL_LIGHT1, GL_DIFFUSE, light1_diffuse)
    glLightfv(GL_LIGHT1, GL_SPECULAR, light1_specular)

def first_light():
    glEnable(GL_LIGHT0)  # İlk ışık kaynağını etkinleştir
    glDisable(GL_LIGHT1)  # İkinci ışık kaynağını devre dışı bırak
    f_light_position()
    print("First light activated. Second light deactivated.")


def second_light():
    glEnable(GL_LIGHT0)  # İlk ışık kaynağını etkinleştir
    glEnable(GL_LIGHT1)  # İkinci ışık kaynağını etkinleştir
    glDisable(GL_LIGHT2)  # Tavandan gelen ışık kaynağını devre dışı bırak
    
    f_light_position()
    s_light_position()
    print("First and second lights activated. Third light deactivated.")

def third_light():
    glEnable(GL_LIGHT0)  # İlk ışık kaynağını etkinleştir
    glEnable(GL_LIGHT1)  # İkinci ışık kaynağını etkinleştir
    glEnable(GL_LIGHT2)  # Üçüncü ışık kaynağını etkinleştir
    
    f_light_position()
    s_light_position()
    
    light2_position = [0.0, 5.0, 0.0, 1.0]  # Tavandan aşağıya doğru gelen ışık
    light2_ambient = [0.1, 0.1, 0.1, 1.0]    # Ortam ışığı
    light2_diffuse = [0.9, 0.9, 0.8, 1.0]    # Yayılma ışığı
    light2_specular = [1.0, 1.0, 0.9, 1.0]   # Yansıma ışığı

    glLightfv(GL_LIGHT2, GL_POSITION, light2_position)
    glLightfv(GL_LIGHT2, GL_AMBIENT, light2_ambient)
    glLightfv(GL_LIGHT2, GL_DIFFUSE, light2_diffuse)
    glLightfv(GL_LIGHT2, GL_SPECULAR, light2_specular)


def init():
    glEnable(GL_DEPTH_TEST)
    glClearColor(0.5, 0.5, 0.5, 1.0)  # Arka plan rengi
    glEnable(GL_LIGHTING)  # Aydınlatmayı etkinleştir
    glEnable(GL_NORMALIZE)  # Normalleri normalize et
    glShadeModel(GL_SMOOTH)  # Düzgün gölgelendirme etkin
    glEnable(GL_COLOR_MATERIAL)  # Malzeme renklerini etkinleştir


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

# bu sorulur
# def draw_shadow():
#     """
#     Zemin üzerinde her şekil için gölge projeksiyonu oluşturur.
#     """
#     dynamic_light_pos = [
#         camera_distance * sin(camera_angle_y) * cos(camera_angle_x),
#         camera_distance * sin(camera_angle_x),
#         camera_distance * cos(camera_angle_y) * cos(camera_angle_x),
#         1.0
#     ]

#     ground_plane = [0, 1, 0, 0]  # Zemin düzlemi (yukarı doğru normalli)
#     shadow_matrix = create_shadow_matrix(dynamic_light_pos, ground_plane)

#     glDisable(GL_LIGHTING)  # Gölgeyi aydınlatmasız çiz
#     glEnable(GL_BLEND)      # Şeffaf gölgeler için karışımı etkinleştir
#     glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

#     glPushMatrix()
#     glMultMatrixf(shadow_matrix)
#     glColor4f(0.1, 0.1, 0.1, 0.1)  # Hafif gri, daha şeffaf gölge

#     # Gölgeyi her şekil için ayrı ayrı çiz
#     glPushMatrix()
#     glTranslatef(-1, -0.5, -2.5)  # Küpün gölgesi
#     draw_cube()
#     glPopMatrix()

#     glPushMatrix()
#     glTranslatef(0.25, -0.5, -3.5)  # Kürenin gölgesi
#     draw_sphere()
#     glPopMatrix()

#     # glPushMatrix()
#     # glTranslatef(-0.25, -0.5, -2)  # Silindirin gölgesi
#     # glRotatef(-90, 1, 0, 0)
#     # draw_cylinder()
#     # glPopMatrix()

#     glPushMatrix()
#     glTranslatef(1.022, -0.5, -3.25)  # Piramidin gölgesi
#     glScalef(0.8, 0.8, 0.8)
#     draw_pyramid()
#     glPopMatrix()

#     glPopMatrix()

#     glDisable(GL_BLEND)  # Şeffaflığı devre dışı bırak
#     glEnable(GL_LIGHTING)  # Aydınlatmayı geri getir


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
    glTranslatef(-1.2, -0.5, -2.5)
    glRotatef(rotation_angle_cube, 1, 1, 0)
    set_material((1.0, 1.0, 0.9, 1), (1, 1, 1, 1), 50)
    draw_cube()
    glPopMatrix()

    glPushMatrix()
    glTranslatef(0.25, -0.5, -2.5)
    set_material((0.5, 0.0, 0.5, 1), (1, 1, 1, 1), 50)
    draw_sphere()
    glPopMatrix()

    glPushMatrix()
    glTranslatef(-0.30, -0.5, -1.75)
    glRotatef(-90, 1, 0, 0)
    set_material((0.7, 0.5, 1.0, 1), (1, 1, 1, 1), 50)
    draw_cylinder()
    glPopMatrix()

    glPushMatrix()
    glTranslatef(1.3, 0.3, -3.25)
    glScalef(0.8, 0.8, 0.8)
    glRotatef(rotation_angle_pyramid, 0, 1, 1)
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

# bu fonk sorulur
def set_material(diffuse, specular, shininess):
    glMaterialfv(GL_FRONT, GL_AMBIENT_AND_DIFFUSE, diffuse)
    glMaterialfv(GL_FRONT, GL_SPECULAR, specular)
    glMaterialf(GL_FRONT, GL_SHININESS, shininess)


def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    gluLookAt(
        camera_position_x + camera_distance * sin(camera_angle_y) * cos(camera_angle_x),
        camera_position_y + camera_distance * sin(camera_angle_x),
        camera_position_z + camera_distance * cos(camera_angle_y) * cos(camera_angle_x),
        camera_position_x, camera_position_y, camera_position_z,
        0, 1, 0
    )

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


def keyboard(key, x, y):
    if key == b'1':
        first_light()
    elif key == b'2':
        second_light()
    elif key == b'3':
        third_light()
    elif key == b' ':
        toggle_rotation()
    elif key == b'\x1b':  # Escape tuşu
        print("Exiting...")
        glutLeaveMainLoop()


def special_keys(key, x, y):
    global camera_angle_x, camera_angle_y
    global camera_position_x, camera_position_y, camera_position_z

    move_speed = 0.1

    if key == GLUT_KEY_UP:
        camera_position_y += move_speed
    elif key == GLUT_KEY_DOWN:
        camera_position_y -= move_speed
    elif key == GLUT_KEY_LEFT:
        camera_position_x -= move_speed * cos(camera_angle_y)
        camera_position_z -= move_speed * sin(camera_angle_y)
    elif key == GLUT_KEY_RIGHT:
        camera_position_x += move_speed * cos(camera_angle_y)
        camera_position_z += move_speed * sin(camera_angle_y)
    elif key == GLUT_KEY_PAGE_UP:
        camera_position_z -= move_speed * cos(camera_angle_y)
        camera_position_x += move_speed * sin(camera_angle_y)
    elif key == GLUT_KEY_PAGE_DOWN:
        camera_position_z += move_speed * cos(camera_angle_y)
        camera_position_x -= move_speed * sin(camera_angle_y)

    glutPostRedisplay()

# bu kesin
def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(width, height)
    glutCreateWindow(b"3D Lighting and Keyboard Interaction")
    init()

    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutKeyboardFunc(keyboard)
    glutSpecialFunc(special_keys)
    glutIdleFunc(update_rotation)
    glutMainLoop()

if __name__ == "__main__":
    main()
