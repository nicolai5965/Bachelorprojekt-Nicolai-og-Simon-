import pygame

pygame.init() # used to initialise all of the pygame modules


#Colors
BLACK = ( 0, 0, 0)
WHITE = ( 255, 255, 255)
GREEN = ( 0, 255, 0)
RED = ( 255, 0, 0)
PURPLE =(128, 0, 128)
BLUE = (0,0,255)
ORANGE = (255,165,0)



#Variables
size = (300,450) #screen size

framerate = 60

rect_lenght = 175 #Loading bar
rect_height = 25 #Loading bar







# In game variables
red_value = 1*5
purple_value = 2*5
white_value = 3*5
green_value = 4*5

draw_red = False
draw_purple = False
draw_white = False
draw_green = False

length_red = 0
length_purple = 0
length_white = 0
length_green = 0

speed_red = 5
speed_purple = 4
speed_white = 3
speed_green = 2

score = 90

#Butttons cost and manager
cost_red = 2
cost_purple = 5
cost_white = 10
cost_green = 20

owned_red =False
owned_purple =False
owned_white =False
owned_green =False

manager_red = 100
manager_purple = 500
manager_white = 2000
manager_green = 4000

x_coord = 12.5
dist_between_manager = 75


screen = pygame.display.set_mode(size)
pygame.display.set_caption("Like Hero Clicker game")

font = pygame.font.Font("freesansbold.ttf", 16)


carryOn = True

timer = pygame.time.Clock()

#keys=pygame.key.get_pressed()

def draw_task(color,y_coord,value,draw, length ,speed):
    global score
    if draw and length < 200:
        length += speed
    elif length >= 200:
        draw = False
        length = 0
        score += value
        
    #What is on the screen
    task = pygame.draw.circle(screen, color, (30, y_coord), 20,  4)
    pygame.draw.rect(screen, color, [70,y_coord-15,200,30],4)
    pygame.draw.rect(screen, color, [70,y_coord-15,length,30],0)
    value_text = font.render(str(round(value,2)), True, WHITE)
    screen.blit(value_text, ( 25 ,y_coord - 8))
    
    return task, length , draw
    




def draw_buttons(color,x_coord, cost, owned,manager_cost):

    self_click_button_upgade = pygame.draw.rect(screen, color, (x_coord,340,50,30))
    self_button_upgade_cost = font.render(str(round(cost,2)),True,BLACK)
    screen.blit(self_button_upgade_cost, (x_coord + 20,348.5))
    if not owned:
        manager_button = pygame.draw.rect(screen, color, (x_coord,410,50,30))
        manager_text = font.render(str(round(manager_cost,2)),True,BLACK)
        screen.blit(manager_text, (x_coord+10,418.5))
    else:
        manager_button = pygame.draw.rect(screen, BLACK, (x_coord,410,50,30))
    return self_click_button_upgade , manager_button


    

while carryOn:
    #main screen loop
    timer.tick(framerate)
    if owned_red and not draw_red:
        draw_red = True
    if owned_purple and not draw_purple:
        draw_purple = True
    if owned_white and not draw_white:
        draw_white = True
    if owned_green and not draw_green:
        draw_green = True
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            keys = pygame.key.get_pressed()
            if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
                carryOn = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if task1.collidepoint(event.pos):
                draw_red = True
            if task2.collidepoint(event.pos):
                draw_purple = True
            if task3.collidepoint(event.pos):
                draw_white = True
            if task4.collidepoint(event.pos):
                draw_green = True
            if red_manager_buy.collidepoint(event.pos) and score >= manager_red and not owned_red:
                owned_red = True
                score -= manager_red
            if purple_manager_buy.collidepoint(event.pos) and score >= manager_purple and not owned_purple:
                owned_purple = True
                score -= manager_purple    
            if white_manager_buy.collidepoint(event.pos) and score >= manager_white and not owned_white:
                owned_white = True
                score -= manager_white
            if green_manager_buy.collidepoint(event.pos) and score >= manager_green and not owned_green:
                owned_green = True
                score -= manager_green
            if red_buy.collidepoint(event.pos) and score >= cost_red:
                red_value *= 1.15
                score -= cost_red
                cost_red *= 1.1
            if purple_buy.collidepoint(event.pos) and score >= cost_purple:
                purple_value *= 1.15
                score -= cost_purple
                cost_purple *= 1.1
            if white_buy.collidepoint(event.pos) and score >= cost_white:
                white_value *= 1.15
                score -= cost_white
                cost_white *= 1.1
            if green_buy.collidepoint(event.pos) and score >= cost_green:
                green_value *= 1.15
                score -= cost_green
                cost_green *= 1.1
                    
    
    screen.fill(BLACK)
    
    # --- Game logic should go here

    display_score = font.render("Points: "+str(round(score,2)), True, WHITE)
    screen.blit(display_score,(100,20)) 


    buy_self_click_upgrade = font.render("Buy self click upgrad", True, WHITE)
    screen.blit(buy_self_click_upgrade,(75,300)) 

    task1 , length_red , draw_red = draw_task(RED,100,red_value,draw_red,length_red,speed_red)
    task2 , length_purple , draw_purple = draw_task(PURPLE,150,purple_value,draw_purple,length_purple,speed_purple)
    task3 , length_white , draw_white = draw_task(WHITE,200,white_value , draw_white, length_white, speed_white)
    task4 , length_green , draw_green = draw_task(GREEN,250,green_value , draw_green, length_green, speed_green ) 

    buy_manager_upgrade = font.render("Buy manager upgrad", True, WHITE)
    screen.blit(buy_manager_upgrade,(70,385)) 
    red_buy , red_manager_buy = draw_buttons(RED, x_coord, cost_red, owned_red, manager_red)
    purple_buy , purple_manager_buy = draw_buttons(PURPLE, x_coord+dist_between_manager, cost_purple, owned_purple, manager_purple)
    white_buy , white_manager_buy = draw_buttons(WHITE, x_coord+dist_between_manager*2, cost_white, owned_white, manager_white)
    green_buy , green_manager_buy = draw_buttons(GREEN, x_coord+dist_between_manager*3, cost_green, owned_green, manager_green)
    

    
    pygame.display.flip()
    timer.tick(framerate)


pygame.quit()

