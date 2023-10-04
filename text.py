import pygame
"""
This file will included classes like normal score, high score, timer, lives, etc
"""
class TimerText:
  def __init__(self):
    self.image = pygame.Rect(360, 765, 160, 30) # x, y, width, height
    self.green_color = (0, 255, 0)
    self.red_color = (255, 0, 0)
    self.white_color = (255, 255, 255)
    self.color = self.green_color
    self.line_color = self.white_color
    self.x = self.image.x
    self.y = self.image.y
    self.original_width = self.image.width

    self.TURN_RED_PERCENTAGE = 0.3

  
  def draw(self, screen, percentage_scale):
    '''self.image = pygame.transform.scale(self.image, (self.original_width * percentage_scale, 30))'''
    self.image.width = self.original_width * percentage_scale
    # screen.blit(self.image, (self.x, self.y))

    # Makes bar red when it is below 20%
    if self.color == self.green_color and percentage_scale <= self.TURN_RED_PERCENTAGE: self.color = self.red_color

    # Draws white lines around the bar
    pygame.draw.line(screen, self.line_color, (self.image.x-1, self.image.y-1), (self.image.x+self.original_width, self.image.y-1), 1)
    pygame.draw.line(screen, self.line_color, (self.image.x-1, self.image.y+self.image.height), (self.image.x+self.original_width, self.image.y+self.image.height), 1)
    pygame.draw.line(screen, self.line_color, (self.image.x-1, self.image.y-1), (self.image.x-1, self.image.y+self.image.height), 1)
    pygame.draw.line(screen, self.line_color, (self.image.x+self.original_width, self.image.y-1), (self.image.x+self.original_width, self.image.y+self.image.height), 1)
    
    pygame.draw.rect(screen, self.color, self.image)
    pass

  # Determines whether or not time is up
  def times_up(self, percentage_scale):
    if percentage_scale <= 0: return True
    else: return False

class ScoreText:
  def __init__(self,x_input, y_):
    pass
    
class LivesText:
  def __init__(self, x_input, y_input):
    pass
  
  def draw(self, screen):
    pass

class HighScoreText:
  def __init__(self, x_input, y_input):
    pass
  
  def draw(self, screen):
    pass

class NormalScoreText:
  def __init__(self, x_input, y_input):
    pass
  
  def draw(self, screen):
    pass
