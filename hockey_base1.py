import pygame
import sys

# ゲームの初期化
pygame.init()


# 定数の設定
WIDTH, HEIGHT = 800, 400
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PADDLE_WIDTH, PADDLE_HEIGHT = 10, 100
PUCK_RADIUS = 10
FPS = 60

# 画面の作成
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('エアホッケー')

# パドルとパックのクラス
class Paddle(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((PADDLE_WIDTH, PADDLE_HEIGHT))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect(topleft=(x, y))

    def move(self, y):
        self.rect.y += y
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT

class Puck(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((PUCK_RADIUS * 2, PUCK_RADIUS * 2), pygame.SRCALPHA)
        pygame.draw.circle(self.image, BLACK, (PUCK_RADIUS, PUCK_RADIUS), PUCK_RADIUS)
        self.rect = self.image.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        self.speed_x = 4
        self.speed_y = 4

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        if self.rect.top <= 0 or self.rect.bottom >= HEIGHT:
            self.speed_y = -self.speed_y

        if self.rect.left <= 0 or self.rect.right >= WIDTH:
            self.speed_x = -self.speed_x

# インスタンスの作成
paddle1 = Paddle(10, HEIGHT // 2 - PADDLE_HEIGHT // 2)
paddle2 = Paddle(WIDTH - 20, HEIGHT // 2 - PADDLE_HEIGHT // 2)
puck = Puck()

all_sprites = pygame.sprite.Group()
all_sprites.add(paddle1, paddle2, puck)

# メインゲームループ
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        paddle1.move(-5)
    if keys[pygame.K_s]:
        paddle1.move(5)
    if keys[pygame.K_UP]:
        paddle2.move(-5)
    if keys[pygame.K_DOWN]:
        paddle2.move(5)

    puck.update()

    # 衝突処理
    if pygame.sprite.collide_rect(puck, paddle1) or pygame.sprite.collide_rect(puck, paddle2):
        puck.speed_x = -puck.speed_x

    screen.fill(WHITE)
    all_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(FPS)
