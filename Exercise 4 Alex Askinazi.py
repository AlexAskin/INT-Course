# Alex -=ASKIN=- Askinazi 
# askinazialex@gmail.com
# t/z: 346318009
# +972538535530
#Exercise 4 for INT college
# (Random range) 


# Exercise 4:

# Targil 1:
print('\nTargil 1:')
print('"Sum of the Random List"')

import random as rd




#c = rd.randint(0,10)
#print('Random num:',c)


def sum_randomList(num_min, num_max, num_length):
    num_list = []
    print('Length of the Random List:', num_length)    
    print('Min value:', num_min)
    print('Max value:', num_max)
    
    for  i in range(num_length):
        rand_num = rd.randint(num_min,num_max)
        num_list.append(rand_num)
        
    num_list.sort()
    print('Random List = ', end = '')
    print(num_list)
    
    return(sum(num_list))

def call_randomList():
    
    num_min = int(input('\nPlease, set the Minimum value of the Random List-> '))
    num_max = int(input('Please, set the Maximum value of the Random List-> '))
    num_length =int(input('Please, set the Length (2..n) of the Random List-> '))
    
    print('Sum of the Random List:',sum_randomList(num_min, num_max, num_length)) # Calling Sum function 
    print('\n<Repeat> - press Enter or random key\n <Exit>  - press 0') # Repeat or Exit 
    res = input()
    if res == '0':
        print('Exit from "Random List"...\n')
    else:
        call_randomList()

        
call_randomList() # Start function of Targil 1
#________________


#=========================================

 
# Targil 2:
print('\nTargil 2:')
print('"Guess Number"\n')
attempts = 0 # number of attempts
def startGuessNumber():
    global attempts
    global some_num
    print('So... I get some X-number from 1 to 100')
    some_num = rd.randint(1,100)

    #print(f'({some_num})')


    attempts = 0 # number of attempts
    attempt()


def attempt():
    global attempts
    attempts += 1
    print('\nAttempt #', attempts)
    print('Try to guess this Number-> ', end = '')
    guess_num = input()
    guess_num = int(guess_num)

    if guess_num == some_num:
        print(f'\nEeeaah! You WIN! it was {some_num}!')
        print('Sum of attempts:', attempts)

        print('\n<Repeat> - press Enter or random key\n <Exit>  - press 0')
        res = input()
        if res == '0':
            print('Exit from "Guess Number"...\n')
            print('See you on the next lesson!')
        else:
            print()
            startGuessNumber()
      
    elif guess_num > some_num:
        print(f'Your guess number {guess_num} is MORE than X-number!')
        attempt()
        
    elif guess_num < some_num:
        print(f'Your guess number {guess_num} is LESS than X-number!')
        attempt()


startGuessNumber() # Start function of Targil 2
#_________________


