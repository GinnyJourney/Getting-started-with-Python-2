import pygame
import sys
import copy
import random

class Snake(object):

    def __init__(self, head, direction, length, body, score, fruit_pos):
        """
        Initializing the snake.
        """
        self.head = head
        self.direction = [dx, dy] = direction
        self.length = length
        self.body = body
        self.score = score
        self.fruit_pos = fruit_pos

    def change_direction(self, direction):
        """
        Change the direction of the snake after receiving the KEYDOWN event.
        Be aware that snake cannot shift to inverse direction against the ongoing one.
        :param direction: the coordinate of the head direction.
               direction = [dx, dy] : [1, 0]--right, [-1, 0]--left, [0, 1]--up, [0, -1]--down
        :return: the direction, [dx, dy], of the snake head.
        """
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                elif event.key == pygame.K_UP:
                    if self.direction == [0, 1]:
                        self.direction == [0, 1]
                        return self.direction
                    else:
                        self.direction = [dx, dy] = [0, -1]
                        return self.direction
                elif event.key == pygame.K_DOWN:
                    if self.direction == [0, -1]:
                        self.direction == [0, -1]
                        return self.direction
                    else:
                        self.direction = [dx, dy] = [0, 1]
                        return self.direction
                elif event.key == pygame.K_LEFT:
                    if self.direction == [1, 0]:
                        self.direction == [1, 0]
                        return self.direction
                    else:
                        self.direction = [dx, dy] = [-1, 0]
                        return self.direction
                elif event.key == pygame.K_RIGHT:
                    if self.direction == [-1, 0]:
                        self.direction == [-1, 0]
                        return self.direction
                    else:
                        self.direction = [dx, dy] = [1, 0]
                        return self.direction

    def move(self, direction):
        """
        Move the snake in certain direction depending on the snake head direction .
        :param direction: the coordinate of the head direction.
        """
        dx = direction[0]
        dy = direction[1]

        self.head[0] += dx * 10
        self.head[1] += dy * 10

        for i in range(self.length - 1):
            self.body[i] = self.body[i + 1]
        self.body[-1] = copy.copy(self.head)

    def check_boundary(self, width, height):
        """
        Check if the snake head collided with the boundary.
        Return TRUE if snake reaches boundary, FALSE if not.
        :param width: the width of boundary.
        :param height: the height of boundary.
        :return: Return TRUE if snake reaches boundary, FALSE if not.
        """
        if 0 <= self.head[0] + self.direction[0]*10 <= width - 10 and 0 <= self.head[1] + self.direction[1]*10 <= height - 10:
            return True
        else:
            return False

    def ate_itself(self):
        """
        Check if the snake is gonna eat itself.
        :return: Return TRUE if it is , FALSE if not.
        """
        ate_flag = False

        for i in self.body:
            if self.head[0] + self.direction[0]*10 == i[0] and self.head[1] + self.direction[1]*10 == i[1]:
                ate_flag = True

        return ate_flag

    def ate_fruit(self):
        if self.head[0]  == self.fruit_pos[0] and self.head[1] == self.fruit_pos[1]:
            self.score += 10    # error: score never changes, self.score changes

            # When eating the fruit, snake length grows
            self.head = [self.head[0] + self.direction[0]*10, self.head[1] + self.direction[1]*10]
            self.body.append(copy.copy(self.head))
            self.length += 1

            # Generate a new fruit position
            fruit_pos = [random.randint(2, 62) * 10, random.randint(2, 48) * 10] # error: (640, 500), not (500, 640)
            for i in self.body[:-1]:
                if i[0] == self.fruit_pos[0] or i[1] == self.fruit_pos[1]:
                    self.fruit_pos = [random.randint(2, 62) * 10, random.randint(2, 48) * 10]

def game_start(screen, orange, blue, brown):

    game_start = False

    screen.fill(orange)

    f = pygame.font.Font(None, 50)
    s = f.render("WELCOME TO", True, blue)
    screen.blit(s, [200, 100])

    f = pygame.font.Font(None, 80)
    s = f.render("SNAKE, SNAKE", True, blue)
    screen.blit(s, [105, 160])

    f = pygame.font.Font(None, 30)
    s = f.render("press ENTER / ESC to start / exit", True, brown)
    screen.blit(s, [160, 320])

    f = pygame.font.Font(None, 30)
    s = f.render("use UP / DOWN / LEFT / RIGHT to change direction", True, brown)
    screen.blit(s, [85, 360])

    pygame.display.update()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

            elif event.key == pygame.K_RETURN:
                game_start = True
                return game_start

def game_over(screen, black, red, brown, player):
    """
    When the snake crashed into the boundary or ate itself,
    the function popped the "Game over" slogan and showed the final score.
    :param screen: a Surface object in pygame
    :param black: color
    :param red: color
    :param brown: color
    :param player: a Snake object
    :return: None
    """
    screen.fill(black)

    f1 = pygame.font.Font(None, 102)
    s1 = f1.render("GAME OVER", True, red)
    screen.blit(s1, [100, 100])

    f2 = pygame.font.Font(None, 70)
    s2 = f2.render("score:  %d" % player.score, True, brown)
    screen.blit(s2, [200, 240])

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()







