import pygame
import random

#Define some colours and other variables
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
movey = 3
movex = 3
x = random.randrange(700)
y = random.randrange(400)
display_game_over = False

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
#Wall Class       
class Wall(pygame.sprite.Sprite):
    """ Class to represent the bounds of the level """
    #Initiate class
    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
#Functions to add walls to existing lists
def add_wallx(x, y, width, height):
    """ Places a wall and adds it to the appropriate class lists for sprite collision uses """
    wallx = Wall(x, y, width, height)
    wall_listx.add(wallx)
    all_sprites_list.add(wallx)
def add_wally(x, y, width, height):
    """ Places a wall and adds it to the appropriate class lists for sprite collision uses """
    wally = Wall(x, y, width, height)
    wall_listy.add(wally)
    all_sprites_list.add(wally)
#Create the window

#Initialize Pygame
pygame.init()
click_sound = pygame.mixer.Sound("coin.ogg")
click_sound1 = pygame.mixer.Sound("SunsetLover.ogg")


#Set perameters for the screen
screen_width = 700
screen_height = 400
screen = pygame.display.set_mode([screen_width, screen_height])
background_image = pygame.image.load("space.jpg").convert()

#Define Font
font = pygame.font.Font(None, 36)
font1 = pygame.font.Font(None, 72)
#Instructions
pygame.mouse.set_visible(False)
display_instructions = True
instruction_page = 1
name = ""
clock = pygame.time.Clock()

try: 
    file = open('highscores.txt', 'r')
except:
    file = open('highscores.txt', 'w')
    file.write("Empty\n0\nEmpty\n0\nEmpty\n0\nEmpty\n0\nEmpty\n0")
    file.close()
    file = open('highscores.txt', 'r')
finally:
    iterate = 0
    highscore_list = []
    name_list = []
    for line in file:
        iterate += 1
        if iterate % 2 == 0:
            highscore_list.append(line)
        else: 
            name_list.append(line)
    file.close()

# Clean up the lists containing the names and the scores
for i in range(len(highscore_list)):
    highscore_list[i].replace("\n", "")
    highscore_list[i] = int(highscore_list[i])
    
for i in range(len(name_list)):
    name_list[i] = name_list[i].replace("\n", "")
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
    #Welcome screen
    if instruction_page == 1:
        """Draws title for the game"""
        text = font1.render("Space Hopper", True, RED)
        screen.blit(text, [200, 200])
    #1st Instruction Page
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
    #2nd Instruction Page
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
wall_listx = pygame.sprite.Group()
wall_listy = pygame.sprite.Group()

#Create Coin
coin = Coin(200, 200)
coin.rect.x = random.randrange(700)
coin.rect.y = random.randrange(400)

#Add the coin to the coin list and the all sprites list
coin_list.add(coin)
all_sprites_list.add(coin)

#Add walls
add_wallx(0, 0, 5, 400)
add_wally(0, 0, 700, 5)
add_wally(0, 400, 700, 5)
add_wallx(700, 0, 5, 400)


for i in range(20):
    #Asteroid
    asteroid = Asteroid()  

    #Add the asteroid to the asteroid list and the all sprites list
    asteroid_list.add(asteroid)
    all_sprites_list.add(asteroid)    
    
    #Set start position for asteroid
    asteroid.rect.x = ((screen_width - 50) - random.randrange(500))
    asteroid.rect.y = ((screen_height - 50) - random.randrange(300))
        
#create player and add to all sprites list
player = Player()
all_sprites_list.add(player)
trashvar = True

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
            if event.key == pygame.K_RETURN:
                done = True
                
               
    #Game logic
    if asteroid.rect.x <= 0 or asteroid.rect.x >= 700:
        movex *= -1
    if asteroid.rect.y <= 0 or asteroid.rect.y >= 400:
        movey *= -1

    #Speed increses after certain scores are reached
    if score >= 0:
        click_sound1.play()
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
        display_game_over = True
        done = True
        
    #See if player collided with coin
    if pygame.sprite.spritecollide(player, coin_list, False):
        score += 1
        print (score)
        coin.rect.x = random.randrange(700)
        coin.rect.y = random.randrange(400)
        click_sound.play()
        
    #See if asteroid collided with side walls
    if pygame.sprite.groupcollide(wall_listx, asteroid_list, False, False):
        movex *= -1
        
    #See if asteroid collided with top walls    
    if pygame.sprite.groupcollide(wall_listy, asteroid_list, False, False):
        movey *= -1
        
    #Highscores
    if display_game_over:
        for i in range(5):
            if not score > int(highscore_list[i]):
                continue
            else:
                highscore_list.insert(i, score)
                name_list.insert(i, name)
                break
        with open('highscores.txt', 'w') as file:
            for i in range(5):
                file.write(str(name_list[i]) + "\n")
                file.write(str(highscore_list[i]) + "\n")  
        print ("Check highscore.txt for highscore list")
    
    clock.tick(60)
   
    pygame.display.flip()
   
        
           
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    