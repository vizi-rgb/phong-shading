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
    light_source = Light(CENTER[0] + 2 * step, CENTER[1] - 2 * step, 1000)
    observer = (CENTER[0], CENTER[1], 800)

    rotation = []

    # Metallic
    sphere = Sphere(150, CENTER[0], CENTER[1], 0, (170, 169, 173))
    phong = Phong(screen, light_source, observer, 0.3, 0.4, 0.9, 150, 0.9, 1)
    rotation.append((sphere, phong, "Metallic"))

    # Pearl
    sphere = Sphere(150, CENTER[0], CENTER[1], 0, (245, 245, 245))
    phong = Phong(screen, light_source, observer, 0.25, 0.296648, 1, 11.264, 1, 1)
    rotation.append((sphere, phong, "Pearl"))

    # Bronze
    sphere = Sphere(150, CENTER[0], CENTER[1], 0, (110, 77, 37))
    phong = Phong(screen, light_source, observer, 0.2125, 0.393548, 0.714, 25.6, 1, 1)
    rotation.append((sphere, phong, "Bronze"))

    # Polished Bronze
    sphere = Sphere(150, CENTER[0], CENTER[1], 0, (110, 77, 37))
    phong = Phong(screen, light_source, observer, 0.25, 0.774597, 0.4, 76.8, 1, 1)
    rotation.append((sphere, phong, "Polished Bronze"))

    # Gold
    sphere = Sphere(150, CENTER[0], CENTER[1], 0, (229, 184, 11))
    phong = Phong(screen, light_source, observer, 0.24725, 0.797357, 0.34615, 83, 1, 1)
    rotation.append((sphere, phong, "Gold"))

    # Chrome
    sphere = Sphere(150, CENTER[0], CENTER[1], 0, (224, 224, 224))
    phong = Phong(screen, light_source, observer, 0.25, 0.774597, 0.4, 76.8, 1, 1)
    rotation.append((sphere, phong, "Chrome"))

    # Wooden
    sphere = Sphere(150, CENTER[0], CENTER[1], 0, (129, 84, 56))
    phong = Phong(screen, light_source, observer, 0.5, 0.01, 0.9, 300, 0.8, 1)
    rotation.append((sphere, phong, "Wooden"))

    # Min Diff Max Spec
    sphere = Sphere(150, CENTER[0], CENTER[1], 0, (129, 84, 56))
    phong = Phong(screen, light_source, observer, 0.5, 1, 0, 300, 0.8, 1)
    rotation.append((sphere, phong, "Min Diff Max Spec"))

    # Max diff Min Spec
    sphere = Sphere(150, CENTER[0], CENTER[1], 0, (129, 84, 56))
    phong = Phong(screen, light_source, observer, 0.5, 0, 1, 300, 0.8, 1)
    rotation.append((sphere, phong, "Min Spec Max Diff"))

    selected = len(rotation) - 1
    pg.display.set_caption(window_config.get_title() + f" | {rotation[selected][2]}")

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
                if event.key == pg.K_b:
                    selected = (selected + len(rotation) - 1) % len(rotation)
                    sphere, phong, title = rotation[selected]
                    pg.display.set_caption(window_config.get_title() + f" | {title}")
                if event.key == pg.K_n:
                    selected = (selected + 1) % len(rotation)
                    sphere, phong, title = rotation[selected]
                    pg.display.set_caption(window_config.get_title() + f" | {title}")


                if event.key == pg.K_o:
                    filename = f"screenshot_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.png"
                    pg.image.save(pg.display.get_surface(), filename)

                if event.key == pg.K_ESCAPE:
                    running = False


        pg.display.get_surface().fill((pg.Color("gray18")))

        phong.render_sphere(sphere)
        pg.draw.circle(screen, pg.Color("white"), light_source.get_position_2d(), 5)

        pg.display.flip()
        clock.tick(fps)

    pg.quit()


if __name__ == '__main__':
    main()
