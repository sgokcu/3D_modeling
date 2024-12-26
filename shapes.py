import pygame
import math

def draw_cube(screen, center_x, center_y, angle_x=0, angle_y=0):
    size = 50
    # Define the square vertices of the cube
    points = [
        (center_x - size//2, center_y - size//2),
        (center_x + size//2, center_y - size//2),
        (center_x + size//2, center_y + size//2),
        (center_x - size//2, center_y + size//2)
    ]
    
    # Rotate points around the center (center_x, center_y) on both axes
    rotated_points = []
    for (x, y) in points:
        # Translate the point to the origin for rotation
        x -= center_x
        y -= center_y
        
        # Rotate around Y-axis (horizontal axis)
        rotated_x = x * math.cos(angle_y) - y * math.sin(angle_y)
        rotated_y = x * math.sin(angle_y) + y * math.cos(angle_y)
        
        # Rotate around X-axis (vertical axis)
        rotated_x_3d = rotated_x
        rotated_y_3d = rotated_y * math.cos(angle_x) - rotated_x * math.sin(angle_x)

        # Translate back to the original position
        rotated_x_3d += center_x
        rotated_y_3d += center_y
        
        rotated_points.append((rotated_x_3d, rotated_y_3d))

    # Draw the rotated square (cube)
    pygame.draw.polygon(screen, (0, 128, 0), rotated_points)


def draw_sphere(screen, center_x, center_y):
    radius = 40
    pygame.draw.circle(screen, (255, 0, 0), (center_x, center_y), radius)

def draw_pyramid(screen, center_x, center_y):
    points = [
        (center_x, center_y - 40),
        (center_x - 40, center_y + 40),
        (center_x + 40, center_y + 40)
    ]
    pygame.draw.polygon(screen, (255, 255, 0), points)

def draw_cylinder(screen, center_x, center_y):
    radius = 30
    height = 60
    pygame.draw.circle(screen, (0, 0, 255), (center_x, center_y), radius)
    pygame.draw.rect(screen, (0, 0, 255), (center_x - radius, center_y, 2 * radius, height))
    pygame.draw.circle(screen, (0, 0, 255), (center_x, center_y + height), radius)


def calculate_center(center_x, center_y):
    x1, y1 = center_x + int(26), center_y + int(181)
    x2, y2 = center_x - int(100), center_y + int(100)
    x3, y3 = center_x - int(600), center_y + int(250)
    x4, y4 = center_x - int(124), center_y + int(331)

    center_x = (x1 + x2 + x3 + x4) / 4
    center_y = (y1 + y2 + y3 + y4) / 4

    return int(center_x), int(center_y)