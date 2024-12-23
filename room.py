import pygame

def initialize_pygame(screen_size=800):
    pygame.init()
    screen = pygame.display.set_mode((screen_size, screen_size))
    return screen

def draw_polygons(screen, center_x, center_y, line_width):
    pygame.draw.polygon(screen, (211, 211, 211), [(center_x, center_y - int(200)),
                                                  (center_x + int(950), center_y - int(500)),
                                                  (center_x - int(950), center_y - int(500))])

    pygame.draw.polygon(screen, (0, 0, 128), [(center_x + int(100), center_y - int(50)),
                                             (center_x + int(100), center_y + int(250)),
                                             (center_x + int(368), center_y + int(384)),
                                             (center_x + int(368), center_y - int(84))], line_width)

    pygame.draw.polygon(screen, (135, 206, 235), [(center_x + int(103), center_y - int(49)),
                                                 (center_x + int(103), center_y + int(249)),
                                                 (center_x + int(367), center_y + int(383)),
                                                 (center_x + int(367), center_y - int(83))])

    pygame.draw.line(screen, (0, 0, 128), (center_x + int(100), center_y + int(110)),
                     (center_x + int(368), center_y + int(110)), line_width)  # Horizontal line
    pygame.draw.line(screen, (0, 0, 128), (center_x + int(220), center_y - int(65)),
                     (center_x + int(220), center_y + int(310)), line_width)  # Vertical Line

def draw_table(screen, center_x, center_y, ):
    pygame.draw.polygon(screen, (180, 120, 60), [(center_x + int(26), center_y + int(181)),
                                                (center_x - int(100), center_y + int(100)),
                                                (center_x - int(600), center_y + int(250)),
                                                (center_x - int(124), center_y + int(331))])

def draw_legs(screen, center_x, center_y, line_width):
    back_leg_x_start = center_x + int(23)
    back_leg_x_end = center_x + int(3)
    back_leg_y_start = center_y + int(181)
    back_leg_y_end = center_y + int(581)

    front_leg_x_start = center_x - int(125)
    front_leg_x_end = center_x - int(100)
    front_leg_y_start = center_y + int(308)
    front_leg_y_end = center_y + int(400)

    pygame.draw.line(screen, (110, 50, 10), (back_leg_x_start, back_leg_y_start), (back_leg_x_start, back_leg_y_end), line_width)
    pygame.draw.line(screen, (180, 120, 60), (center_x + int(13), center_y + int(188)),
                     (center_x + int(13), center_y + int(588)), line_width)
    pygame.draw.line(screen, (110, 50, 10), (back_leg_x_end, center_y + int(204)),
                     (back_leg_x_end, back_leg_y_end), line_width)

    pygame.draw.line(screen, (110, 50, 10), (front_leg_x_start, front_leg_y_start + 26), (front_leg_x_start, front_leg_y_end), line_width)
    pygame.draw.line(screen, (180, 120, 60), (center_x - int(110), center_y + int(318)),
                     (center_x - int(110), center_y + int(400)), line_width)
    pygame.draw.line(screen, (110, 50, 10), (front_leg_x_end, front_leg_y_start), (front_leg_x_end, front_leg_y_end), line_width)

def update_pixels(screen, x_start, x_end, y_start, y_end, color_to_replace, new_color):
    for y in range(y_start, y_end):
        for x in range(x_start, x_end):
            if 0 <= x < screen.get_width() and 0 <= y < screen.get_height():
                current_pixel = screen.get_at((x, y))
                if current_pixel != color_to_replace:
                    screen.set_at((x, y), new_color)

def main():
    screen_size = 800

    screen = initialize_pygame(screen_size)
    
    light_brown = (180, 120, 60)
    brown = (160, 82, 82)
    line_width = 3
    
    running = True
    while running:
        screen.fill((245, 245, 220))  # Wall color
        center_x, center_y = screen_size // 2, screen_size // 2

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Drawing the main elements
        draw_polygons(screen, center_x, center_y, line_width)
        draw_table(screen, center_x, center_y, )
        draw_legs(screen, center_x, center_y, line_width)

        # Update colored legs
        update_pixels(screen, center_x + int(3), center_x + int(23), center_y + int(181), center_y + int(581), light_brown, brown)
        update_pixels(screen, center_x - int(125), center_x - int(100), center_y + int(308), center_y + int(400), light_brown, brown)

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
