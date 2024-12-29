from OpenGL.GL import *

def setup_global_lighting():
    # Global ambient light settings
    global_ambient = [0.3, 0.3, 0.3, 1.0]
    glLightModelfv(GL_LIGHT_MODEL_AMBIENT, global_ambient)
    
    # Enable two sided lighting
    glLightModeli(GL_LIGHT_MODEL_TWO_SIDE, GL_TRUE)
    
    # Enable local viewer mode for more accurate specular reflections
    glLightModeli(GL_LIGHT_MODEL_LOCAL_VIEWER, GL_TRUE)

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

def t_light_position():
    light2_direction = [0.0, 5.0, 0.0, 0.0]  # Light from ceiling downward
    light2_ambient = [0.1, 0.1, 0.1, 1.0]    # Ambient light
    light2_diffuse = [0.9, 0.9, 0.8, 1.0]    # Diffuse light
    light2_specular = [1.0, 1.0, 0.9, 1.0]   # Specular light
    
    glLightfv(GL_LIGHT2, GL_POSITION, light2_direction)
    glLightfv(GL_LIGHT2, GL_AMBIENT, light2_ambient)
    glLightfv(GL_LIGHT2, GL_DIFFUSE, light2_diffuse)
    glLightfv(GL_LIGHT2, GL_SPECULAR, light2_specular)

def first_light():
    setup_global_lighting()  # Add global lighting setup
    glEnable(GL_LIGHTING)   # Enable lighting system
    glEnable(GL_LIGHT0)     # Enable first light source
    glDisable(GL_LIGHT1)    # Disable second light source
    glDisable(GL_LIGHT2)
    f_light_position()
    print("First light activated. Second light deactivated.")

def second_light():
    setup_global_lighting()  # Add global lighting setup
    glEnable(GL_LIGHTING)   # Enable lighting system
    glEnable(GL_LIGHT0)     # Enable first light source
    glEnable(GL_LIGHT1)     # Enable second light source
    glDisable(GL_LIGHT2)    # Disable third light source
    
    f_light_position()
    s_light_position()
    print("First and second lights activated. Third light deactivated.")

def third_light():
    setup_global_lighting()  # Add global lighting setup
    glEnable(GL_LIGHTING)   # Enable lighting system
    glEnable(GL_LIGHT0)     # Enable first light source
    glEnable(GL_LIGHT1)     # Enable second light source
    glEnable(GL_LIGHT2)     # Enable third light source
    
    f_light_position()
    s_light_position()
    t_light_position()
