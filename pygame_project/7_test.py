import pygame
import os

pygame.init()

screen_width = 1080
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("MAPLE STORY")

clock = pygame.time.Clock()

###########################################################################################
current_path = os.path.dirname(__file__) # 현재 파일의 위치 반환
image_path = os.path.join(current_path, "images") # 이미지 파일의 위치 반환

# 배경 만들기
background = pygame.image.load(os.path.join(image_path, "background2.png"))

# 발판 만들기
foothold_images = [
    pygame.image.load(os.path.join(image_path, "foothold1.png")),
    pygame.image.load(os.path.join(image_path, "foothold2.png")),
    pygame.image.load(os.path.join(image_path, "foothold3.png")),
    pygame.image.load(os.path.join(image_path, "foothold4.png")),
]

foothold1_size = foothold_images[0].get_rect().size
foothold1_width = foothold1_size[0]
foothold1_height = foothold1_size[1]

foothold2_size = foothold_images[1].get_rect().size
foothold2_width = foothold2_size[0]
foothold2_height = foothold2_size[1]

foothold3_size = foothold_images[2].get_rect().size
foothold3_width = foothold3_size[0]
foothold3_height = foothold3_size[1]

foothold4_size = foothold_images[3].get_rect().size
foothold4_width = foothold4_size[0]
foothold4_height = foothold4_size[1]

# 캐릭터 만들기
character = pygame.image.load(os.path.join(image_path, "character.png"))
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = 10
character_y_pos = screen_height - foothold1_height - character_height

# 포탈 만들기
portal = pygame.image.load(os.path.join(image_path, "portal.png"))
portal_size = portal.get_rect().size
portal_width = portal_size[0]
portal_height = portal_size[1]

###########################################################################################

speed = 3
character_to_x = 0
character_to_y = 0
running = True
teleport_left = False
teleport_right = False
isJump = False
jumpCount = 10

###########################################################################################


while running:

    dt = clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        character_x_pos -= speed
    if keys[pygame.K_RIGHT]:
        character_x_pos += speed

    # 점프 코드
    if not(isJump):
        if keys[pygame.K_LALT]:
            isJump = True
    else:
        if jumpCount >= -10:
            neg = 1
            if jumpCount < 0:
                neg = -1
            character_y_pos -= (jumpCount ** 2) * 0.5 * neg
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10

    screen.blit(background, (0,0))
    screen.blit(foothold_images[0], (0 , screen_height - foothold1_height))
    screen.blit(foothold_images[1], (0 , 2 * (screen_height / 3) - foothold2_height))
    screen.blit(foothold_images[2], (screen_width - foothold2_width , 2 * (screen_height / 3) - foothold2_height))
    screen.blit(foothold_images[3], ((screen_width / 2) - foothold4_width / 2, screen_height / 3 - foothold3_height))
    screen.blit(portal, (screen_width - portal_width - 10, screen_height - foothold1_height - portal_height))
    screen.blit(character, (character_x_pos, character_y_pos))
    pygame.display.update()

pygame.quit()  