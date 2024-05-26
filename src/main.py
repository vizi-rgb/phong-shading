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
    light_source = Light(CENTER[0], CENTER[1], 300)
    observer = (CENTER[0], CENTER[1], 800)

    rotation = []

    # Metallic
    sphere = Sphere(150, CENTER[0], CENTER[1], 0, (170, 169, 173))
    phong = Phong(screen, light_source, observer, 0.9, 0.4, 0.9, 150, 0.9, 1)
    rotation.append((sphere, phong))

    # Wooden
    sphere = Sphere(150, CENTER[0], CENTER[1], 0, (129, 84, 56))
    phong = Phong(screen, light_source, observer, 0.5, 0.9, 0.1, 100, 0.5, 1)
    rotation.append((sphere, phong))

    # Brick
    sphere = Sphere(150, CENTER[0], CENTER[1], 0, (255, 87, 51))
    phong = Phong(screen, light_source, observer, 0.3, 0.1, 0.8, 10, 0.8, 1)
    rotation.append((sphere, phong))

    # Brick
    sphere = Sphere(150, CENTER[0], CENTER[1], 0, (255, 0, 255))
    phong = Phong(screen, light_source, observer, 0.5, 0.4, 0.4, 200, 0.8, 1)
    rotation.append((sphere, phong))

    # Gold
    sphere = Sphere(150, CENTER[0], CENTER[1], 0, (229, 184, 11))
    phong = Phong(screen, light_source, observer, 0.24725, 0.797357, 0.34615, 83, 1, 1)
    rotation.append((sphere, phong))

    # Chrome
    sphere = Sphere(150, CENTER[0], CENTER[1], 0, (224, 224, 224))
    phong = Phong(screen, light_source, observer, 0.25, 0.774597, 0.4, 77, 1, 1)
    rotation.append((sphere, phong))


    selected = len(rotation) - 1

    # Dunno
    # sphere = Sphere(150, CENTER[0], CENTER[1], 0, (255, 255, 255))
    # phong = Phong(screen, light_source, observer, 0.5, 0.25, 0.75, 100, 0.8, 1)

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
                if event.key == pg.K_n:
                    selected = (selected + 1) % len(rotation)
                    sphere, phong = rotation[selected]


                if event.key == pg.K_o:
                    filename = f"screenshot_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.png"
                    pg.image.save(pg.display.get_surface(), filename)

                if event.key == pg.K_ESCAPE:
                    running = False


        pg.display.get_surface().fill((pg.Color("black")))

        phong.render_sphere(sphere)
        pg.draw.circle(screen, pg.Color("white"), light_source.get_position_2d(), 5)

        pg.display.flip()
        clock.tick(fps)

    pg.quit()


if __name__ == '__main__':
    main()
