# Alex -=ASKIN=- Askinazi 
# askinazialex@gmail.com
# t/z: 346318009
# +972538535530

#Exercise 6 for INT college:


''' Brackets Checker (with using of Stack) ''' # 19/06/2022



dict_skobok = {'(':')',  # Dictionary of Brackets:  key = opening : value = closing
               '[':']',
               '{':'}',
               '<':'>'
               }

for i in dict_skobok:
    print(i, ':', dict_skobok[i] )


    
checker_run_flag = True # Flag for running of Main Function is On 


def BracketsChecker(): # Main Function of Check
    global checker_run_flag
    print('\n')
    
    someStr = input('Insert String for Check-> ')

    if someStr == "0":     # For exit from Bracket-Checker 
        print('Exit from Bracket-Checker...')
        print('\nThanks for using!')
        checker_run_flag = False # Flag for running of Main Function is Offed
        return 

    print('\nYour String for Check:')

#someStr = ']()(){<>}[[()]]'  # String for Checking

    print(someStr)

    someStr_status_flag = True # True - Correct, False - Not correct
    brackets_flag = False
    
    check_stack = [] # Checking Stack
    print()





#------Scanning and checking a string by the cycle----------
    
    res = 'var not in dict' # for print comments - is Offed
    
    stop = 0 # var for stopping cycle

    for i in someStr:    # First level of  cycle

        for j in dict_skobok: # Second level of  cycle
            if i == j:
                brackets_flag = True
                res =  f'i = key "{j}"'
                #print(res)
                check_stack.append(i)

     
            elif i == dict_skobok[j]:
                brackets_flag = True
                res = f'i = value "{dict_skobok[j]}"'
                #print(res)
                if len(check_stack) == 0:
                    print(f'Close bracket "{i}" is wrong!')
                    someStr_status_flag = False
                    stop = 1
                    break
                    
                print('Last item and i:', check_stack[-1], i )
                #print('A : B')

                #print(j, dict_skobok[j])


                if check_stack[-1] == j:
                    print('Okey!!!')
                    print('May to continue...')
                    check_stack.pop()
                else:
                    print('NO!')
                    print('Last item in Checker Stack is another!')
                    print(f'"{i}" is wrong bracket!')
                    someStr_status_flag = False
                    stop = 1
                    break

        if stop == 0:
             None
        elif stop == 1:
            break

#======End of the Chacking cycle=============
 


    if brackets_flag == False:
        someStr_status_flag = None
        

    print()

    if someStr_status_flag == True:
        if len(check_stack) > 0:
            print('\nWrong with nums of brackets!')
            print('(Opens > Closes)')
            someStr_status_flag = False
            print('String is Not correct!')
        else:
            print('String is Correct!')
            

    elif someStr_status_flag == False:
        print('String is Not correct!')
        
    elif someStr_status_flag == None:
        print('String has no brackets!')
        
    else:
        print('Somesthing else...?')





while checker_run_flag == True:
    BracketsChecker()



