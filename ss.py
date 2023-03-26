import pygame
import os
import random
pygame.font.init()
pygame.mixer.init()

MONEY_TOUCH = pygame.USEREVENT + 1
HIT_BALL = pygame.USEREVENT + 2

WIDTH, HEIGHT = 900,500
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption(" Grab the money, not the ball ")


#import ścieżek
WIN_SOUND = pygame.mixer.Sound(
    os.path.join('Assets','money_sound.mp3'))
WIN_SOUND.set_volume(0.1)
LOSER_SOUND = pygame.mixer.Sound(
    os.path.join('Assets','loser_sound.mp3'))
LOSER_SOUND.set_volume(0.1)

#Kolory RGB
WHITE = (255,255,255)
GOLD = (255,215,0)
RED = (255,0,0)




FPS = 60
VEL = 5
VEL_MONEY = 10
VEL_BALL = 3
VEL_METEOR = 2
VEL_SPACESHIP = 4

FACE_WIDTH, FACE_HEIGHT = 64,70
MONEY_WIDTH, MONEY_HEIGHT = 70,50
BALL_WIDTH, BALL_HEIGHT = 45,45
PLAY_WIDTH, PLAY_HEIGHT = 200,150
INFO_WIDTH, INFO_HEIGHT = 40,40
BACK_WIDTH, BACK_HEIGHT = 200,100
METEOR_WIDTH, METEOR_HEIGHT = 64,64
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 64,64
GAMEOVER_WIDTH, GAMEOVER_HEIGHT = 256,256
WINIMG_WIDTH, WINIMG_HEIGHT = 256,256
SCORE_WIDTH, SCORE_HEIGHT = 100,45
UFO_WIDTH, UFO_HEIGHT = 45,45

SCORE_FONT = pygame.font.SysFont('freesansbold.ttf', 50)
AUTOR_FONT = pygame.font.SysFont('comicsan', 40)
INFO_FONT = pygame.font.SysFont('comicsan', 35)



SPACE = pygame.image.load(
    os.path.join('Assets','space.png'))
FACE = pygame.image.load(
    os.path.join('Assets','face.png'))
FACE = pygame.transform.scale(FACE, (FACE_WIDTH,FACE_HEIGHT))
MONEY = pygame.image.load(
    os.path.join('Assets','money.png'))
pygame.display.set_icon(MONEY)
MONEY = pygame.transform.scale(MONEY, (MONEY_WIDTH,MONEY_HEIGHT))
MONEY_X = 0
MONEY_Y = random.randint(64,460)

BALL = pygame.image.load(
    os.path.join('Assets', 'ball.png'))
BALL = pygame.transform.scale(BALL,(BALL_WIDTH,BALL_HEIGHT))
BALL_X = 0
BALL_Y = random.randint(BALL_HEIGHT,450)
PLAY = pygame.image.load(
    os.path.join('Assets','play_button.png')) 
PLAY = pygame.transform.scale(PLAY,(PLAY_WIDTH,PLAY_HEIGHT))
INFO = pygame.image.load(
    os.path.join('Assets','info_button.png'))
INFO = pygame.transform.scale(INFO,(INFO_WIDTH,INFO_HEIGHT))
BACK = pygame.image.load(
    os.path.join('Assets','back_button.png'))
BACK = pygame.transform.scale(BACK,(BACK_WIDTH,BACK_HEIGHT))

METEOR = pygame.image.load(
    os.path.join('Assets','meteor.png'))
METEOR = pygame.transform.scale(METEOR,(METEOR_WIDTH,METEOR_HEIGHT))
METEOR_X = random.randint(0,900)
METEOR_Y = 0
SPACESHIP = pygame.image.load(
    os.path.join('Assets','spaceship.png'))
SPACESHIP = pygame.transform.rotate(pygame.transform.scale(SPACESHIP,(SPACESHIP_WIDTH,SPACESHIP_HEIGHT)), 285)
SPACESHIP_X = 0
SPACESHIP_Y = random.randint(0,400)
GAMEOVER = pygame.image.load(
    os.path.join('Assets','game-over.png'))
GAMEOVER = pygame.transform.scale(GAMEOVER,(GAMEOVER_WIDTH,GAMEOVER_HEIGHT))
WIN_IMG = pygame.image.load(
    os.path.join('Assets','you_win.png'))
WIN_IMG = pygame.transform.scale(WIN_IMG,(WINIMG_WIDTH,WINIMG_HEIGHT))
SCORE = pygame.image.load(
    os.path.join('Assets','score_button.png'))
SCORE = pygame.transform.scale(SCORE,(SCORE_WIDTH,SCORE_HEIGHT))
UFO = pygame.image.load(
    os.path.join('Assets','ufo.png'))
UFO = pygame.transform.scale(UFO,(UFO_WIDTH,UFO_HEIGHT))

def draw_effects(meteor, spaceship):
    WIN.blit(METEOR,(meteor.x,meteor.y))
    meteor.x += VEL_METEOR
    meteor.y += VEL_METEOR
    change_x_meteor = random.randint(0,800)
    if meteor.x + VEL_METEOR > 1000 or meteor.y + VEL_METEOR > 600:
        meteor.y = 0
        meteor.x = change_x_meteor
    WIN.blit(SPACESHIP,(spaceship.x,spaceship.y))
    spaceship.x += VEL_SPACESHIP
    spaceship.y -=1
    change_y = random.randint(0,440)
    if spaceship.x + VEL_BALL > 900:
        spaceship.x = 0
        spaceship.y = change_y


def draw_first(play,info,meteor,spaceship):
    WIN.blit(SPACE,(0,0))
    draw_effects(meteor,spaceship)
    WIN.blit(PLAY,(play.x,play.y))
    WIN.blit(INFO,(info.x,info.y))
    pygame.display.update()
def first_screen():
    play = pygame.Rect(350,175,PLAY_WIDTH,PLAY_HEIGHT)
    info = pygame.Rect(5, 5, INFO_WIDTH,INFO_HEIGHT)
    meteor = pygame.Rect(METEOR_X,METEOR_Y,METEOR_WIDTH,METEOR_HEIGHT)
    spaceship = pygame.Rect(SPACESHIP_X,SPACESHIP_Y,SPACESHIP_WIDTH,SPACESHIP_HEIGHT)

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS) #ustawiamy prędkość pętli 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False      
        draw_first(play,info,meteor,spaceship)
        pos = pygame.mouse.get_pos()
        if play.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                game_main()
        if info.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                info_screen()

    pygame.quit()


def draw_info(back):
    autortext = "Game made by @Tomasz Mielnicki | mielnicki-tomek@wp.pl"
    uptext = "1. Arrow Up - up movement"
    downtext = "2. Arrow Down - down movement"
    righttext = "3. Arrow Rigth - right movement"
    lefttext = "4. Arrow Left - left movement"
    # howplaytext= 
    WIN.blit(SPACE,(0,0))
    WIN.blit(BACK,(back.x,back.y))
    autor_text = AUTOR_FONT.render(autortext,1, RED)
    up_text = INFO_FONT.render(uptext,1,WHITE)
    down_text = INFO_FONT.render(downtext,1,WHITE)
    right_text = INFO_FONT.render(righttext,1,WHITE)
    left_text = INFO_FONT.render(lefttext,1,WHITE)

    
    WIN.blit(autor_text,(0,10))
    WIN.blit(up_text,(0,40))
    WIN.blit(down_text,(0,70))
    WIN.blit(right_text,(0,100))
    WIN.blit(left_text,(0,130))


    pygame.display.update()
def info_screen():
    back = pygame.Rect(350,300, BACK_WIDTH,BACK_WIDTH)
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS) #ustawiamy prędkość pętli 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        draw_info(back)
        pos = pygame.mouse.get_pos()
        if back.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                pygame.time.delay(50)
                first_screen()
    pygame.quit()

def draw_game(face,money,score,ball,ufo):
    WIN.blit(SPACE,(0,0))
    WIN.blit(UFO,(ufo.x,ufo.y))
    WIN.blit(SCORE,(357.5,0))
    score_text = SCORE_FONT.render(str(score) + "/150",1, WHITE)   
    WIN.blit(score_text,(467.5,8))
    WIN.blit(FACE,(face.x,face.y))
    WIN.blit(MONEY,(money.x,money.y))
    WIN.blit(BALL,(ball.x,ball.y))

    pygame.display.update()
def face_movement(keys_pressed,face):
    if keys_pressed[pygame.K_LEFT] and face.x - VEL > 0: # LEFT
        face.x -= VEL
    if keys_pressed[pygame.K_RIGHT] and face.x + VEL + FACE_WIDTH < WIDTH: # RIGH
        face.x += VEL
    if keys_pressed[pygame.K_UP] and face.y - VEL > 50: # UP
        face.y -= VEL
    if keys_pressed[pygame.K_DOWN] and face.y + VEL + FACE_HEIGHT < HEIGHT: # DOWN
        face.y += VEL                
    if keys_pressed[pygame.K_ESCAPE]:
        first_screen()
def game_main():
    score = 0
    health = 1

    face = pygame.Rect(300,100,FACE_WIDTH,FACE_HEIGHT)
    money = pygame.Rect(MONEY_X, MONEY_Y, MONEY_WIDTH, MONEY_HEIGHT)
    ball = pygame.Rect(BALL_X, BALL_Y,BALL_WIDTH, BALL_HEIGHT)
    ufo = pygame.Rect(0,0,UFO_WIDTH,UFO_HEIGHT)
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS) #ustawiamy prędkość pętli 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            
        keys_pressed = pygame.key.get_pressed()
        face_movement(keys_pressed,face)
        draw_game(face,money,score,ball,ufo)
        ball.x += VEL_BALL
        money.x += VEL_MONEY
        change_y = random.randint(50,440)
        ufo.x += VEL
        if ufo.x + VEL >950:
            ufo.x = 0

        if money.x + VEL_MONEY > 900:
            money.x = 0
            money.y = change_y
            score -= 5
        if face.colliderect(money):
            pygame.event.post(pygame.event.Event(MONEY_TOUCH))
            score += 1

        if ball.x + VEL_BALL > 900:
            ball.x = 0
            ball.y = change_y
        if face.colliderect(ball):
            pygame.event.post(pygame.event.Event(HIT_BALL))
            health -= 1
            
        if health <= 0:
            WIN.blit(GAMEOVER,(322,122))
            LOSER_SOUND.play()
            pygame.display.update()
            pygame.time.delay(2000)            
            break

        if score >= 151:
            WIN.blit(WIN_IMG,(322,122))
            WIN_SOUND.play()
            pygame.display.update()
            pygame.time.delay(2000)            
            break
        if score <= -45:
            WIN.blit(GAMEOVER,(322,122))
            LOSER_SOUND.play()
            pygame.display.update()
            pygame.time.delay(2000)
            break
    first_screen()


if __name__ == "__main__":
    first_screen()

    