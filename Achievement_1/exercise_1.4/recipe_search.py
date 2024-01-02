import pickle

def display_recipe(recipe):
  print("Recipe:", recipe["name"])
  print("Cooking time (min):", recipe["cooking_time"])
  print("Ingredients:")
  for ingredient in recipe["ingredients"]:
    print(ingredient)
  print("Difficulty:", recipe["difficulty"])
  print()  

# Function to search for recipes containing a particular ingredient
def search_ingredient(data):
  # Print the list of ingredients
  print("Available ingredients:")
  for index, ingredient in enumerate(data["all_ingredients"]):
    print(index, ingredient)
  print()
  # Ask user for the ingredient they want to search for
  try:
    ingredient_searched = data["all_ingredients"][
      int(input("Enter the number of the ingredient you want to search for: "))
    ]
  except:
    print("Incorrect input")
    return
  else:
    #search for recipes containing the ingredient
    recipes_found = []
    for recipe in data["recipes_list"]:
      if ingredient_searched in recipe["ingredients"]:
        recipes_found.append(recipe)
    # Display the recipes found
    for recipe in recipes_found:
      display_recipe(recipe)

# Ask user for the name of the file containing the recipes
filename = input("Enter the filename where you've stored your recipes: ")

try:
    file = open(filename, "rb")
    data = pickle.load(file)
except FileNotFoundError:
    print("File doesn't exist")
else:
    search_ingredient(data)
finally:
    print("Goodbye!")
    file.close() 