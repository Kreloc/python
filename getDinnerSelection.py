#! python3
# getDinnerSelection - Gets dinner selection from collection in script

import random
#Define dinner options
dinnerOptions = ['breakfast burritos',
'chicken enchiladas',
'fajitas',
'kalua pork',
'lasagna',
'mac & cheese',
'manicotti',
'meatloaf',
'pulled pork',
'red beans with hammock',
'ribs',
'roasted chicken & veggies',
'salmon chowder',
'Shit on Rice',
'Hamburger Pie',
'Sloppy Joes',
'Chicken drumsticks',
'Teriyaki chicken',
'Chicken and Noodles',
'Chicken and Green Beans',
'Chicken pot pie',
'Bbq chicken',
'Pork chops',
'Ham - spiral',
'Hot dogs',
'Chili dogs',
'Frito Pie',
'Taco salad',
'Nachoes',
'Rib eye steak',
'Chicken fried steak',
'Tri tip sandwhich',
'Soup and grilled cheese sandwhiches',
'Pizza rolls',
'Teriyaki meat with rice and brocoli',
'Pot roast and vegetables',
'Beef stew',
'Breakfast for dinner',
'Oven fried chicken',
'Spaghetti',
'Taco Dip',
'Beer battered halibut',
'Trout',
'Blackened salmon',
'Tacoes',
'Shrimp scampi',
'White bean chicken chili',
'Chicken wings']

#TODO: Pick random dinner
#randomNumber = random.randint(0,(len(dinnerOptions) - 1))
#print('Dinner tonight is ' + dinnerOptions[randomNumber])
#TODO: Get week worth of dinners and the ingredients needed
for i in range(0, 7):
    if i == 0:
        day = "Sunday"
    elif i == 1:
        day = "Monday"
    elif i == 2:
        day = "Tuesday"
    elif i == 3:
        day = "Wednesday"
    elif i == 4:
        day = "Thursday"
    elif i == 5:
        day = "Friday"
    elif i == 6:
        day = "Saturday"
    else:
        day = "Anyday"
    randomNumber = random.randint(0,(len(dinnerOptions) - 1))
    print('Dinner on ' + day + ' is ' + dinnerOptions[randomNumber])
#Remove dinner selection from list before making next selection
    del dinnerOptions[randomNumber]
#TODO: Create shopping list


