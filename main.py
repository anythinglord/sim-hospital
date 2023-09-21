from patient import Patient

import pygame
import random
import time

# Configure Pygame
pygame.init()

# Window`s Dimensions
WIDTH, HEIGHT = 800, 600

# Colours
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Hospital`s class
class Hospital:
    def __init__(self):
        self.patients = []

    def admit_patient(self):
        new_patient = Patient()
        self.patients.append(new_patient)

    def discharge_patient(self):
        if self.patients:
            discharged_patient = self.patients.pop()
            print(f"Patient discharged with health: {discharged_patient.health}")

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

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
