import pygame
from snake import *
from food import Food
pygame.init()
bounds = (300,300)
window = pygame.display.set_mode(bounds)
pygame.display.set_caption("Snake.")
block_size = 20
snake = Snake(block_size, bounds)
run = True
pygame.font.init()
font = pygame.font.SysFont('comicsans',60, True)

food = Food(block_size,bounds)
food.respawn()
score = 0
while run:
  pygame.time.delay(100-score)
  window.fill((0,0,0))
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False
  keys = pygame.key.get_pressed()
  if keys[pygame.K_LEFT]:
    snake.steer(Direction.LEFT)
  elif keys[pygame.K_RIGHT]:
    snake.steer(Direction.RIGHT)
  elif keys[pygame.K_UP]:
    snake.steer(Direction.UP)
  elif keys[pygame.K_DOWN]:
    snake.steer(Direction.DOWN)
  snake.move()
  #print(snake.check_for_food(food,score))
  score = snake.check_for_food(food,score)
  if score == None:
    score = 0
  fontscore = str(score)
  #print(score)
  #print(score)
  scoretext = font.render(fontscore, True, (255,255,255))
  window.blit(scoretext, (20,20))
  
  #snake.check_for_food(food,score)
  if snake.check_bounds() == True or snake.check_tail_collision() == True:
    window.fill((0,0,0))
    text = font.render('Git Gud lol', True, (255,255,255))
    fontscore = "Points: " + fontscore
    scoretext = font.render(fontscore, True, (255,255,255))
    window.blit(text, (20,80))
    window.blit(scoretext, (20,120))
    pygame.display.update()
    pygame.time.delay(1000)
    snake.respawn()
    food.respawn()
    score = 0

  
  
  snake.draw(pygame, window)
  food.draw(pygame, window)
  pygame.display.flip()
  window.blit(scoretext, (20,120))
  