class CookieRecipe:
    def __init__(self, filename):
        self.ingredients = list()  # Name, capacity, durability, flavor, texture, calories
        with open(filename, "r") as file:
            raw_ingredients = file.readlines()
        for raw_ingredient in raw_ingredients:
            ingredient_parts = raw_ingredient.strip("\n").split()
            self.ingredients.append((
                ingredient_parts[0].strip(":"),
                int(ingredient_parts[2].strip(",")),
                int(ingredient_parts[4].strip(",")),
                int(ingredient_parts[6].strip(",")),
                int(ingredient_parts[8].strip(",")),
                int(ingredient_parts[10])
            ))
        print(self.ingredients)

    def find_best_cookie(self, total_spoons):
        best_score = 0
        best_recipe = list()
        for no_1 in range(1, total_spoons + 1):
            for no_2 in range(1, total_spoons - no_1 + 1):
                for no_3 in range(1, total_spoons - no_1 - no_2 + 1):
                    no_4 = total_spoons - no_1 - no_2 - no_3
                    score = (
                        max(self.ingredients[0][1] * no_1 + self.ingredients[1][1] * no_2
                            +self.ingredients[2][1] * no_3 + self.ingredients[3][1] * no_4, 0)
                        * max(self.ingredients[0][2] * no_1 + self.ingredients[1][2] * no_2
                            +self.ingredients[2][2] * no_3 + self.ingredients[3][2] * no_4, 0)
                        * max(self.ingredients[0][3] * no_1 + self.ingredients[1][3] * no_2
                            +self.ingredients[2][3] * no_3 + self.ingredients[3][3] * no_4, 0)
                        * max(self.ingredients[0][4] * no_1 + self.ingredients[1][4] * no_2
                            +self.ingredients[2][4] * no_3 + self.ingredients[3][4] * no_4, 0)
                    )
                    calories = (self.ingredients[0][5] * no_1 + self.ingredients[1][5] * no_2
                                + self.ingredients[2][5] * no_3 + self.ingredients[3][5] * no_4
                                )
                    if calories == 500 and score > best_score:
                        best_score = score
                        best_recipe = [no_1, no_2, no_3, no_4]
        print("Best recipe:")
        print(f"{best_recipe[0]} spoons of {self.ingredients[0][0]}")
        print(f"{best_recipe[1]} spoons of {self.ingredients[1][0]}")
        print(f"{best_recipe[2]} spoons of {self.ingredients[2][0]}")
        print(f"{best_recipe[3]} spoons of {self.ingredients[3][0]}")
        print(f"For a total score of {best_score}")


cookie_recipe = CookieRecipe("InputData/d15.txt")
cookie_recipe.find_best_cookie(100)
