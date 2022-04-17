import pygame
import os
import random
import time
pygame.font.init()

HAPPY_FONT = pygame.font.SysFont('comicsans', 50)
BLACK = (0, 0, 0)
WIDTH, HEIGHT = 1200 , 380
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
WIN2 = pygame.display.set_mode((WIDTH, HEIGHT))
FPS = 60
sadmans = []
HAPPY_TEXT_DISPLAYED = pygame.USEREVENT + 1
HEALTH_TEXT_DISPLAYED = pygame.USEREVENT + 2
pygame.display.set_caption('HAPPY GAME')
points = 0
health = 3
PLAYER_WIDTH, PLAYER_HEIGHT = 60, 60
PLAYER_START_X, PLAYER_START_Y = 50, 250
sadman_WIDTH, sadman_HEIGHT = 60, 60
LIFE_WIDTH,LIFE_HEIGHT = 60, 60
VICTORY_TEXT_DISPLAYED = pygame.USEREVENT
DEFEAT_TEXT_DISPLAYED = pygame.USEREVENT
IS_TRY_AGAIN = pygame.USEREVENT + 3
HOW_TO_PLAY_TEXT_DISPLAYED = pygame.USEREVENT + 4
HUGG_WIDTH, HUGG_HEIGHT = 60, 60

def draw_window(background, hero, sadmans, is_display_hug_text, hug_text):
    background.update()
    background.render()

    for sadman in sadmans:
        WIN.blit(sadman.box, (sadman.x, sadman.y))
    WIN.blit(hero.box, (hero.x, hero.y))
    hero.draw(WIN)

    points_text = HAPPY_FONT.render(f'Hug Points: {hero.points}', True, BLACK)
    WIN.blit(points_text, (10, 10))
    health_text = HAPPY_FONT.render(f'Attempts: {hero.health}', True, BLACK)
    WIN.blit(health_text, (900, 10))


    pygame.display.update()


def create_sadman():
    y = random.randrange(50, 250)
    item = man(1050, y)
    return item

def start():
    hero = player(PLAYER_START_X, PLAYER_START_Y)
    sadman = create_sadman()
    sadmans.append(sadman)
    run = True
    clock = pygame.time.Clock()
    background = Background()
    is_display_hug_text = False
    hug_text = HAPPY_FONT.render('I am happy', True, BLACK)
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == HAPPY_TEXT_DISPLAYED:
                is_display_hug_text = True

        keys_pressed = pygame.key.get_pressed()

        for sadman in sadmans:
            sadman.draw(WIN, hero)

        hero.handle_movement(keys_pressed)
        draw_window(background, hero, sadmans, is_display_hug_text, hug_text)
        clock.tick(FPS)
def main():
    preView()

def preView():
    pygame.init()
    res = (1200, 380)
    screen = pygame.display.set_mode(res)
    color = (255, 255, 255)
    color_light = (255, 255, 255)
    color_dark = (100, 100, 100)
    width = screen.get_width()
    height = screen.get_height()
    smallfont = pygame.font.SysFont('Corbel', 35)
    art = smallfont.render('HUGGING BEAR ', True, color)
    startg = smallfont.render('Start',True,color)
    while True:
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if width / 2 <= mouse[0] <= width / 2 + 140 and height / 2 <= mouse[1] <= height / 2 + 40:
                    start()
        screen.fill((0, 0, 0))
        mouse = pygame.mouse.get_pos()
        if width / 2 <= mouse[0] <= width / 2 + 140 and height / 2 <= mouse[1] <= height / 2 + 40:
            pygame.draw.rect(screen, color_light, [width / 2.3, height / 2, 140, 40])

        else:
            pygame.draw.rect(screen, color_dark, [width / 2.1, height / 2, 70, 30])
            screen.blit(art, (width / 2.45, height / 6))
            screen.blit(startg, (width / 2.1, height / 2))
        pygame.display.update()

def text_objects(text, font):
    textSurface = font.render(text, True, BLACK)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf', 115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((WIDTH / 2), (HEIGHT / 2))
    WIN.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(5)
    pygame.stop()




class Background(object):
    def __init__(self):
        self.bgimage = pygame.image.load(os.path.join('images', 'bg.jpg'))
        self.rectBGimg = self.bgimage.get_rect()

        self.bgY1 = 0
        self.bgX1 = 0

        self.bgY2 = 0
        self.bgX2 = self.rectBGimg.width
        self.moving_speed = 4

    def update(self):
        self.bgX1 -= self.moving_speed
        self.bgX2 -= self.moving_speed
        if self.bgX1 <= -self.rectBGimg.width:
            self.bgX1 = self.rectBGimg.width
        if self.bgX2 <= -self.rectBGimg.width:
            self.bgX2 = self.rectBGimg.width

    def render(self):
        WIN.blit(self.bgimage, (self.bgX1, self.bgY1))
        WIN.blit(self.bgimage, (self.bgX2, self.bgY2))


class man(object):
    def __init__(self, x, y):
        self.image = pygame.image.load(os.path.join('images', 'sadman.png'))
        self.box = pygame.transform.scale(self.image, (sadman_WIDTH, sadman_HEIGHT))
        self.rect = pygame.Rect(x, y, sadman_WIDTH, sadman_HEIGHT)
        self.x = x
        self.y = y

    def draw(self, win, hero):
        #hero.Bsound.play()
        self.x -= hero.sadman_vel
        self.rect = pygame.Rect(self.x, self.y, sadman_WIDTH, sadman_HEIGHT)

        if self.x <= 0:
            sadmans.remove(self)
            item = create_sadman()
            sadmans.append(item)
            if hero.health > 0:
                hero.health -= 1

        if hero.health == 0:
            message_display("Game Over")


        if hero.rect.colliderect(self.rect):  # hug
            hero.sound.play()
            sadmans.remove(self)
            item = create_sadman()
            sadmans.append(item)
            pygame.event.post(pygame.event.Event(HAPPY_TEXT_DISPLAYED))
            pygame.event.post(pygame.event.Event(HEALTH_TEXT_DISPLAYED))
            hero.points += 1
            if hero.points == 5:
                hero.won.play()
                message_display("Congrats you WON !!")


            if hero.points % 5 == 0:
                hero.sadman_vel += 3
        else:
            WIN.blit(self.box, (self.x, self.y))



class player(object):
    def __init__(self, x, y):
        self.image = pygame.image.load(os.path.join('images', 'player.png'))
        self.box = pygame.transform.scale(self.image, (PLAYER_WIDTH, PLAYER_HEIGHT))
        self.rect = pygame.Rect(x, y, PLAYER_WIDTH, PLAYER_HEIGHT)
        self.x = x
        self.y = y
        self.points = 1
        self.jumping = 5
        self.sadman_vel = 5
        self.health = 3
        self.sound = pygame.mixer.Sound(os.path.join('Sounds', 'hug.mp3'))
        self.Bsound = pygame.mixer.Sound(os.path.join('Sounds', 'BGM.mp3'))
        self.won = pygame.mixer.Sound(os.path.join('Sounds', 'won.mp3'))

    def draw(self, win):
        WIN.blit(self.box, (self.x, self.y))

    def handle_movement(self, keys_pressed):
        pressed = False
        if keys_pressed[pygame.K_DOWN]:
            if self.y < HEIGHT - self.rect.height:
                self.y += 5
                self.rect = pygame.Rect(self.x, self.y, PLAYER_WIDTH, PLAYER_HEIGHT)
        if keys_pressed[pygame.K_UP]:
            if self.y > 0:
                self.y -= 5
                self.rect = pygame.Rect(self.x, self.y, PLAYER_WIDTH, PLAYER_HEIGHT)


        if not pressed and self.jumping:
            if self.y >= PLAYER_START_Y:
                self.jumping = False
            else:
                self.y += 1
                self.rect = pygame.Rect(self.x, self.y, PLAYER_WIDTH, PLAYER_HEIGHT)

if __name__ == "__main__":
    main()
