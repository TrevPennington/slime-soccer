# Example file showing a circle moving on screen
import pygame
import random

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

player_radius = 40

def get_random(start, end, buffer):
    return random.randrange(start + buffer, end - buffer)

score_tile_pos = pygame.Vector2(get_random(0, screen.get_width(), 20), get_random(0, screen.get_height(), 20))
buff_tile_pos = pygame.Vector2(get_random(0, screen.get_width(), 20), get_random(0, screen.get_height(), 20))
nerf_tile_pos = pygame.Vector2(get_random(0, screen.get_width(), 20), get_random(0, screen.get_height(), 20))


player_one_pos = pygame.Vector2(screen.get_width() * 0.25, screen.get_height() / 2)
player_two_pos = pygame.Vector2(screen.get_width() * 0.75, screen.get_height() / 2)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("grey")

    # Player 1
    pygame.draw.circle(screen, "red", player_one_pos, player_radius)

    # Player 2
    pygame.draw.circle(screen, "blue", player_two_pos, player_radius)

    # Score tile
    pygame.draw.rect(screen, "white", pygame.Rect(score_tile_pos.x, score_tile_pos.y, 40, 40))

    # Buff tile
    pygame.draw.rect(screen, "green", pygame.Rect(buff_tile_pos.x, buff_tile_pos.y, 40, 40))

    # Nerf tile
    pygame.draw.rect(screen, "yellow", pygame.Rect(nerf_tile_pos.x, nerf_tile_pos.y, 40, 40))

    def randomize_score_tile():
        score_tile_pos.x = get_random(0, screen.get_width(), 20)
        score_tile_pos.y = get_random(0, screen.get_height(), 20)

    # Check for score tile touch
    def check_for_score(x, y, player):
        # Score hit box
        min_score_x = score_tile_pos.x - 20
        max_score_x = score_tile_pos.x + 20
        min_score_y = score_tile_pos.y - 20
        max_score_y = score_tile_pos.y + 20

        # Player hit box
        min_player_x = x - 20
        max_player_x = x + 20
        min_player_y = y - 20
        max_player_y = y + 20

        # Right collision
        if max_player_x > min_score_x and min_player_x < min_score_x and y < max_score_y and y > min_score_y:
            print("SCORE ------------------- ", player)
            randomize_score_tile()


        # # Left collision
        # if min_player_x < max_score_x and y < max_score_y and y > min_score_y:
        #     print("SCORE ------------------- ", player)
        #     randomize_score_tile()


        # # Top collision
        # if min_player_y < max_score_y and x < max_score_x and x > min_score_x:
        #     print("SCORE ------------------- ", player)
        #     randomize_score_tile()

        
        # # Bottom collision
        # if max_player_y > min_score_y and x < max_score_x and x > min_score_x:
        #     print("SCORE ------------------- ", player)
        #     randomize_score_tile()


    # Player 1 controls
    keys = pygame.key.get_pressed()
    # MOVE UP
    if keys[pygame.K_w]:
        if player_one_pos.y - player_radius > 0:
            check_for_score(player_one_pos.x, player_one_pos.y, 1)
            player_one_pos.y -= 300 * dt
    # MOVE DOWN
    if keys[pygame.K_s]:
        if player_one_pos.y + player_radius < screen.get_height():
            check_for_score(player_one_pos.x, player_one_pos.y, 1)
            player_one_pos.y += 300 * dt
    # MOVE LEFT
    if keys[pygame.K_a]:
        if player_one_pos.x - player_radius > 0:
            check_for_score(player_one_pos.x, player_one_pos.y, 1)
            player_one_pos.x  -= 300 * dt
    # MOVE RIGHT
    if keys[pygame.K_d]:
        if player_one_pos.x + player_radius < screen.get_width():
            check_for_score(player_one_pos.x, player_one_pos.y, 1)
            player_one_pos.x += 300 * dt

    # Player 2 controls
    keys = pygame.key.get_pressed()
    # MOVE UP
    if keys[pygame.K_UP]:
        if player_two_pos.y - player_radius > 0:
            check_for_score(player_two_pos.x, player_two_pos.y, 2)
            player_two_pos.y -= 300 * dt
    # MOVE DOWN
    if keys[pygame.K_DOWN]:
        if player_two_pos.y + player_radius < screen.get_height():
            check_for_score(player_two_pos.x, player_two_pos.y, 2)
            player_two_pos.y += 300 * dt
    # MOVE LEFT
    if keys[pygame.K_LEFT]:
        if player_two_pos.x - player_radius > 0:
            check_for_score(player_two_pos.x, player_two_pos.y, 2)
            player_two_pos.x -= 300 * dt
    # MOVE RIGHT
    if keys[pygame.K_RIGHT]:
        if player_two_pos.x + player_radius < screen.get_width():
            check_for_score(player_two_pos.x, player_two_pos.y, 2)
            player_two_pos.x += 300 * dt

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()