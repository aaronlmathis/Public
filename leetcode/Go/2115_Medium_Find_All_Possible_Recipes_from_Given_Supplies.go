/*
You have information about n different recipes. You are given a string array recipes and a 2D string array ingredients. The ith recipe has the name recipes{i], and you can create it if you have all the needed ingredients from ingredients[i]. A recipe can also be an ingredient for other recipes, i.e., ingredients[i] may contain a string that is in recipes.

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
*/
package main

import (
	"fmt"
)

func findAllRecipes(recipes []string, ingredients [][]string, supplies []string) []string {
	n := len(recipes)
	// Build Hashmaps for the graph depends[ingredient]->recipe
	depends := make(map[string][]string, n*2)
	// Build hashmap to track inDegree of every recipe.
	inDegree := make(map[string]int, n)
	// Hash map for quick lookup of ingredients in the pantry (what we have)
	pantry := make(map[string]struct{}, n+len(supplies))
	// Answer string slice.
	answer := []string{}

	// Build map of recipe->index
	recipeIndex := make(map[string]int, len(recipes))
	for i, recipe := range recipes {
		recipeIndex[recipe] = i
	}

	// Build Graph of dependencies.
	for i, recipe := range recipes {
		inDegree[recipe] = len(ingredients[i])
		for _, ingredient := range ingredients[i] {
			depends[ingredient] = append(depends[ingredient], recipe)
		}
	}

	// Fill pantry
	for _, supply := range supplies {
		pantry[supply] = struct{}{}
	}

	// Queue for BFS traversal
	queue := []string{}

	// Fill queue with recipes that have an inDegree of 0 OR have everything required in pantry already
	for i, recipe := range recipes {
		if inDegree[recipe] == 0 {
			queue = append(queue, recipe)
		} else {
			haveIngredients := true
			for _, ingredient := range ingredients[i] {
				if _, ok := pantry[ingredient]; !ok {
					haveIngredients = false
				}
			}
			if haveIngredients {
				queue = append(queue, recipe)
			}
		}
	}
	// Process the queue using BFS.
	for len(queue) > 0 {
		recipe := queue[0]
		queue = queue[1:]

		// It's assumed that if a recipe makes it to queue, it can be made, so add it to answer.
		answer = append(answer, recipe)
		// Add recipe as ingredient in pantry
		pantry[recipe] = struct{}{}

		// Find other recipes that can now be made and add them to queue.
		if _, ok := depends[recipe]; ok {
			for _, drecipe := range depends[recipe] {
				inDegree[drecipe]--
				if inDegree[drecipe] == 0 {
					queue = append(queue, drecipe)
				} else {
					haveIngredients := true
					for _, ingredient := range ingredients[recipeIndex[drecipe]] {
						if _, ok := pantry[ingredient]; !ok {
							haveIngredients = false
						}
					}
					if haveIngredients {
						queue = append(queue, drecipe)
					}
				}
			}
		}
	}

	return answer
}

func findAllRecipesDFS(recipes []string, ingredients [][]string, supplies []string) []string {
	n := len(recipes)
	ms := make(map[string]bool)
	mr := make(map[string]int)

	for _, sup := range supplies {
		ms[sup] = true
	}
	for i, rec := range recipes {
		mr[rec] = i
	}

	good := make([]bool, n)
	vis := make([]bool, n)

	var dfs func(index int) bool
	dfs = func(index int) bool {
		if vis[index] {
			return good[index]
		}
		vis[index] = true

		for _, ing := range ingredients[index] {
			if ms[ing] {
				continue
			}
			idx, ok := mr[ing]
			if !ok {
				return false
			}
			if !vis[idx] {
				if !dfs(idx) {
					return false
				}
			}
			if vis[idx] && !good[idx] {
				return false
			}
		}

		good[index] = true
		return true
	}

	res := make([]string, 0)
	for i := 0; i < n; i++ {
		if dfs(i) {
			res = append(res, recipes[i])
		}
	}

	return res
}
func main() {
	//recipes := []string{"bread"}
	//ingredients := [][]string{{"yeast", "flour"}}
	//supplies := []string{"yeast", "flour", "corn"}

	recipes := []string{"bread", "sandwich", "burger"}
	ingredients := [][]string{{"yeast", "flour"}, {"bread", "meat"}, {"sandwich", "meat", "bread"}}
	supplies := []string{"yeast", "flour", "meat"}

	fmt.Println(findAllRecipes(recipes, ingredients, supplies))
}
