from datetime import datetime

import pygame as pg
import math
from WindowConfig import WindowConfig
from Camera import Camera
from Renderer import Renderer
import numpy as np

window_config = WindowConfig()

center = (window_config.get_width() // 2, window_config.get_height() // 2)
radius = 200


def draw_sphere(renderer):
    """Draw the 3D sphere by projecting points onto the 2D screen"""
    for theta in range(0, 360, 2):
        for phi in range(0, 360, 2):
            theta_rad = math.radians(theta)
            phi_rad = math.radians(phi)
            x = radius * math.sin(phi_rad) * math.cos(theta_rad)
            y = radius * math.sin(phi_rad) * math.sin(theta_rad)
            z = radius * math.cos(phi_rad)

            screen_x, screen_y = renderer.project(np.array([x, y, z]))

            # Calculate shading based on z value (depth)
            shade = 255 - int((z + radius) / (2 * radius) * 255)
            color = (shade, shade, shade)

            if 0 <= screen_x < window_config.get_width() and 0 <= screen_y < window_config.get_height():
                pg.display.get_surface().set_at((screen_x, screen_y), color)


def config():
    pg.display.set_mode((window_config.get_width(), window_config.get_height()))
    pg.display.set_caption(window_config.get_title())


def main():
    pg.init()
    config()
    clock = pg.time.Clock()

    running = True
    fps = 60
    camera = Camera()
    amount = 45
    renderer = Renderer(list(), camera, window_config)

    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_LEFT:
                    camera.move_left(amount)
                if event.key == pg.K_RIGHT:
                    camera.move_right(amount)
                if event.key == pg.K_UP:
                    camera.move_forward(amount)
                if event.key == pg.K_DOWN:
                    camera.move_backward(amount)
                if event.key == pg.K_LSHIFT:
                    camera.move_up(amount)
                if event.key == pg.K_LCTRL:
                    camera.move_down(amount)
                if event.key == pg.K_w:
                    camera.rotate_roll(amount)
                if event.key == pg.K_s:
                    camera.rotate_roll(-amount)
                if event.key == pg.K_q:
                    camera.rotate_pitch(-amount)
                if event.key == pg.K_e:
                    camera.rotate_pitch(amount)
                if event.key == pg.K_a:
                    camera.rotate_yaw(amount)
                if event.key == pg.K_d:
                    camera.rotate_yaw(-amount)
                if event.key == pg.K_EQUALS:
                    camera.zoom_in()
                if event.key == pg.K_MINUS:
                    camera.zoom_out()
                if event.key == pg.K_0:
                    camera.reset_zoom()
                if event.key == pg.K_o:
                    filename = f"screenshot_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.png"
                    pg.image.save(pg.display.get_surface(), filename)

                if event.key == pg.K_ESCAPE:
                    running = False


        pg.display.get_surface().fill((0, 0, 0))
        draw_sphere(renderer)
        pg.display.flip()
        clock.tick(fps)

    pg.quit()


if __name__ == '__main__':
    main()
