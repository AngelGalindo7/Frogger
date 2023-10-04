import pygame
from constants import SQUARE_SIZE, WATER_COLOR, END_GRASS_SKIN_SPRITE
import random
"""
File for the water class
"""

"""We need to make some of these sprites to do detection for achieving the end and when you drop in the water.

Water lanes: It has lanes size of 7. In the main loop a detection should be made if there is contact between the frog with the turtles and logs which causes them to move in their direction which has been implemented. Assuming that there is no contact and your within the lanes of water, you would lose a life and gert reset back to the beginning

Goal grass: I believe there must be some other detection collision than sprite.spritecollideany because some threshold of the frogger dimensions need to be touching the goal grass section which is 40x40. Automatic collision shouldn't result in success. There is a video that deals with this idea of threshold collision and will be researching more to implement tests -A.G"""

"I will also implement randomized rain in the game. I will also implement a frogger super mario star that spawns a gun and shoots anything in its path. These two features will be done by tuesday to be shown on club rush- A.G "

def rand_color():
  return (random.randint(0, 255), random.randint(0, 255),random.randint(0, 255))


class Water:

    def __init__(self, x_input, y_input):
        self.x = x_input
        self.y = y_input
        self.size = SQUARE_SIZE
        counter = 0
        self.rand_color = WATER_COLOR
        counter = counter+1
        #self.image ["Water/water_sample.png"]

        """
        Noah's attempt at messing around and doing smooth color transitions with water
        self.begin_color = rand_color()
        self.end_color = rand_color()
        self.current_color = self.begin_color
        self.color_counter = 0
        self.color_counter_max = 60 * 6
        """
        if(counter == 5):
          self.rand_color = rand_color()
          counter = 0
        
          
    def draw(self, screen):
          pygame.draw.rect(
            screen, self.rand_color,
            pygame.Rect(self.x, self.y, SQUARE_SIZE,
                        SQUARE_SIZE))  
    '''  pygame.draw.rect(
            screen, constants.WATER_COLOR,
            pygame.Rect(self.x, self.y, constants.SQUARE_SIZE,
                        constants.SQUARE_SIZE))
'''
'''
class Water:

    def __init__(self, x_input, y_input):
      # Variables for animation
      self.current_anim = 0
      self.anim_counter = 0
      self.animation_speed = 10
      self.flip = False

      
      self.image_list = [pygame.image.load("Water_sampleC1.png"), pygame.image.load("Water_sampleC2.png"), pygame.image.load("Water_sampleC3.png"),
                         pygame.image.load("Water_sampleC1.png")]
      self.image = self.image_list[self.current_anim]
      self.rect = self.image.get_rect()
      self.rect.x = x_input
      self.rect.y = y_input

    def draw(self, screen):
      # Updates the animation frames
      self.anim_counter += 1


      #if (self.rect.y ==          
      #print("Y dimension:" +str(self.rect.y))
      if self.anim_counter >= 15: #speed of animation
        self.current_anim += 1 #how many animations there are
        self.anim_counter = 0

      if self.current_anim == len(self.image_list):
        self.current_anim = 0

      if (self.rect.y == 320 or self.rect.y == 200 or self.rect.y == 120):
          self.flip = True
      if (self.rect.y == 280):
          self.flip = False
      screen.blit(pygame.transform.flip(self.image_list[self.current_anim], self.flip, False), self.rect)       
      #screen.blit(self.image_list[self.current_anim], (self.rect.x, self.rect.y))'''

class SafeGrass:

    def __init__(self, x_input, y_input):
        self.x = x_input
        self.y = y_input
        self.size = SQUARE_SIZE
        self.color = (0, 155, 0)  # Color of safe grass

    def draw(self, screen):
        pygame.draw.rect(screen, self.color,
                         pygame.Rect(self.x, self.y, SQUARE_SIZE,
                                     SQUARE_SIZE))  # Draws grass



class Rain(pygame.sprite.Sprite):
    def __init__(self, x_input, y_input):
      super(). __init__()
      # Variables for animation
      #self.current_anim = 0
      #self.anim_counter = 0
      #self.animation_speed = 10
      #self.flip = False
      
      self.direction = pygame.math.Vector2(-2,4)
      # self.speed = random.randint(2,8)
      self.speed = abs(random.gauss(5, 1))
      
 
      self.image = pygame.image.load("Rain/rain_sample3.png")
      self.rect = self.image.get_rect()
      self.rect.x = x_input
      self.rect.y = y_input
      self.angle = -20
      self.pos = pygame.math.Vector2(self.rect.x, self.rect.y)
      
      """ Vector is used with speed to access the new updated x and y coordinates.

      Initial coords = (600, 0)
      vector = (-2,4)
      position = (600,0)
      random speed = 2
      new updated pos= (600,0) + (-2,4)*2
       => (594, 8)
       
      """
    def update(self):
          self.pos += self.direction *self.speed
          self.rect.x = round(self.pos.x)
          self.rect.y = round(self.pos.y)
    """Issue is self.rect.x and self.rect.y is not getting updated
    We need to extract the x and y coords from self.pos and assign them to self.rect.x and self.rect.y
    """
  
    def draw(self, screen):
        screen.blit(
                pygame.transform.rotozoom(self.image, self.angle, 1),
                self.rect)
        
'''
class SafeGrass:

    
    def __init__(self, x_input, y_input):
      self.image = pygame.image.load("Grass_sample2.png")
      self.rect = self.image.get_rect()
      self.rect.x = x_input
      self.rect.y = y_input

    def draw(self,screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))
      '''

class EndGrass(pygame.sprite.Sprite): #create sprite 

    def __init__(self, x_input, y_input):
        super().__init__()
        self.x = x_input
        self.y = y_input
        self.size = SQUARE_SIZE
        self.color = (250, 250, 210)  # Gold
        self.image = END_GRASS_SKIN_SPRITE
        self.rect = self.image.get_rect()
        self.rect.x = x_input
        self.rect.y = y_input
        self.hitbox = self.rect.inflate(-60,-20) # Changing the dimensions of the hitbox
        self.hitbox.y += 5

        self.showing_hitbox = False
        
        # self.hitbox.scale_by(0.5, 0.5)
        
  
    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

        # This line of code will draw the hitboxes
        if self.showing_hitbox: pygame.draw.rect(screen, (255, 0, 0), self.hitbox)
        
        """pygame.draw.rect(
            screen, self.color,
            self.rect)"""
      
    def test_collision(self, frog_object):
      return self.hitbox.colliderect(frog_object.rect)
      

class Sidewalk:

    def __init__(self, x_input, y_input):
        self.x = x_input
        self.y = y_input
        self.size = SQUARE_SIZE
        self.color = (105, 105, 105)  # Gray

    def draw(self, screen):
        pygame.draw.rect(
            screen, self.color,
            pygame.Rect(self.x, self.y, SQUARE_SIZE,
                        SQUARE_SIZE))

class Frog(pygame.sprite.Sprite):
    def __init__(self, color_input, x_input, y_input):
      super().__init__()
      self.x = x_input;
      self.y = y_input;
      self.color = color_input
      # This can probably be optimized/better organized
      if self.color == "purple":
        self.image = pygame.image.load("Frogger_main_skin/skin_BlueFrog_base.png")
      elif self.color == "green":
        self.image = pygame.image.load("Frogger_main_skin/skin_Classic_base.png")
        self.image = pygame.transform.flip(self.image, True, True).convert_alpha()

      self.rotating = True
      self.counter = 0
      

  #make a 
  
#make a loop where it rotates the frog left and then bottom
  
    def draw(self, screen):
      """if self.rotating == True:
        
        if self.counter == 50:
        self.image = pygame.transform.rotate(self.image, 90)
        elif self.counter == 100
        self.image = pygame.transform.rotate(self.image, 180)
        elif self.counter > 100
        self.rotating = False
        """

      
        
      screen.blit(self.image, (self.x, self.y))  