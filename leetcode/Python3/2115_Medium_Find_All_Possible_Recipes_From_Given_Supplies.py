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
from typing import List
from collections import deque, defaultdict
import heapq
class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        pantry = set(supplies)
        inDegree = defaultdict(int)
        depends = defaultdict(list)
        answer = []

        for recipe, ing_list in zip(recipes, ingredients):
            inDegree[recipe] = len(ing_list)
            for ing in ing_list:
                if ing not in depends:
                    depends[ing] = []
                depends[ing].append(recipe)
  
        queue = deque()
        for recipe in recipes:
            if inDegree[recipe] == 0 or all(ing in pantry for ing in ingredients[recipes.index(recipe)]):
                queue.append(recipe)

        while queue:
            recipe = queue.popleft()
            answer.append(recipe)
            pantry.add(recipe)

            if recipe in depends:
                for drecipe in depends[recipe]:
                    inDegree[drecipe] -=1
                    if inDegree[drecipe] == 0 or all(ing in pantry for ing in ingredients[recipes.index(drecipe)]):
                        queue.append(drecipe)
        return answer
sol = Solution()
recipes = ["bread","sandwich","burger"]
ingredients = [["yeast","flour"],["bread","meat"],["sandwich","meat","bread"]]
supplies = ["yeast","flour","meat"]     
print(sol.findAllRecipes(recipes, ingredients, supplies))   


"""        for r in range(len(ingredients)):
            for ingredient in ingredients[r]:
                depends[recipes[r]].append(ingredient)
        
        for recipe, ingredients in depends.items():
            d,c = False,0
            for ingredient in ingredients:
                if ingredient in recipes:
                    d=True
                    c+=1
            if d:
                inDegree[recipe]+=c
            else:
                inDegree[recipe]=0
            

        for supply in supplies:
            pantry[supply]+=1

        queue = deque([r for r, d in inDegree.items() if d == 0])
        while queue:
            curr = queue.popleft()
            print(curr)"""