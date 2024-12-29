from OpenGL.GL import *
from controls import *
from shapes import *

def draw_shadow():
    """
    Zemin üzerinde her şekil için gölge projeksiyonu oluşturur.
    """
    # Dinamik ışık kaynağı pozisyonunu hesapla
    dynamic_light_pos = [
        Control.camera_distance * sin(Control.camera_y) * cos(Control.camera_x),
        Control.camera_distance * sin(Control.camera_x),
        Control.camera_distance * cos(Control.camera_y) * cos(Control.camera_x),
        1.0
    ]

    # Zemin düzlemi tanımlama (yukarı yönlü normal: [0, 1, 0])
    ground_plane = [0, 1, 0, 0]

    # Gölge projeksiyon matrisi oluştur
    shadow_matrix = create_shadow_matrix(dynamic_light_pos, ground_plane)

    # Gölge çizimi için ışığı devre dışı bırak ve şeffaflığı etkinleştir
    glDisable(GL_LIGHTING)
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

    # Gölge matrisini uygula
    glPushMatrix()
    glMultMatrixf(shadow_matrix)

    # Gölge rengi (şeffaf gri)
    glColor4f(0.1, 0.1, 0.1, 0.5)

    # Her şekil için gölgeyi çiz
    glPushMatrix()
    glTranslatef(-1.2, -0.5, -2.5)  # Küpün gölgesi
    draw_cube()
    glPopMatrix()

    glPushMatrix()
    glTranslatef(0.25, -0.5, -2.5)  # Kürenin gölgesi
    draw_sphere()
    glPopMatrix()

    glPushMatrix()
    glTranslatef(-0.3, -0.5, -1.75)  # Silindirin gölgesi
    glRotatef(-90, 1, 0, 0)
    draw_cylinder()
    glPopMatrix()

    glPushMatrix()
    glTranslatef(1.3, -0.5, -3.25)  # Piramidin gölgesi
    glScalef(0.8, 0.8, 0.8)
    draw_pyramid()
    glPopMatrix()

    glPopMatrix()

    # Şeffaflık ve ışık ayarlarını geri yükle
    glDisable(GL_BLEND)
    glEnable(GL_LIGHTING)


def create_shadow_matrix(light_pos, plane):
    """
    Bir ışık kaynağı ve düzlemden gölge projeksiyonu matrisi oluşturur.
    """
    dot = sum(plane[i] * light_pos[i] for i in range(4))  # Nokta çarpımı

    shadow_matrix = []
    for i in range(4):
        row = []
        for j in range(4):
            if i == j:
                row.append(dot - light_pos[j] * plane[i])
            else:
                row.append(-light_pos[j] * plane[i])
        shadow_matrix.append(row)

    return [item for sublist in shadow_matrix for item in sublist]  # Düz liste döndür
