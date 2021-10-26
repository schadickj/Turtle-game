from turtle import Turtle
from turtle import Screen
from keyboardturtle import KeyboardTurtle
from randomove import goto_random
from walls import Wall

#screen
window = Screen()
screen_width = 770
screen_height = 400 
window.setup(screen_width, screen_height)

collision_list = []
print("You are a green turtle. Catch the 5 other turtles around the screen. You can only catch them by running into them from the front or behind. What are you waiting for go, go, go!")

wall_list = []

player_6 = KeyboardTurtle(window,other_player = collision_list)
player_5 = KeyboardTurtle(window,other_player = collision_list)
player_4 = KeyboardTurtle(window,other_player = collision_list)
player_3 = KeyboardTurtle(window,other_player = collision_list)
player_2 = KeyboardTurtle(window,other_player = collision_list)
player_1 = KeyboardTurtle(window,other_player = collision_list, walls = wall_list)
player_2.color("red")
player_3.color("white")
player_4.color("blue")
player_5.color("yellow")
player_6.color("purple")
player_3.goto(x=100, y=100)
player_4.goto(x=-900, y=-500)
player_6.goto(x=333, y=20)


collision_list.append(player_1)
collision_list.append(player_2)
collision_list.append(player_3)
collision_list.append(player_4)
collision_list.append(player_5)
collision_list.append(player_6)



w1 = Wall(370,0, 2, 5)
wall_list.append(w1)
wall_list.append(Wall(330, 50, 5, 2))
wall_list.append(Wall(330, -50, 5, 2))
wall_list.append(Wall(300, 0, 2, 5))

riddle = input("What has 13 hearts, but no other organs? ")
if (riddle == "a deck of cards"):
  print ("yes")
  player_4.goto(x=-100,y=-100)
else:
  print ("You must answer collect to get the turtle. Try Again")


player_2.goto_random()
player_3.hide_me()
player_5.make_x()

window.listen()
window.mainloop()