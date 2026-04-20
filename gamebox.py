from pymunk import *;
from pygame import Color;

class Game_Box:
    """
    Hộp chứa trái cây

    Mình có thể thay đổi các giá trị của hộp tại đây

    Attributes:
        W_LENGTH (int): Độ dài tường ở 2 bên
        F_LENGTH (int): Độ dài tường ở trên, dưới
        W_WIDTH (int): Độ dày của tường
        lid (Lid): Nấp hộp
    """
    
    W_LENGTH = 500;
    F_LENGTH = 450;
    W_WIDTH = 10;
    
    def __init__(self, space: Space, width:int = 1080, height: int = 720):
        """
        Khi khởi tạo sẽ thêm các tường vào không gian trò chơi
        """
        
        rect = [
            [(width / 2, height - self.W_WIDTH / 2), (self.F_LENGTH, self.W_WIDTH)],
            [(width / 2 - self.F_LENGTH / 2 + self.W_WIDTH / 2, height - self.W_LENGTH / 2), (self.W_WIDTH, self.W_LENGTH)],
            [(width / 2 + self.F_LENGTH / 2 - self.W_WIDTH / 2, height - self.W_LENGTH / 2), (self.W_WIDTH, self.W_LENGTH)]
        ]
        
        for pos, size in rect:
            body = Body(body_type=Body.STATIC);
            body.position = pos;
            
            shape = Poly.create_box(body, size);
            shape.friction = 0.7;
            shape.color = Color('white');
            space.add(body, shape);
 
        pos, size = (width / 2, height - self.W_WIDTH / 2 - self.W_LENGTH), (self.F_LENGTH, self.W_WIDTH);
        
        self.lid = self.Lid();
        self.lid.body = Body(body_type=Body.STATIC);
        self.lid.body.position = pos;
        
        self.lid.shape = Poly.create_box(self.lid.body, size);
        self.lid.shape.sensor = True;
        self.lid.shape.color = Color('yellow');
        space.add(self.lid.body, self.lid.shape);
    
    class Lid:
        """
        Nấp hộp
        
        Nếu trái cây chạm vào nấp hộp thì trò chơi sẽ kết thúc.
        """
        
        def __init__(self):
            return None;