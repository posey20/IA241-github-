'''
lab5
'''

#3.1
alien_color = 'red'

if alien_color == 'green':
   print('the player just earned 5 points')
   
#3.2
if alien_color == 'green':
   print('the player just earned 5 points')

else:
   print('that the player just earned 10 points')
   
#3.3
favorite_fruits = ['apple','banana','grapes']

if 'banana' in favorite_fruits:
   print('You really like bananas!')
   
if 'mango' in favorite_fruits:
   print('You really like mangos!')
   
if 'orange' in favorite_fruits:
   print('You really like oranges!')
   
#3.4
age = 50

if age < 10: 
   print('kid')

elif age >= 10 and age < 20: 
   print('teenager') 

else:
   print('adult')

   if age >= 65:
      print('elder') 

