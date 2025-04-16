# 🧁 ChefMoi  
*A mood-based AI recipe recommender built for glow-ups, gym days, and your feminine vibe.* 🍓

---

## 👩🏻‍🍳 Project Overview

Built for those who want their food to align with their feminine goals, **ChefMoi** delivers smart suggestions based on glow-up vibes, comfort cravings, and even supports you on those tough PMS days.

Instead of focusing only on calories or macros, ChefMoi recommends meals based on real-life feelings — like a “lazy girl dinner” or “cramp relief comfort food.”

It’s my attempt at combining AI, lifestyle, and a little bit of ✨Paria sparkle✨ into something helpful, personal, and heartfelt.

---

## ❔ What’s in the Project

🧼 `data_cleaning.py` → Custom data cleaning pipeline to filter & format messy raw recipe data  
🍰 `recipe_recommender.py` → AI-powered recipe recommendations based on ingredients + mood using content-based filtering  
🍽️ `paria_recipes.csv` → 180+ real recipes with hand-curated `paria_tag` lifestyle labels (like glow_up, cramp_relief, lazy_girl_dinner)  
📸 `images/` → 20+ aesthetic food visuals ready for future UI integration or mockups  
🎨 `assets/` → Designed interface preview

---

## 📊 Dataset Details

The dataset used in this project was sourced from [Food.com Recipes and Interactions](https://www.kaggle.com/datasets/shuyangli94/food-com-recipes-and-user-interactions).  
Originally, it contained over 230,000 raw recipes with unstructured data such as ingredients, nutrition values as stringified lists, and inconsistent formatting.

🥞 To make the dataset more useful for AI-based recommendations, I:
- Filtered it down to ~180 recipes
- Cleaned the nutrition values and converted them from strings to usable lists
- Removed unnecessary columns (like contributor IDs, etc.)
- Combined key columns (`ingredients` + `paria_tag`) into a single text field for modeling

🥡 I also manually added a new column called `paria_tag`, which assigns a mood-based lifestyle label to each recipe.  
Tags include categories like:
- `gut_healing`  
- `pilates_glow`  
- `lazy_girl_dinner`  
- `glow_up`  
- `post_leg_day`  
- `comfort_cute`  
- `cramp_relief`  
- `snack_attack`  

These tags were hand-curated based on the vibe, ingredients, and overall nutritional mood of each recipe — and became the foundation of ChefMoi’s vibe-matching AI engine.

---

## 🤖 How It Works

ChefMoi uses a **content-based recommendation system** powered by scikit-learn.  
The goal is to find recipes that are similar in both ingredients and mood — so I combined two key columns: `ingredients` and `paria_tag`.

These were merged into a new column called `combined_columns`, which looks something like:
> `"chicken, spinach, garlic, olive oil glow_up lazy_girl_dinner"`

This "vibe string" was then transformed into a numerical matrix using **TF-IDF Vectorization**, which helps the model understand which words are unique or important to each recipe.  
Then, I calculated the **cosine similarity** between recipes — meaning, the model compares how similar the vibe vectors are in direction (not just content).

ChefMoi then:
- Finds the top 5 most similar recipes to the one you input
- Prints the name + a cute match percentage 🎂

---

🛒 **Example usage:**

```python
get_similar_recipe("Grilled Pizza Crust")
```

**Returns:**
```text
- Garlic Chicken Spaghetti (83.5% match)
- BLT Pizza (78.4% match)
- Cramp-Relief Nachos (75.9% match)
- Easy Chickpea Bowl (74.0% match)
- Spinach Cream Pasta (71.8% match)
```

---

## 🎨 UI & Images

ChefMoi was designed to feel visual, soft, and personalized — not just technical.

To prepare for future UI integration, I created 20+ custom recipe visuals using free AI-powered image tools (like Bing Image Creator).  
Each image matches a real recipe from the dataset and is stored in the `/images/` folder.

I also designed a mobile-friendly UI mockup in Figma to reflect the vibe of the project: pastel, feminine, and easy to use.

---

### 📱 Figma Preview

Here’s a sneak peek of what ChefMoi could look like as a full mobile app:

![ChefMoi UI Mockup](assets/figma_mockup.png)

---

---

## 💖 Why I Made This

I wanted to build something that reflects who I am — not just as a student, but as a woman, a creator, and a tech learner.

ChefMoi was a way to explore my love for food, moods, aesthetics, and human-centered AI.  
It taught me how to go beyond tutorials and create something that actually feels *real*, warm, and useful.

---

## 🌱 Real-World Impact & Future Plans

ChefMoi has the potential to evolve into a real mobile or web app that helps people — especially women — find meals that match how they *feel*, not just what they have in the fridge.

This project could be expanded into:
- Personalized wellness tools  
- Cycle-aware nutrition systems  
- Gym recovery meal planners  
- Mood-boosting food apps  

In the future, I’d love to:
- Add more recipes and deeper tag logic  
- Include user preference history  
- Integrate nutrition APIs  
- Build a full UI with search, filters, and vibe-based recommendations

---

## 🚧 Challenges I Faced

ChefMoi may look soft and simple on the outside, but building it came with real challenges behind the scenes:

- 🧼 **Messy raw data:** The original dataset included over 230,000 recipes, many with missing values, inconsistent formats, and stringified lists. Cleaning and preparing a usable subset took a lot of effort and experimentation.
- 📝 **Missing portion sizes:** The dataset didn’t include ingredient quantities, which limited the accuracy of any nutrition-based filtering or deeper analysis.
- 🩸 **Tagging with care:** Creating the `paria_tag` system was deeply creative but also time-consuming. I had to manually review and categorize recipes in a way that reflected real moods and use cases, like “cramp relief” or “post-leg day.”
- 📸 **Image generation limits:** To bring the project’s aesthetic to life, I generated custom food visuals using free AI tools. Managing tool limitations and matching visuals to real recipes took several iterations.


Despite the challenges, this became one of my favorite projects. It let me explore not just machine learning, but also creative thinking, emotional design, and the importance of building tools that feel like they understand you.

---

## ✨ Built by 

[@buildwithparia](https://github.com/buildwithparia) 
🍝 Cooked up with Python, pandas, and scikit-learn — seasoned with snacks, playlists, and a sprinkle of mood.

