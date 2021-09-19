print("Credits:\n@TheLowEnd\nTheLowEndStudios Founder-Raghav Gohil\nDownload my games : https://low-end-studios.itch.io")


#imports
import pygame
import random
import time

#initialize
pygame.init()
pygame.font.init()

#gamesettings:
fps = 60
fontsize = 30
antialiasing = True
wins = ((800,600))
screen = pygame.display.set_mode(wins)
pygame.display.set_caption("Snake Game") #setthenameofthegame
font = pygame.font.SysFont('aerial' , fontsize)
clock = pygame.time.Clock()
    
#data--initial
startx,starty = wins[0]/2 , wins[1]/2
step = 20
up , left , down , right = False , False , False , True
speed = 0.04
playerwidth, playerheight = 20,20
playerxreps = [startx , startx-20 , startx - 40] #replicas,initialvalassigned
playeryreps = [starty , starty , starty]
newplayerxreps = []
newplayeryreps = []
playerlength = 3
applewidth = 20
appleheight = 20
generateapple = True
randstartx , randstarty = 0,wins[1]

#gameflow:
stopgame = False

#colours:
backgroundcolorwhite = (255,255,255)
backgroundcolorblack = (0,0,0)
playerheadcolor = (0,150,150)
playerbodycolor = (0,255,0)
applecolor = (255,0,0)
textcolorblack = (0,0,0)
textcolorwhite = (255,255,255)

def quitGame():
    print("quitting game")
    pygame.quit()
    quit()

def renderPlayer():
    pygame.draw.rect(screen , playerheadcolor , ( startx , starty , playerwidth , playerheight))
    for i in range(1,playerlength):
        pygame.draw.rect(screen , playerbodycolor , ( playerxreps[i] , playeryreps[i] , playerwidth , playerheight))


def renderApple():
    global generateapple,randx,randy
    
    if generateapple: #setnewpositionfortheapple
        randx,randy = 0,0

        randx = random.randrange(randstartx , randstarty , step) #usingrangeforstepvalues
        randy = random.randrange(randstartx , randstarty , step)

    pygame.draw.rect(screen , applecolor , ( randx , randy , applewidth , appleheight)) #drawapple

    generateapple = False

def eatApple():
    global playerlength,generateapple

    try:
        if screen.get_at((int(startx),int(starty))) == (255,0,0): #ifitisredincreaselength
            playerlength += 1
            print(playerlength)
            playerxreps.append(playerxreps[playerlength-2])
            playeryreps.append(playeryreps[playerlength-2])
            print(playerxreps, playeryreps)
            generateapple = True
            renderApple()
    except:
        print("Exception-Failed Detection")

def die():
    global stopgame,up

    #youdiewhenyoueatyouself

    try:
        if screen.get_at((int(startx),int(starty))) == (0,255,0): #dieifyoutouchyourself
            stopgame = True
    except:
        print("Exception-Failed Detection")

    #youdiewhenyougooutsidethebounds

    if startx >= 800 or startx <0 or starty >=600 or starty <0:
        stopgame = True #stoptheflowofthegame

    restart()#restartafteryoudie
        
def movePlayer():
    global startx,starty,newplayerxreps,newplayeryreps,playerxreps,playeryreps,playerlength,up,right,left,down
    
    for e in events:
        if e.type == pygame.KEYDOWN:
            if (e.key == pygame.K_w or e.key == pygame.K_UP) and not down:
                up = True
                left = False
                right = False
                down = False
                print("w")
            elif (e.key == pygame.K_a or e.key == pygame.K_LEFT) and not right:
                left = True
                right = False
                down = False
                up = False
                print("a")
            elif (e.key == pygame.K_s or e.key == pygame.K_DOWN) and not up:
                down = True
                right = False
                left = False
                up = False
                print("s")
            elif (e.key == pygame.K_d or e.key == pygame.K_RIGHT) and not left:
                right = True
                down = False
                left = False
                up = False
                print("d")
                
    if stopgame == False:
        if up: #moveplayerandquickmafs
            starty -= step

            
            for i in range(1,playerlength):
                playerxreps[i] = playerxreps[i-(playerlength-1)]
                playeryreps[i] = playeryreps[i-(playerlength-1)]
            playerxreps[0] = startx
            playeryreps[0] = starty
        elif left:
            startx -= step
            for i in range(1,playerlength):
                playerxreps[i] = playerxreps[i-(playerlength-1)]
                playeryreps[i] = playeryreps[i-(playerlength-1)]
            playerxreps[0] = startx
            playeryreps[0] = starty
        elif down:
            starty += step
            for i in range(1,playerlength):
                playerxreps[i] = playerxreps[i-(playerlength-1)]
                playeryreps[i] = playeryreps[i-(playerlength-1)]
            playerxreps[0] = startx
            playeryreps[0] = starty
        elif right:
            startx += step
            for i in range(1,playerlength):
                playerxreps[i] = playerxreps[i-(playerlength-1)]
                playeryreps[i] = playeryreps[i-(playerlength-1)]
            playerxreps[0] = startx
            playeryreps[0] = starty

    #decreaseplayerspeed
    time.sleep(speed)

def renderblackscreen():
    screen.fill((backgroundcolorblack))

def renderText(x,y,text,color):
    renderedfont = font.render(text,antialiasing,color)#therenderedfont
    screen.blit(renderedfont,(x,y))
    
def renderScore():
    renderText(20,20,"Your Score Is: "+str(playerlength),textcolorblack)

def renderStatus():
    if stopgame:
        renderblackscreen()
        renderText(wins[0]/2-80,wins[1]/2,"You died. Score:"+str(playerlength),textcolorwhite)
        renderText(wins[0]/2-100,wins[1]/2+fontsize+20,"Press enter to restart.",textcolorwhite)
    
def restart():
    global stopgame,playerxreps,playeryreps,startx,starty,playerlength,up,down,left,right
    
    for e in events: #restartkeyenter
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_RETURN and stopgame:

                #restartvalues
                
                startx,starty = wins[0]/2 , wins[1]/2

                up,down,left,right = False,False,False,True
                
                playerlength = 3
                
                playerxreps , playeryreps = [startx , startx-20 , startx - 40] , [starty , starty , starty]

                print(startx,starty)
                print(playerxreps , playeryreps)
                 
                stopgame = False

                #end
                
            else:
                return

def main():
    #callfunctions
    movePlayer()
    renderPlayer()
    renderApple()
    renderScore()
    renderStatus()
    eatApple()
    die()


while True: #mainloop

    #events

    events = pygame.event.get()
    
    for e in events:
        if e.type == pygame.QUIT:
            quitGame()

    screen.fill(backgroundcolorwhite)

    #main

    if __name__ == "__main__":
        main()

    #updatedisplayandsetfps
    pygame.display.update()
    clock.tick(fps)

