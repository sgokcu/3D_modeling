from OpenGL.GL import *

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