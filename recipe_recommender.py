# hello again!
# after adding the precious "paria_tag" to our dataset, we're finally ready to build the heart of this whole project 💖
# yep, it's time for the content-based recommender engine 🍲✨

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# alright besties, we’ve got our secret ingredient: DATA 🌶️
df = pd.read_csv("paria_recipes.csv")

# okay listen carefully? this part is SUPER important 👀
# we’re gonna blend together the "ingredients" and "paria_tag" columns into one vibe smoothie 🧉 
# WHY? because:
# - using just ingredients is like telling someone there's chicken & butter, but not WHY you're eating it (comfort? cramps? glow-up?)
# - using just paria_tag makes everything sound the same ("cramp_relief" could mean 100 different dishes)
# so we need BOTH the *what* and the *why* for real vibes to come through, the AI need a big picture to actually understand💫

# blend..blend...👩🏻‍🍳
df["combined_columns"] = df["ingredients"].fillna("") + " " + df["paria_tag"].fillna("")
print("combined features created! 🌟")

# time to teach the AI how to read our food poetry 📖 and you now words can't help it so we need numbers
# TF-IDF will turn words into numbers that actually *mean* something:
# - it highlights what makes each recipe special (exotic, cozy, bold, etc.)
# - and tones down the noise (garlic is in everything, let’s be real girl)
vibe_reader = TfidfVectorizer(lowercase=True)


# transforming our big smoothie into a numerical matrix
recipe_vibe_matrix = vibe_reader.fit_transform(df["combined_columns"])

# just curious how many unique food words we ended up with... ( well it was 541! not bad!)
print("💫 recipe vibe matrix shape:", recipe_vibe_matrix.shape)
# (rows = recipes, columns = unique TF-IDF terms, aka our flavor-vibe dimensions)

# time to find some tasty recipes with similar vibe🍜✨
def get_similar_recipe(recipe_name, top_n=5):
    # sanity check – did we even get a real recipe?
    if recipe_name.lower() not in df['name'].str.lower().values:

        print("😭 Recipe not found. Double check the spelling, babe.")
        return
     # figure out where the recipe is in the dataframe
    recipe_index = df[df['name'] == recipe_name].index[0]  # using list instead of df logic, could be better tbh

     # it's time to compute the ~vibe distances~ using cosine sim
     # we need to calculate how much two dishesh have similarity and base on this number the model choose top similar recipes for user
    vibe_similarity_scores = cosine_similarity(
        recipe_vibe_matrix[recipe_idx], recipe_vibe_matrix
    ).flatten()

    # get indices of top similar recipes
    sorted_similar_idxs = vibe_similarity_scores.argsort()[::-1] 
    top_similar = sorted_similar_idxs[1:top_n + 1]  # skip the recipe itself of course!

    print(f"\n✨ Recipes similar to: {recipe_name} 💫\n")

     # show the vibes
     # lets find some recipes and similarity scores
    results = []
    for recipe_idx in top_similar:
        # rounding to 2 decimals just to keep it cute
        similarity_pct = round(vibe_similarity_scores[recipe_idx] * 100, 2)
        recipe_match = df.iloc[recipe_idx]['name']
        print(f"- {recipe_match} ({similarity_pct}% match)")
        results.append((recipe_match, similarity_pct))

    return results #for future app🍳

# test run 💅
get_similar_recipe("grilled pizza crust")

# TODO: making a web app with streamlit or even using html/css...i'll create the mockup on figma for you🍱
# TODO: I can add tag based filtering...
# NOTE: I find out something! The raw dataset that I use from kaggle dosen't have the portion of each ingredients!!!
# TODO: in the future i need to use external API like Spoonacular API to have quantities for each ingredient 
