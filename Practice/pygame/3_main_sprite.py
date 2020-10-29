import pygame

pygame.init()

screen_width = 480
screen_height = 640

screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Nado Game")
background = pygame.image.load("C:/Users/USER3/Desktop/PythonWorkspace/background.png")

character = pygame.image.load("C:/Users/USER3/Desktop/PythonWorkspace/character.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = screen_width / 2
character_y_pos = screen_height / 2









running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.blit(background,(0,0))
    screen.blit(character,(character_x_pos,character_y_pos))
    pygame.display.update()

pygame.quit()