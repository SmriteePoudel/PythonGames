import pygame
import random

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 400
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GROUND_HEIGHT = HEIGHT - 50

# Create window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dino Runner")


dino_img = pygame.image.load("dino.png")  
cactus_img = pygame.image.load("cactus.png") 

class Dino:
    def __init__(self):
        self.x, self.y = 50, GROUND_HEIGHT - 40
        self.vel_y = 0
        self.is_jumping = False

    def jump(self):
        if not self.is_jumping:
            self.vel_y = -12
            self.is_jumping = True

    def update(self):
        self.y += self.vel_y
        self.vel_y += 0.5  
        if self.y >= GROUND_HEIGHT - 40:
            self.y = GROUND_HEIGHT - 40
            self.is_jumping = False

    def draw(self, screen):
        screen.blit(dino_img, (self.x, self.y))


class Cactus:
    def __init__(self):
        self.x, self.y = WIDTH, GROUND_HEIGHT - 40
        self.speed = 5

    def update(self):
        self.x -= self.speed
        if self.x < -20:
            self.x = WIDTH + random.randint(200, 400)

    def draw(self, screen):
        screen.blit(cactus_img, (self.x, self.y))

# Main game loop
def game_loop():
    clock = pygame.time.Clock()
    running = True
    dino = Dino()
    cactus = Cactus()

    while running:
        screen.fill(WHITE)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                dino.jump()

        # Update game objects
        dino.update()
        cactus.update()

        # Collision detection
        if dino.x + 40 > cactus.x and dino.y + 40 > cactus.y:
            print("Game Over!")
            running = False

        # Draw objects
        dino.draw(screen)
        cactus.draw(screen)

        pygame.display.update()
        clock.tick(30)

    pygame.quit()

# Run the game
game_loop()
