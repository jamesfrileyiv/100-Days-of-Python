import turtle
from turtle import Screen
import pandas as pd
from statewriter import StateWriter
from scoreboard import Scoreboard

MAP_IMAGE = "blank_states_img.gif"
STATE_DATA = "50_states.csv"
SCREEN_TITLE = "50 States Game"
INPUT_PROMPT = "Guess a state name"
INPUT_PROMPT_TITLE = "Guess a state"
MAX_WRONG_ANSWERS = 10


def main():
    df = pd.read_csv(STATE_DATA)
    previous_answers = {}
    screen = screen_setup()
    turtle.shape(MAP_IMAGE)
    state_writer = StateWriter()
    sb = Scoreboard()
    while not sb.confirm_game_over():
        game_turn(screen=screen,previous_answers=previous_answers, df=df, state_writer=state_writer, score_board=sb)
    screen.mainloop()


def game_turn(
        screen: Screen, previous_answers: dict, df: pd.DataFrame, state_writer: StateWriter, score_board: Scoreboard):
    user_input = screen.textinput(title=INPUT_PROMPT_TITLE, prompt=INPUT_PROMPT)
    if user_input != "" and user_input is not None:
        if user_input not in previous_answers:
            previous_answers[user_input] = 0
            if user_input in df["state"].values:
                row = df.iloc[df.index[df["state"] == user_input]]
                state_writer.write_state(row.iloc[0].iloc[0], row.iloc[0].iloc[1], row.iloc[0].iloc[2])
                score_board.increment_score()
            else:
                score_board.increment_wrong()
            score_board.refresh()
    if score_board.confirm_game_over():
        score_board.game_over()


def screen_setup():
    screen = Screen()
    screen.title(SCREEN_TITLE)
    screen.addshape(MAP_IMAGE)
    return screen


if __name__ == "__main__":
    main()
