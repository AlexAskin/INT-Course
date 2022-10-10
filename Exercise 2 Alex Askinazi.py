# Alex -=ASKIN=- Askinazi 
# askinazialex@gmail.com
# +972538535530
#Exercise 2 for INT college


print('Exercise 1\n')
# print every EVEN number before 1000.

a = 0

while a < 1000:
    a += 1
    if a % 2 == 0:
        print(a, end =' ')
        
print('\n')


#__________________________________________________________
print('Exercise 2\n')
# 100 : 350:

number = input('Please, input your nubmer->')

try:
    number = int(number)
    print(type(number))
    if number % 2 == 1: print(f'Your numder {number} is ODD')
    elif number % 2 == 0: print(f'Your numder {number} is EVEN')

    if number >= 100 and number <= 350:
        print(f'Your number {number} is in the range of 100 : 350')
    else:
        print(f'Your number {number} is NOT in the range of 100 : 350')
        
except:
    print('Your number is Incorrect. Try again!')


#__________________________________________________________
print('Exercise 3\n')
# Range of Numbers:

number_1 = input('Please, input your nubmer_1->')
number_2 = input('Please, input your nubmer_2->')

try:
    number_1 = int(number_1)
    number_2 = int(number_2)

    if number_1 > number_2:

        delta = number_1 - number_2
        num = number_2+1

        print(f'The Range between {number_1} and {number_2}:')
        while num < number_1:
            print(num)
            num += 1
             
    else:
        delta = number_2 - number_1
        num = number_1+1    
    #print(abs(delta))
        print(f'The Range between {number_1} and {number_2}:')
        while num < number_2:
            print(num)
            num += 1       
     
except:
    print('One of your numbers is Incorrect. Try again!')







