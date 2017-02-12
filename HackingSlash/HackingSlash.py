import pygame, sys, time, random, math, os
from pygame.locals import *
sys.path.append ("../")

pygame.init()
mainClock = pygame.time.Clock()

WINDOWWIDTH = 1366
WINDOWHEIGHT = 768

SOUTH = 0
NORTH = 180
EAST = 90
WEST = 270

FACING = SOUTH
FACING2 = SOUTH
FACING3 = SOUTH
FACING4 = SOUTH
GREY = (220,220,220)

quit = False

BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
YELLOW = (255,255,0)
PURPLE = (128,0,128)
ORANGE = (255,165,0)
LPURPLE = (218,112,214)

player1 = pygame.Rect(619, 320, 64, 64)
player2 = pygame.Rect(619, 388, 64, 64)
player3 = pygame.Rect(687, 320, 64, 64)
player4 = pygame.Rect(687, 388, 64, 64)
knight1 = pygame.image.load('Knight_1.png')
knight2 = pygame.image.load('Knight_2.png')
ghost1 = pygame.image.load('Ghost_1.png')
ghost2 = pygame.image.load('Ghost_2.png')
ghost_files = [ghost1, ghost2, ghost1, ghost2, ghost1]
knight3 = pygame.image.load('Knight_Attack_3.png')
knight4 = pygame.image.load('Knight_Attack_2.png')
knight5 = pygame.image.load('Knight_Attack_1.png')
mage1 = pygame.image.load('Mage_1.png')
mage2 = pygame.image.load('Mage_2.png')
mage3 = pygame.image.load('Mage_Attack_1.png')
mage4 = pygame.image.load('Mage_Attack_2.png')
mage_files = [mage1, mage2, mage3, mage4, mage3]

ranger1 = pygame.image.load('Ranger_1.png')
ranger2 = pygame.image.load('Ranger_2.png')
ranger3 = pygame.image.load('Ranger_Attack_1.png')
ranger4 = pygame.image.load('Ranger_Attack_AOE.png')
ranger_files = [ranger1, ranger2, ranger3, ranger4, ranger3]

cleric1 = pygame.image.load('Cleric_1.png')
cleric2 = pygame.image.load('Cleric_2.png')
cleric3 = pygame.image.load('Cleric_Attack_1.png')
cleric4 = pygame.image.load('Cleric_Block.png')
cleric_files = [cleric1, cleric2, cleric3, cleric4, cleric3]

titleImg = pygame.image.load('titlecard.png')
knight_files = [knight1, knight2, knight3, knight4, knight5]
currentKnight1 = 0
currentKnight2 = 0
currentKnight3 = 0
currentKnight4 = 0
sword1 = pygame.image.load('sword 1.png')
sword2 = pygame.image.load('sword 2.png')
sword3 = pygame.image.load('sword 3.png')
potImg = pygame.image.load('Health_Potion.png')
sword_files =  [sword1,sword2,sword3]
claw1 = pygame.image.load('Enemy_Claw_1.png')
claw2 = pygame.image.load('Enemy_Claw_2.png')
claw_files =  [claw1,claw2,claw1]
enemypic1 = pygame.image.load('barbed eye.png')
enemypic2 = pygame.image.load('black sentinel.png')
enemypic3 = pygame.image.load('contract demon.png')
enemypic4 = pygame.image.load('draining burn.png')
enemypic5 = pygame.image.load('returned ghoul.png')
enemypic12 = pygame.image.load('barbed eye2.png')
enemypic22 = pygame.image.load('black sentinel2.png')
enemypic32 = pygame.image.load('contract demon2.png')
enemypic42 = pygame.image.load('draining burn2.png')
enemypic52 = pygame.image.load('returned ghoul2.png')
fireball = pygame.image.load('Fireball.png')
enemy1_files = [enemypic1, enemypic12]
enemy2_files = [enemypic2, enemypic22]
enemy3_files = [enemypic3, enemypic32]
enemy4_files = [enemypic4, enemypic42]
enemy5_files = [enemypic5, enemypic52]
boss1 = pygame.image.load('boss bragon.png')
boss2 = pygame.image.load('boss bragon2.png')
boss_files = [boss1,boss2,boss1]
Background_dungeon = pygame.image.load('Background_dungeon.png')
gameover = pygame.image.load('GameOver.png')
victory = pygame.image.load('victory.png')
animateSec = 0
aniSwing = 0
p1hp = 100
p2hp = 100
p3hp = 100
p4hp = 100
flipTime = 1
play1 = True
enemiesLeft = 30
spawnRate = 3000
lastPot = 0
bossNotSpawned = True
fightingBoss = False
won = False
notStarted = True
outsideRotate = 2
swordSound = pygame.mixer.Sound('sfx_wpn_sword1.wav')
eHitSound = pygame.mixer.Sound('sfx_sounds_damage1.wav')
pHitSound = pygame.mixer.Sound('sfx_sounds_error2.wav')
clawSound = pygame.mixer.Sound('sfx_sounds_impact2.wav')
eDie = pygame.mixer.Sound('sfx_exp_short_hard2')
hDie = pygame.mixer.Sound('sfx_deathscream_human2')

windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), pygame.FULLSCREEN, 32)
pygame.display.set_caption('Hack Em\' Up!')

basicFont2 = pygame.font.Font('freesansbold.ttf',20)

pygame.mouse.set_visible(False)
pygame.mouse.set_pos(WINDOWWIDTH/2, WINDOWHEIGHT/2)

lastSpawn = 0

attacks = []
enes = []
eneA = []
Emissiles = []
pots = []

pygame.mixer.music.load('8 Bit Battle in G Minor.mp3')

class swingAttack:
    duration = 2
    def __init__(self, x, y):
                self.position = pygame.Rect(x, y, 64, 64)

class health:
    def __init__(self, x, y):
        self.position = pygame.Rect(x, y, 32, 32)

class missileUp:
    monX = 0
    monY = -10
    color = ORANGE
    def __init__(self, x, y):
            self.position = pygame.Rect(x, y, 64, 64)

class missileUPR:
    monX = 10
    monY = -10
    color = ORANGE
    def __init__(self, x, y):
        self.position = pygame.Rect(x, y, 64, 64)

class missileRight:
    monX = 10
    monY = 0
    color = ORANGE
    def __init__(self, x, y):
        self.position = pygame.Rect(x, y, 64, 64)
class missileDownR:
    monX = 10
    monY = 10
    color = ORANGE
    def __init__(self, x, y):
        self.position = pygame.Rect(x, y, 64, 64)
class missileDown:
    monX = 0
    monY = 10
    color = ORANGE
    def __init__(self, x, y):
        self.position = pygame.Rect(x, y, 64, 64)
class missileDownL:
    monX = -10
    monY = 10
    color = ORANGE
    def __init__(self, x, y):
        self.position = pygame.Rect(x, y, 64, 64)
class missileLeft:
    monX = -10
    monY = 0
    color = ORANGE
    def __init__(self, x, y):
        self.position = pygame.Rect(x, y, 64, 64)
class missileUpL:
    monX = -10
    monY = -10
    color = ORANGE
    def __init__(self, x, y):
        self.position = pygame.Rect(x, y, 64, 64)
class enemy1:
    hp = 20
    facing = SOUTH
    monX = 0
    monY = 0
    def __init__(self, x, y):
                self.position = pygame.Rect(x, y, 64, 64)
                temp = random.randint(1,5)
                if temp == 1:
                    self.picture = enemy1_files
                if temp == 2:
                    self.picture = enemy2_files
                if temp == 3:
                    self.picture = enemy3_files
                if temp == 4:
                    self.picture = enemy4_files
                if temp == 5:
                    self.picture = enemy5_files
class enemy2:
    hp = 1000
    facing = SOUTH
    monX = 0
    monY = 0
    def __init__(self, x, y):
                self.position = pygame.Rect(x, y, 256, 256)
                self.picture = boss_files

def swing(x, y, facing):
    if facing == NORTH:
        return swingAttack(x, y-64)
    if facing == SOUTH:
        return swingAttack(x, y+64)
    if facing == EAST:
        return swingAttack(x+64, y)
    if facing == WEST:
        return swingAttack(x-64, y)

pygame.mixer.music.play(-1, 0.0)

mageSide1 = pygame.image.load('Mage_Side_1.png')
mageSide2 = pygame.image.load('Mage_Side_2.png')
mageSide3 = pygame.image.load('Mage_Side_3.png')
mageSide_files = [mageSide1, mageSide2, mageSide3]

rangerSide1 = pygame.image.load('Ranger_Side_1.png')
rangerSide2 = pygame.image.load('Ranger_Side_2.png')
rangerSide3 = pygame.image.load('Ranger_Side_3.png')
rangerSide_files = [rangerSide1, rangerSide2, rangerSide3]

knightSide1 = pygame.image.load('Knight_Side_1.png')
knightSide2 = pygame.image.load('Knight_Side_2.png')
knightSide3 = pygame.image.load('Knight_Side_3.png')
knightSide_files = [knightSide1, knightSide2, knightSide3]

clericSide1 = pygame.image.load('Cleric_Side_1.png')
clericSide2 = pygame.image.load('Cleric_Side_2.png')
clericSide3 = pygame.image.load('Cleric_Side_3.png')
clericSide_files = [clericSide1, clericSide2, clericSide3]

walkTime = 0
tempx = 0
while notStarted:
    mainClock.tick_busy_loop(60)
    windowSurface.blit(Background_dungeon, (0,0,1366,768))
    windowSurface.blit(titleImg, (0,0,1366,768))
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_RETURN:
                notStarted = False
        if event.type == KEYUP:
            if event.key == K_ESCAPE:
                    quit = True
                    notStarted = False  
    tempx += 5
    if tempx >= WINDOWWIDTH+600:
        tempx = 0;
    windowSurface.blit(boss_files[outsideRotate], (650,30,256,256))
    windowSurface.blit(knightSide_files[outsideRotate], (tempx,500,128,128))
    windowSurface.blit(mageSide_files[outsideRotate], (tempx-150,500,128,128))
    windowSurface.blit(rangerSide_files[outsideRotate], (tempx-300,500,128,128))
    windowSurface.blit(clericSide_files[outsideRotate], (tempx-450,500,128,128))
    if walkTime + 100 < pygame.time.get_ticks():
        outsideRotate -= 1
        walkTime = pygame.time.get_ticks()
    if outsideRotate <=0:
        outsideRotate = 2
    pygame.display.update()

while not quit:
        mainClock.tick_busy_loop(60)

        windowSurface.blit(Background_dungeon, (0,0,1366,768))

        for event in pygame.event.get():
            if event.type == QUIT:
                    quit = True        
            if event.type == KEYUP:
                    if event.key == K_ESCAPE:
                            quit = True
            if event.type == KEYDOWN:
                if event.key == K_w:
                    if  FACING == NORTH and player1.y > 0 and p1hp > 0:
                            player1.y -= 30
                    else:
                            FACING = NORTH
                if event.key == K_s:
                    if  FACING == SOUTH and player1.y < WINDOWHEIGHT - 64 and p1hp > 0:
                            player1.y += 30
                    else:
                            FACING = SOUTH
                if event.key == K_a:
                    if  FACING == WEST and player1.x > 0 and p1hp > 0:
                            player1.x -= 30
                    else:
                            FACING = WEST
                if event.key == K_d:
                    if  FACING == EAST and player1.x < WINDOWWIDTH - 128 and p1hp > 0:
                            player1.x += 30
                    else:
                            FACING = EAST
                if event.key == K_e and p1hp > 0:
                    attacks.append(swing(player1.x, player1.y, FACING))
                    currentKnight1 = 4
                    swordSound.play()
                if event.key == K_t:
                    if  FACING2 == NORTH and player2.y > 0 and p2hp > 0:
                            player2.y -= 30
                    else:
                            FACING2 = NORTH
                if event.key == K_g:
                    if  FACING2 == SOUTH and player2.y < WINDOWHEIGHT - 64 and p2hp > 0:
                            player2.y += 30
                    else:
                            FACING2 = SOUTH
                if event.key == K_f:
                    if  FACING2 == WEST and player2.x > 0 and p2hp > 0:
                            player2.x -= 30
                    else:
                            FACING2 = WEST
                if event.key == K_h:
                    if  FACING2 == EAST and player2.x < WINDOWWIDTH - 128 and p2hp > 0:
                            player2.x += 30
                    else:
                            FACING2 = EAST
                if event.key == K_y and p2hp > 0:
                    attacks.append(swing(player2.x, player2.y, FACING2))
                    currentKnight2 = 4
                    swordSound.play()
                if event.key == K_i:
                    if  FACING3 == NORTH and player3.y > 0 and p3hp > 0:
                            player3.y -= 30
                    else:
                            FACING3 = NORTH
                if event.key == K_k:
                    if  FACING3 == SOUTH and player3.y < WINDOWHEIGHT - 64 and p3hp > 0:
                            player3.y += 30
                    else:
                            FACING3 = SOUTH
                if event.key == K_j:
                    if  FACING3 == WEST and player3.x > 0 and p3hp > 0:
                            player3.x -= 30
                    else:
                            FACING3 = WEST
                if event.key == K_l:
                    if  FACING3 == EAST and player3.x < WINDOWWIDTH - 128 and p3hp > 0:
                            player3.x += 30
                    else:
                            FACING3 = EAST
                if event.key == K_o and p3hp > 0:
                    attacks.append(swing(player3.x, player3.y, FACING3))
                    currentKnight3 = 4
                    swordSound.play()
                if event.key == K_UP:
                    if  FACING4 == NORTH and player4.y > 0 and p4hp > 0:
                            player4.y -= 30
                    else:
                            FACING4 = NORTH
                if event.key == K_DOWN:
                    if  FACING4 == SOUTH and player4.y < WINDOWHEIGHT - 64 and p4hp > 0:
                            player4.y += 30
                    else:
                            FACING4 = SOUTH
                if event.key == K_LEFT:
                    if  FACING4 == WEST and player4.x > 0 and p4hp > 0:
                            player4.x -= 30
                    else:
                            FACING4 = WEST
                if event.key == K_RIGHT:
                    if  FACING4 == EAST and player4.x < WINDOWWIDTH - 128 and p4hp > 0:
                            player4.x += 30
                    else:
                            FACING4 = EAST
                if event.key == K_SPACE and p4hp > 0:
                    attacks.append(swing(player4.x, player4.y, FACING4))
                    currentKnight4 = 4
                    swordSound.play()

        if lastSpawn + 3000 < pygame.time.get_ticks() and enemiesLeft > 0:
            enes.append(enemy1(random.randint(0,WINDOWWIDTH-64),random.randint(0,WINDOWHEIGHT-64)))
            lastSpawn = pygame.time.get_ticks()
            spawnRate -= 10
        if enemiesLeft <= 0 and enes == [] and bossNotSpawned:
            enes.append(enemy2(WINDOWWIDTH, WINDOWHEIGHT/2))
            bossNotSpawned = False
            fightingBoss = True
            lastAttack = pygame.time.get_ticks()
        if lastPot + 5000 < pygame.time.get_ticks():
            pots.append(health(random.randint(32,WINDOWWIDTH-32), random.randint(32,WINDOWHEIGHT-32)))
            lastPot = pygame.time.get_ticks()

        if fightingBoss and enes != []:
            if lastAttack + 1500 < pygame.time.get_ticks():
                Emissiles.append(missileUp(enes[0].position.centerx, enes[0].position.centery))
                Emissiles.append(missileUPR(enes[0].position.centerx, enes[0].position.centery))
                Emissiles.append(missileRight(enes[0].position.centerx, enes[0].position.centery))
                Emissiles.append(missileDownR(enes[0].position.centerx, enes[0].position.centery))
                Emissiles.append(missileDown(enes[0].position.centerx, enes[0].position.centery))
                Emissiles.append(missileDownL(enes[0].position.centerx, enes[0].position.centery))
                Emissiles.append(missileUp(enes[0].position.centerx, enes[0].position.centery))
                Emissiles.append(missileLeft(enes[0].position.centerx, enes[0].position.centery))
                Emissiles.append(missileUpL(enes[0].position.centerx, enes[0].position.centery))
                lastAttack = pygame.time.get_ticks()

        for mis in Emissiles:
            mis.position.x += mis.monX
            mis.position.y += mis.monY
            windowSurface.blit(fireball, mis.position)
            if player1.colliderect(mis.position) and p1hp > 0:
                p1hp -= 1
                player1.x += random.randint(-5,5)
                player1.y += random.randint(-5,5)
                pHitSound.play()
            if player2.colliderect(mis.position) and p2hp > 0:
                p2hp -= 1
                player2.x += random.randint(-5,5)
                player2.y += random.randint(-5,5)
                pHitSound.play()
            if player3.colliderect(mis.position) and p3hp > 0:
                p3hp -= 1
                player3.x += random.randint(-5,5)
                player3.y += random.randint(-5,5)
                pHitSound.play()
            if player4.colliderect(mis.position) and p4hp > 0:
                p4hp -= 1
                player4.x += random.randint(-5,5)
                player4.y += random.randint(-5,5)
                pHitSound.play()

        for attack in attacks:
            windowSurface.blit(sword_files[attack.duration], attack.position)

            for enemy in enes:
                if attack.position.colliderect(enemy.position):
                    enemy.hp -= 1
                    enemy.position.x += random.randint(-5,5)
                    enemy.position.y += random.randint(-5,5)
                    temp = random.randint(0,20)
                    if temp == 20:
                        pots.append(health(enemy.position.x, enemy.position.y))
                    if enemy.hp < 0:
                        enes.remove(enemy)
                        eDie.play()
                        enemiesLeft -= 1
                    else:
                        eHitSound.play()
            attack.duration -= 1
            if attack.duration < 0:
                attacks.remove(attack)
        for eAttack in eneA:
            windowSurface.blit(claw_files[eAttack.duration], eAttack.position)
            eAttack.duration -= 1
            if eAttack.duration < 0:
                eneA.remove(eAttack)
            if player1.colliderect(eAttack.position) and p1hp > 0:
                p1hp -= 1
                player1.x += random.randint(-5,5)
                player1.y += random.randint(-5,5)
                pHitSound.play()
            if player2.colliderect(eAttack.position) and p2hp > 0:
                p2hp -= 1
                player2.x += random.randint(-5,5)
                player2.y += random.randint(-5,5)
                pHitSound.play()
            if player3.colliderect(eAttack.position) and p3hp > 0:
                p3hp -= 1
                player3.x += random.randint(-5,5)
                player3.y += random.randint(-5,5)
                pHitSound.play()
            if player4.colliderect(eAttack.position) and p4hp > 0:
                p4hp -= 1
                player4.x += random.randint(-5,5)
                player4.y += random.randint(-5,5)
                pHitSound.play()

        for pot in pots:
            windowSurface.blit(potImg, pot.position)
            if player1.colliderect(pot.position) and p1hp < 100:
                p1hp += 10
                if pots != []:
                    pots.remove(pot)
            if player2.colliderect(pot.position) and p2hp < 100:
                p2hp += 10
                if pots != []:
                    pots.remove(pot)
            if player3.colliderect(pot.position) and p3hp < 100:
                p3hp += 10
                if pots != []:
                    pots.remove(pot)
            if player4.colliderect(pot.position) and p4hp < 100:
                p4hp += 10
                if pots != []:
                    pots.remove(pot)

        for enemy in enes:
            direction = random.randint(1,100)
            if enemy.position.colliderect(player1) and p1hp > 0:
                p1hp -= 1
                player1.x += random.randint(-5,5)
                player1.y += random.randint(-5,5)
                pHitSound.play()
            if enemy.position.colliderect(player2) and p2hp > 0:
                p2hp -= 1
                player2.x += random.randint(-5,5)
                player2.y += random.randint(-5,5)
                pHitSound.play()
            if enemy.position.colliderect(player3) and p3hp > 0:
                p3hp -= 1
                player3.x += random.randint(-5,5)
                player3.y += random.randint(-5,5)
                pHitSound.play()
            if enemy.position.colliderect(player4) and p4hp > 0:
                p4hp -= 1
                player4.x += random.randint(-5,5)
                player4.y += random.randint(-5,5)
                pHitSound.play()
            if direction == 1:
                    enemy.monX = 0
                    enemy.monY = -1
            elif direction == 2:
                    enemy.facing = EAST
                    enemy.monX = 1
                    enemy.monY = 0
            elif direction == 3:
                    enemy.monX = 0
                    enemy.monY = 1
            elif direction == 4:
                    enemy.facing = WEST
                    enemy.monX = -1
                    enemy.monY = 0
            else:
                if enemy.position.x <= 0:
                    enemy.monX += 5
                    enemy.monY += 0
                if enemy.position.y <= 0:
                    enemy.monX += 0
                    enemy.monY += 5
                if enemy.position.x >= WINDOWWIDTH-64:
                    enemy.monX -= 5
                    enemy.monY += 0
                if enemy.position.y >= WINDOWHEIGHT-64:
                    enemy.monX += 0
                    enemy.monY -= 5
                if enemy.monX != 0:
                    enemy.position.x += enemy.monX
                if enemy.monY != 0:
                    enemy.position.y += enemy.monY

            temp = random.randint(0,100)
            if temp == 1:
                eneA.append(swing(enemy.position.x, enemy.position.y, enemy.facing))
                clawSound.play()
            tempPic = enemy.picture[flipTime]
            if enemy.facing == EAST:
                windowSurface.blit(pygame.transform.flip(tempPic, True, False), enemy.position)
            else:
                windowSurface.blit(tempPic, enemy.position)

            pygame.transform.rotate(enemy.picture[flipTime], 0)
            text = basicFont2.render(str(enemy.hp), True, BLACK)
            windowSurface.blit(text, enemy.position)
        if p1hp > 0:
            windowSurface.blit(pygame.transform.rotate(cleric_files[currentKnight1], FACING), player1)
            text = basicFont2.render(str(p1hp), True, BLACK)
            windowSurface.blit(text, player1)
        if p2hp > 0:
            windowSurface.blit(pygame.transform.rotate(mage_files[currentKnight2], FACING2), player2)
            text = basicFont2.render(str(p2hp), True, BLACK)
            windowSurface.blit(text, player2)
        if p3hp > 0:
            windowSurface.blit(pygame.transform.rotate(ranger_files[currentKnight3], FACING3), player3)
            text = basicFont2.render(str(p3hp), True, BLACK)
            windowSurface.blit(text, player3)
        if p4hp > 0:
            windowSurface.blit(pygame.transform.rotate(knight_files[currentKnight4], FACING4), player4)
            text = basicFont2.render(str(p4hp), True, BLACK)
            windowSurface.blit(text, player4)

        if p1hp <= 0:
            windowSurface.blit(ghost_files[currentKnight1], player1)
        if p2hp <= 0:
            windowSurface.blit(ghost_files[currentKnight2], player2)
        if p3hp <= 0:
            windowSurface.blit(ghost_files[currentKnight3], player3)
        if p4hp <= 0:
            windowSurface.blit(ghost_files[currentKnight4], player4)

        if enemiesLeft > 0:
            text = basicFont2.render("Enemies Left: "+str(enemiesLeft)+ " Cleric: W,A,S,D Attack: E Mage: T,F,G,H Attack: Y Archer: I,J,K,L Fire: O Knight: UP,DOWN,LEFT,RIGHT Attack: Space", True, BLACK)
            windowSurface.blit(text, (5,5,50,50))

        if p1hp <= 0 and p2hp <= 0 and p3hp <= 0 and p4hp <= 0:
            windowSurface.blit(gameover, (0,0,1366,768))
            if play1:
                hDie.play()
                play1 = False
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_RETURN:
                        p1hp = 100
                        p2hp = 100
                        p3hp = 100
                        p4hp = 100
                        enes = []
                        pots = []
                        Emissiles = []
                        play1 = True
                        enemiesLeft = 30
                        spawnRate = 3000
                        bossNotSpawned =  True
                        won = False
                        lastSpawn = pygame.time.get_ticks()
                        fightingBoss = False
        if enes == [] and not bossNotSpawned:
            won = True;
            Emissiles = []
            fightingBoss = False
        if won:
            windowSurface.blit(victory, (0,0,1366,768))
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_RETURN:
                        p1hp = 100
                        p2hp = 100
                        p3hp = 100
                        p4hp = 100
                        enes = []
                        pots = []
                        play1 = True
                        enemiesLeft = 30
                        spawnRate = 3000
                        bossNotSpawned =  True
                        won = False
                        enes = []
                        Emissiles = []
                        lastSpawn = pygame.time.get_ticks()
                        fightingBoss = False

        pygame.display.update()
        pygame.transform.rotate(cleric_files[currentKnight1], 0)
        pygame.transform.rotate(mage_files[currentKnight2], 0)
        pygame.transform.rotate(ranger_files[currentKnight3], 0)
        pygame.transform.rotate(knight_files[currentKnight4], 0)

        if animateSec + 250 < pygame.time.get_ticks():
            
            if currentKnight1 == 0:
                currentKnight1 = 1
            else:
                currentKnight1 -=1
            if currentKnight2 == 0:
                currentKnight2 = 1
            else:
                currentKnight2 -=1
            if currentKnight3 == 0:
                currentKnight3 = 1
            else:
                currentKnight3 -=1
            if currentKnight4 == 0:
                currentKnight4 = 1
            else:
                currentKnight4 -=1
            if flipTime == 0:
                flipTime = 1
            elif flipTime == 1:
                flipTime = 0
            animateSec = pygame.time.get_ticks()
pygame.quit()
sys.exit()