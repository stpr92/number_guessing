import random
mini=1
maxi=100
guessed_number=random.randint(mini,maxi)
print(guessed_number)
human=''
while human!='Bingo!' :
    human=input()
    if human=='larger' :
        mini=guessed_number
        guessed_number=random.randint(mini,maxi)
        print(guessed_number)
    elif human=='smaller' :
        maxi=guessed_number
        guessed_number=random.randint(mini,maxi)
        print(guessed_number) 
print('Finally I got it!!')        
         
        





