"""

You have information about n different recipes. You are given a string array recipes and a 2D string array ingredients. The ith recipe has the name recipes[i], and you can create it if you have all the needed ingredients from ingredients[i]. A recipe can also be an ingredient for other recipes, i.e., ingredients[i] may contain a string that is in recipes.

You are also given a string array supplies containing all the ingredients that you initially have, and you have an infinite supply of all of them.

Return a list of all the recipes that you can create. You may return the answer in any order.

Note that two recipes may contain each other in their ingredients.

 

Example 1:

Input: recipes = ["bread"], ingredients = [["yeast","flour"]], supplies = ["yeast","flour","corn"]
Output: ["bread"]
Explanation:
We can create "bread" since we have the ingredients "yeast" and "flour".
Example 2:

Input: recipes = ["bread","sandwich"], ingredients = [["yeast","flour"],["bread","meat"]], supplies = ["yeast","flour","meat"]
Output: ["bread","sandwich"]
Explanation:
We can create "bread" since we have the ingredients "yeast" and "flour".
We can create "sandwich" since we have the ingredient "meat" and can create the ingredient "bread".
Example 3:

Input: recipes = ["bread","sandwich","burger"], ingredients = [["yeast","flour"],["bread","meat"],["sandwich","meat","bread"]], supplies = ["yeast","flour","meat"]
Output: ["bread","sandwich","burger"]
Explanation:
We can create "bread" since we have the ingredients "yeast" and "flour".
We can create "sandwich" since we have the ingredient "meat" and can create the ingredient "bread".
We can create "burger" since we have the ingredient "meat" and can create the ingredients "bread" and "sandwich".
 

Constraints:

n == recipes.length == ingredients.length
1 <= n <= 100
1 <= ingredients[i].length, supplies.length <= 100
1 <= recipes[i].length, ingredients[i][j].length, supplies[k].length <= 10
recipes[i], ingredients[i][j], and supplies[k] consist only of lowercase English letters.
All the values of recipes and supplies combined are unique.
Each ingredients[i] does not contain any duplicate values.

"""

"""

Complexity Analysis

Let n be the number of recipes, m be the total number of ingredients across all recipes, and s be the number of supplies.

Time complexity: O(n+m+s)

The algorithm uses DFS to check each recipe's ingredients. Initially, we process supplies and create recipe mappings in O(s) and O(n) time, respectively. For each recipe, we perform DFS through its ingredients, visiting each ingredient exactly once due to the visited set preventing cycles. Since we memoize results in the canMake map, each ingredient and recipe is processed at most once across all DFS calls. Therefore, the total number of operations is proportional to the number of recipes plus the total number of ingredients, giving us O(n+m+s) time complexity.

Space complexity: O(n+m)

The solution uses several key data structures for its space requirements. The hash map canMake stores recipe and ingredient results using O(n+m) space, while recipeToIndex maps recipes to indices using O(n) space. For cycle detection, a visited set and result list possibleRecipes each take O(n) space. The recursion stack in worst-case scenarios with chained recipe dependencies also requires O(n) space. Considering these components, the total auxiliary space complexity is O(n+m).
"""

class Solution1:
    def findAllRecipes(
        self,
        recipes: list[str],
        ingredients: list[list[str]],
        supplies: list[str],
    ) -> list[str]:
        # Initialize tracking dictionaries using comprehensions
        can_make = dict.fromkeys(supplies, True)
        recipe_to_idx = {recipe: idx for idx, recipe in enumerate(recipes)}

        def _check_recipe(recipe: str, visited: set) -> bool:
            # Already processed and can be made
            if can_make.get(recipe, False):
                return True

            # Not a valid recipe or cycle detected
            if recipe not in recipe_to_idx or recipe in visited:
                return False

            visited.add(recipe)

            # Check if all ingredients can be made
            can_make[recipe] = all(
                _check_recipe(ingredient, visited)
                for ingredient in ingredients[recipe_to_idx[recipe]]
            )

            return can_make[recipe]

        # Process each recipe and collect those that can be made
        return [recipe for recipe in recipes if _check_recipe(recipe, set())]

class SolutionII:
    def findAllRecipes(self, recipes, ingredients, supplies):
        recipe_index = {r: i for i, r in enumerate(recipes)}
        can_cook = {s: True for s in supplies}

        def dfs(r):
            if r in can_cook:
                return can_cook[r]
            
            if r not in recipe_index:
                return False

            # Cycle detection
            can_cook[r] = False

            for nei in ingredients[recipe_index[r]]:
                if not dfs(nei):
                    return False
            
            can_cook[r] = True

            return True

        return [r for r in recipes if dfs(r)]

from collections import deque
class Solution:
    def findAllRecipes(
        self,
        recipes,
        ingredient,
        supplies
    ):
        # Track available ingredients and recipes
        available = set(supplies)

        # Queue to process recipe indices
        recipe_queue = deque(range(len(recipes)))
        created_recipes = []
        last_size = -1  # Tracks last known available count

        # Continue while we keep finding new recipes
        while len(available) > last_size:
            last_size = len(available)
            queue_size = len(recipe_queue)

            # Process all recipes in current queue
            while queue_size > 0:
                queue_size -= 1
                recipe_idx = recipe_queue.popleft()
                if all(
                    ingredient in available
                    for ingredient in ingredients[recipe_idx]
                ):
                    # Recipe can be created - add to available items
                    available.add(recipes[recipe_idx])
                    created_recipes.append(recipes[recipe_idx])
                else:
                    recipe_queue.append(recipe_idx)

        return created_recipes

recipes = ["bread","sandwich"]
ingredients = [["yeast","flour"],["bread","meat"]]
supplies = ["yeast","flour","meat"]

solution = Solution()

print("res:", solution.findAllRecipes(recipes, ingredients, supplies))


# Kahn's algorithm DFS
class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        graph = defaultdict(list)

        for i in range(len(recipes)):
            graph[recipes[i]] = ingredients[i]

        available_recipes = set(supplies)

        stack = set()

        def dfs(r):
            if r in available_recipes:
                return True
            if r not in graph:
                return False

            if r in stack:
                return False

            stack.add(r)

            for recipe in graph[r]:
                if not dfs(recipe):
                    return False
            
            available_recipes.add(r)
            stack.remove(r)
            return True

        return [r for r in graph if dfs(r)]
        
# BFS
# Time complexity: O(n+m+s)
# Space complexity: O(n+m+s)
class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:

        graph = defaultdict(list)
        indegree = [0] * len(recipes)

        for i in range(len(recipes)):
            for ingredient in ingredients[i]:
                graph[ingredient].append(i)
                indegree[i] += 1

        q = deque(supplies)

        res = []
        while q:
            available = q.popleft()
            recipe 

            for neighbor in graph[available]:
                indegree[neighbor] -= 1

                if indegree[neighbor] == 0:
                    q.append(recipes[neighbor])
                    res.append(recipes[neighbor])

            

            

        return res
         

class Solution:
    def findAllRecipes(
        self,
        recipes: list[str],
        ingredients: list[list[str]],
        supplies: list[str],
    ) -> list[str]:
        # Store available supplies
        available_supplies = set(supplies)
        # Map recipe to its index
        recipe_to_index = {recipe: idx for idx, recipe in enumerate(recipes)}
        # Map ingredient to recipes that need it
        dependency_graph = defaultdict(list)
        # Count of non-supply ingredients needed for each recipe
        in_degree = [0] * len(recipes)

        # Build dependency graph
        for recipe_idx, ingredient_list in enumerate(ingredients):
            for ingredient in ingredient_list:
                if ingredient not in available_supplies:
                    dependency_graph[ingredient].append(recipes[recipe_idx])
                    in_degree[recipe_idx] += 1

        # Start with recipes that only need supplies
        queue = deque(idx for idx, count in enumerate(in_degree) if count == 0)
        created_recipes = []

        # Process recipes in topological order
        while queue:
            recipe_idx = queue.popleft()
            recipe = recipes[recipe_idx]
            created_recipes.append(recipe)

            # Skip if no recipes depend on this one
            for dependent_recipe in dependency_graph[recipe]:
                in_degree[recipe_to_index[dependent_recipe]] -= 1
                if in_degree[recipe_to_index[dependent_recipe]] == 0:
                    queue.append(recipe_to_index[dependent_recipe])

        return created_recipes
