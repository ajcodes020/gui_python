from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]
    
    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_body(position)
    
    def add_body(self, position):
        snake = Turtle(shape="square")
        snake.color("white")
        snake.penup()
        snake.goto(position)
        self.snake_body.append(snake)
    
    def extend(self):
        self.add_body(self.snake_body[-1].position())

    def move(self):
        for snake_num in range(len(self.snake_body) - 1, 0, -1):
            x = self.snake_body[snake_num - 1].xcor()
            y = self.snake_body[snake_num - 1].ycor()
            self.snake_body[snake_num].goto(x, y)
        self.head.forward(MOVE_DISTANCE)
    
    def reset_position(self):
        for snake_part in self.snake_body:
            snake_part.goto(320, 320)
        self.snake_body.clear()
        self.create_snake()
        self.head = self.snake_body[0]
    
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
