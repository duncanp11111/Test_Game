import pygame
import random

#Define some colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
movey = 3
movex = 3
asteroid_list = ""

x = random.randrange(700)
y = random.randrange(400)

#CLASSES

#Coin Class
class Coin(pygame.sprite.Sprite):
    def __init__(self, X, Y):
        
        # Call the parent class (Sprite) constructor
        super().__init__()
        
        self.image = pygame.Surface([10, 10])

        pygame.draw.circle(self.image, YELLOW, (0, 0), 30, 0)
        
        self.rect = self.image.get_rect()
        
        
#Asteroid class
class Asteroid(pygame.sprite.Sprite):
    def __init__(self):
        
        # Call the parent class (Sprite) constructor
        super().__init__()
    
        # Load the image
        self.image = pygame.transform.scale(pygame.image.load("star.bmp").convert(), (20, 20))
    
        # Set transparent color
        self.image.set_colorkey(BLACK)
        
        self.rect = self.image.get_rect() 
        self.movex = 3
        self.movey = 3
        
    def update(self):
            
        self.rect.x -= movex
        self.rect.y -= movey

#Player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        
        # Call the parent class (Sprite) constructor
        super().__init__()
    
        # Load the image
        self.image = pygame.transform.scale(pygame.image.load("Spaceship.bmp").convert(), (20, 20))
    
        # Set transparent color
        self.image.set_colorkey(WHITE)
        
        self.rect = self.image.get_rect()  
    def update(self):
        #Update player position
        #Get the current mouse position
        pos = pygame.mouse.get_pos()
        
        #Set the player's x and y positions to the mouses coordinates
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        
class SideWalls(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        
        self.image = pygame.Surface([10, 10])
        
        pygame.draw.line(self.image, BLACK, (0, 0), (0, 400), 1)
        pygame.draw.line(self.image, BLACK, (700, 0), (700, 400), 1)

        self.rect = self.image.get_rect() 
class TopWalls(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        
        self.image = pygame.Surface([10, 10])
        
        pygame.draw.line(self.image, BLACK, (0, 0), (700, 0), 1)
        pygame.draw.line(self.image, BLACK, (0, 400), (700, 400), 1)   
        
        self.rect = self.image.get_rect()     
        
#Create the window

#Initialize Pygame
pygame.init()
click_sound = pygame.mixer.Sound("coin.ogg")

#Set perameters for the screen
screen_width = 700
screen_height = 400
screen = pygame.display.set_mode([screen_width, screen_height])
background_image = pygame.image.load("space.jpg").convert()

#Define Font
font = pygame.font.Font(None, 36)

#Instructions
pygame.mouse.set_visible(False)
display_instructions = True
instruction_page = 1
name = ""
clock = pygame.time.Clock()
#Instruction Loop
done = False
while not done and display_instructions:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.unicode.isalpha():
                name += event.unicode
            elif event.key == pygame.K_BACKSPACE:
                name = name[:-1]
            elif event.key == pygame.K_RETURN:
                instruction_page += 1
                if instruction_page == 4:
                    display_instructions = False

    screen.blit(background_image, [0 , 0])
    
    if instruction_page == 1:
        """Draws title for the game"""
        text = font.render("Space Hopper", True, RED)
        screen.blit(text, [350, 200])
        
        text = font.render("Current High Score is: ", True, WHITE)
        screen.blit(text, [100, 250])
        
        text = font.render("10", True, WHITE)
        screen.blit(text, [360, 250])
        
    if instruction_page == 2:
        """Draws the instructions for page 1"""
        text = font.render("Instructions", True, WHITE)
        screen.blit(text, [10, 10])
        
        text = font.render("Enter your name: ", True, WHITE)
        screen.blit(text, [10, 40])     
        
        text = font.render(name, True, WHITE)
        screen.blit(text, [220, 40])
        
        text = font.render("Hit enter to continue", True, WHITE)
        screen.blit(text, [10, 80])
        
        text = font.render("Page 1", True, WHITE)
        screen.blit(text, [10, 120])      
        
    if instruction_page == 3:
        """Draws the instructions for page 2"""
        text = font.render("This program throws stars towards you.", True, WHITE)
        screen.blit(text, [10, 10])
        
        text = font.render("Avoid the stars and collect all of the coins to progress.", True, WHITE)
        screen.blit(text, [10, 40])
        
        text = font.render("Hit enter to continue", True, WHITE)
        screen.blit(text, [10, 80])        
        
        text = font.render("During the game, hit enter to end the game.", True, WHITE)
        screen.blit(text, [10, 120])
        
        text = font.render("Page 2", True, WHITE)
        screen.blit(text, [10, 160])        
    
    clock.tick(20)
     
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()    
    
#Sprite lists

#all spirtes
all_sprites_list = pygame.sprite.Group()

#List of each coin
coin_list = pygame.sprite.Group()

#List of each asteroid
asteroid_list = pygame.sprite.Group()

#List of walls
xwalls_list = pygame.sprite.Group()
ywalls_list = pygame.sprite.Group()

#Create Sprites
coin = Coin(200, 200)

coin.rect.x = random.randrange(700)
coin.rect.y = random.randrange(400)
#Add the coin to the coin list and the all sprites list
coin_list.add(coin)
all_sprites_list.add(coin)

for i in range(25):
    #Asteroid
    asteroid = Asteroid()  

    #Add the asteroid to the asteroid list and the all sprites list
    asteroid_list.add(asteroid)
    all_sprites_list.add(asteroid)    
    
    #Set start position for asteroid
    asteroid.rect.x = (screen_width - random.randrange(screen_width))
    asteroid.rect.y = (screen_height - random.randrange(screen_height))
        
#create player and add to all sprites list
player = Player()
all_sprites_list.add(player)
trashvar = True

sidewalls=SideWalls()
all_sprites_list.add(sidewalls)
xwalls_list.add(sidewalls)
topwalls=TopWalls()
all_sprites_list.add(topwalls)
ywalls_list.add(topwalls)

#Loop until closed
done = False

#Screen update speed 
clock = pygame.time.Clock()

#Set the score to 0
score = 0

#MAIN PROGRAM LOOP
while not done:
    #Process events
    for event in pygame.event.get():
        #in case of quit
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN or pygame.QUIT:
            
                file = open('highscores.txt', 'w')
                writescore = str(score) + "\n"
                writename = name + "\n"                   
                if score > highscores_list[0]:
                    highscores_list.insert(0, score)
                    highscores_list.insert(1, name)
                elif score <= highscores_list[0] and score > highscores_list[4]:
                    highscores_list.insert(2, score)
                    highscores_list.insert(3, name)
                elif score <= highscores_list[2] and score > highscores_list[6]:
                    highscores_list.insert(4, score)
                    highscores_list.insert(5, name)
                elif score <= highscores_list[4] and score > highscores_list[8]:
                    highscores_list.insert(6, score)
                    highscores_list.insert(7, name)
                elif score <= highscores_list[6] and score > highscores_list[10]:
                    highscores_list.insert(4, score)
                    highscores_list.insert(9, name)
                elif score <= highscores_list[8] and score > 0:
                    highscores_list.insert(10, score)  
                    hgihscores_list.insert(11, name)
                file.write(highscores_list)
                file.close
                
               
    #Game logic
    if asteroid.rect.x <= 0 or asteroid.rect.x >= 700:
        movex *= -1
    if asteroid.rect.y <= 0 or asteroid.rect.y >= 400:
        movey *= -1

    if score == 10 and trashvar:
        movex = 5
        movey = 5
        trashvar = False
    if score == 20 and not trashvar:
        movex = 10
        movey = 10
        trashvar = True
    if score == 30 and trashvar:
        movex = 30
        movey = 30
        trashvar = False    
    
    screen.blit(background_image, [0 , 0])
    all_sprites_list.draw(screen)
    pygame.display.flip()
    
    #Call the update method
    all_sprites_list.update()
    

    #for player in asteroid_list:
        
    
    #See if the player collided with an asteroid
    if pygame.sprite.spritecollide(player, asteroid_list, True):
        print ("Game Over")
        print ("Your score is:", score)        
        done = True
        
    if pygame.sprite.spritecollide(player, coin_list, False):
        score += 1
        print (score)
        coin.rect.x = random.randrange(700)
        coin.rect.y = random.randrange(400)
        click_sound.play()
        
    if pygame.sprite.spritecollideany(sidewalls, asteroid_list, False):
        movex *= -1
        
    if pygame.sprite.spritecollideany(topwalls, asteroid_list, False):
        movey *= -1
        
        
    clock.tick(60)
   
    pygame.display.flip()
   
        
           
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    