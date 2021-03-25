from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.core.window import Window

import random
import math

class Point:
    def __init__(self, value=None, x=None, y=None):
        self.x = random.randint(0, 3) if x == None else x
        self.y = random.randint(0, 3) if y == None else y
        self.value = random.randint(1, 2) * 2 if value == None else value
        self.combined = False
        self.destruct = False
    
    def __str__(self):
        return f'({self.x}, {self.y}) {self.value}'

class Game(App):
    def init(self, **kwargs):
        super().init(**kwargs)
    
    def build(self):
        self.title = "2048"
        self.root = Builder.load_file('2048.kv')
        Window.size = (600, 700)

        self.game_over = False
        self.points = []
        self.create_random_point()
        self.create_random_point()
        self.draw()

        return self.root
    
    def draw(self):
        self.root.ids.row_0.clear_widgets()
        self.root.ids.row_1.clear_widgets()
        self.root.ids.row_2.clear_widgets()
        self.root.ids.row_3.clear_widgets()
        board = {}
        for point in self.points:
            point.combined = False
            pos = point.y * 4 + point.x
            board[pos] = point.value
        board_keys = sorted(board)
        for i in range(16):
            label = Button(text=str(board[i]) if i in board_keys else '')
            color = math.log(board[i], 2)/11 if i in board_keys else 0
            label.background_color = (min(color, 1), min(color/2, 1), min(color/2, 1), 1)
            if i < 4:
                self.root.ids.row_0.add_widget(label)
            elif i < 8:
                self.root.ids.row_1.add_widget(label)
            elif i < 12:
                self.root.ids.row_2.add_widget(label)
            else:
                self.root.ids.row_3.add_widget(label)
    
    def move(self, direction, test=False):
        points = self.points
        valid_move = True
        movement = False
        if direction == 'up' or (direction == 'key' and self.root.ids.text.text[-1:].lower() == 'w'):
            points = sorted(self.points, key=self.sort_for_up)
            for point in points:
                blocked = False
                while blocked == False:
                    if point.y - 1 >= 0:
                        for obstacle in points:
                            if point.y - 1 == obstacle.y and point.x == obstacle.x:
                                if obstacle.value == point.value and obstacle.combined == False:
                                    point.value = point.value * 2
                                    obstacle.value = obstacle.value * 2
                                    obstacle.destruct = True
                                    point.y = point.y - 1
                                    point.combined = True
                                    obstacle.combined = True
                                    movement = True
                                blocked = True
                        if blocked == False:
                            point.y = point.y - 1
                            movement = True
                    else:
                        blocked = True
        elif direction == 'down' or (direction == 'key' and self.root.ids.text.text[-1:].lower() == 's'):
            points = sorted(self.points, key=self.sort_for_down)
            for point in points:
                blocked = False
                while blocked == False:
                    if point.y + 1 <= 3:
                        for obstacle in points:
                            if point.y + 1 == obstacle.y and point.x == obstacle.x:
                                if obstacle.value == point.value and obstacle.combined == False:
                                    point.value = point.value * 2
                                    obstacle.value = obstacle.value * 2
                                    obstacle.destruct = True
                                    point.y = point.y + 1
                                    point.combined = True
                                    obstacle.combined = True
                                    movement = True
                                blocked = True
                        if blocked == False:
                            point.y = point.y + 1
                            movement = True
                    else:
                        blocked = True
        elif direction == 'left' or (direction == 'key' and self.root.ids.text.text[-1:].lower() == 'a'):
            points = sorted(self.points, key=self.sort_for_left)
            for point in points:
                blocked = False
                while blocked == False:
                    if point.x - 1 >= 0:
                        for obstacle in points:
                            if point.x - 1 == obstacle.x and point.y == obstacle.y:
                                if obstacle.value == point.value and obstacle.combined == False:
                                    point.value = point.value * 2
                                    obstacle.value = obstacle.value * 2
                                    obstacle.destruct = True
                                    point.x = point.x - 1
                                    point.combined = True
                                    obstacle.combined = True
                                    movement = True
                                blocked = True
                        if blocked == False:
                            point.x = point.x - 1
                            movement = True
                    else:
                        blocked = True
        elif direction == 'right' or (direction == 'key' and self.root.ids.text.text[-1:].lower() == 'd'):
            points = sorted(self.points, key=self.sort_for_right)
            for point in points:
                blocked = False
                while blocked == False:
                    if point.x + 1 <= 3:
                        for obstacle in points:
                            if point.x + 1 == obstacle.x and point.y == obstacle.y:
                                if obstacle.value == point.value and obstacle.combined == False:
                                    point.value = point.value * 2
                                    obstacle.value = obstacle.value * 2
                                    obstacle.destruct = True
                                    point.x = point.x + 1
                                    point.combined = True
                                    obstacle.combined = True
                                    movement = True
                                blocked = True
                        if blocked == False:
                            point.x = point.x + 1
                            movement = True
                    else:
                        blocked = True
        else:
            valid_move = False
        existing_points = []
        for point in points:
            if point.destruct == False:
                existing_points.append(point)
        if valid_move and movement and test == False:
            self.points = existing_points
            self.create_random_point()
            self.draw()
        if test:
            if movement:
                return True
            else:
                return False
        if self.game_over:
            self.root.ids.text.text = 'Game Over'
    
    def sort_for_up(self, point):
        return int(point.y)
    
    def sort_for_down(self, point):
        return -int(point.y)
    
    def sort_for_left(self, point):
        return int(point.x)
    
    def sort_for_right(self, point):
        return -int(point.x)
    
    def sort_by_x(self, tuple):
        return int(tuple[0])

    def sort_by_y(self, tuple):
        return int(tuple[1])
    
    def create_random_point(self):
        if len(self.points) < 16:
            free = False
            while free == False:
                x = random.randint(0, 3)
                y = random.randint(0, 3)
                free = True
                for point in self.points:
                    if point.x == x and point.y == y:
                        free = False
            self.points.append(Point(None, x, y))
        if len(self.points) == 16:
            up = self.move('up', True)
            down = self.move('down', True)
            left = self.move('left', True)
            right = self.move('right', True)
            if up == False and down == False and left == False and right == False:
                self.game_over = True

if __name__ == '__main__':
    Game().run()