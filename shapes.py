import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import math

# Şekil pozisyonları
cube_x = -7
cylinder_x = -2.5
pyramid_x = 2.5
sphere_x = 7

# Malzeme özelliklerini ayarlayan fonksiyon
def set_material(diffuse, specular, shininess):
    glMaterialfv(GL_FRONT, GL_AMBIENT_AND_DIFFUSE, diffuse)  # Yayılma ve ortam ışığı
    glMaterialfv(GL_FRONT, GL_SPECULAR, specular)  # Yansıtıcı ışık
    glMaterialf(GL_FRONT, GL_SHININESS, shininess)  # Parlaklık

# Küp çizen fonksiyon
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
    for face in faces:
        for vertex in face:
            glVertex3fv(vertices[vertex])
    glEnd()

# Silindir çizen fonksiyon
def Cylinder():
    radius = 1.0
    height = 2.0
    slices = 50

    # Alt yüzey
    glBegin(GL_TRIANGLE_FAN)
    glColor3f(1, 0.3, 0.7)  # Pembe renk
    glVertex3f(0, 0, -height / 2)
    for i in range(slices + 1):
        angle = 2 * math.pi * i / slices
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        glVertex3f(x, y, -height / 2)
    glEnd()

    # Üst yüzey
    glBegin(GL_TRIANGLE_FAN)
    glColor3f(1, 0.3, 0.7)  # Pembe renk
    glVertex3f(0, 0, height / 2)
    for i in range(slices + 1):
        angle = 2 * math.pi * i / slices
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        glVertex3f(x, y, height / 2)
    glEnd()

    # Yan yüzeyler
    glBegin(GL_QUAD_STRIP)
    for i in range(slices + 1):
        angle = 2 * math.pi * i / slices
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        t = i / slices
        glColor3f(1, 0.4 + t * 0.6, 0.7 - t * 0.6)  # Çift renkli pembe-mor gradyan
        glVertex3f(x, y, -height / 2)
        glVertex3f(x, y, height / 2)
    glEnd()

# Piramit çizen fonksiyon
def Pyramid():
    vertices = (
        (0, 1, 0),     # Tepe noktası
        (-1, -1, -1),  # Sol alt arka
        (1, -1, -1),   # Sağ alt arka
        (1, -1, 1),    # Sağ alt ön
        (-1, -1, 1),   # Sol alt ön
    )

    glBegin(GL_TRIANGLES)
    for i in range(1, 5):
        t = i / 4
        glColor3f(1, 0.4 + t * 0.6, 0.7 - t * 0.6)  # Çift renkli pembe-mor gradyan
        glVertex3fv(vertices[0])
        glVertex3fv(vertices[i])
        glVertex3fv(vertices[1 if i == 4 else i + 1])
    glEnd()

# Küre çizen fonksiyon
def Sphere():
    slices = 32
    stacks = 16
    radius = 1.0

    for i in range(stacks):
        lat0 = math.pi * (-0.5 + i / stacks)
        z0 = radius * math.sin(lat0)
        zr0 = radius * math.cos(lat0)

        lat1 = math.pi * (-0.5 + (i + 1) / stacks)
        z1 = radius * math.sin(lat1)
        zr1 = radius * math.cos(lat1)

        glBegin(GL_QUAD_STRIP)
        for j in range(slices + 1):
            lng = 2 * math.pi * j / slices
            x = math.cos(lng)
            y = math.sin(lng)

            t = j / slices
            glColor3f(1, 0.4 + t * 0.6, 0.7 - t * 0.6)  # Çift renkli pembe-mor gradyan
            glVertex3f(x * zr0, y * zr0, z0)
            glVertex3f(x * zr1, y * zr1, z1)
        glEnd()

# Ana fonksiyon
def main():
    pygame.init()  # Pygame başlat
    display = (1280, 720)  # Ekran boyutları
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)  # Çift tamponlama ve OpenGL ile ekranı ayarla
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)  # Perspektif ayarla
    glTranslatef(0, 0, -15)  # Görüntüyü uzaklaştır

    glEnable(GL_DEPTH_TEST)  # Derinlik testi etkinleştir
    glEnable(GL_LIGHTING)  # Aydınlatma etkinleştir
    glEnable(GL_LIGHT0)  # Işık kaynağı etkinleştir

    # Işık özellikleri
    glLightfv(GL_LIGHT0, GL_POSITION, (10, 1, 1, 1))
    glLightfv(GL_LIGHT0, GL_DIFFUSE, (10, 10, 10, 0))
    glLightfv(GL_LIGHT0, GL_SPECULAR, (0, 0, 0, 1))  # Beyaz ışık parlamasını kaldır

    while True:
        for event in pygame.event.get():  # Pygame olaylarını kontrol et
            if event.type == pygame.QUIT:  # Çıkış yapılmak istenirse
                pygame.quit()
                quit()

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)  # Ekranı ve derinlik tamponunu temizle

        # Küp (Parlak malzeme)
        glPushMatrix()  # Geçerli matris durumunu sakla
        glTranslatef(cube_x, 0, 0)  # Küpün pozisyonunu ayarla
        #glRotatef(pygame.time.get_ticks() / 60, 1, 1, 0)  # Küpü döndür
        set_material((1, 0.4, 0.6, 1), (0.8, 0.8, 0.8, 1), 80)  # Pembe parlak malzeme
        Cube()  # Küp çiz
        glPopMatrix()  # Önceki matris durumunu geri yükle

        # Silindir (Parlak malzeme)
        glPushMatrix()  # Geçerli matris durumunu sakla
        glTranslatef(cylinder_x, 0, 0)  # Silindirin pozisyonunu ayarla
        glRotatef(90, 1, 0, 0)  # Silindiri dikey konuma getir
        #glRotatef(pygame.time.get_ticks() / 60, 1, 1, 0)  # Silindiri döndür
        set_material((1, 0.4, 0.6, 1), (0.8, 0.8, 0.8, 1), 80)  # Pembe parlak malzeme
        Cylinder()  # Silindir çiz
        glPopMatrix()  # Önceki matris durumunu geri yükle

        # Piramit (Mat malzeme)
        glPushMatrix()  # Geçerli matris durumunu sakla
        glTranslatef(pyramid_x, 0, 0)  # Piramitin pozisyonunu ayarla
       # glRotatef(pygame.time.get_ticks() / 60, 1, 1, 0)  # Piramiti döndür
        set_material((1, 0.4, 0.6, 1), (0.3, 0.3, 0.3, 1), 10)  # Pembe mat malzeme
        Pyramid()  # Piramit çiz
        glPopMatrix()  # Önceki matris durumunu geri yükle

        # Küre (Mat malzeme)
        glPushMatrix()  # Geçerli matris durumunu sakla
        glTranslatef(sphere_x, 0, 0)  # Kürenin pozisyonunu ayarla
        #glRotatef(pygame.time.get_ticks() / 60, 1, 1, 0)  # Küreyi döndür
        set_material((1, 0.4, 0.6, 1), (0.3, 0.3, 0.3, 1), 10)  # Pembe mat malzeme
        Sphere()  # Küre çiz
        glPopMatrix()  # Önceki matris durumunu geri yükle

        pygame.display.flip()  # Ekranı güncelle
        pygame.time.wait(10)  # Biraz bekle

main()  # Ana fonksiyonu çalıştır
