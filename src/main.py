from datetime import datetime

import pygame as pg
from WindowConfig import WindowConfig
from src.light import Light
from src.phong import Phong
from src.sphere import Sphere

window_config = WindowConfig()
CENTER = (window_config.get_width() // 2, window_config.get_height() // 2)

def config():
    pg.display.set_mode((window_config.get_width(), window_config.get_height()))
    pg.display.set_caption(window_config.get_title())


def main():
    pg.init()
    config()
    clock = pg.time.Clock()
    screen = pg.display.get_surface()

    running = True
    fps = 60

    step = 100
    light_source = Light(CENTER[0], CENTER[1], 150)
    sphere = Sphere(150, CENTER[0], CENTER[1], 0, (170, 169, 173))
    observer = (CENTER[0], CENTER[1], 800)
    phong = Phong(screen, light_source, observer, 0.1, 0.4, 0.9, 150, 0.6, 1)

    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_UP:
                    light_source.move(0, 0, -step)
                    print(light_source.get_position())
                if event.key == pg.K_DOWN:
                    light_source.move(0, 0, step)
                    print(light_source.get_position())
                if event.key == pg.K_LEFT:
                    light_source.move(-step, 0, 0)
                    print(light_source.get_position())
                if event.key == pg.K_RIGHT:
                    light_source.move(step, 0, 0)
                    print(light_source.get_position())
                if event.key == pg.K_LSHIFT:
                    light_source.move(0, -step, 0)
                    print(light_source.get_position())
                if event.key == pg.K_LCTRL:
                    light_source.move(0, step, 0)
                    print(light_source.get_position())
                if event.key == pg.K_o:
                    filename = f"screenshot_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.png"
                    pg.image.save(pg.display.get_surface(), filename)

                if event.key == pg.K_ESCAPE:
                    running = False


        pg.display.get_surface().fill((pg.Color("black")))

        phong.render_sphere(sphere)
        pg.draw.circle(screen, pg.Color("white"), light_source.get_position_2d(), 5)
        print("done")

        pg.display.flip()
        clock.tick(fps)

    pg.quit()


if __name__ == '__main__':
    main()
