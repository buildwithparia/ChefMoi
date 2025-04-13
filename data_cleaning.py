# Lets start another girly project
# As we deal with real-world data, we need to customize it so it'll be easier to handle data 
# and of course I'll make the dataset more ✨me✨

import pandas as pd
from ast import literal_eval

df = pd.read_csv("RAW_recipes.csv")

# before starting this python file I make some changes manually like deleting the columns I don't need or add my own column
# but of course we can do it here!

# one of the most important columns is "nutritions" because i want to filter recipes base on it
# and the value of this column is string so I need to convert it to list

df["nutrition"] = df["nutrition"].apply(literal_eval)

#now we need to extract the nutrions because we want to apply filtering on these new columns
df["calories"] = df["nutrition"].apply(lambda x: x[0])
df["fat"] = df["nutrition"].apply(lambda x: x[1])
df["sugar"] = df["nutrition"].apply(lambda x: x[2])
df["sodium"] = df["nutrition"].apply(lambda x: x[3])
df["protein"] = df["nutrition"].apply(lambda x: x[4])
df["sat_fat"] = df["nutrition"].apply(lambda x: x[5])
df["carbs"] = df["nutrition"].apply(lambda x: x[6])

# some little filtering...💅🏻 This will give us a sweet healthy set
filtered_df = df[
    (df["minutes"] <= 60) &                # quick to make (I'm not lazy)
    (df["calories"] < 500) &              # glow-up friendly🧚🏻
    (df["protein"] > 10) &                # high protein💪🏻
    (df["sugar"] < 20)                    # low sugar (skin needs to skining👱🏻‍♀️)
]

# then randomly pick 180 recipes
selected_recipes = filtered_df.sample(n=180, random_state=42).copy()

# it's time to export final file
selected_recipes.to_csv("paria_recipes.csv", index=False)

# now we’ve got a ✨clean, filtered, girly, ready-to-code✨ dataset!
# it was just first step...keep going girl
# TODO1: I'll add my own recipes later!
# TODO2: paria_tags column is still empty but I'll fill it!
