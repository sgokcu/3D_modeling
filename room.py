import pygame
pygame.init()

# Ekran boyutunu kare formatına getirelim
screen_size = 700
screen = pygame.display.set_mode((screen_size, screen_size))

black = (0, 0, 0)
line_width = 3
running = True

while running:
    screen.fill((255, 255, 255))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Odanın merkezini bulalım
    center_x = screen_size // 2
    center_y = screen_size // 2
    
    # Corner çizgileri
    pygame.draw.line(screen, black, (center_x, center_y - 200), (center_x, center_y + 464), line_width)
    pygame.draw.line(screen, black, (center_x, center_y + 506), (center_x, center_y + 600), line_width)
    
    # Çatı (roof)
    pygame.draw.line(screen, black, (center_x, center_y - 200), (center_x + 500, center_y - 350), line_width)
    pygame.draw.line(screen, black, (center_x, center_y - 200), (center_x - 500, center_y - 350), line_width)
    
    # Zemin (floor)
    pygame.draw.line(screen, black, (center_x, center_y + 600), (center_x + 6, center_y + 601), line_width)
    pygame.draw.line(screen, black, (center_x + 26, center_y + 608), (center_x + 500, center_y + 850), line_width)
    
    pygame.draw.line(screen, black, (center_x, center_y + 600), (center_x - 100, center_y + 638), line_width)
    pygame.draw.line(screen, black, (center_x - 120, center_y + 645), (center_x - 500, center_y + 850), line_width)
    
    # Pencere (window)
    pygame.draw.polygon(screen, black, [(center_x + 100, center_y - 50), (center_x + 100, center_y + 250), (center_x + 368, center_y + 384), (center_x + 368, center_y - 84)], line_width)
    
    # Pencere içi çizgiler
    # Yatay çizgi (ortada)
    pygame.draw.line(screen, black, (center_x + 100, center_y + 110), (center_x + 368, center_y + 110), line_width)  # üst yatay çizgi
    # Dikey çizgi (orta)
    pygame.draw.line(screen, black, (center_x + 220, center_y - 65), (center_x + 220, center_y + 310), line_width)  # dikey çizgi

    # Masa üstü (table top)
    pygame.draw.polygon(screen, black, [(center_x + 26, center_y + 181), (center_x - 100, center_y + 100), (center_x - 600, center_y + 250), (center_x - 124, center_y + 331)], line_width)
    pygame.draw.line(screen, black, (center_x + 26, center_y + 196), (-124, center_y + 346), line_width)
    
    # Masa ayakları (table legs)
    pygame.draw.line(screen, black, (center_x + 26, center_y + 181), (center_x + 26, center_y + 581), line_width)
    pygame.draw.line(screen, black, (center_x + 16, center_y + 200), (center_x + 16, center_y + 588), line_width)
    pygame.draw.line(screen, black, (center_x + 6, center_y + 204), (center_x + 6, center_y + 581), line_width)
    
    pygame.draw.line(screen, black, (center_x + 26, center_y + 581), (center_x + 16, center_y + 588), line_width)
    pygame.draw.line(screen, black, (center_x + 16, center_y + 588), (center_x + 6, center_y + 581), line_width)
    
    pygame.draw.line(screen, black, (center_x - 100, center_y + 245), (center_x - 100, center_y + 400), line_width)
    pygame.draw.line(screen, black, (center_x - 110, center_y + 240), (center_x - 110, center_y + 393), line_width)
    pygame.draw.line(screen, black, (center_x - 120, center_y + 249), (center_x - 120, center_y + 393), line_width)
    
    pygame.draw.line(screen, black, (center_x - 100, center_y + 400), (center_x - 110, center_y + 393), line_width)
    pygame.draw.line(screen, black, (center_x - 100, center_y + 400), (center_x - 120, center_y + 393), line_width)
    
    pygame.display.flip()

pygame.quit()
