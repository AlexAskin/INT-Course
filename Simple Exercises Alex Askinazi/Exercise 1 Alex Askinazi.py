# Alex -=ASKIN=- Askinazi 
# askinazialex@gmail.com
# +972538535530
#Exercise 1 for INT college
#Simple Even/Odd checker
#Used if/else, % modulus operator 
#type() and try/except block
#Main and def functions
#Created on QPython3, 08/05/22

print('Wellcome to Even/Odd Checker!\n')

def Main():
    global number
    number=input('Please, enter your number:')
  
    checkType()
  
def checkType():
    global number
    try:
      number=int(number)
      print(f'Welldone! Your number {[number]} is valid!')
      response()
    except: 
      print(f'Oops! Your number {[number]} is incorrect!')
      number=input('Pleas, try again:')
      checkType()
  
    
def response():

    result=number%2
    print('\nRemainder:', result,'\n')

    if result == 0:
        print(f'Wooouw! Your number {number} is EVEN!')
    else:
        print(f'Hey,hey! Your number {number} is ODD!')


    print('\nPress Enter or any key to continue...\
    \n(for Exit press [num 1] and Enter)')
    
    cyrcle=input()
    
    if cyrcle == '1': 
        print('Thanks for using and hope to see you soon!') 
    else: Main()
       

Main()
exit()
