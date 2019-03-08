import pygame
from pygame.locals import *

class Control:
    def __init__(self):
        self.flag_game = True
        self.flag_direction = 'RIGHT'
        self.flag_pause = True

    def control(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.flag_game = False  
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT and self.flag_direction != 'LEFT':
                    self.flag_direction = 'RIGHT'
                elif event.key == K_LEFT and self.flag_direction != 'RIGHT':
                    self.flag_direction = 'LEFT'
                elif event.key == K_UP and self.flag_direction != 'DOWN':
                    self.flag_direction = 'UP'
                elif event.key == K_DOWN and self.flag_direction != 'UP':
                    self.flag_direction = 'DOWN'
                elif event.key == K_d and self.flag_direction != 'LEFT':
                    self.flag_direction = 'RIGHT'
                elif event.key == K_a and self.flag_direction != 'RIGHT':
                    self.flag_direction = 'LEFT'
                elif event.key == K_w and self.flag_direction != 'DOWN':
                    self.flag_direction = 'UP'
                elif event.key == K_s and self.flag_direction != 'UP':
                    self.flag_direction = 'DOWN'
                elif event.key == K_q and self.flag_direction != 'LEFT':
                    self.flag_direction = 'RIGHT'
                elif event.key == k_e and self.flag_direction != 'RIGHT':
                    self.flag_direction = 'LEFT'
                elif event.key == k_z and self.flag_direction != 'LEFT':
                    self.flag_direction = 'RIGHT'
                elif event.key == k_x and self.flag_direction != 'DOWN':
                    self.flag_direction = 'UP'

