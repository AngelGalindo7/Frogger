"""

Frogger
Developed by the Computer Science Club of Crafton Hills College
Developed in Spring 2022 & Spring 2023
An iteration of the arcade game "Frogger"

Game Designers: Angel Galindo, Noah Hensley, Joseph Godizen, Kyonosuke Watanabe
Lead Game Programmer: Noah Hensley
Game Programmers: Angel Galindo, Measured Moth, Jakob Barringer, Joseph Godinez, Adrian Toquero
Graphic Designer: Angel Galindo

"""


#----------------------------------
import pygame, time  # Pygame is used for any function that affects the GUI(display)

from frogger import Frogger  # Importing different classes from different files
"""
Will delete this code once I know using an all-import instead of these will not cause an error -Noah H

from immovable_object import Water  # from <filename> import <classname>
from immovable_object import SafeGrass
from immovable_object import Sidewalk
from immovable_object import EndGrass
from immovable_object import Rain
from immovable_object import Frog
"""
from immovable_object import *

# from immovable_object import *

#import moveable_object import Rain
from moveable_object import Vehicle, Turtle, Log, VEHICLES, TURTLES, LOGS

from text import HighScoreText
from text import TimerText
from text import LivesText
from text import NormalScoreText

from constants import FPS, WATER_X, WATER_Y, WIDTH, HEIGHT, GAME_SQUARE_HEIGHT, GAME_SQUARE_WIDTH, SQUARE_SIZE, DEBUG_TOGGLE
import time
import random

#----------------------------------------------

pygame.init() # Initiates the GUI(display)

# Constants BEGIN

# Divide game into squares: 16 by 20
# Each square dimension: 40 by 40

BACKGROUND_COLOR = (0, 0, 0)  # RGB value for black
LANES = 14

# Constants END

screen = pygame.display.set_mode([WIDTH,HEIGHT]) # This variable will be used whenever drawing something onto the GUI

"""
Classes:
Frogger
Vehicle
Log
Safe Grass
Goal Grass
Turtle
Jogger
Snake
Water
Timer
Lives
High and Normal scores
BonusFrog
Camera Movement
Map Generation
"""

"""
This is old code that I (Noah) was testing for playing music & sound effects (probably doesn't work in Replit)

# Starting the mixer
pygame.mixer.init()
  
# Loading the song
pygame.mixer.music.load("sounds/level_music.mp3")
  
# Setting the volume
pygame.mixer.music.set_volume(0.7)
  
# Start playing the song
pygame.mixer.music.play()

# Testing music over
"""

# Clock for retrieving & attempting to maintain FPS
clock = pygame.time.Clock()
previous_time = time.time()

# Variables for the timer bar
beginning_time = time.time()
game_over_time = 90 # 1 minute 30 seconds
# game_over_time = 10 # For testing purposes

"""
Key for 2D MAP list:
0 = road
1 = goal grass
2 = water
3 = safe grass
4 = sidewalk
5 = high scores 
6 = timer stuff
7 = normal score
8 = lives
"""

# Mapping the whole board
MAP = [[0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0],
       [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
       [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
       [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
       [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
       [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
       [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
       [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
       [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
       [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
       [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
       [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
       [0, 0, 0, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

# Creating objects
frog_object = Frogger()
water_object = Water(WATER_X, WATER_Y)
snakes = []  # Starting to create empty lists for objects (some are normal lists, others are sprite groups to hold sprite objects)
timer = TimerText()
vehicles = pygame.sprite.Group()
logs = pygame.sprite.Group()
grasses = pygame.sprite.Group()
safe_grasses = []
goal_grasses = []
joggers = []
turtles = pygame.sprite.Group()
bullets = pygame.sprite.Group()
droplets = pygame.sprite.Group()
frogs = pygame.sprite.Group()
waters = []
sidewalk = []
highScore = []
normalScore = []
lifeTracker = []

def lose_life():
  if len(frogs.sprites()) > 0:
    frogs_sprites_list = frogs.sprites()
    frogs_sprites_list.pop(len(frogs.sprites())-1)
    frogs.empty()
    frogs.add(*frogs_sprites_list)

def show_gameover():
  
  print("ITSSSSS")
  
# Looping through map & putting each element from the 2D list into their respective lists
for row_num in range(len(MAP)):  # row
    for tile_num in range(GAME_SQUARE_WIDTH):  # column
        x_coord = tile_num * SQUARE_SIZE
        y_coord = row_num * SQUARE_SIZE
        test_val = MAP[row_num][tile_num]
        if test_val == 1:  # goal grass
            new_object = EndGrass(x_coord, y_coord)
            goal_grasses.append(new_object)
        elif test_val == 2:  # water
            new_object = Water(x_coord, y_coord)
            waters.append(new_object)
        elif test_val == 3:  # safe grass
            new_object = SafeGrass(x_coord, y_coord)
            safe_grasses.append(new_object)
        elif test_val == 4:  # sidewalk
            new_object = Sidewalk(x_coord, y_coord)
            sidewalk.append(new_object)
        elif test_val == 5:  # high scores
            new_object = HighScoreText(x_coord, y_coord)
            highScore.append(new_object)
        # elif test_val == 6:  # timer
            # timer = TimerText(x_coord, y_coord)
        elif test_val == 7:  # normal score
            new_object = NormalScoreText(x_coord, y_coord)
            normalScore.append(new_object)
        elif test_val == 8:  # lives tracker
            new_object = LivesText(x_coord, y_coord)
            lifeTracker.append(new_object)


# Each lane will have three variables: a counter that increments per frame to keep track of time, a variable to keep track of how many cars
# have spawned in the group, and a "phase" string that determines whether or not the lane will spawn a vehicle, wait to spawn another vehicle, or wait to spawn another group of 3 vehicles
lane_properties = []
for a in range(LANES): # LANES is a constant (6)
  lane_properties.append([0.0, 0, "group_separation"])
  
# Elements: counter, cars_spawned, phase
# Phases: spawn, car_separation, group_separation

car_separation_max_ticktock = 6 * FPS # 2 seconds - amount of time that passes between each car in a group spawning
group_separation_max_ticktock = 8 * FPS # 6 seconds - amount of time that passes between groups of cars spawning

"""
Current issues:
Clock function: spawns vehicle one by one
At the start of the game you need: All vehicles on the screen

Solutions:
Spawn vehicles manually then the clock function operates 
"""

# Last-minute variables before we enter the main game loop
list_display_counter = 0
list_display_counter_max = FPS * 1
clockfps = 0
listcounter = 0 
total = 0
fpslist = []
vehicles_lane_num = 0
logs_lane_num = 0
turtles_lane_num = 0
lane_num_type = 0
type = "None"
object_type = []
death_counter = 0
counterr = 0
random_number = 0
timeAtLastFrame = time.time()
rainy_day = False
# Main game loop
in_game = True
game_over = False
# Randomizes whether or not there will be rain
rand_num = random.randint(1,3)
delta_time = 0
print(rand_num)

if (1 <= rand_num <= 3):
  rainy_day = True

frog_gap = 44
for x in range(0, frog_gap*3, frog_gap):
  frogs.add(Frog("purple", x,760))

x_endgrasses = 80
for x in range(0, x_endgrasses*10,x_endgrasses):
  grasses.add(EndGrass(x,40))

clock.tick(FPS)

while in_game:
  # Fresh canvas
  screen.fill(BACKGROUND_COLOR)  # Draws background
  vehicles_lane_num = 0
  logs_lane_num = 0
  turtles_lane_num = 0
  # Spawning code begins    
  # In miliseconds
  
  
  for lane_num in range(len(lane_properties)): # Goes through each lane
    
    # Temporary while the jogger doesn't exist
    if lane_num == 6:
      continue

    # Assigns unique variables
    if lane_num <6:  
      object_type = VEHICLES
      lane_num_type = vehicles_lane_num
      type = "vehicles"
      #print("The dog is a great responsibility Samantha")
    elif lane_num in [7, 10, 12]:
      object_type = TURTLES
      lane_num_type = turtles_lane_num
      
      type = "turtles"
    elif lane_num in [8, 9, 11, 13]:
      object_type = LOGS
      lane_num_type = logs_lane_num
      type = "logs"


    """
      Assignment of the type based on the lane requires the use of a variable object_group to make the access of the type of list dynamic making the clock universal for all vehicles, turtles and logs
      lane_num_type at the bottom of the code has to be dependent on the type of moeveable object i.e(vehicle, log, and turtle)
      If its vehicle the new lane_num_type would be from 0 to 5
      If its log the new lane_num_type would be from 0 to 3 
      If its turtle the new lane_num_type would be from 0 to 2

      This is because this is the length of the VEHICLES TURTLES AND LOGS
      superceeding the length will make the program acess an undefined index value for the list 
      The lane_num_type at the bottom increments for every for iteration
      so we should have specific variables for each type of moveable object
      in the beginning before the for loop set to 0.
      During the for loop the specific variable for the type of moveable object which is focused on for the iteration(which is dependent on the number lane 0-14) gets incremented, which would keep track of each individual moveable object type when its it's own turn. At the end of the for loop iterations each specific variable would be at its max
      vehicle_lane_num = 5
      log_lane_num = 3
      turtle_lane_num = 2
      
      A type string will be assigned in the assignment of variables depending on which lane is being considered
      and at the end of the iteration, the type string will be used to distinguish which moveable object type was used for the iteration and it will create a increment on the specific variable. Depending on the type of moveable object it will reset it to zero if it reaches the max 
      A.G-still working on it
      Update: I realized lane_properties must reference lane_num as if you try to make it reference lane_num_type you would overlap the clocks for different moveable objects
      Update: The clock is finished and is now considered universal as shown in the console output. The structure of the clock can now incorporate the jogger and the purple frog considering the list is similar to an extent. The purple frog will require considerations with possibly creating a list for each water lane 
      Update: The collision works also with the water lane object types. There is also a weird slowing down as vehicles,logs and turtles reach x coordinate zero. I suspect it might be a rounding issue?  -A.R.A
      """
    
    if lane_properties[lane_num][2] == "spawn": # If the "phase" of the lane is to spawn a vehicle
      # Creates the moving object
      if lane_num < 6:
        vehicles.add(Vehicle(lane_num_type))# Creates the vehicle
        #print("What are you doing with fluffy")
      elif lane_num == 7 or lane_num == 10 or lane_num == 12:
        ##print(lane_num_type)
        turtles.add(Turtle(lane_num_type))
        #print("Dr Maxis we are successful")
      elif lane_num == 8 or lane_num == 9 or lane_num == 11 or lane_num == 13:
       logs.add(Log(lane_num_type))
       #print("The test subjects have survived telportation")

      lane_properties[lane_num][1] += 1 # Increments the variable that stores number of cars that have spawned in group
      if lane_properties[lane_num][1] >= object_type[lane_num_type][1]: # If the number of sprites is greater or equal to the max in group
        lane_properties[lane_num][1] = 0 # Resets variables that stores number of sprites in a group
        lane_properties[lane_num][2] = "group_separation" # Goes to phase where lane waits for a time between groups
      else: # If the number of cars that have spawned is less than 3
        lane_properties[lane_num][2] = "car_separation" # Goes to phase where lane waits for 2 seconds for separation between cars in group
    elif lane_properties[lane_num][2] == "car_separation": # If the "phase" of the lane is waiting between cars in a car group
      lane_properties[lane_num][0] += delta_time # Increments counter
      #print("Subject is within the test chamber activate power")
      if lane_properties[lane_num][0] >= object_type[lane_num_type][5]: # If 2 seconds have passed...
        lane_properties[lane_num][0] = 0 # Resets counter
        lane_properties[lane_num][2] = "spawn" # Goes to phase where the lane spawns a vehicle
    elif lane_properties[lane_num][2] == "group_separation": # If the "phase" of the lane is waiting between car groups
      lane_properties[lane_num][0] += delta_time # Increments counter

      if lane_properties[lane_num][0] >= object_type[lane_num_type][6]: # If 6 seconds have passed...
        lane_properties[lane_num][0] = 0 # Resets counter
        lane_properties[lane_num][2] = "spawn" # Goes to phase where lane spawns a vehicle
        
    if (type == "vehicles"):
      
      #print(vehicles_lane_num)
      vehicles_lane_num +=1
      if (vehicles_lane_num >= 6):
        vehicles_lane_num = 0
    elif(type == "turtles"):
      #print(turtles_lane_num)
      turtles_lane_num += 1
      
      if (turtles_lane_num>= 3):
        turtles_lane_num = 0
      #print("Max ammo")
    elif(type == "logs"):
      logs_lane_num +=1
      if (logs_lane_num >= 4):
        logs_lane_num = 0
      #print("I order you")
  
          
  
  # Spawning code ends
  
  # A bunch of code
  #print("Bring me another")
  #print(lane_properties)

  frog_object.movement(game_over, delta_time)  # Takes in keyboard input for the frog

  if (frog_object.bullets):
    bullets.add(frog_object.bullet)
    # bullets.add(Bullet(frog_object.rect.x, frog_object.rect.y, frog_object.angle))
  
    #bullet = frog_object.create_bullet()
    #bullets.add(bullet)

  # Code for spawning rain
  random_number = random.randint(1,2)
  random_number_x = random.randint(0, 1200) # Original upper bound: 720
  
  if (random_number == 1  and rainy_day):
    droplets.add(Rain(random_number_x, 20))
    
  
  # Drawing all moving objects
  for water in waters:  # Draws the water
    water.draw(screen)
  for sidewalk_ind in sidewalk:  # Draws the sidewalks
    sidewalk_ind.draw(screen)
  for safe_grass in safe_grasses:  # Draws the sidewalks
    safe_grass.draw(screen)
  for goal_grass in goal_grasses:
    goal_grass.draw(screen)
  for vehicle in vehicles:
    if vehicle.rect.x < -90 or vehicle.rect.x > 650 :
       vehicle.kill()
    vehicle.movement(delta_time)
    pygame.sprite.groupcollide(bullets, vehicles, True, True)
    vehicle.draw(screen)
  for turtle in turtles:
    if turtle.rect.x < -90 or turtle.rect.x > 650:
       turtle.kill()
    turtle.movement(delta_time)
    pygame.sprite.groupcollide(bullets, turtles, True, True)
    turtle.draw(screen)
  for log in logs:
    if log.rect.x < -90 or log.rect.x > 650:
       log.kill()
    log.movement(delta_time)
    pygame.sprite.groupcollide(bullets, logs, True, True)
    log.draw(screen)

  for bullet in bullets:
    if bullet.rect.x < - 90 or bullet.rect.x > 650 or bullet.rect.y > 820 or bullet.rect.y < 0:
      bullet.kill()
    bullet.update()
    bullet.draw(screen)
  for rain in droplets:
      if rain.rect.x < - 90 or rain.rect.x > 900 or rain.rect.y > 820 or rain.rect.y < -10:
        rain.kill()
      
      rain.update()
      rain.draw(screen) 
  for Endgrass in grasses:
    Endgrass.draw(screen)
  for individual_frog in frogs:
    individual_frog.draw(screen)

  if not game_over: frog_object.draw(screen)# Draws the frog overlaps the background and the cars

  if (counterr == 100):
    #print(bullets)
    counterr = 0

  counterr += 1

  # Tests if the Frogger collided with any of the hitboxes of the goal grass
  end_collided = False
  for Endgrass in grasses:
    end_collided = Endgrass.test_collision(frog_object)
    if end_collided:
      # This variable keeps track of which endgrass the Frogger collided with
      end_grass_collided_with = Endgrass
      break
    else:
      frog_object.at_end = False
  if end_collided:
    # The frog_object.at_end variable may be unused
    
    # Resets the time
    beginning_time = time.time()
    # Makes the bar green again
    timer.color = timer.green_color

    # Resets the Frogger's position when it completes the level
    #frog_object.rect.x = 7 * SQUARE_SIZE  # 7 tiles from the left of the screen
    #frog_object.rect.y = HEIGHT - SQUARE_SIZE * 2  # 2 tiles from the bottom of the screen
    frog_object.death_reset()

    # Places a pseudo-frog where the Frogger collided with the end grass
    frogs.add(Frog("green", end_grass_collided_with.hitbox.x - 10, end_grass_collided_with.hitbox.y - 10))
    
  
 # print(Droplets)
  """I have implemented three total functions here. 
  collision_detection is in the frog object and it checks to see if the frog object touches the turtles or logs, with there being a increment or decrease of its x position based on if it was a turtle or log. Incorporation of the specific speed of that turtle/log would be necessary into the variable of the increment/decrease of the x position of the frog to cause the changing velocity to match that of the specific turtle and log
  
  This spritecollideany is meant to check if there is a collision between the frog and vehicle, if there is, a death counter is incremented where soon after the death_counter would reach 10 and it would call the frog_object.death_reset() function which spawns the frog to the beginning of the map. -A.G
  
  Update: I will plan to implement these in the frogger class to keep the main more tidy. With this in mind, I believe we should also think about reallocating the universal timer to its own specified class but its not neccessary. Also the implementation of the run-over animation should be done when the death_counter ticker is reached. Also lives should be implemented to decrease everytime a death happens- A.R.A"""
  frog_object.collision_detection(pygame.sprite.Group(turtles.sprites() + logs.sprites()), delta_time)
    

  if frog_object.drowning():
    frog_object.kill()
    death_counter +=5
    print("Hey you dieeed")
    
    # Frog.kill()

  
  #if (pygame.sprite.spritecollideany(frog_object, logs)):
  # print logs[pygame.sprite.spritecollideany(frog_object, logs)]
  #example_log = pygame.sprite.spritecollideany(frog_object, logs)
  #print(example_log.log_properties)
  if pygame.sprite.spritecollideany(frog_object, vehicles):
    #print("Blood...Blood...BLOOD!!")
    frog_object.kill()
    death_counter += 1
  """if pygame.sprite.spritecollideany(frog_object, grasses.hitbox?)
  
  """

  if (death_counter >= 5):
    lose_life()
    print("YOUHHHHHHHHHHHHHHHHHHHHHHHHHH DIED")
    
    # Resets the time
    beginning_time = time.time()

    # Kills Frogger
    frog_object.death_reset()
    frog_object.kill()
    death_counter = 0

  if (len(frogs.sprites()) <= 0):
    game_over = True
    my_font2 = pygame.font.SysFont('Comic Sans MS', 50)
    gameover_text = "GAME OVER"
    gameover_text_surface = my_font2.render(gameover_text, False, (255, 255, 255))
    screen.blit(gameover_text_surface, (WIDTH/2 - 100, HEIGHT/2 ))
    frog_object.kill()

  
      



 
  """ 
  pop up game over screen while the cars and vehicles continue playing. Until you pick a option(play again      or quit itll have two options)
  """

    
  #pygame.sprite.groupcollide(bullets, vehicles, True, True)
  #blocks_hit_list = pygame.sprite.spritecollide(frog_object, vehicles, True)
  #f pygame.sprite.spritecollide
  #blocks_hit_list = pygame.sprite.spritecollide(frog_object, turtles, True)
  #blocks_hit_list = pygame.sprite.spritecollide(frog_object, logs, True)
  # if (blocks_hit_list) 
  # print(frog_object + vehicle)
  """
  for vehicle in vehicles:
    if pygame.sprite.collide_rect(vehicle, frog_object):
      print("We have collided!")
  """
  # Testing
  """
  list_display_counter += 1
  if list_display_counter >= list_display_counter_max:
    for vehicle in blocks_hit_list:
      print(str(vehicle.rect))
    print()
    list_display_counter = 0
  """
    
  # Draws the coordinates of frog
  my_font = pygame.font.SysFont('Comic Sans MS', 30)
  text_surface = my_font.render(str(frog_object.rect.x) + ", " + str(frog_object.rect.y), False, (255, 255, 255))
  screen.blit(text_surface, (0,0))

  # Draws the fps
  fps_text = "FPS: " + str(clock.get_fps())
  fps_text_surface = my_font.render(fps_text, False, (255, 255, 255))
  screen.blit(fps_text_surface, (WIDTH - 300, 0))

  #Draws time
  time_text = "TIME"
  time_font = pygame.font.SysFont('Comic Sans MS', 30)
  time_text_surface = time_font.render(time_text, False, (255, 255, 255))
  screen.blit(time_text_surface, (268, 757))
  
  # Testing - draws car sample next to Frogger
  #screen.blit(car_sample, (210, 440))
  current_time = time.time()
  percentage_time = 1 - ((current_time - beginning_time) / game_over_time)
  timer.draw(screen, percentage_time)

  # Code for killing the Frogger when the timer runs out
  if timer.times_up(percentage_time):
    # Resets the time
    beginning_time = time.time()
    # Makes the bar green again
    timer.color = timer.green_color
    
    lose_life()
    print("YOUHHHHHHHHHHHHHHHHHHHHHHHHHH DIED")
    frog_object.death_reset()
    frog_object.kill()
    death_counter = 0
  
  clock.tick(64)

  delta_time = clock.tick(FPS) / 1000.0
  
  pygame.display.flip()  # Not sure what it does, makes display work

# Quits the GUI application once if the main game loop is terminated
pygame.quit()
