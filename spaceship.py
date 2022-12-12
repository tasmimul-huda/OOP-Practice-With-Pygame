from config import Config
import pygame

config = Config()

class SpaceShip():
    def __init__(self,spaceship_image_path, spaceship_width, spaceship_height, x_position,y_position):
        self.spaceship_width = spaceship_width
        self.spaceship_height = spaceship_height
        self.spaceship_image = spaceship_image_path
        self.x_position = x_position
        self.y_position = y_position
    
    def image(self):
        SPACESHIP_IMAGE = pygame.image.load(self.spaceship_image)
        space_ship = pygame.transform.rotate(
                pygame.transform.scale(SPACESHIP_IMAGE, (self.spaceship_width, self.spaceship_height)), 90)
        return space_ship

    def place(self):
        return pygame.Rect(self.x_position, self.y_position,
                                self.spaceship_width, self.spaceship_height)

# spaceship = SpaceShip(config.RED_SPACESHIP_IMG_PATH,config.SPACESHIP_WIDTH, config.SPACESHIP_HEIGHT, config.red_x, config.red_y)
# print(spaceship.place())