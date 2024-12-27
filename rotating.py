# rotating.py
class Rotation:
    # Rotasyon açılarının değerleri
    angle_cube = 0.0
    angle_sphere = 0.0
    angle_cylinder = 0.0
    angle_pyramid = 0.0

    # Rotasyon hızları
    speed_cube = 1.0
    speed_sphere = 1.5
    speed_cylinder = 2.0
    speed_pyramid = 0.8

    @staticmethod
    def update():
        """
        Rotasyon açılarını günceller.
        """
        Rotation.angle_cube += Rotation.speed_cube
        Rotation.angle_sphere += Rotation.speed_sphere
        Rotation.angle_cylinder += Rotation.speed_cylinder
        Rotation.angle_pyramid += Rotation.speed_pyramid

        # Açılar 360 dereceyi aşarsa sıfırla
        Rotation.angle_cube %= 360
        Rotation.angle_sphere %= 360
        Rotation.angle_cylinder %= 360
        Rotation.angle_pyramid %= 360
