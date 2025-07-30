import pygame,random,time
from pygame.locals import *
pygame.init()
c=pygame.time.Clock()
s=pygame.display.set_mode((1200,600))
stt=time.time()
pygame.display.set_caption('snake')
font=pygame.font.Font('fixel.ttf',30)
font2=pygame.font.Font('comic.ttf',100)
over_image1=font.render('Press 1 to move',1,(255,0,0))
over_image2=font.render('Press 0 to move',1,(255,0,0))
over_image3=font2.render('P1 win',1,(255,0,0))
over_image4=font2.render('P2 win',1,(255,0,0))  
over_image5=font2.render('Tie',1,(255,0,0)) 
food=[600,300]
food_list=[]
for i in range(1,7):
    food_image=pygame.image.load('f{}.png'.format(i))
    food_list.append(pygame.transform.smoothscale(food_image,(20,20)))
    food_image=food_list[0]
pos=20
over=[0,0]
def my_init2():
    global snake_list2,snake_head2,dirct2,score2,over
    snake_list2=[[100,100],[120,100],[140,100]]
    snake_head2=[140,100]
    score2=0
    dirct2='right'
    over[1]=0
def my_init():
    global snake_list,snake_head,dirct,score,over
    score=0
    snake_list=[[1040,500],[1020,500],[1000,500]]
    snake_head=[1000,500]
    dirct='left' 
    over[0]=0
my_init()
my_init2()
while True:
    edt=180-round(time.time()-stt)
    time_image=font2.render('%03d'%edt,1,(200,200,200))
    if edt<=0:
        over=[2,2]
    c.tick(10)
    s.fill((200,230,250))
    s.blit(time_image,(500,20))
    s.blit(food_image,tuple(food))
    score_image=font.render('P1score:'+str(score),1,(150,100,160))
    score_image2=font.render('P2score:'+str(score2),1,(100,160,150))
    s.blit(score_image,(20,20)) 
    s.blit(score_image2,(1080,20)) 
    print(over)
    if over[0]==1:
        s.blit(over_image1,(70,240))
    if over[1]==1:
        s.blit(over_image2,(970,240))
    if over==[2,2]:
        s.blit(time_image,(370,240))
        pygame.display.update()
        time.sleep(2)
        s.fill((200,230,250))
        if score==score2:
            s.blit(over_image5,(500,240))
        elif score<score2:
            s.blit(over_image4,(370,240))
        else:
            s.blit(over_image3,(370,240))
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
            if event.type==KEYDOWN:
                if event.key==K_1 and over[0]==1:   
                    my_init()
                    break
                if event.key==K_0 and over[1]==1:
                    my_init2()
                    break
    #snake
    for i in range(len(snake_list)):
        if over!=2:
            pygame.draw.rect(s,(127*i//len(snake_list),0,255-127*i//len(snake_list)),\
                             (snake_list[i][0],snake_list[i][1],pos,pos))
    for i in range(len(snake_list2)):
        if over!=1:
            pygame.draw.rect(s,(255-255*i//len(snake_list2),255,0),\
                             (snake_list2[i][0],snake_list2[i][1],pos,pos))            
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
        if event.type==KEYDOWN:
            if over[0]==0:
                if event.key==K_UP and dirct!='down':
                    dirct='up'
                if event.key==K_DOWN and dirct!='up':
                    dirct='down'  
                if event.key==K_LEFT and dirct!='right':
                    dirct='left'
                if event.key==K_RIGHT and dirct!='left':
                    dirct='right'
            if over[1]==0:
                if event.key==K_w and dirct2!='down':
                    dirct2='up'
                if event.key==K_s and dirct2!='up':
                    dirct2='down'  
                if event.key==K_a and dirct2!='right':
                    dirct2='left'
                if event.key==K_d and dirct2!='left':
                    dirct2='right' 
            if event.key==K_1 and over[0]==1:   
                my_init()
            if event.key==K_0 and over[1]==1:
                my_init2()          
    if over[0]==0:
        if dirct=='up':
            snake_head[1]-=pos
        if dirct=='down':
            snake_head[1]+=pos       
        if dirct=='left':
            snake_head[0]-=pos
        if dirct=='right':
            snake_head[0]+=pos
    if over[1]==0:
        if dirct2=='up':
            snake_head2[1]-=pos
        if dirct2=='down':
            snake_head2[1]+=pos       
        if dirct2=='left':
            snake_head2[0]-=pos
        if dirct2=='right':
            snake_head2[0]+=pos        
    snake_list.append(list(snake_head))
    snake_list2.append(list(snake_head2))
    del snake_list[0]
    del snake_list2[0]
    #food
    if snake_head==food:
        score+=1
        snake_list.append([-200,-200])
        food_image=random.choice(food_list)
        food=[random.randint(2,57)*pos,random.randint(2,27)*pos]
    if snake_head2==food:
        score2+=1
        snake_list2.append([-200,-200])
        food_image=random.choice(food_list)
        food=[random.randint(2,57)*pos,random.randint(2,27)*pos]        
    #over
    if snake_head[0]<0 or snake_head[0]>=1200 or snake_head[1]<0 or snake_head[1]>=600:
        over[0]=1
    if snake_head2[0]<0 or snake_head2[0]>=1200 or snake_head2[1]<0 or snake_head2[1]>=600:
        over[1]=1
    pygame.display.update()