from flask import Flask, render_template
import random
import os
import json
import datetime
import time
import calendar
app = Flask(__name__)
app.secret_key = 'This is really unique and secret'

#@app.route('/')
#! python3
# getDinnerSelection - Gets dinner selection for the week from list in script

#Dictionary of dinners and their ingeredients
@app.route('/')
def getDinnerMenu():
    final_output = []
    with open('/home/Kreloc/mysite/dinners.json') as json_file:
        json_data = json.load(json_file)

    #Define dinner options
    dinner_ingredients = json_data
    dinner_options = list(json_data.keys())
    #Determine week number
    now = datetime.datetime.now()
    calendar.setfirstweekday(6)
    weeks = calendar.monthcalendar(now.year, now.month)
    for x in range(len(weeks)):
        if now.day in weeks[x]:
            week_number = x+1    
    #Parse text file(s) based on weeknumber and remove dinner options found from the past
    #week's menu from dinner options.    
    if week_number == 1:
        if os.path.isfile('/home/Kreloc/mysite/static/menus/dinner_week_five.txt') == True:
            dinner_file = open('/home/Kreloc/mysite/static/menus/dinner_week_five.txt')
            dinner_choices = (dinner_file.readline()).split(',')
            for dinner_choice in dinner_choices:
                dinner_options.remove(dinner_choice)
            dinner_file.close()
        if os.path.isfile('/home/Kreloc/mysite/static/menus/dinner_week_four.txt') == True:
            dinner_file = open('/home/Kreloc/mysite/static/menus/dinner_week_four.txt')
            dinner_choices = (dinner_file.readline()).split(',')
            for dinner_choice in dinner_choices:
                dinner_options.remove(dinner_choice)
            dinner_file.close()
    if week_number == 2:
        if os.path.isfile('/home/Kreloc/mysite/static/menus/dinner_week_one.txt') == True:
            dinner_file = open('/home/Kreloc/mysite/static/menus/dinner_week_one.txt')
            dinner_choices = (dinner_file.readline()).split(',')
            for dinner_choice in dinner_choices:
                dinner_options.remove(dinner_choice)
            dinner_file.close()        
    if week_number == 3:
        if os.path.isfile('/home/Kreloc/mysite/static/menus/dinner_week_one.txt') == True:
            dinner_file = open('/home/Kreloc/mysite/static/menus/dinner_week_one.txt')
            dinner_choices = (dinner_file.readline()).split(',')
            for dinner_choice in dinner_choices:
                dinner_options.remove(dinner_choice)
            dinner_file.close()
        if os.path.isfile('/home/Kreloc/mysite/static/menus/dinner_week_two.txt') == True:
            dinner_file = open('/home/Kreloc/mysite/static/menus/dinner_week_two.txt')
            dinner_choices = (dinner_file.readline()).split(',')
            for dinner_choice in dinner_choices:
                dinner_options.remove(dinner_choice)
            dinner_file.close()
    if week_number == 4:
        if os.path.isfile('/home/Kreloc/mysite/static/menus/dinner_week_three.txt') == True:
            dinner_file = open('/home/Kreloc/mysite/static/menus/dinner_week_three.txt')
            dinner_choices = (dinner_file.readline()).split(',')
            for dinner_choice in dinner_choices:
                dinner_options.remove(dinner_choice)
            dinner_file.close()              
    if week_number == 5:
        if os.path.isfile('/home/Kreloc/mysite/static/menus/dinner_week_four.txt') == True:
            dinner_file = open('/home/Kreloc/mysite/static/menus/dinner_week_four.txt')
            dinner_choices = (dinner_file.readline()).split(',')
            for dinner_choice in dinner_choices:
                dinner_options.remove(dinner_choice)
            dinner_file.close()      

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
    final_output.append('Dinners this week:')
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

    final_output.append('Ingredients:')
    #final_output.append(all_ingredients)
    for ingredient_list in all_ingredients:
        final_output.append(ingredient_list)
    date_string = ('Menu generated on ' + (str(now.month)) + '-' + (str(now.day)) + '-' + str((now.year)))
    final_output.append(date_string)
    #TODO: Format as shopping list with number of each item
    #TODO: Output text file for each week
    if week_number == 3:
        #Remove leftovers from list using list comprhension]
        dinner_list = [x for x in dinner_list if x != 'Leftovers']
        dinner_file = open('/home/Kreloc/mysite/static/menus/dinner_week_three.txt', 'w')
        dinner_file.write(','.join(dinner_list))
        dinner_file.close()    
    ##    #TODO: Remove past dinner text files
    return render_template('index.html', pages=final_output)
#TODO: Add save button to recipe page
