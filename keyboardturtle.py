from turtle import Turtle, ontimer
from random import randint


class KeyboardTurtle(Turtle):
    # our 'wrapper' class of the Turtle class
    def __init__(self,
                 window,
                 straight="Up",
                 turn_right="Right",
                 turn_left="Left",
                 down="Down",
                 other_player=None,
                 walls=None):
        # Runs Keyboard Turtle Constructor as well as the Turtle Constructor
        Turtle.__init__(self)

        # Sets up incoming variables
        self.window = window
        self.straight = straight
        self.turn_right = turn_right
        self.other_player = other_player
        self.turn_left = turn_left
        self.down = down
        self.walls = walls

        #set turtle starting states
        self.shape("turtle")
        self.color("green")
        self.penup()

        # Sets up keyboard command examples
        self.window.onkey(self.go_right, self.turn_right)
        self.window.onkey(self.go_forward, self.straight)
        self.window.onkey(self.go_left, self.turn_left)
        self.window.onkey(self.go_backward, self.down)

        #sets up controlling variables (y not implemented)
        self.movement_speed = 7
        self.turn_speed = 45
        self.collision_distance = 20

    # Movement Methods
    def go_forward(self):
        last_position = (250, 0)
        collided = False
        self.forward(self.movement_speed)
        if self.other_player != None:
            for player in self.other_player:
                if self.check_collision(player) and player != self:
                    print("You caught me!")
                    player.hideturtle()
                    self.other_player.remove(player)

        if self.walls != None:
            for wall in self.walls:
                if self.check_wall_collision(wall):
                    collided = True
                    break
            if collided:
                self.goto(last_position)

    def go_right(self):
        self.right(self.turn_speed)

    def go_left(self):
        self.left(self.turn_speed)

    def go_backward(self):
        self.back(self.movement_speed)
        for player in self.other_player:
            if self.check_collision(player) and player != self:
                print("You caught me!")
                player.hideturtle()
                self.other_player.remove(player)

    # Useful Methods

    # This checks if object collides with another object.
    # Right now it checks against the other player, but
    # it doesn't NEED to.  It can check against any
    # other turtle object

    def check_collision(self, obj_to_check):
        distance_x = obj_to_check.xcor() - self.xcor()
        distance_x = abs(distance_x)

        distance_y = obj_to_check.ycor() - self.ycor()
        distance_y = abs(distance_y)

        if distance_x < self.collision_distance and distance_y < self.collision_distance:
            return True
        else:
            return False

    def check_wall_collision(self, obj_to_check):
        turtle_rad = 10
        wall_rad = 10
        distance_x = obj_to_check.xcor() - self.xcor()
        distance_x = abs(distance_x)

        distance_y = obj_to_check.ycor() - self.ycor()
        distance_y = abs(distance_y)

        if distance_x < turtle_rad + (
                wall_rad * obj_to_check.x_size) and distance_y < turtle_rad + (
                    wall_rad * obj_to_check.y_size):
            return True
        else:
            return False

    def goto_random(self):
        self.speed(10)
        x_location = randint(-400, 400)
        y_location = randint(-200, 200)
        self.goto(x_location, y_location)
        ontimer(self.goto_random, 2500)

    def hide_me(self):
        self.color("black")
        self.color("white")
        ontimer(self.hide_me, 5000)

    def make_x(self):
        self.goto(x=300, y=300)
        self.goto(x=-300, y=300)
        self.goto(x=300, y=-300)
        self.goto(x=-300, y=-300)
        ontimer(self.make_x, 2500)
