# This is part of day 25 but unrelated to the main project for the day
# Goal is to take NYC Central Park squirrel data and use Pandas to count total of each type of squirrel
# Data Source: https://data.cityofnewyork.us/Environment/2018-Central-Park-Squirrel-Census-Squirrel-Data/vfnx-vebw

import pandas as pd

FILENAME = "2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv"
OUTPUT_FILENAME = "squirrel_counts.csv"

squirrel_df = pd.read_csv(FILENAME)
squirrel_type_counts = squirrel_df["Primary Fur Color"].value_counts()
squirrel_type_counts.to_csv(OUTPUT_FILENAME)
print(squirrel_type_counts)
