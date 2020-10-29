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

to_x = 0
to_y = 0

character_speed = 0.6

clock = pygame.time.Clock()




running = True

while running:
    dt = clock.tick(10)
    print("fps : " , str(clock.get_fps()))
  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed
            elif event.key == pygame.K_UP:
                to_y -= character_speed
            elif event.key == pygame.K_DOWN:
                to_y += character_speed
        if event.type == pygame.KEYUP:
            if event.key ==pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x =0

            elif event.key ==pygame.K_UP or event.key == pygame.K_DOWN:
                to_y =0
                

    character_x_pos += to_x*dt
    character_y_pos += to_y*dt
    character_x_pos= min(screen_width-character_width,max(0,character_x_pos))
    character_y_pos= min(screen_height-character_height,max(0,character_y_pos))


    screen.blit(background,(0,0))
    screen.blit(character,(character_x_pos,character_y_pos))
    pygame.display.update()

pygame.quit()