from flask import Flask, render_template
import random
import json
app = Flask(__name__)
app.secret_key = 'This is really unique and secret'

#@app.route('/')
#! python3
# getDinnerSelection - Gets dinner selection for the week from list in script

##import random
##import os
##import json
#Dictionary of dinners and their ingeredients
@app.route('/')
def getDinnerMenu():
    final_output = []
    with open('/home/Kreloc/mysite/dinners.json') as json_file:
        json_data = json.load(json_file)

    #Define dinner options
    dinner_ingredients = json_data
    dinner_options = list(json_data.keys())

    #TODO: Parse text file(s) and remove dinner options found from the past
    all_ingredients = []
    dinner_list = []
    random_leftover_number = random.randint(4, 6)
    for i in range(0, 7):
        if i == random_leftover_number:
            dinner_list.append('Leftovers')
            continue
        dinner_choice = random.choice(dinner_options)
        dinner_list.append(dinner_choice)
        #Remove dinner selection from list before making next selection
        dinner_options.remove(dinner_choice)
    #Change dinner choices if nachoes or taco dip found but tacoes are
    #not a meal that week
    if 'Tacos' not in dinner_list:
        for f in ('Nachos', 'Taco Dip'):
            if f in dinner_list:
                dinner_list.remove(f)
                dinner_choice = random.choice(dinner_options)
                dinner_list.append(dinner_choice)
                dinner_options.remove(dinner_choice)
    #Loop thru dinner_list, assign to days, and get ingredients needed
    #print week menu plan
    dinner_menu = []
    final_output.append('Dinners this week')
    days_of_week = (
        "Monday: ",
        "Tuesday: ",
        "Wednesday: ",
        "Thursday: ",
        "Friday: ",
        "Saturday: ",
        "Sunday: ")
    for i, dinner_choice in enumerate(dinner_list):
        try:
            day = days_of_week[i-1]
        except IndexError:
            day = "Anyday"

        final_output.append(day + dinner_choice)
        dinner_menu.append((day + dinner_choice))
        if dinner_choice != 'Leftovers':
            found_ingredients = dinner_ingredients[dinner_choice]
            all_ingredients.append(dinner_choice + ':')
            all_ingredients.append(found_ingredients)

    final_output.append('\nIngredients:')
    #final_output.append(all_ingredients)
    for ingredient_list in all_ingredients:
        final_output.append(ingredient_list)
    #TODO: Format as shopping list with number of each item
    #TODO: Output text file for each week
    ##    #TODO: Remove past dinner text files
    return render_template('index.html', pages=final_output)
