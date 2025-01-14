from turtle import Turtle, Screen
import turtle
import pandas
from map_generator import MapGenerator

screen = turtle.Screen()
screen.title('Españita\'s game')
image = 'espagne23.gif'
screen.addshape(image)
turtle.shape(image)
# painting_turtle = Turtle()
# # FROM MAP TO CSV
# spanish_map = MapGenerator()
#
# turtle.onscreenclick(spanish_map.save_click_into_coordinates)
# turtle.mainloop()
#
# spanish_map.save_provinces_into_dictionary('codprov.csv')
# spanish_map.generate_final_csv('spanish')
# #
data = pandas.read_csv('spanish_prov.csv')
all_provinces = data.provinces.to_list()
game_is_on = True
i = 0

while game_is_on:
    if i == 51:
        game_is_on = False
    else:
        answer = screen.textinput(title="Guess the province", prompt="What's another province's name?").title()

        if answer in all_provinces:
            t = Turtle()
            t.pu()
            t.ht()
            provinces_row = data[data.provinces == answer]
            t.goto(provinces_row.xcor.item(), provinces_row.ycor.item())
            t.write(provinces_row.provinces.item(), align="center", font=("Arial", 8, "normal"))
            i += 1

turtle.mainloop()
