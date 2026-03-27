import pygame

pygame.init()

start_position = pygame.Vector2(3,4)
destination = pygame.Vector2(8,7)
destination_2= pygame.Vector2(9,1)
wey_lenght = start_position.distance_to(destination)
wey_lenght2= destination.distance_to(destination_2)
wey_lenght3= destination_2.distance_to(start_position)
print(wey_lenght)
print(wey_lenght2)
print(wey_lenght3)