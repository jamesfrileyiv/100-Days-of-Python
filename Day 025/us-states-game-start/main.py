import turtle
from turtle import Screen
from turtle import Turtle
import pandas as pd
from statewriter import StateWriter
import pprint

MAP_IMAGE = "blank_states_img.gif"
STATE_DATA = "50_states.csv"
SCREEN_TITLE = "50 States Game"
INPUT_PROMPT = "Guess a state name"
INPUT_PROMPT_TITLE = "Guess a state"
MAX_WRONG_ANSWERS = 10

pp = pprint.PrettyPrinter(indent=4)

def main():
    df = pd.read_csv(STATE_DATA)
    previous_answers = {}
    screen = screen_setup()
    turtle.shape(MAP_IMAGE)
    state_writer = StateWriter()
    wrong_answer_count = 0
    game_is_on = True
    while game_is_on:
        # Get user input
        user_input = screen.textinput(title=INPUT_PROMPT_TITLE, prompt=INPUT_PROMPT)

        # check if user input is already used
        if user_input not in previous_answers:
            # add user input to previous answers
            previous_answers[user_input] = 0
            # check if a valid state
            if user_input in df["state"]:
                # if a valid state, then print name on map
                index = df.index(df["state"] == user_input)
                row = df.loc(index)
                print(row)
                state_writer.write_state(row[0], row[1], row[2])
            else:
                wrong_answer_count += 1
                if wrong_answer_count == MAX_WRONG_ANSWERS:
                    game_is_on = False
        else:
            previous_answers[user_input] += 1
        pp.pprint(previous_answers)



        #
        # game_is_on = game_turn(screen, df)
    screen.mainloop()


# def game_turn(screen: turtle.Screen, df: pd.DataFrame):
#     game_is_on = False
#     user_input = screen.textinput(title=INPUT_PROMPT_TITLE, prompt=INPUT_PROMPT)
#     if user_input in df.states:
#
#     return game_is_on


def screen_setup():
    screen = Screen()
    screen.title(SCREEN_TITLE)
    screen.addshape(MAP_IMAGE)
    return screen


if __name__ == "__main__":
    main()
