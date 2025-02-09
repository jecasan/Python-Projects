from turtle import Screen, Turtle
import pandas

screen = Screen()
turtle = Turtle()
writer = Turtle()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
writer.penup()
writer.hideturtle()
ALIGNMENT = "center"
FONT = ("Courier", 12, "normal")


""" 
Get coordinates on map
def get_mouse_click_coor(x, y):
    print(x,y)
    
screen.onscreenclick(get_mouse_click_coor)
""" 
data = pandas.read_csv("50_states.csv")

states_list = data.state.tolist()
guessed_state = []

while len(guessed_state) != 50:
    answer_state = screen.textinput(title = f"{len(guessed_state)}/50 States Correct", 
                                    prompt = "What's another state's name?").title()
    if answer_state == "Exit":
        not_guessed = []
        for state in states_list:
            if state not in guessed_state:
                not_guessed.append(state)
        states_to_learn = pandas.DataFrame(not_guessed)
        states_to_learn.to_csv("states_to_learn.csv")
        break
    if answer_state in states_list and answer_state not in guessed_state:
        get_state = data[data.state == answer_state]
        writer.goto(int(get_state.x), int(get_state.y))
        writer.write(answer_state, align = ALIGNMENT, font = FONT)
        guessed_state.append(answer_state)
            
        
    




