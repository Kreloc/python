#! python3
# getDinnerSelection - Gets dinner selection for the week from list in script

import random
#Dictionary of dinners and their ingeredients
dinner_ingredients = {
'breakfast burritos': 'Eggs, tortillas(Burrito size), maple sausage, cheese, sour cream',
'chicken enchiladas': 'Boneless skinless chicken, cheese, black olives (chopped), green onions, enchilada sauce mix, flour tortillas, tomato paste',
'fajitas': 'Chicken/Steak meat, large onion, orange pepper, yellow pepper, refried beans, tortillas, shredded cheese, sour cream, salsa',
'kalua pork': 'Pork butt roast, Hawaiian sea salt, Liquid smoke flavoring',
'lasagna': 'Ground beef, tomato sauce, tomato paste, garlic clove, Ricotta cheese, lasagna noodles, eggs, Italian seasonings, shredded cheese, shredded parmesan cheese',
'mac & cheese': 'Macaroni noodles, butter, seasoned dry crumbs, flour, salt, milk, Velveeta, shredded cheddar cheese',
'manicotti': 'Ground beef, eggs, tomato sauce, tomato paste, garlic clove, Ricotta cheese, lasagna noodles, eggs, Italian seasonings, shredded cheese, shredded parmesan cheese',
'meatloaf': 'Ground beef, eggs, ketchup, bread crumbs, salt, pepper, Italian seasoning',
'pulled pork': 'Pork shoulder, hamburger buns, leafy green lettuce, Root beer, chili sauce, garlic cloves, root beer concentrate, tomato slices, hot pepper sauce, salt, pepper, cooking oil',
'red beans with hammock': 'Red beans, hammocks, rice',
'ribs': 'Pork spare ribs, Bbq sauce',
'roasted chicken & veggies': 'Chicken thighs with skin, oil, salt, pepper, dill, italian seasoning, carrots, zucchini',
'salmon chowder': 'Salmon, butter, onion, celery, garlic, potatoes, carrots, chicken broth, salt, butter, dried dill weed, evaporated milk, creamed corn, shredded cheddar cheese',
'Shit on Rice': 'Ground beef, rice, cream of mushroom soup',
'Hamburger Pie': 'Ground beef, green beans, corn, shredded cheese, tomato soup, onion, mashed potatoes',
'Sloppy Joes': 'Ground beef, hamburger buns, tomato paste, sloppy joe mix',
'Chicken drumsticks': 'Chicken thighs/drumsticks',
'Teriyaki chicken burgers': 'Boneless skinless chicken, hamburger buns, Swiss cheese - sliced, pineapple - ring slices, teriyaki sauce',
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
'Nachos': 'Ground turkey/leftover tacos, shredded cheese, jalapenos, tortilla chips',
'Rib eye steak': 'Rib eye steak, raspberry chipotle sauce',
'Chicken fried steak': 'Round steak, crackers, eggs, shortening',
'Tri tip sandwich': 'Tri tip steak, mushrooms, itlaian bread, mozzarella cheese',
'Soup and grilled cheese sandwiches': 'sliced cheese, tomato soup, bread, butter',
'Pizza rolls': 'Pizza meats (Pepperoni, sausage, etc.), egg roll wrappers, shredded cheese, pizza sauce',
'Teriyaki meat with rice and broccoli': 'Mock beef/Chicken tender/pork loin, rice, broccoli, teriyaki sauce',
'Pot roast and vegetables': 'Pot roast, potatoes, beef broth',
'Beef stew': 'Pot roast meat, beef broth, carrots, Worchester sauce, flour, onion, potatoes',
'Breakfast for dinner': 'Eggs, bacon, bread, butter',
'Oven fried chicken': 'Chicken drumsticks/thigs, eggs, cornmeal, milk',
'Spaghetti': 'Ground beef, spaghetti rigatoni, mushrooms, tomato paste, tomato sauce, italian seasoning, black pepper, minced garlic, italian bread',
'Taco Dip': 'Leftover taco stuff (meat and beans), shredded cheese, sour cream',
'Beer battered halibut': 'Halibut, batter, beer, shortening',
'Trout': 'Trout, shortening, cornmeal',
'Blackened salmon': 'Salmon, butter, blackened seasonings',
'Tacos': 'Ground turkey, taco seasoning, tortillas, shredded cheese, lettuce, olives, avocado, sour cream',
'Shrimp scampi': 'Shrimp, butter, garlic, noodles',
'White bean chicken chili': 'White beans, chicken meat, olive oil, onion (chopped), chicken stock, salsa verde, ground cumin, coriander, two jalapenos, salt, ground white pepper, white corn',
'Chicken wings': 'Chicken wings'
    }
#Define dinner options
dinner_options = [x for x in dinner_ingredients.keys()]

all_ingredients = []
dinner_list = []
#leftover_day_set = False
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
#Loop thru dinnerList, assign to days, and get ingredients needed
#print week menu plan
dinner_menu = []
print('Dinners this week')
days_of_week = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
for i, dinner_choice in enumerate(dinner_list):
    try:
        day = days_of_week[i-1]
    except IndexError:
        day = "Anyday"

    day = "{}: ".format(day)
    #dinner_choice = dinner_list[i]
    print(day + dinner_choice)
    dinner_menu.append((day + dinner_choice))
    if dinner_choice != 'Leftovers':
        found_ingredients = dinner_ingredients[dinner_choice]
        all_ingredients.append(dinner_choice + ':')
        all_ingredients.append(found_ingredients)

print('\nIngredients:')
print('\n'.join(all_ingredients))

#TODO: Format as shopping list with number of each item

