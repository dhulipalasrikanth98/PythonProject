import random
print('Welcome to snake game')
print("*********************")
game_play=input('Do you want to play the game press y for yes and n for no?\n')
user_win=0
bot_win=0
if(game_play=='y'):
    while True:
        l=['s','w','g']
        game_choice=random.choice(l)
        user_choice=input('enter s or w or g')
        if user_choice=='s' and game_choice=='w':
           
            user_win=user_win+1
            print('user won this time')
            print('current statistics','user',user_win,'computer',bot_win)
            c=input('Enter c to continue and x to exit\n')
            if c=='x':
                
                break
            else:
                continue
        elif user_choice=='s' and game_choice=='g':
            bot_win=bot_win+1
            print('computer won this time')
            print('Current statisctics')
            print('User won',user_win,'times','computer won',bot_win,'times')
            c=input('Enter c to continue and x to exit\n')
            if c=='x':
               
                break
            else:
                continue
        else:
            bot_win=bot_win+1
            user_win=user_win+1
            print('user and bot won')
            print(f'current statistics \nuser won-->{user_win},computer won --> {bot_win}')
            c=input('Enter c to continue and x to exit\n')
            if c=='x':
                
                break
                
            else:
                continue
else:
    print('You did played\n Thankyou')
    pass
print(f'Playing statictic is \n user won{user_win} and computer won {bot_win}')
if user_win>bot_win:
    print('User won')
if user_win<bot_win:
    print('Computer won')
if user_win==bot_win:
    print('both won match tied')
print('Thank you for playing play again')



 