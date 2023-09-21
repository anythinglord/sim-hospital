import random

# Dimensiones de la ventana
WIDTH, HEIGHT = 800, 600

class Patient:
    def __init__(self):
        self.health = random.randint(1, 100)
        self.x = random.randint(50, WIDTH - 50)
        self.y = random.randint(50, HEIGHT - 50)
        self.radius = 10

    def move(self):
        self.x += random.randint(-5, 5)
        self.y += random.randint(-5, 5)