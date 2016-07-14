#! python3
# getDinnerSelection - Gets dinner selection for the week from list in script

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
'Teriyaki chicken burgers',
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
'Tri tip sandwich',
'Soup and grilled cheese sandwiches',
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

#Dictionary of dinners and their ingeredients
dinnerIngredients = {
'breakfast burritos': 'Eggs, tortillas(Burrito size), maple sausage, cheese, sour cream',
'chicken enchiladas': 'Boneless skinless chicken, cheese, black olives (chopped), green onions, enchilada sauce mix, flour tortillas, tomate paste',
'fajitas': 'Chicken/Steak meat, large onion, organe pepper, yellow pepper, refried beans, tortillas, shredded cheese, sour cream, salsa',
'kalua pork': 'Pork butt roast, Hawaiian sea salt, Liquid smoke flavoring',
'lasagna': 'Ground beef, tomato sauce, tamato paste, garlic clove, Ricotta cheese, lasagna noodles, eggs, Italian seasonings, shredded cheese, shredded parmesean cheese',
'mac & cheese': 'Macaroni noodles, butter, seasoned dry crumbs, flour, salt, milk, Velveeta, shredded cheddar cheese',
'manicotti': 'Ground beef, eggs, tomato sauce, tamato paste, garlic clove, Ricotta cheese, lasagna noodles, eggs, Italian seasonings, shredded cheese, shredded parmesean cheese',
'meatloaf': 'Ground beef, eggs, ketchup, bread crumbs, salt, pepper, Italian seasoning',
'pulled pork': 'Pork shoulder, hamburger buns, leafy green lettuce, Root beer, chili sauce, garlic cloves, root beer concentrate, tomato slices, hot pepper sauce, salt, pepper, cooking oil',
'red beans with hammock': 'Red beans, hammocks, rice',
'ribs': 'Pork spare ribs, Bbq sauce',
'roasted chicken & veggies': 'Chicken thighs with skin, oil, salt, pepper, dill, italian seasoing, carrots, zucinni',
'salmon chowder': 'Salmon, butter, onion, celery, garlic, potatoes, carrots, chicken broth, salt, butter, dried dill weed, evaporated milk, creamed corn, shredded cheddar cheese',
'Shit on Rice': 'Ground beef, rice, cream of mushroom soup',
'Hamburger Pie': 'Ground beef, green beans, corn, shredded cheese, tomato soup, onion, mashed potatoes',
'Sloppy Joes': 'Ground beef, hamburger buns, tomato paste, sloppy joe mix',
'Chicken drumsticks': 'Chicken thighs/drumsticks',
'Teriyaki chicken burgers': 'Boneless skinless chicken, hamburger buns, swiss cheese - sliced, pineapple - ring slices, teriyaki sauce',
'Chicken and Noodles': 'Chicken, onion, egg noodles',
'Chicken and Green Beans': 'Boneless skinless chicken, green beans, cream of chicken soup',
'Chicken pot pie': 'Boneless skinless chicken, mixed vegetables, pie crust, onion',
'Bbq chicken': 'Chicken drumsticks/thigs, Bbq sauce',
'Pork chops': 'Pork chops, milk, cream of mushroom soup',
'Ham - spiral': 'Honey spiral ham',
'Hot dogs': 'Hot dogs, hot dog buns, ketchup, mustard',
'Chili dogs': 'Chili, hot dogs, hot dog buns, cheese, jalapenos',
'Frito Pie': 'Fritos, chili, corn, diced tomatoes, jalapenos',
'Taco salad': 'Ground turkey, tortillas, shredded cheese, olives, beans, sour cream',
'Nachoes': 'Ground turkey/leftover tacoes, shredded cheese, jalapenos, tortilla chips',
'Rib eye steak': 'Rib eye steak, rapsberry chipolte sauce',
'Chicken fried steak': 'Round steak, crackers, eggs, shortening',
'Tri tip sandwich': 'Tri tip steak, mushrooms, itlaian bread, mozzarella cheese',
'Soup and grilled cheese sandwiches': 'sliced cheese, tomato soup, bread, butter',
'Pizza rolls': 'Pizza meats (Pepperoni, sausage, etc.), egg roll wrappers, shredded cheese, pizza sauce',
'Teriyaki meat with rice and brocoli': 'Mock beef/Chiken tender/pork loin, rice, brocoli, teriyaki sauce',
'Pot roast and vegetables': 'Pot roast, potatoes, beef broth',
'Beef stew': 'Pot roast meat, beef broth, carrots, worchester sauce, flour, onion, potatoes',
'Breakfast for dinner': 'Eggs, bacon, bread, butter',
'Oven fried chicken': 'Chicken drumsticks/thigs, eggs, cornmeal, milk',
'Spaghetti': 'Ground beef, spaghetti rigatoni, mushrooms, tomato paste, tomato sauce, italian seasoning, black pepper, minced garlic, italian bread',
'Taco Dip': 'Leftover taco stuff (meat and beans), shredded cheese, sour cream',
'Beer battered halibut': 'Halibut, batter, beer, shortening',
'Trout': 'Trout, shortening, cornmeal',
'Blackened salmon': 'Salmon, butter, blackened seasonings',
'Tacoes': 'Ground turkery, taco seasoning, tortillas, shredded cheese, lettuce, olives, avocado, sour cream',
'Shrimp scampi': 'Shrimp, butter, garlic, noodles',
'White bean chicken chili': 'White beans, chicken meat, olive oil, onion (chopped), chicken stock, salsa verde, ground cumin, coriander, two jalapenos, salt, ground white pepper, white corn',
'Chicken wings': 'Chicken wings'
    }


#Pick random dinner
#randomNumber = random.randint(0,(len(dinnerOptions) - 1))
#print('Dinner tonight is ' + dinnerOptions[randomNumber])
#Get week worth of dinners
####allIngredients = []
####for i in range(0, 7):
####    if i == 0:
####        day = "Sunday"
####    elif i == 1:
####        day = "Monday"
####    elif i == 2:
####        day = "Tuesday"
####    elif i == 3:
####        day = "Wednesday"
####    elif i == 4:
####        day = "Thursday"
####    elif i == 5:
####        day = "Friday"
####    elif i == 6:
####        day = "Saturday"
####    else:
####        day = "Anyday"
####    randomNumber = random.randint(0,(len(dinnerOptions) - 1))
####    print('Dinner on ' + day + ' is ' + dinnerOptions[randomNumber])
####    dinnerChoice = dinnerOptions[randomNumber]
####    #print('Ingredients needed: ')
####    #print(dinnerIngredients[dinnerChoice])
####    foundIngredients = dinnerIngredients[dinnerChoice]
####    allIngredients.append(dinnerChoice + ':')
####    allIngredients.append(foundIngredients)
####Remove dinner selection from list before making next selection
####    del dinnerOptions[randomNumber]
####Create shopping list
####print('\n'.join(allIngredients))
#Get week worth of dinners setting one day after Tuesday as leftovers day
allIngredients = []
dinnerList = []
leftoverDaySet = False
randomLeftoverNumber = random.randint(4, 6)
for i in range(0, 7):
    if i == randomLeftoverNumber:
        dinnerChoice = 'Leftovers'
        leftoverDaySet = True
    if leftoverDaySet == True:
        #print('Dinner on ' + day + ' is ' + dinnerChoice)
        leftoverDaySet = False
        dinnerList.append(dinnerChoice)
    else:
        randomNumber = random.randint(0,(len(dinnerOptions) - 1))
        dinnerChoice = dinnerOptions[randomNumber]
        dinnerList.append(dinnerChoice)
        #Remove dinner selection from list before making next selection
        dinnerOptions.remove(dinnerChoice)
#Change dinner choices if nachoes or taco dip found but tacoes are
#not a meal that week
if 'Nachos' in dinnerList:
    if 'Tacos' not in dinnerList:
        dinnerList.remove('Nachos')
        randomNumber = random.randint(0,(len(dinnerOptions) - 1))
        dinnerChoice = dinnerOptions[randomNumber]
        dinnerList.append(dinnerChoice)
        dinnerOptions.remove(dinnerChoice)
if 'Taco Dip' in dinnerList:
    if 'Tacos' not in dinnerList:
        dinnerList.remove('Taco Dip')
        randomNumber = random.randint(0,(len(dinnerOptions) - 1))
        dinnerChoice = dinnerOptions[randomNumber]
        dinnerList.append(dinnerChoice)
        dinnerOptions.remove(dinnerChoice)
#Loop thru dinnerList, assign to days, and get ingredients needed
#print week menu plan
dinnerMenu = []
print('Dinners this week')
for i in range (0, 7):
    if i == 0:
        day = "Sunday: "
    elif i == 1:
        day = "Monday: "
    elif i == 2:
        day = "Tuesday: "
    elif i == 3:
        day = "Wednesday: "
    elif i == 4:
        day = "Thursday: "
    elif i == 5:
        day = "Friday: "
    elif i == 6:
        day = "Saturday: "
    else:
        day = "Anyday: "
    dinnerChoice = dinnerList[i]
    print(day + dinnerChoice)
    dinnerMenu.append((day + dinnerChoice))
    if dinnerChoice != 'Leftovers':
        foundIngredients = dinnerIngredients[dinnerChoice]
        allIngredients.append(dinnerChoice + ':')
        allIngredients.append(foundIngredients)
print('\nIngredients:')
print('\n'.join(allIngredients))

#TODO: Format as shopping list with number of each item


