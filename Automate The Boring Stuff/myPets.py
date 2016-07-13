myPets =  ['Zeek', 'Kai']
print('Enter a pet name:')
name = input()
if name not in myPets:
    print('I do not have a pet name ' + name)
else:
    print(name + ' is my pet.')
