from Hospital import Hospital
import pygame

# Configure Pygame
pygame.init()

# Window`s Dimensions
WIDTH, HEIGHT = 800, 600

# Colours
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (1, 29, 105)

# Window`s configuration
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hospital Simulation")

hospital = Hospital()
clock = pygame.time.Clock()

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                hospital.admit_patient()
            elif event.key == pygame.K_d:
                hospital.discharge_patient()

    # Patient`s Movement
    for patient in hospital.patients:
        patient.move()

    # Draw in the screen
    screen.fill(WHITE)
    for patient in hospital.patients:
        pygame.draw.circle(screen, RED, (patient.x, patient.y), patient.radius)

    pygame.draw.rect(screen, BLUE,[0, 0, WIDTH, 10])
    pygame.draw.rect(screen, BLUE,[0, HEIGHT - 10, WIDTH, 10])
    pygame.draw.rect(screen, BLUE,[0, 0, 10, HEIGHT])
    pygame.draw.rect(screen, BLUE,[WIDTH - 10, 0, 10, HEIGHT])
    #pygame.display.flip()
    pygame.display.update()
    clock.tick(60)

pygame.quit()
