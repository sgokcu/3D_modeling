# controls.py

from math import cos, sin
from OpenGL.GLUT import *
from lighting import *

class Control:
    camera_x = 0.0
    camera_y = 0.0
    camera_z = 0.0
    camera_distance = 1.10
    is_rotating = True

    rotation_cube = 0.0
    rotation_pyramid = 0.0

    @staticmethod
    def toggle_rotation():
        Control.is_rotating = not Control.is_rotating

    @staticmethod
    def update_rotation():
        if Control.is_rotating:
            Control.rotation_cube += 1.0
            Control.rotation_pyramid += 1.0
            Control.rotation_cube %= 360
            Control.rotation_pyramid %= 360

    @staticmethod
    def keyboard(key, x, y):
        if key == b'1':
            first_light()
        elif key == b'2':
            second_light()
        elif key == b'3':
            third_light()
        elif key == b' ':
            Control.toggle_rotation()
        elif key == b'\x1b':  # Escape tuşu
            print("Exiting...")
            glutLeaveMainLoop()

    @staticmethod
    def special_keys(key, x, y):
        move_speed = 0.1

        if key == GLUT_KEY_UP:
            Control.camera_y += move_speed
        elif key == GLUT_KEY_DOWN:
            Control.camera_y -= move_speed
        elif key == GLUT_KEY_LEFT:
            Control.camera_x -= move_speed * cos(Control.camera_distance)
            Control.camera_z -= move_speed * sin(Control.camera_distance)
        elif key == GLUT_KEY_RIGHT:
            Control.camera_x += move_speed * cos(Control.camera_distance)
            Control.camera_z += move_speed * sin(Control.camera_distance)
        elif key == GLUT_KEY_PAGE_UP:
            Control.camera_distance -= move_speed
        elif key == GLUT_KEY_PAGE_DOWN:
            Control.camera_distance += move_speed

        glutPostRedisplay()