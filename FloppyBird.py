import pygame
import random


pygame.init()


WIDTH, HEIGHT = 400, 600
WHITE = (255, 255, 255)
BLUE = (135, 206, 250)
PIPE_COLOR = (0, 200, 0)
GRAVITY = 0.5
JUMP_STRENGTH = -10
PIPE_GAP = 150
PIPE_WIDTH = 60
BIRD_X = 50


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")

bird_img = pygame.image.load("flappy_bird.png")  
bird_img = pygame.transform.scale(bird_img, (40, 30))

# Bird Class
class Bird:
    def __init__(self):
        self.x = BIRD_X
        self.y = HEIGHT // 2
        self.velocity = 0

    def jump(self):
        self.velocity = JUMP_STRENGTH

    def update(self):
        self.velocity += GRAVITY
        self.y += self.velocity
        if self.y >= HEIGHT - 40:  
            self.y = HEIGHT - 40

    def draw(self, screen):
        screen.blit(bird_img, (self.x, self.y))

# Pipe Class
class Pipe:
    def __init__(self, x):
        self.x = x
        self.height = random.randint(100, 400)
        self.speed = 3

    def update(self):
        self.x -= self.speed
        if self.x < -PIPE_WIDTH:  
            self.x = WIDTH
            self.height = random.randint(100, 400)

    def draw(self, screen):
        pygame.draw.rect(screen, PIPE_COLOR, (self.x, 0, PIPE_WIDTH, self.height))  
        pygame.draw.rect(screen, PIPE_COLOR, (self.x, self.height + PIPE_GAP, PIPE_WIDTH, HEIGHT))  # Bottom pipe


def game_loop():
    clock = pygame.time.Clock()
    bird = Bird()
    pipes = [Pipe(WIDTH), Pipe(WIDTH + 200)]
    running = True

    while running:
        screen.fill(BLUE)

        # Event Handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                bird.jump()

        # Update Game Objects
        bird.update()
        for pipe in pipes:
            pipe.update()

        
        for pipe in pipes:
            if bird.x + 40 > pipe.x and bird.x < pipe.x + PIPE_WIDTH:
                if bird.y < pipe.height or bird.y + 30 > pipe.height + PIPE_GAP:
                    print("Game Over!")
                    running = False

       
        bird.draw(screen)
        for pipe in pipes:
            pipe.draw(screen)

        pygame.display.update()
        clock.tick(30)

    pygame.quit()

# Run the Game
game_loop()
