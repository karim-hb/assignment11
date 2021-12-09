import pygame , sys , random
from pygame.math import Vector2


class Fruit:
    def __init__(self):
        self.randomize()
    
    def draw(self):
        fruits_rect = pygame.Rect(self.position.x*cell_size,self.position.y*cell_size,cell_size,cell_size)
        screen.blit(APPLE,fruits_rect)
        #pygame.draw.rect(screen,(0,0,0),fruits_rect)
        
    def randomize(self):
        self.x = random.randint(0,cell_size-1)
        self.y = random.randint(0,cell_size-1)
        self.position = Vector2(self.x,self.y)        
        
        
class POPO:
    def __init__(self):
        self.randomize()
    
    def draw(self):
        fruits_rect = pygame.Rect(self.position.x*cell_size,self.position.y*cell_size,cell_size,cell_size)
        screen.blit(popo,fruits_rect)
        
    def randomize(self):
        self.x = random.randint(0,cell_size-1)
        self.y = random.randint(0,cell_size-1)
        self.position = Vector2(self.x,self.y)   

class Snake():
    def __init__(self):
        self.body = [Vector2(5,10),Vector2(4,10),Vector2(3,10)]
        self.direction = Vector2(1,0)        
        self.add_block = False
        self.remove_block = False
        self.stop = False
        
    def draw(self):
        for block in self.body:
           snak_rect = pygame.Rect(block.x*cell_size,block.y*cell_size,cell_size,cell_size)
           pygame.draw.rect(screen,(120,120,120),snak_rect) 
    
    def move(self): 
        if len(self.body) == 1 : 
              pygame.quit()
              sys.exit()   
        if self.add_block == False and self.stop == False:
             copy_body = self.body[:-1]
             copy_body.insert(0,copy_body[0]+self.direction)
             self.body = copy_body[:] 
        if self.remove_block == True:
             copy_body = self.body[:]
             copy_body.pop(0)
             self.body = copy_body[:] 
             self.remove_block = False      
        if self.add_block == True:
             copy_body = self.body[:]
             copy_body.insert(0,copy_body[0]+self.direction)
             self.body = copy_body[:]      
             self.add_block = False      
      
        
class Main():
    def __init__(self):
        self.snake = Snake()
        self.fruit = Fruit()   
        self.popo = POPO()
        self.show_reset = False   
    
    def update(self):
         self.snake.move()
         self.check_game()
         self.roles()
         
    
    def draw(self):
        self.draw_grass()
        self.snake.draw()
        self.fruit.draw()
        self.popo.draw()
        self.draw_score()
        if self.show_reset == True:
            self.game_over_msg()

       
    
    def check_game(self):
        if self.fruit.position == self.snake.body[0]:
            self.fruit.randomize()
            self.snake.add_block = True      
        if self.popo.position == self.snake.body[0]:
            self.popo.randomize()
            self.snake.remove_block = True  
    def roles(self):
        if not 0 <= self.snake.body[0].x < cell_numbers or not 0 <= self.snake.body[0].y < cell_numbers :
            self.game_over()
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()
                
                
    def game_over(self):
              
             self.show_reset = True
    
    def game_over_msg(self):
              score_text = "Game over  ... "
              score_surface = game_font.render(score_text,True,(0,0,0))
              score_rect = score_surface.get_rect(center=(200,300))
              screen.blit(score_surface,score_rect)
              
              self.snake.stop = True      
            
    def draw_grass(self):
        for row in range(cell_numbers):
            if row % 2 == 0:
                for col in range(cell_numbers):
                    if col % 2 == 0:
                        grass_rect = pygame.Rect(col*cell_size,row*cell_size,cell_size,cell_size)
                        pygame.draw.rect(screen,(67,238,73),grass_rect)
            else:
                 for col in range(cell_numbers):
                    if col % 2 != 0:
                        grass_rect = pygame.Rect(col*cell_size,row*cell_size,cell_size,cell_size)
                        pygame.draw.rect(screen,(67,238,73),grass_rect)
    
    
    def draw_score(self):
        score_text = str(len(self.snake.body)-3)
        score_surface = game_font.render(score_text,True,(0,0,0))
        score_x = int(cell_size * cell_numbers -40 )
        score_y = int(cell_size * cell_numbers -60 )
        score_rect = score_surface.get_rect(center=(score_x,score_y))
        apple_rect = APPLE.get_rect(midright=(score_rect.left,score_rect.centery))
        bg_rect = pygame.Rect(apple_rect.left,apple_rect.top,apple_rect.width + score_rect.width ,apple_rect.height)
        
        pygame.draw.rect(screen,(120,120,120),bg_rect)
        screen.blit(score_surface,score_rect)
        screen.blit(APPLE,apple_rect)


              
pygame.init()
cell_size = 20
cell_numbers =30
screen = pygame.display.set_mode((cell_size*cell_numbers,cell_size*cell_numbers))
clock = pygame.time.Clock()

APPLE = pygame.image.load('attachmeny/apple.png').convert_alpha()
APPLE = pygame.transform.scale(APPLE, (20, 20)) 

popo = pygame.image.load('attachmeny/PngItem_1255256.png').convert_alpha()
popo = pygame.transform.scale(popo, (20, 20)) 

SCREEN_UPDATER = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATER,150)

game_font = pygame.font.SysFont("comicsansms", 24)

mian_game = Main()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == SCREEN_UPDATER:
            mian_game.update()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if mian_game.snake.direction.y != 1:
                     mian_game.snake.direction = Vector2(0,-1)
            if event.key == pygame.K_DOWN:
                if mian_game.snake.direction.y != -1:
                    mian_game.snake.direction = Vector2(0,+1)
            if event.key == pygame.K_RIGHT:
                if mian_game.snake.direction.x != -1:
                     mian_game.snake.direction = Vector2(+1,0)
            if event.key == pygame.K_LEFT:
                if mian_game.snake.direction.x != 1:
                    mian_game.snake.direction = Vector2(-1,0)
            if event.key == pygame.K_SPACE:
                 
                   mian_game.snake.body = [Vector2(5,10),Vector2(4,10),Vector2(3,10)]
                   mian_game.show_reset = False
                
        
    screen.fill((73,233,137))
    mian_game.draw()
    pygame.display.update()
    clock.tick(60) 