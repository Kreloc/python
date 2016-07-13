#! python3
# generateRandomPassword - Genereates a random password, displays it
# and copies it to the clipboard.

#import random, pyperclip

import random, string, pyperclip

#Set password length
length = 7

#Character list
chars = string.ascii_letters + string.digits

#Randomize character list and set password

password = ''.join(random.choice(chars) for i in range((length + 1)))
password = password + '!'
    

print('The following password was copied to the clipboard:')
print(password)
#Copy password to clipboard
pyperclip.copy(password)
