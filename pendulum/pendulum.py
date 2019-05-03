import pygame
import time
import math
from colorama import init, AnsiToWin32, Fore, Back, Style
init(autoreset=True)

print(Fore.YELLOW + """
       ▄▄▄▄▄▄▄▄▄▄
            /
           / 
          /    
         /     
        /
     ▄████▄
     ██████
      ▀▀▀▀
.....................................
                                                    """)

pygame.init()

Dwidth = 400
Dheight = 600

white = (255, 255, 255)
black = (0, 0, 0)
red = (150, 0, 0)
green = (0, 150, 0)
blue = (100, 100, 255)

clock = pygame.time.Clock()

#G = (10)
F = (0) 
def giveL():
    global L
    L = -1
    while not(L >= 0.10 and L <= 1):
        try:
            L =float(input('Length(m): ').encode('utf-8'))
        except ValueError:
            print(Fore.RED + '**It must be a number**')
        if not(L >= 0.10 and L <= 1 ):
            print(Fore.RED + '**The Length must be > 0.9 and < 1**')
def giveG():
    global G
    G = -1
    while not(G >= 1 and G <= 25 ):
        try:
            G = float(input('Gravitational acceleration(m/sec^2): ').encode('utf-8'))
        except ValueError:
            print(Fore.RED + '**It must be a number**')
        if not(G >= 1 and G <= 25 ):
            print(Fore.RED + '**Gravity acceleration must be > 0 and < 26**')
def givea():
    global a
    a = 1000
    while not (a >= -9 and a<= 9):
        try:
            a = float(input('Angle: ').encode('utf-8'))
        except ValueError:
            print(Fore.RED + '**It must be a number**')
        if not(a >= -9 and a <= 9 ):
            print(Fore.RED + '**The angle must be > -10 and < 10**')
    global b
    b = math.radians(180-90-a)
    a = math.radians(a)

def start():
    yorn = -1
    while yorn not in (1,2):
        try:
            yorn = float(input('Want to give length(1) or period/frequency(2)? (1 or 2): ').encode('utf-8'))
        except ValueError:
            print(Fore.RED + '**It must be a 1 or 2**')
        if yorn not in (1,2):
            print(Fore.RED + '**It must be a 1 or 2**')

    if yorn == 1:
        global L
        giveL()

        giveG()
            
        givea()

        global T  
        T = 2*math.pi*math.sqrt(L/G)
        print('-------------------------------------')
        print('')
        print(Fore.YELLOW + 'Period: ' + str(round(T,3)) + ' seconds')
        global freq
        freq = 1/T
        print(Fore.YELLOW + 'Frequency: ' + str(round(freq,3)) + ' Hz')
        print('_____________________________________')

    if yorn == 2:
        yorn2 = -1
        while not yorn2 in (1,2):
            try:
                yorn2 = float(input('Want to give period(1) or frequency(2)? (1 or 2): ').encode('utf-8'))
            except ValueError:
                print(Fore.RED + '**It must be a 1 or 2**')
            if not yorn2 in (1,2):
                print(Fore.RED + '**It must be a 1 or 2**')
       
        if yorn2 == 1:
            T = -1
            while not(T >= 0.5 and T <= 2.2):
                try:
                    T =float(input('Period(sec): ').encode('utf-8'))
                except ValueError:
                    print(Fore.RED + '**It must be a number**')
                if not(T >= 0.5 and T <= 2.2):
                    print(Fore.RED + '**The Period must be > 0.5 and < 2.1**')
           
            giveG()
            givea()
            
            L = ((T*math.sqrt(G)/(2*math.pi)))**2

            print('-------------------------------------')
            print('')
            print(Fore.YELLOW + 'Length: ' + str(round(L,3)) + ' m')
            freq = 1/T
            print(Fore.YELLOW + 'Frequency: ' + str(round(freq,3)) + ' Hz')
            print('_____________________________________')

        if yorn2 == 2:
            F = -1
            while not(F >= 0.10 and F <= 1):
                try:
                    F =float(input('Frequency(n/sec): ').encode('utf-8'))
                except ValueError:
                    print(Fore.RED + '**It must be a number**')
                if not(F >= 0.00001 and F <= 1 ):
                    print(Fore.RED + '**The Frequency must be > 0.1 and < 1**')
            
            giveG() 
            givea()
            
            T = 1/F
            L = ((T*math.sqrt(G)/(2*math.pi)))**2

            print('-------------------------------------')
            print('')
            print(Fore.YELLOW + 'Period: ' + str(round(T,3)) + ' m')
            freq = 1/T
            print(Fore.YELLOW + 'Length: ' + str(round(L,3)) + ' Hz')
            print('_____________________________________')

    x = (L*430*math.sin(a)/math.sin(90))+(Dwidth/2)
    y = (L*430*math.sin(b)/math.sin(90))+(Dheight/10)
    
    global mouseXY
    mouseXY = [int(x),int(y)]
    
    #start = True

    #while start:
        #for event in pygame.event.get():
            #print(event)
            #if event.type == pygame.QUIT:
                #quit()
            #if event.type == pygame.KEYDOWN:
                #if event.key == pygame.K_ESCAPE:
                    #quit()
                #if event.key == pygame.K_r:
                    #start = False

        #mouseXY = pygame.mouse.get_pos()
    global Display
    Display = pygame.display.set_mode((int(Dwidth),int(Dheight)))
    pygame.display.set_caption('pendulum')

    Display.fill(black)
    pygame.draw.aaline(Display, red, (int(Dwidth/2),int(Dheight/10)), mouseXY)
    pygame.draw.circle(Display, red, (int(Dwidth/2),int(Dheight/10)), 5)
    pygame.draw.circle(Display, green, mouseXY, 20)

        #if pygame.mouse.get_pressed() == (1,0,0):
            #start = False
        
    pygame.display.update()
    

def drop():
    #mouseXY = pygame.mouse.get_pos()

    #L = (math.sqrt(((mouseXY[0]-Dwidth/2)**2)+((mouseXY[1]-Dheight/2)**2)))/10
    #L = 100
    #print('Length: ' + str(L) + 'cm')
    

    #print(L)
    #print(T)  
    
    x = int(Dwidth/2)
    y = int(Dheight/10)
    
    x1 = mouseXY[0]
    y1 = mouseXY[1]

    tail = []

    speed = 0
    run = True

    angleOfRotation = 0.04/T
    #angleOfRotation = math.acos(((2*(L**2))-(G**2))/(2*(L**2)))
    #print(angleOfRotation)
    
    while run:
        printspeed ="Speed: " +("█"*int(abs(speed)*20)) + ('        ')
        print (Fore.GREEN + printspeed, end="\r")
        if len(tail) < 100:
            tail.append((int(x1),int(y1)))
            #print(tail)
        
        if x1 < int(Dwidth/2):
            heheBoy = -1
            if heheBoy == 1:
                print("o katsaros eftoiaxe to programma kai opoios leei to antitheto leei psemata reeeeeeeee")
                print("Katsaros made the program and anybody who says something else is layingggggggggggg")
            speed -= angleOfRotation
        else:
            speed += angleOfRotation
            
        u = math.radians(speed)
        x2 = math.cos(u)*(x1-x) - math.sin(u)*(y1-y)+x
        y2 = math.sin(u)*(x1-x) + math.cos(u)*(y1-y)+y
        Display.fill(black)

        pygame.draw.aaline(Display,(119,136,153), (int(Dwidth/2),0), [int(Dwidth/2),(Dheight)])
        pygame.draw.aaline(Display, red, (int(Dwidth/2),int(Dheight/10)), [int(x2), int(y2)])
        pygame.draw.circle(Display, red, (int(Dwidth/2),int(Dheight/10)), 5)
        for xytail in tail:
            pygame.draw.circle(Display, blue, xytail, int(0.7))
        pygame.draw.circle(Display, green, (int(x2),int(y2)), 20)
        
        pygame.display.update()

        x1 = x2
        y1 = y2

        clock.tick(60)
                
        #print(int(speed*10))

        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    quit()
                if event.key == pygame.K_r:
                    run = False
                    print('                                   ', end='\r')


while True:    
    start()
    drop()

























