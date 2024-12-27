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
