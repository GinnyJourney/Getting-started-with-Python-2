import pygame
import sys
import random
from snake import Snake
from snake import game_over
from snake import game_start

# Initialize color
black = [0, 0, 0]
red = [255, 69, 0]
blue = [65, 105, 225]
brown = [205, 133, 63]
yellow = [240, 128, 128]
orange = [252, 230, 201]

# Initialize screen Surface object
speed = 200
start_flag = False
screen_width = 640
screen_height = 500
screen = pygame.display.set_mode([screen_width,screen_height])

# Initialize pygame.font module, set display caption
pygame.font.init()
pygame.display.init()
pygame.display.set_caption('Snake, snake')

# Initialize the Snake named player
score = 0
length = 10
head = [110, 250]
direction = [dx, dy] = [1, 0]
body =  [[20, 250], [30, 250], [40, 250], [50, 250], [60, 250], [70, 250], [80, 250], [90, 250], [100, 250], [110, 250]]
fruit_pos = [random.randint(2, 62)*10, random.randint(2, 48)*10]
player = Snake(head, direction, length, body, score, fruit_pos)

# Generate the first fruit for player
for i in player.body:
    if i[0] == player.fruit_pos[0] or i[1] == player.fruit_pos[1]:
        player.fruit_pos = [random.randint(2, 62) * 10, random.randint(2, 48) * 10]

# Main function
if __name__ == '__main__':

    while 1:

        start_flag = game_start(screen, orange, blue, brown)

        while start_flag:

            if player.check_boundary(screen_width, screen_height) and not player.ate_itself():

                player.ate_fruit()

                player.move(player.direction)

                player.change_direction(player.direction)   # error: 可变对象能被改变后传出，整型变量不能被改变后传出

                # set background
                screen.fill(orange)

                # display snake and fruit
                for i in player.body:
                    player_body_rect = pygame.draw.rect(screen, blue, i + [10, 10], 0)
                fruit_rect = pygame.draw.rect(screen, yellow, player.fruit_pos + [10, 10], 0)

                # display score
                f2 = pygame.font.Font(None, 40)
                s2 = f2.render("score: %d" % player.score, True, brown)
                screen.blit(s2, [450, 50])

                pygame.display.update()
                pygame.time.delay(50)

            else:
                game_over(screen, black, red, brown, player)





