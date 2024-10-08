from pico2d import *
import random


# Game object class here
class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(400, 30)

    pass


class Boy:
    def __init__(self):
        self.x, self.y = random.randint(0, 200), 90
        self.frame = random.randint(0, 7)
        self.image = load_image('run_animation.png')

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += 5

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)


class Ball:
    def __init__(self):
        self.x, self.y = random.randint(0, 700), 599
        self.speed = random.randint(5, 10)
        self.size = random.randint(0, 1)
        self.image1 = load_image('ball21x21.png')
        self.image2 = load_image('ball41x41.png')

    def update(self):
        if (self.y > 70):
            self.y -= self.speed
        else:
            self.y = 70

    def draw(self):
        if (self.size == 0):
            self.image1.draw(self.x, self.y)
        else:
            self.image2.draw(self.x, self.y)

    pass


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


def update_world():
    for o in world:
        o.update()

    pass


def render_world():
    clear_canvas()
    for o in world:
        o.draw()

    update_canvas()
    pass


def reset_world():
    global running
    global grass
    global team
    global world
    global balls

    running = True
    world = []
    grass = Grass()
    world.append(grass)
    team = [Boy() for i in range(11)]
    world += team
    balls = [Ball() for i in range(21)]
    world += balls


open_canvas()

# initialization code
reset_world()

# game main loop code
while running:
    handle_events()
    update_world()
    render_world()
    delay(0.05)
# finalization code

close_canvas()
