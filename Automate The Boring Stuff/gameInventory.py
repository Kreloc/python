items = {'rope': 1, 'torch': 3, 'gold crowns': 8, 'dagger': 1, 'cloak': 1, 'Clothes': 1}

def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        #My code
        print('You have ' + str(v) + ' ' + k)
        #End my code
        item_total = item_total + v
        
    print("Total number of items: " + str(item_total))

#def addToInventory(inventory, addedItems):
    #My code below
    

#dragonLoot = ['gold crowns', 'dagger', 'gold crowns', 'gold crowns', 'ruby']
#items = addToInventory(items, dragonLoot)

displayInventory(items)
