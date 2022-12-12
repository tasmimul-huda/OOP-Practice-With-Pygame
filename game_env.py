from config import Config
import pygame
from spaceship import SpaceShip


config = Config()

red_spaceship = SpaceShip(config.RED_SPACESHIP_IMG_PATH,config.SPACESHIP_WIDTH, 
                                config.SPACESHIP_HEIGHT, config.red_x, config.red_y)
yellow_spaceship = SpaceShip(config.YELLOW_SPACESHIP_IMG_PATH,config.SPACESHIP_WIDTH,
                                config.SPACESHIP_HEIGHT, config.yellow_x, config.yellow_y)


WIN = pygame.display.set_mode((config.WIDTH, config.HEIGHT))
pygame.display.set_caption(config.CAPTION)


class Space:
    def __init__(self):
        pass
    
    @staticmethod
    def create_space(bg_image_path):
        SPACE = pygame.transform.scale(pygame.image.load(bg_image_path), (config.WIDTH, config.HEIGHT))
        WIN.blit(SPACE, (0,0))
        WIN.blit(red_spaceship.image(), red_spaceship.place())
        WIN.blit(yellow_spaceship.image(), yellow_spaceship.place())

        pygame.display.update()

env = Space.create_space(config.SPACE_IMAGE_PATH)