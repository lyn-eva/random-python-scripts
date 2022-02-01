import pygame,random

pygame.init()
screen = pygame.display.set_mode((650,650))
pygame.display.set_caption("random moving block")

x = random.randint(0,600)
y = random.randint(0,600)
v = 7
temp = v
temp1 = v
col = (255,0,0)
# main loop
run = True
while run:
    pygame.time.delay(50)
    for eve in pygame.event.get():
        if eve.type == pygame.QUIT:
            run = False

    pygame.display.update()

    # x--,y++ if x==600
    if x >= 600:
        temp = -v-1      
        col = (255, 255, 0)
    # x--,y-- if y==600
    if y >= 600:
        if x>300:
            temp1 = -v
            temp = v-1
        else:
            temp = -v-1
            temp1 = -v
        col = (51, 51, 204)      

    # x++,y-- if x==0
    if x <= 0:
        temp1 = -v
        temp = v-1
        col = (0, 0, 102)

    # x++,y++ if y==0
    if y <= 0:
 
        temp1 = v-1
        temp = v

        col = (255,0,0)
   
    #movement
    x += temp
    y += temp1


    screen.fill((102, 255, 153))
    pygame.draw.rect(screen,col,(x,y,50,50))
    

pygame.quit()