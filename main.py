from pygame import *;
from pymunk import *;
from pymunk.pygame_util import *;
from fruits import *;
from gamebox import Game_Box;
import random;

init();
SPW_CD = 0.75; 
"""Thời gian hồi mặc định để tiếp tục thả trái cây."""

WIDTH, HEIGHT = 1080, 720; 
"""Kích thước màn hình"""

FPS = 60; 
"""Lượng khung hình trên giây"""

screen = display.set_mode((WIDTH, HEIGHT));
spawn_cooldown = 0;
current_fruit = None;
spawn_position = None;
fruit_queue = [];

def draw_screen(screen, space, draw_options):
    """
    Xử lí vẽ các đối tượng lên cửa sổ game.
    """
    
    global spawn_cooldown;
    global current_fruit_type;
    global spawn_position;
    global current_fruit
    
    screen.fill("black");
    space.debug_draw(draw_options);
    if spawn_cooldown <= 0:
        draw.circle(screen, Color('pink'), spawn_position, current_fruit.shape.radius);
    
    display.flip();

def run(screen):
    """
    Chạy game.
    """
    
    global spawn_cooldown;
    global current_fruit;
    global spawn_position;
    global fruit_queue;
    
    isRunning = True;
    clock = time.Clock();
    delta_time = 1 / FPS;
    
    space = Space();
    space.gravity = (0, 800);
    space.damping = 0.7;
    draw_options = DrawOptions(screen);
    
    Game_Box(space, WIDTH, HEIGHT);
    
    current_fruit = Fruit(0);
    for i in range(7):
        type = random.randint(0, 4);
        fruit_queue.append(Fruit(type));
    
    while isRunning:
        for ev in event.get():
            if(ev.type == QUIT):
                isRunning = False;
        
        spawn_position = (mouse.get_pos()[0], 150);
        if(mouse.get_just_pressed()[0] and spawn_cooldown <= 0):
            current_fruit.add_fruit(space, spawn_position);
            spawn_cooldown = SPW_CD;
            
            current_fruit = fruit_queue[0];
            fruit_queue.pop(0);
            type = random.randint(0, 4);
            fruit_queue.append(Fruit(type));
        
        spawn_cooldown -= delta_time;
        draw_screen(screen, space, draw_options);
        space.step(delta_time);
        clock.tick(FPS);
        
    quit();

if __name__ == "__main__":
    run(screen);