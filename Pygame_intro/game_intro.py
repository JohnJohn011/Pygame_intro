import pygame  # import pygame, duh
from sys import exit  # exit the game

# Call

pygame.init()                                                   # init pygame will start pygame
screen = pygame.display.set_mode((800, 400))                     # Window size
pygame.display.set_caption('Snail It!')                          # Name of window
clock = pygame.time.Clock()                                     # Calls clock for Framerate
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)          # Choose font if you want to use a words surface(should check if it can use system fonts)

# Surfaces- bottom will be last to load

sky_surface = pygame.image.load('graphics/Sky.png').convert()   # pygame.image.load- load image from file in same folder always use .convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()
test_surface = test_font.render('Snail It!', True, 'Black')      #('words', AA(smoothing), 'color')
player_surface = pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()   # use alpha when?
player_rect = player_surface.get_rect(topleft=(80, 200))        # .get_rect is calling player surface and forcing it into a rectangle so you can choose where it goes
snail_surface = pygame.image.load('graphics/snail/snail1.png').convert_alpha()

snail_x_pos = 600                                                # original position of the snail

while True:                                                      # While True loop actually implements it
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()                                        # You have to call this or it will try to loop and break unless you use this function
            exit()                                               # Have to use this to break the loop using sys tools

    screen.blit(sky_surface, (0, 0))                             # screen.blit (calls whatever surface you want, (sets the position)
    screen.blit(ground_surface, (0, 300))
    screen.blit(test_surface, (350, 50))
    snail_x_pos -= 4                                             # moves the snail left(-) or right (+) per...number? i forget
    if snail_x_pos < -100:                                       # Once it passes the screen it will hit -100 (left side)
        snail_x_pos = 800                                        # Then return back to 800 and loop around (right side)
    screen.blit(snail_surface, (snail_x_pos, 250))
    screen.blit(player_surface, (80, 200))                       # puts player surface on screen

    pygame.display.update()                                      # updates it every time the while loop runs
    clock.tick(60)                                               # Framerate
