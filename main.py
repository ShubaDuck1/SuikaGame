from pygame import *;
from pymunk import *;
from pymunk.pygame_util import *;
from math import *;

init();
WIDTH, HEIGHT = 1080, 720; # Độ lớn màn hình
SPAWN = (WIDTH / 2, 100);

screen = display.set_mode((WIDTH, HEIGHT));


def add_box(space):
    W_LENGTH = 500; # Độ dài tường
    F_LENGTH = 400; # Độ dài sàn
    W_WIDTH = 30; # Độ dày tường và sàn
    
    rect = [
        [(WIDTH / 2, HEIGHT - W_WIDTH / 2), (F_LENGTH, W_WIDTH)],
        [(WIDTH / 2 - F_LENGTH / 2 + W_WIDTH / 2, HEIGHT - W_LENGTH / 2), (W_WIDTH, W_LENGTH)],
        [(WIDTH / 2 + F_LENGTH / 2 + W_WIDTH / 2, HEIGHT - W_LENGTH / 2), (W_WIDTH, W_LENGTH)]
    ]
    
    for pos, size in rect:
        body = Body(body_type=Body.STATIC);
        body.position = pos;
        
        shape = Poly.create_box(body, size);
        shape.friction = 0.7;
        shape.color = Color('white');
        space.add(body, shape);

def add_circle(space, position, radius, mass):
    body = Body(mass, 1);
    body.mass = mass;
    body.moment = moment_for_circle(mass, 0, radius);
    body.position = position;
    
    shape = Circle(body, radius);   
    shape.friction = 0.5;
    shape.color = Color('red');
    space.add(body, shape);
    return shape;    

def draw_screen(screen, space, draw_options):
    screen.fill("black");
    space.debug_draw(draw_options);
    draw.circle(screen, Color('pink'), (mouse.get_pos()[0], 100), 30);
    
    display.flip();

# game loop
def run(screen):
    isRunning = True;
    clock = time.Clock();
    fps = 60;
    delta_time = 1 / fps;
    
    space = Space();
    space.gravity = (0, 981);
    space.damping = 0.7;
    draw_options = DrawOptions(screen);
    
    add_box(space);
    
    while isRunning:
        for ev in event.get():
            if(ev.type == QUIT):
                isRunning = False;
        
        spawn_pos = (mouse.get_pos()[0], 100);
        if(mouse.get_just_pressed()[0]):
            add_circle(space, spawn_pos, 30, 30);
        
        draw_screen(screen, space, draw_options);
        space.step(delta_time);
        clock.tick(fps);
        
    quit();

if __name__ == "__main__":
    run(screen);