import pygame
import random


pygame.init()



x = 1200
y = 620


screen = pygame.display.set_mode((x,y))
pygame.display.set_caption('Meu jogo com Python')


fundo = pygame.image.load('imagens/predio2.png').convert_alpha()
fundo = pygame.transform.scale(fundo,(x,y))


virus = pygame.image.load('imagens/virus2.png').convert_alpha()
virus = pygame.transform.scale(virus,(60,60))



missel = pygame.image.load('imagens/test1.png').convert_alpha()
missel = pygame.transform.scale(missel,(45,45))
missil = pygame.transform.rotate(missel, -45)



vel_x_missel = 0
posi_missel_x = 28
posi_missel_y = 350

posi_virus_x = 200
posi_virus_y = 200

posi_player_x = 5 
posi_player_y = 300

player = pygame.image.load('imagens/atual.png').convert_alpha()
player = pygame.transform.scale(player, (100,100))





triggered  = False
rodando = True



#funções
def respawn():
    x= 1300
    y= random.randint(1,605)
    return[x,y]


def respawn_missel():
    triggered = False
    respawn_missel_x = posi_player_x
    respawn_missel_y = posi_player_y
    vel_x_missel = 0
    return [respawn_missel_x, respawn_missel_y, triggered, vel_x_missel]



while rodando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False

    screen.blit(fundo, (0,0))
    

    #teclas comandos
    tecla= pygame.key.get_pressed()
    if tecla[pygame.K_UP] and posi_player_y > 1:
        posi_player_y -=1

        if not triggered:
            posi_missel_y -=1


    if tecla[pygame.K_DOWN] and posi_player_y < 450:
        posi_player_y += 1


        if not triggered:
            posi_missel_y +=1
        

    if tecla[pygame.K_SPACE]:
        triggered = True
        vel_x_missel = 1
        
        
    #respawn
    if posi_virus_x == 0:
        posi_virus_x = respawn()[0]
        posi_virus_y = respawn()[1]


    if posi_missel_x == 1200:
        posi_missel_x, posi_missel_y, triggered, vel_x_missel = respawn_missel()

    #movimento
    
    posi_virus_x -= 1
    posi_missel_x += vel_x_missel






    
    # criar imagens
    screen.blit(virus, (posi_virus_x, posi_virus_y))
    screen.blit(missel,(posi_missel_x, posi_missel_y))
    screen.blit(player, (posi_player_x, posi_player_y))
    





    
    pygame.display.update()

