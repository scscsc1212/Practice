import pygame
import random

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
character_x_pos = 0
character_y_pos = screen_height-character_height

to_x = 0
to_y = 0

character_speed = 0.6

enemy = pygame.image.load("C:/Users/USER3/Desktop/PythonWorkspace/enemy.png")
enemy_size = enemy.get_rect().size
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
enemy_x_pos = random.randrange(0,screen_width)
enemy_y_pos = 0

enemy_y_vel = 0.2

point = 0


clock = pygame.time.Clock()

game_font = pygame.font.Font(None, 40)

total_time = 10

start_ticks = pygame.time.get_ticks()
 


running = True

while running:
    dt = clock.tick(60)

  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed
            # elif event.key == pygame.K_UP:
            #     to_y -= character_speed
            # elif event.key == pygame.K_DOWN:
            #     to_y += character_speed
        if event.type == pygame.KEYUP:
            if event.key ==pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x =0

            elif event.key ==pygame.K_UP or event.key == pygame.K_DOWN:
                to_y =0
                

    character_x_pos += to_x*dt
    character_y_pos += to_y*dt
    character_x_pos= min(screen_width-character_width,max(0,character_x_pos))
    character_y_pos= min(screen_height-character_height,max(0,character_y_pos))

    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_y_pos += enemy_y_vel*dt

    if enemy_y_pos>screen_height:
        print("미쓰")
        running = False


    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    if(character_rect.colliderect(enemy_rect)):
        print("충돌")
        enemy_x_pos = random.randrange(0,screen_width)
        enemy_y_pos = 0
        enemy_y_vel +=0.1
        point +=enemy_y_vel*10


    screen.blit(background,(0,0))
    screen.blit(character,(character_x_pos,character_y_pos))
    screen.blit(enemy,(enemy_x_pos,enemy_y_pos))
    
    elapsed_time = (pygame.time.get_ticks()-start_ticks)/1000
    timer = game_font.render (str(int(total_time-elapsed_time)),True,(255,255,255))
    Game_point = game_font.render (str(int(point)),True,(255,255,255))
    screen.blit(timer,(10,10))
    screen.blit(Game_point,(200,10))

    if total_time - elapsed_time <= 0:
        print("타임아웃")
        running = False

    pygame.display.update()

Game_over= game_font.render ("Game Over",True,(255,255,255))
screen.blit(Game_over,(screen_width/2,screen_height/2))
pygame.display.update()
pygame.time.delay(2000)
pygame.quit()