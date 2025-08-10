# Problem: 2115. Find All Possible Recipes from Given Supplies - https://leetcode.com/problems/find-all-possible-recipes-from-given-supplies/description/

class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        supply_set = set(supplies)
        recipe_list = recipes
        ingredient_list = ingredients
        recipe_to_index = {recipe: i for i, recipe in enumerate(recipe_list)}
        dependency_count = [0] * len(recipe_list)
        ingredient_to_recipe = {}
        
        for i in range(len(recipe_list)):
            recipe = recipe_list[i]
            ingredients_needed = ingredient_list[i]
            for ingredient in ingredients_needed:
                if ingredient not in supply_set:
                    if ingredient in recipe_to_index:
                        ingredient_to_recipe.setdefault(ingredient, []).append(i)
                        dependency_count[i] += 1
                    else:
                        dependency_count[i] = -1
                        break
        
        queue = deque()
        for i in range(len(recipe_list)):
            if dependency_count[i] == 0:
                queue.append(i)
        
        creatable = []
        while queue:
            recipe_idx = queue.popleft()
            recipe = recipe_list[recipe_idx]
            creatable.append(recipe)
            if recipe in ingredient_to_recipe:
                for dependent_recipe_idx in ingredient_to_recipe[recipe]:
                    dependency_count[dependent_recipe_idx] -= 1
                    if dependency_count[dependent_recipe_idx] == 0:
                        queue.append(dependent_recipe_idx)
        
        return creatable