from turtle import Turtle, Screen
import pandas

screen = Screen()
screen.setup(width= 800, height=500)
screen.addshape('blank_states_img.gif')
screen.title("Guess The State")
turtle = Turtle()
turtle.shape("blank_states_img.gif")

states_data = pandas.read_csv("50_states.csv")
state_name_list = states_data['state'].to_list()
print(state_name_list)
# answer_state = screen.textinput("Guess a state name?", "Enter here")
guessed_states = []
game_is_on = True
current_score = 0
total_score = 50
all_states = states_data.state.to_list()

def write_state_name_on_map(name,x,y):
    t = Turtle()
    t.penup()
    t.hideturtle()
    t.goto(x,y)
    t.write(name, "center")

print(state_name_list)
while len(guessed_states)<50:
    answer_state = screen.textinput(f"{current_score}/{total_score} states guessed", "Enter a state name here")
    answer_state = answer_state.title()
    if answer_state=="Exit":
        missed_states = [state for state in all_states if state not in guessed_states]
        missed_states_df = pandas.DataFrame(missed_states)
        missed_states_df.to_csv("missed_states.csv")
        break
    if answer_state.strip() in state_name_list:
        if answer_state.strip() not in guessed_states:
            guessed_states.append(answer_state)
            x_cor = int(states_data[states_data.state == answer_state]['x'])
            y_cor = int(states_data[states_data.state == answer_state]['y'])
            # write_state = Turtle()
            write_state_name_on_map(answer_state,x_cor,y_cor)
            current_score += 1

# print(states_data[~states_data.state.isin(guessed_states)])
# states_missed = states_data[~states_data.state.isin(guessed_states)]
# print(states_missed)

# states_missed.to_excel("states_missed.xlsx")
screen.exitonclick()