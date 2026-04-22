from typing import Self
from pymunk import *;
from pygame import Color;
from math import pi;

SCALING_FACTOR = 1.22
"""Hệ số tăng kích thước trái cây"""

class Fruit:
    """
    Class trái cây của trò chơi.
    
    Attributes:
        type (int): Loại trái cây từ 0 -> 10.
        body (Body): Quản lí cơ thể vật lí của trái cây.
        shape (Shape): Quản lí hình dạng của trái cây.
    """
    
    def __init__(self, type: int):
        if not 0 <= type <= 10:
            raise ValueError(f"Invalid type: {type}");
      
        radius = 15 * pow(SCALING_FACTOR, type)
        mass = pi * radius * radius;
        moment = moment_for_circle(mass, 0, radius);

        self.body = Body(mass, moment);
        self.shape = Circle(self.body, radius);
        self.shape.friction = 0.7;
        self.shape.color = Color('red');

    def add_fruit(self, space: Space, position: tuple[int, int]):
        """
        Thêm một đối tượng trái cây vào không gian chơi.
        
        Args:
            space: Không gian để thêm trái cây.
            position: Vị trí sinh sinh ra trái cây.
        """
        
        self.body.position = position;
        space.add(self.body, self.shape);