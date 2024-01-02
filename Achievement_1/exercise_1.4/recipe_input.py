import pickle

# Function to take user recipe
def take_recipe():
  name = input("Enter the name of the recipe: ")
  cooking_time = int(input("Enter the cooking time (in minutes): "))
  ingredients = []

  # Prompt user for ingredients until they enter "done"
  while True:
    ingredient = input(
      "Enter an ingredient (or enter 'done' if you are finished): "
    )
    if ingredient == "done":
      break
    else:
      ingredients.append(ingredient)

  # Create a recipe dictionary with name, coking time, and ingredients
  recipe = {"name": name, "cooking_time": cooking_time, "ingredients": ingredients}
  # Calculate the recipe difficulty
  difficulty = calc_difficulty(recipe)
  # Add the difficulty to the recipe dictionary
  recipe["difficulty"] = difficulty
  return recipe   

# Function to calculate recipe difficulty based on cooking time and ingredient count
def calc_difficulty(recipe):
  if recipe["cooking_time"] < 10 and len(recipe["ingredients"]) < 4:
    difficulty = "Easy"
  elif recipe["cooking_time"] < 10 and len(recipe["ingredients"]) >= 4:
    difficulty = "Medium"
  elif recipe["cooking_time"] >= 10 and len(recipe["ingredients"]) < 4:
    difficulty = "Intermediate"
  else:
    difficulty = "Hard"
  return difficulty

# Main code
filename = input("Enter the filename where you've stored your recipes: ")
try:
  with open(filename, "rb") as file:
    data = pickle.load(file)
    print("Recipe loaded successfully!")
# If the file doesn't exist, print a message and create a new dictionary
except FileNotFoundError:
  print("File doesn't exist -creating new file.")
  data = {"recipes_list": [], "all_ingredients": []}
# If there is an unexpected error, print a message and create a new dictionary
except:
  print("An unexpected error occurred.")
  data = {"recipes_list": [], "all_ingredients": []}
else:
  file.close()
# If the file exists, extract the recipes_list and all_ingredients from the dictionary
finally:
  recipes_list = data["recipes_list"]
  all_ingredients = data["all_ingredients"]

# Get the number of recipes to add from the user
n= int(input("How many recipes would you like to add? "))

# Take recipes and append to the recipes_list
for i in range(n):
  recipe = take_recipe()

  # Update all_ingredients with new ingredients
  for ingredient in recipe["ingredients"]:
    if ingredient not in all_ingredients:
      all_ingredients.append(ingredient)

  # Add recipe to recipes_list
  recipes_list.append(recipe)

# Save the recipes_list and all_ingredients to a dictionary
data = {"recipes_list": recipes_list, "all_ingredients": all_ingredients}

# Save the dictionary to a user-specified file
filename = input("Enter the filename where you'd like to store your recipes: ")
with open(filename, "wb") as file:
  pickle.dump(data, file)
  print("Recipes saved successfully!")
  file.close()