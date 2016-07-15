#! python3
# getDinnerSelection - Gets dinner selection for the week from list in script

##import random
##import os
##import json
#Dictionary of dinners and their ingeredients
with open('/home/Kreloc/mysite/dinners.json') as json_file:
    json_data = json.load(json_file)

#Define dinner options
dinner_ingredients = json_data
dinner_options = list(json_data.keys())

#TODO: Parse text file(s) and remove dinner options found from the past
#two weeks
##week_number = 0
##if os.path.isfile('dinner_week_one.txt') == True:
##    week_number = 1
##    dinner_file = open('dinner_week_one.txt')
##    dinner_choices = (dinner_file.readline()).split(',')
##    for dinner_choice in dinner_choices:
##        dinner_options.remove(dinner_choice)
##    dinner_file.close()
##
##if os.path.isfile('dinner_week_two.txt') == True:
##    week_number = 2
##    dinner_file = open('dinner_week_two.txt')
##    dinner_choices = (dinner_file.readline()).split(',')
##    for dinner_choice in dinner_choices:
##        dinner_options.remove(dinner_choice)
##    dinner_file.close()
##
##if os.path.isfile('dinner_week_three.txt') == True:
##    week_number = 3  
##    dinner_file = open('dinner_week_three.txt')
##    dinner_choices = (dinner_file.readline()).split(',')
##    for dinner_choice in dinner_choices:
##        dinner_options.remove(dinner_choice)
##    dinner_file.close()
##    #Re-add dinner_week_one.txt dinner items
##    if os.path.isfile('dinner_week_one.txt') == True:
##        dinner_file = open('dinner_week_one.txt')
##        dinner_choices = (dinner_file.readline()).split(',')
##        for dinner_choice in dinner_choices:
##            dinner_options.append(dinner_choice)
##        dinner_file.close()
##
##if os.path.isfile('dinner_week_four.txt') == True:
##    week_number = 4  
##    dinner_file = open('dinner_week_four.txt')
##    dinner_choices = (dinner_file.readline()).split(',')
##    for dinner_choice in dinner_choices:
##        dinner_options.remove(dinner_choice)
##    dinner_file.close()
##    #Re-add dinner_week_one and dinner_week_two dinner items
##    if os.path.isfile('dinner_week_one.txt') == True:
##        dinner_file = open('dinner_week_one.txt')
##        dinner_choices = (dinner_file.readline()).split(',')
##        for dinner_choice in dinner_choices:
##            dinner_options.append(dinner_choice)
##        dinner_file.close()    
##    if os.path.isfile('dinner_week_two.txt') == True:
##        dinner_file = open('dinner_week_two.txt')
##        dinner_choices = (dinner_file.readline()).split(',')
##        for dinner_choice in dinner_choices:
##            dinner_options.append(dinner_choice)
##            dinner_file.close()

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
return('Dinners this week')
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

    return(day + dinner_choice)
    dinner_menu.append((day + dinner_choice))
    if dinner_choice != 'Leftovers':
        found_ingredients = dinner_ingredients[dinner_choice]
        all_ingredients.append(dinner_choice + ':')
        all_ingredients.append(found_ingredients)

return('\nIngredients:')
return('\n'.join(all_ingredients))
#TODO: Format as shopping list with number of each item
#TODO: Output text file for each week
##if week_number == 0:
##    #Remove leftovers from list using list comprhension]
##    dinner_list = [x for x in dinner_list if x != 'Leftovers']
##    dinner_file = open('dinner_week_one.txt', 'w')
##    dinner_file.write(','.join(dinner_list))
##    dinner_file.close()
##elif week_number == 1:
##    dinner_file = open('dinner_week_two.txt', 'w')
##    dinner_list = [x for x in dinner_list if x != 'Leftovers']    
##    dinner_file.write(','.join(dinner_list))
##    dinner_file.close()
##elif week_number == 2:
##    dinner_file = open('dinner_week_three.txt', 'w')
##    dinner_list = [x for x in dinner_list if x != 'Leftovers']    
##    dinner_file.write(','.join(dinner_list))
##    dinner_file.close()    
##elif week_number == 3:
##    dinner_file = open('dinner_week_four.txt', 'w')
##    dinner_list = [x for x in dinner_list if x != 'Leftovers']    
##    dinner_file.write(','.join(dinner_list))
##    dinner_file.close()
##elif week_number == 4:
##    #TODO: Remove past dinner text files
##    os.remove('dinner_week_one.txt')
##    os.remove('dinner_week_two.txt')
##    os.remove('dinner_week_three.txt')
##    os.remove('dinner_week_four.txt')
