import pygame  # import pygame, duh
from sys import exit  # exit the game

# Call

pygame.init()                                                   # init pygame will start pygame
screen = pygame.display.set_mode((800, 400))                    # Window size
pygame.display.set_caption('Snail It!')                         # Name of window
clock = pygame.time.Clock()                                     # Calls clock for Framerate
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)          # Choose font if you want to use a words surface(should check if it can use system fonts)

# Surfaces- bottom will be last to load

sky_surface = pygame.image.load('graphics/Sky.png').convert()   # pygame.image.load- load image from file in same folder always use .convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()

score_surface = test_font.render('Snail It!', False, 'Black')      #('words', AA(smoothing), 'color')
score_rect = score_surface.get_rect(center = (400, 50))           # puts words into a rectangle

player_surface = pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()   # use alpha when?
player_rect = player_surface.get_rect(midbottom = (80, 300))        # .get_rect is calling player surface and forcing it into a rectangle so you can choose where it goes
player_gravity = 0

snail_surface = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_rect = snail_surface.get_rect(bottomright = (600, 300))


while True:                                                      # While True loop actually implements it
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()                                        # You have to call this or it will try to loop and break unless you use this function
            exit()                                               # Have to use this to break the loop using sys tools
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and player_rect.bottom >= 100:
                player_gravity = -20
    # Methods
    screen.blit(sky_surface, (0, 0))                             # screen.blit (calls whatever surface you want, (sets the position)
    screen.blit(ground_surface, (0, 300))
    pygame.draw.rect(screen, 'White', score_rect)                # background fill color
    pygame.draw.rect(screen, 'White', score_rect, 10)            #border to make background bigger. add one more variable after to round corners
    screen.blit(score_surface, score_rect)

    snail_rect.x -= 4                                           #Moves snail_rect
    if snail_rect.right <= 0: snail_rect.left = 800             #Loops snail back around, 800 is the size of the screen
    screen.blit(snail_surface, snail_rect)                      #puts snail on surface

    #Player
    player_gravity += 1
    player_rect.y += player_gravity
    if player_rect.bottom >= 300: player_rect.bottom = 300      #puts player on ground, doesn't allow it to fall
    screen.blit(player_surface, player_rect)                    # puts player surface on screen


    pygame.display.update()                                      # updates it every time the while loop runs
    clock.tick(60)                                               # Framerate
