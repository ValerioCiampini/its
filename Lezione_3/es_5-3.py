#5-3


alien_color:str = input('Choose a color between Yellow, Red, Purple, Cyan and Green: ')
if alien_color == 'Green':
    print(f'You shot down the alien! You just earned 5 points!')
    
elif alien_color == 'Yellow':
        print(f'You destroyed the mother-ship. 10 points!')

elif alien_color == 'Cyan':
    print('You decimated the alien race! 100 points')
        
else:
    print('You missed')