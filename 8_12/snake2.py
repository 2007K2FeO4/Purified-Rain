import pygame,random,time
from pygame.locals import *
pygame.init()
c=pygame.time.Clock()
size=sw,sh=1200,600
s=pygame.display.set_mode((size),RESIZABLE)
pygame.display.set_caption('snake')
foodspown=True
food=[600,300]
pos=20
snake_list2=[[1000,100],[1020,100],[1040,100]]
snake_head2=[1040,100]
score2=0
dirct='right'
over=False
score=0
snake_list=[[180,520],[160,520],[140,520]]
snake_head=[140,520]
dirct2='left'
winner=''
food_list=[]
for i in range(1,7):
    food_image=pygame.image.load('f{}.png'.format(i))
    food_list.append(pygame.transform.smoothscale(food_image,(20,20)))
    food_image=food_list[0]
def showscore(a,b):
    sfont=pygame.font.Font('fixel.ttf',30)
    ssurf=sfont.render('P{}score:{}'.format(b,a),1,(200-b*50,50+b*50,160))
    s.blit(ssurf,(1000*b-950,20))
def showend():
    font=pygame.font.Font('comic.ttf',80)
    fonting=font.render('Game Over',1,(150,100,160))
    s.blit(fonting,(370,150))
    fonting2=font.render('press return to start',1,(190,150,200))
    s.blit(fonting2,(200,250))    
    if winner=='1p':
        fontimg3 = font.render('winner is ' + winner, True, (128,0,128))
    elif winner=='2p':
        fontimg3 = font.render('winner is ' + winner, True, (128,128,0))
    else:
        if score > score2:
            fontimg3 = font.render('winner is 1p', True, (128,0,128))
        elif score < score2:
            fontimg3 = font.render('winner is 2p', True, (128,128,0))
        elif score == score2:
            fontimg3 = font.render('      Tie', True, (100,100,100))
    s.blit(fontimg3, (370,350))  
def key2p(aa):
    if event.key==K_UP and aa!='down':
        aa='up'
    if event.key==K_DOWN and aa!='up':
        aa='down'  
    if event.key==K_LEFT and aa!='right':
        aa='left'
    if event.key==K_RIGHT and aa!='left':
        aa='right'  
    return aa
def key1p(aa):
    if event.key==K_w and aa!='down':
        aa='up'
    if event.key==K_s and aa!='up':
        aa='down'  
    if event.key==K_a and aa!='right':
        aa='left'
    if event.key==K_d and aa!='left':
        aa='right' 
    return aa
def move(a,b):
    if a=='up':
        b[1]-=pos
    if a=='down':
        b[1]+=pos
    if a=='left':
        b[0]-=pos
    if a=='right':
        b[0]+=pos
def isgameover():
    #wall
    if (snake_head[0] >= sw or snake_head[0] < 0 or snake_head[1] >= sh or snake_head[1] < 0)\
        and(snake_head2[0] >= sw or snake_head2[0] < 0 or snake_head2[1] >= sh or snake_head2[1] < 0):
        return True, ''    
    if snake_head[0] >= sw or snake_head[0] < 0 or snake_head[1] >= sh or snake_head[1] < 0:
        return True, '2p'
    if snake_head2[0] >= sw or snake_head2[0] < 0 or snake_head2[1] >= sh or snake_head2[1] < 0:
        return True, '1p'
    #interval
    if snake_head in snake_list2 and snake_head2 in snake_list:
        return True, ''
    if snake_head in snake_list2:
        return True, '2p'
    if snake_head2 in snake_list:
        return True, '1p'  
    return False,''
def motion(sc,fdsp,snbd,snps,p):
    snbd.insert(0,list(snps))
    if snps==food:
        fdsp=False
        sc+=1
    else:
        snbd.pop()   
    for i in range(len(snbd)):
        if p==1:
            clr=(127*i//len(snbd),0,255-127*i//len(snbd))
        elif p==2:
            clr=(255-255*i//len(snbd),255,0)         
        pygame.draw.rect(s,clr,(snbd[i][0],snbd[i][1],pos,pos))     
    return sc, fdsp    
while True:
    c.tick(10)
    s.fill((255,255,255)) 
    pygame.draw.rect(s,(200,230,250),(0,0,sw,sh))
    showscore(score,1)
    showscore(score2,2)
    event = pygame.event.poll()
    if event.type==QUIT:
        pygame.quit()
    elif event.type==KEYDOWN:
        dirct=key1p(dirct)
        dirct2=key2p(dirct2)
    move(dirct,snake_head)   
    move(dirct2,snake_head2)
    score,foodspown=motion(score,foodspown,snake_list,snake_head,1)
    score2,foodspown=motion(score2,foodspown,snake_list2,snake_head2,2)
    over,winner=isgameover()
    if False==foodspown:
        food_image=random.choice(food_list)
        food=[random.randint(2,sw//pos-3)*pos,random.randint(2,sh//pos-3)*pos]  
        foodspown=True
    s.blit(food_image,tuple(food))
    if over:
        showend()
        while True:
            event = pygame.event.poll()
            if event.type == QUIT:
                pygame.quit()
            elif event.type == KEYDOWN:
                if event.key == K_RETURN:
                    foodspown=True
                    food=[600,300]
                    pos=20
                    snake_list2=[[1000,100],[1020,100],[1040,100]]
                    snake_head2=[1000,100]
                    score2=0
                    dirct='right'
                    over=False
                    score=0
                    snake_list=[[140,500],[120,500],[100,500]]
                    snake_head=[140,500]
                    dirct2='left'
                    winner=''
                    break
            keys = pygame.key.get_pressed()
            if keys[K_ESCAPE]:
                pygame.quit()
            pygame.display.update()
            
    keys = pygame.key.get_pressed()
    if keys[K_ESCAPE]:
        pygame.quit() 
    pygame.display.update()
