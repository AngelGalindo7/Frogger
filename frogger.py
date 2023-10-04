import pygame
from pygame.math import Vector2
from decimal import Decimal
from constants import SQUARE_SIZE, HEIGHT, WIDTH, WATER_ZONE_X, WATER_ZONE_Y
from enum import IntEnum
"""
Frogger file
Member variables:
w
x
y
speed
direction

"""
class DIR_FACE(IntEnum):
    UP = 0
    DOWN = 180
    LEFT = 90
    RIGHT = 270

class Frogger(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        self.vel = SQUARE_SIZE  #speed of movement
        # Counter  for flashing frogger
        self.skin_index = 0
        self.angle = 0
        self.hitchhiking = False
        self.at_end = False
        # List of skins
        self.skins = [
            pygame.image.load("Frogger_main_skin/skin_Classic_base.png"),
            #pygame.image.load("Frogger_main_skin/skin_OrangeFrog_base.png"),
            pygame.image.load("Frogger_main_skin/skin_BlueFrog_base.png"),
            pygame.image.load("Frogger_main_skin/skin_BlackFrog_base.png")
        ]

        # Loads Frogger image into this variable
        #self.image = pygame.Surface([constants.SQUARE_SIZE, constants.SQUARE_SIZE])
        #self.rect = self.image.get_rect()
        self.image = pygame.image.load(
            "Frogger_main_skin/skin_Classic_base.png")
        #self.image = pygame.image.load(
            #"Frogger_main_skin/skin_Classic_base.png")
        self.jump_image = pygame.image.load(
            "Frogger_main_skin/skin_Classic_base2.png")
        self.rect = self.image.get_rect()
        # 7 tiles from the left of the screen and 2 tiles from the bottom
        self.position = Vector2(Decimal(7 * SQUARE_SIZE), Decimal(HEIGHT - SQUARE_SIZE * 2))
        self.rect.x = self.position.x
        self.rect.y = self.position.y

        # For jumping animation
        self.just_jumped = False
        self.jumped_counter = 0

        # For bullets
        self.bullets = False

    def collision_detection(self, group, deltaTime):
        """
        Simplified down the collision code, and decreased the unnecessary repeat calls for collider checking.         Now it uses the direction
        stored inside the sprite to decide which direction it should move.

        Hopefully this cleans up this bit of code, and also allows it to be more flexible if we add more              objects the frog can stand on. 
        - Moth
        """
        collision_result = pygame.sprite.spritecollideany(self, group)
        if collision_result and collision_result.can_hitchhike():
            direction = 1 if collision_result.direction else -1
            self.position.x += collision_result.speed * direction * deltaTime
            self.rect.x = round(self.position.x)
            self.hitchhiking = True
        elif self.at_end:
            self.hitchhiking = True
        else:
          self.hitchhiking = False

    def drowning(self):
      if (WATER_ZONE_Y[0] <=self.rect.y <= WATER_ZONE_Y[1]):
        if(self.hitchhiking == False):
          print("Im standing on water")
          self.death_reset()
          return True
      return False
    """
  if movement:
    self.just_jumped = True
  
  In draw function:
    if self.just_jumped == True:
      draw Frogger with the jumped animation frame
    if self.just_jumped == False:
      draw Frogger normally
  
  In some other function that runs every frame:
    self.jumped_counter += 1
    if self.jumped_counter >= 0.5*FPS:
      self.just_jumped = False;
        self.jumped_counter = 0
    """
    """
  For goal grass determine if the frogger's x is within a interval(percentage) of the left and right hand side of that goal grass.
    Once you are within the goal grass, it teleports the frog to the center of the leaflet and rotates it so that it is 
  Technically you can touch death grass and youll still win. 
    """
    def get_input(self):
        x, y, shoot = 0, 0, 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                shoot = 1
            if event.type != pygame.KEYDOWN:
                continue

            if event.key == pygame.K_UP or event.key == ord('w'):
                y -= 1
            elif event.key == pygame.K_LEFT or event.key == ord('a'):
                x -= 1
            elif event.key == pygame.K_DOWN or event.key == ord('s'):
                y += 1
            elif event.key == pygame.K_RIGHT or event.key == ord('d'):
                x += 1

        return x, y, shoot
                
    
    def movement(self, game_over, deltaTime):
        x, y, shoot = self.get_input()
        
        # UP
        if y < 0:
            self.position.y -= self.vel
            self.angle = DIR_FACE.UP
            self.just_jumped = True
            if self.rect.y < SQUARE_SIZE:
                      # Telepeorts Frogger back right next to screen
                      self.rect.y = SQUARE_SIZE

        # DOWN
        elif y > 0:
            self.position.y += self.vel
            self.angle = DIR_FACE.DOWN
            self.just_jumped = True
            if self.rect.y > HEIGHT - 2 * (SQUARE_SIZE):
                self.rect.y = HEIGHT - 2 * (SQUARE_SIZE)
                
        # LEFT
        if x < 0:
            self.position.x -= self.vel
            self.angle = DIR_FACE.LEFT
            self.just_jumped = True
            if self.rect.x < 0:
                self.rect.x = 0
        
        # RIGHT
        elif x > 0:
            self.position.x += self.vel
            self.angle = DIR_FACE.RIGHT
            self.just_jumped = True
            if self.rect.x > WIDTH - SQUARE_SIZE:
                self.rect.x = WIDTH - SQUARE_SIZE
              
        self.rect.x = round(self.position.x)
        self.rect.y = round(self.position.y)
        if shoot and not game_over:
            print("I am out of ammo")

            self.bullet = self.create_bullet()
            self.bullets = True

    def death_reset(self):
        self.position = Vector2(Decimal(7 * SQUARE_SIZE), Decimal(HEIGHT - SQUARE_SIZE * 2))
        self.rect.x = self.position.x
        self.rect.y = self.position.y  # 7 tiles from the left of the screen
      # 2 tiles from the bottom of the screen self.rect.x = 7 * constants.SQUARE_SIZE # 7 tiles from the left of the screen

    def draw(self, screen):
        #pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(self.x, self.y + 5, 30, 30)) # Temporary - will change after image for Frogger
        #self.image = self.skins[self.skin_index %
                                #len(self.skins)]  # For flashing Frogger

      
        # Draws frogger onto screen
        #screen.blit(self.image, (self.rect.x, self.rect.y))
        """
    pygame.transform.rotozoom rotates based on the given angle which is defined based on the wasd value, scale is how big you want the frogger object to be. Scale of 1 is 1x while 0x would result in nothing. A super ability can change the frog to a scale of two and it could destroy anything in its path- A.G"""

        # Updates animation counter
        if self.just_jumped:
            self.jumped_counter += 1
            if self.jumped_counter >= 10:
                self.just_jumped = False
                self.jumped_counter = 0
                return

            screen.blit(
                pygame.transform.rotozoom(self.jump_image, self.angle, 1),
                self.rect)
        else:
            screen.blit(pygame.transform.rotozoom(self.image, self.angle, 1),
                        self.rect)
        #self.skin_index += 1 # For flashing Frogger

  
    def create_bullet(self):
        print("I have two guns now! JOY!")
        print("His head exploded! SUCH JOY!")

        return Bullet(self.rect.x, self.rect.y, self.angle)


class Bullet(pygame.sprite.Sprite):

    def __init__(self, pos_x, pos_y, angle):
        super().__init__()
        #self.image = pygame.Surface((5, 10))
        self.image = pygame.Surface((5, 10))
        #self.image.fill((51, 255, 255))
        self.image.fill((255, 40, 40))

        self.rect = self.image.get_rect(center=(pos_x, pos_y))

        self.rect.x = pos_x + 20
        self.rect.y = pos_y + 20
        self.angle = angle

    def update(self):
        if (self.angle == DIR_FACE.UP):
            self.rect.y -= 5
        if (self.angle == DIR_FACE.LEFT):
            self.rect.x -= 5
        if (self.angle == DIR_FACE.DOWN):
            self.rect.y += 5
        if (self.angle == DIR_FACE.RIGHT):
            self.rect.x += 5

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

