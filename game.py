# Example file showing a circle moving on screen
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

player_radius = 40

player_one_pos = pygame.Vector2(screen.get_width() * 0.25, screen.get_height() / 2)
player_two_pos = pygame.Vector2(screen.get_width() * 0.75, screen.get_height() / 2)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("blue")

    # Player 1
    pygame.draw.circle(screen, "red", player_one_pos, player_radius)

    # Play 2
    pygame.draw.circle(screen, "yellow", player_two_pos, player_radius)


    # Player 1 controls
    keys = pygame.key.get_pressed()
    # MOVE UP
    if keys[pygame.K_w]:
        if player_one_pos.y - player_radius > 0:
            player_one_pos.y -= 300 * dt
    # MOVE DOWN
    if keys[pygame.K_s]:
        if player_one_pos.y + player_radius < screen.get_height():
            player_one_pos.y += 300 * dt
    # MOVE LEFT
    if keys[pygame.K_a]:
        if player_one_pos.x - player_radius > 0:
            player_one_pos.x  -= 300 * dt
    # MOVE RIGHT
    if keys[pygame.K_d]:
        if player_one_pos.x + player_radius < screen.get_width():
            player_one_pos.x += 300 * dt

    # Player 2 controls
    keys = pygame.key.get_pressed()
    # MOVE UP
    if keys[pygame.K_UP]:
        if player_two_pos.y - player_radius > 0:
            player_two_pos.y -= 300 * dt
    # MOVE DOWN
    if keys[pygame.K_DOWN]:
        if player_two_pos.y + player_radius < screen.get_height():
            player_two_pos.y += 300 * dt
    # MOVE LEFT
    if keys[pygame.K_LEFT]:
        if player_two_pos.x - player_radius > 0:
            player_two_pos.x -= 300 * dt
    # MOVE RIGHT
    if keys[pygame.K_RIGHT]:
        if player_two_pos.x + player_radius < screen.get_width():
            player_two_pos.x += 300 * dt

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()