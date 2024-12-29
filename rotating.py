# rotating.py
class Rotation:
    angle_cube = 0.0
    angle_pyramid = 0.0

    speed_cube = 1.0
    speed_pyramid = 0.8

    @staticmethod
    def update():

        Rotation.angle_cube += Rotation.speed_cube
        Rotation.angle_pyramid += Rotation.speed_pyramid

        Rotation.angle_cube %= 360
        Rotation.angle_pyramid %= 360
