import requests
#My Food2Fork Free API. 500 calls per 24 hours
api_key = 'f1a8d378f3d9b5a736f810d9847069c8'

final_output = []

def findRecipes(search, numOfPages):
    #TODO: Add pagination
    #Currently only returns top thirty recipes.
    found_recipes = []
    for num in range (1, (int(numOfPages) + 1)):
        numString = str(num)
        url = 'http://food2fork.com/api/search?key=' + api_key + '&q=' + search + '&page=' + numString
        url = url.replace(' ','%20')
        print(url)
        res = requests.get(url)
        recipes = (res.json())['recipes']
        print(recipes)
        found_recipes.append(recipes)
    return found_recipes

def getRecipe(recipe_id):
    url = 'http://food2fork.com/api/get?key=' + api_key + '&rId=' + recipe_id
    #Debug
    print(url)
    res = requests.get(url)
    recipe = res.json()
    return recipe
    
