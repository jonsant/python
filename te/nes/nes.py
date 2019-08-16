import sys

import pygame

from ship import Ship

def run_game():
    pygame.joystick.init()
    try:
        joystick = pygame.joystick.Joystick(0)
        joystick.init()
        print(joystick.get_name())
        print(joystick.get_numaxes())
        print(joystick.get_numbuttons())
    except:
        print("Joystick error")

    # Initialize game and create a screen object.
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("NES")

    t = pygame.time.Clock()

    # Make a ship.
    ship = Ship(screen)

    # Set the background color.
    bg_color = (230, 230, 230)

    # Start the main loop for the game

    while True:

        ship.update()
        
        # Watch for keyboard and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            # elif event.type == pygame.JOYBUTTONDOWN:
            #     if event.button == 1:
            #         ship.moving_right = True
            # elif event.type == pygame.JOYBUTTONUP:
            #     if event.button == 1:
            #         ship.moving_right = False
            elif event.type == pygame.JOYAXISMOTION:
                print(event)
                if event.axis == 0 or event.axis == 3:
                    val = round(event.value)
                    print(val)
                    if val == 1:
                        ship.moving_right = True
                    if val == -1:
                        ship.moving_left = True
                    if val == 0:
                        ship.moving_left = False
                        ship.moving_right = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    # Move the ship to the right.
                    ship.moving_right = True
                elif event.key == pygame.K_LEFT:
                    ship.moving_left = True

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    ship.moving_right = False
                elif event.key == pygame.K_LEFT:
                    ship.moving_left = False   

        screen.fill(bg_color)
        ship.blitme()

        #t.tick()
        # Make the most recently drawn screen visible.
        pygame.display.flip()
        #pygame.event.pump()

run_game()
