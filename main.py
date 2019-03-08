import pygame
from control import Control
from snake import Snake
from gui import Gui
from food import Food

pygame.init()
window = pygame.display.set_mode((441, 441))
pygame.display.set_caption('ZMEEED')
control = Control()
snake = Snake()
gui = Gui()
food = Food()
gui.init_field()
food.get_food_position(gui)
var_speed = 0

while control.flag_game:
    gui.check_win_lose()
    control.control()
    window.fill(pygame.Color('Black'))
    if gui.game == "GAME":
        snake.draw_snake(window)
        food.draw_food(window)
    elif gui.game == "WIN":
        gui.draw_win(window)
    elif gui.game == "LOSE":
        gui.draw_lose(window)
    gui.draw_indicator(window)
    gui.draw_level(window)
    if var_speed % 30 == 0:
        snake.moove(control)
        snake.check_barrier(gui)
        snake.eat(food, gui)
        snake.check_and_window()
        snake.animation()
    var_speed += 1    
    pygame.display.flip()
