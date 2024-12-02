import pygame, sys, random

pygame.init()

w = 640
h = w
size = (w,h)
surface = pygame.display.set_mode(size)

pygame.display.set_caption("YOUR ISLAND ADVENTURE STORY")

#Color Constants
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
DARKGREEN = (25, 109, 0)

#Makes the screen into a 40 by 40 graph
xu = w/40
yu = h/40

LEFT= pygame.Rect(3*xu,13*yu, 10*xu, 10*yu)
RIGHT= pygame.Rect(26*xu, 13*yu, 10*xu, 10*yu)
MIDDLE=pygame.Rect(15*xu, 2*yu, 10*xu, 10*yu)


def draw_border():
    pygame.draw.rect(surface,DARKGREEN,(0,2*h/3,w,h/3),0)
    pygame.draw.rect(surface,BLACK,(0,0,w,20),0)
    pygame.draw.rect(surface,BLACK,(0,0,20,h),0)
    pygame.draw.rect(surface,BLACK,(0,h-20,w,20),0)
    pygame.draw.rect(surface,BLACK,(w-20,0,20,h),0)
    pygame.draw.rect(surface,BLACK,(0,2*h/3,w,20),0)

'''
Wraps text 
Source code for this function: https://stackoverflow.com/questions/42014195/rendering-text-with-multiple-lines-in-pygame
Has been modified to suit the needs of this program
Created By: Ted Klein Bergman
'''
def wrap_text(surface, text, pos, color=WHITE):
    font=pygame.font.SysFont('Arial',w//20,1)
    words = [word.split(' ') for word in text.splitlines()]  # 2D array where each row is a list of words.
    space = font.size(' ')[0]                                # The width of a space.
    max_width, max_height = surface.get_size()
    max_width-=w/28
    max_height-=h/1.5
    x, y = pos
    for line in words:
        for word in line:
            word_surface = font.render(word, 0, color)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width:
                x = pos[0]        # Reset the x.
                y += word_height  # Start on new row.
            surface.blit(word_surface, (x, y))
            x += word_width + space
        x = pos[0]        # Reset the x.
        y += word_height  # Start on new row.


def display_picture(picture,location):
    surface.blit(pygame.image.load(picture).convert_alpha(),location)
    

def getPictures(level_code):
    topPic = ""
    midPic = ""
    lowPic = ""

    if level_code == "1":
        return ('Emojis/Resources.png', 'Emojis/Island.png', 'Emojis/SOS.png')
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    elif level_code == "2A":
        return ("Emojis/Hammer.png", "Emojis/House.png", "Emojis/ForkKnife.png")
    elif level_code == "2B" or level_code == "2C" or level_code == "2D" or level_code == "3B":
        return ("Emojis/Fish.png", "Emojis/ForkKnife.png", "Emojis/Chicken.png")
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    elif level_code == "3A":
        return ("Emojis/Death.png", "Emojis/X.png", "Emojis/Death.png")
    elif level_code == "3C" or level_code == "3D" or level_code == "3G" or level_code == "3H":
        return ("Emojis/Death.png", "Emojis/Time.png", "Emojis/Death.png")
    elif level_code == "3E":
        return ("Emojis/Hospital.png", "Emojis/Money.png", "Emojis/Hospital.png")
    elif level_code == "3F":
        return ("Emojis/Happy.png", "Emojis/Airplane.png", "Emojis/Happy.png")
    
    return (topPic, midPic, lowPic)


def getLevelText(level_code):
    if level_code == "1":
        return "You're stranded on an island. Do you look for resources or call for help?"
    elif level_code == "2A":
        return "You started building a house, but your malnutrition starts to kick in. Do you want to continue building your house or look for food?"
    elif level_code == "2B":
        return "You started to look for some food. Do you want to fish or hunt?"
    elif level_code == "2C":
        return "You sent a smoke signal and now are very hungry. Do you fish or hunt?"
    elif level_code == "2D":
        return "You built rocks arranged in 'HELP!' However a wave washed them away. Now you're very hungry, do you want to fish or hunt?"
    elif level_code == "3A":
        return "You died from hunger because you refused to eat food."
    elif level_code == "3B":
        return "You started building a house, but your malnutrition starts to kick in. Do you want to continue building your house or look for food?"
    elif level_code == "3C":
        return "It took too long to fish, and no one found you. Therefore, you died."
    elif level_code == "3D":
        return "You found some chicken on the island, but no one finds you. You soon die on the island."
    elif level_code == "3E":
        return "It took too long to fish, but people found you, and brought you to the ER. You're in $1,000,000 in debt."
    elif level_code == "3F":
        return "You found some chicken on the island and short after some paramedics found you."
    elif level_code == "3G":
        return "It took too long to fish, and no one found you. Therefore, you died."
    elif level_code == "3H":
        return "You found some chicken on the island, but no one finds you. You soon die on the island."
    
    return "error"
    

def get_next_level(current_level, choice):
    if current_level == "1":
        if choice == "left":
           return random.choice(["2A", "2B"])
        elif choice == "right":
           return random.choice(["2C", "2D"])
    
    elif current_level == "2A":
        if choice == "left":
            return "3A"
        elif choice == "right":
            return "2B"
    
    elif current_level == "2B":
        if choice == "left":
            return "3C"
        elif choice == "right":
            return "3D"
    
    elif current_level == "2C":
        if choice == "left":
            return "3E"
        elif choice == "right":
            return "3F"
    
    elif current_level == "2D":
        if choice == "left":
            return "3G"
        elif choice == "right":
            return "3H"
    
    return current_level


def draw_screen(game_stage):
    draw_border()
    
    #get level images and text to display
    game_text= getLevelText(game_stage)

    #blit and wrap text
    wrap_text(surface, game_text,(w/20,35 * h/48),WHITE)    
    
    #returns tuple with 3 pix for that level (leftpicture, middlepicture, rightpicture)
    pics_to_display=getPictures(game_stage) 
    display_picture(pics_to_display[0],LEFT) 
    display_picture(pics_to_display[1],MIDDLE)
    display_picture(pics_to_display[2],RIGHT)
     


#*------------------------------------------ MAIN PROGRAM LOOP----------------------------------*
def main():
    #story starts at stage 1
    stage = "1"
    
    while(True):
        for event in pygame.event.get():
            if((event.type == pygame.QUIT) or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE)):
                pygame.quit()
                sys.exit()
           
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_pos = pygame.mouse.get_pos()
                if LEFT.collidepoint(mouse_pos):
                    stage = get_next_level(stage, "left")
                elif RIGHT.collidepoint(mouse_pos):
                    stage = get_next_level(stage, "right")

        surface.fill(WHITE)
        
        #Drawing code goes here
        draw_screen(stage) 
       
        pygame.display.update()
main()