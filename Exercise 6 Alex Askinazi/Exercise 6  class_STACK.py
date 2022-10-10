# Alex -=ASKIN=- Askinazi 
# askinazialex@gmail.com
# t/z: 346318009
# +972538535530

#Exercise 6 for INT college

'''Stack implementation by the List's method:'''  # 16/06/2022

class _Stack():
    
    stack_num = 0
    
    def __init__(self, * items):
        _Stack.stack_num += 1
        self.name = _Stack.stack_num
        print()
        print(f'  --== init object Stack #{self.name} of class Stack() ==--\n')
        
        self.items = items
        self.stack = []

        #print(items)
        #print(type(items))

        for i in range(len(items)):
            #print(items[i])
            self.stack.append(items[i])
    
        print(f'Stack #{self.name} =', self.stack)
        print('_________________________________________\n')
        

    def clear(self): # Clear all Stack's items one by one from end
        if bool(self.stack) == False:
            print('\nHey, this Stack is already Empty!')
            return
        else:
            while self.stack:
                self.pop()
        
    def push(self, item):
        self.stack.append(item) # add item to end
        print(f'Stack #{self.name} =', self.stack)

            
    def pop(self):

        if bool(self.stack) == False:
            print('\nHey, this Stack is already Empty!')
            return
        
        self.poped_item = self.stack.pop() # delete and return last item
        print('poped_item =', self.poped_item)

        print(f'Stack #{self.name} =', self.stack)


    def size(self): # show size of Stack
        
        if bool(self.stack) == False:
            #print('\nHey, this Stack is already Empty!')
            print('Hey, this Stack is already Empty!')
            return len(self.stack)
        else:
            #print(len(self.stack)) # show size of Stack
            return len(self.stack)

    def top(self): # show the Top (Last) item of Stack
        if bool(self.stack) == False:
            print()
            print('Hey, this Stack is already Empty!')
            return 

        print('The Top item is:', self.stack[len(self.stack)-1])

        return self.stack[len(self.stack)-1]


    def what(self):
        if bool(self.stack) == False:
            #print('\nHey, this Stack is Empty!')
            return
        len_item = str(self.stack[-1])
        print('Nums of symbols of Top item:', len(len_item))
        


    def born(self):        
        Stack4  = _Stack(1,'abe',0.5)
        Stack5  = _Stack(1,'abe',0.5)





Stack1 = _Stack('No!', "Gett'off!", 288)
Stack2 = _Stack(44,'adc', 0.532, 'HGF', True, 'Caravan')
Stack3 = _Stack('')

Stack4 = _Stack(24, 0.5, 'abc', False)
Stack5 = _Stack(24, 0.5, 'abc', False)

newStack = ['List of Stacks:', Stack1, Stack2, Stack3, Stack4, Stack5 ]


#newStack = ['List of Stacks:', Stack1, Stack2, Stack3]
 

run_flag = True


print(_Stack)


Stack = Stack1

num = 1



#Stack5 = Stack(1,'abe',0.5)

def manage_menu():
    global Stack, num, newStack, Matching_flag, run_flag

    print(f'\n\nIn work: Stack #{Stack.name}')

    print('\n0 - Choose Stack #1,2,3...\n')
    
    print('1 - Push to Stack some string, integer or  float or bool-value')
    print('2 - Pop the Last item from Stack')
    print('3 - How much syms in Last item of Stack')
    print('4 - Show the Top item')
    
    print('5 - Stack Matching Comparison A<?>B  (Targil 2)')

    print('6 - Create New Empty Stack')
    print('7 - Show the List of Stack')
    print('8 - Length of Stack')
    
    print('9 - Clear Steak')    

    print('10 - Exit\n') 
    
    
    manage = input('Manage menu -> ')
    
    if manage == '1':
        print('self.stack.append(item)')
        item = input('item->')
        try:
            try:
                item = int(item)
            except:
                item = float(item)               
        except:
            if item == 'False':
                item = False
            elif item == 'True':
                item = True
            elif item == 'None':
                item = None               
            else:
                item = str(item)            
        Stack.push(item)
            

    elif manage == '2':
        print('self.stack.pop()')
        Stack.pop()
       
        #print('out:',Stack.poped_item)


    elif manage == '3':
        Stack.top()
        Stack.what()

    elif manage == '4':
        Stack.top()

    elif manage == '5':

        
        
        print('Stack Matching Comparison A<?>B')
        print('From List of Stacks:')


        Num_stack_A = input('Choose Stack A -> ')
        try:
            Num_stack_A = int(Num_stack_A)
            print(newStack[Num_stack_A].stack )       
        except:
            print('\nNumber for Stack A not finded!')   
            return 
            
        Num_stack_B = input('Choose Stack B -> ')
        try:
            Num_stack_B = int(Num_stack_B)        
            print(newStack[Num_stack_B].stack ) 
        except:
            print('\nNumber for Stack B not finded!')   
            return
        
        

#----------Creating two Independent Stacks:-------------------------------
        
        # 1
        Stack_A = _Stack()
        
        for i in range(len(newStack[Num_stack_A].stack)):
            Stack_A.stack.append(newStack[Num_stack_A].stack[i])
      
        Stack_A.name = 'A'
                

        # 2
        Stack_B = _Stack()
        
        for i in range(len(newStack[Num_stack_B].stack)):
            Stack_B.stack.append(newStack[Num_stack_B].stack[i])
            
        Stack_B.name = 'B'        


        _Stack.stack_num = (len(newStack)-1) # For right continuous numbering of 'List of Stacks'



        #  Checking Area    

        Matching_flag = True


        if Stack_A.size() == 0 and Stack_B.size() == 0:
            print()
            print('Stack A and Stack B are Empty!')
            Matching_flag = None
            return  
        
        if Stack_A.size() != Stack_B.size():

            print('Stack A:', Stack_A.stack)
            print('Stack B:', Stack_B.stack)
            print()
            print('Length Stack A:', Stack_A.size())
            print('Length Stack B:', Stack_B.size())
            print()
            print('Stacks AB: Different!')
            Matching_flag = False


        if Matching_flag == True:

            while Stack_A.size() > 0 or Stack_B.size() > 0:
                print()
                print('Stack A:', Stack_A.stack)
                print('Stack B:', Stack_B.stack)
                print('Stacks AB Tops:')
                print('Stack A. ', end = '')
                StackA_top = Stack_A.top()
                print('Stack B. ', end = '')                
                StackB_top = Stack_B.top()

                if StackA_top == StackB_top:
                    print('Tops: Matching!')
                    Stack_A.pop()
                    Stack_B.pop()
                    if Stack_A.size() == 0 and Stack_B.size() == 0:
                        print('Stack A:', Stack_A.stack)
                        print('Stack B:', Stack_B.stack)
                        print('Stacks AB: Matching!')    
                else:
                    print('Tops: Not Matching!')
                    print('Stacks AB: Different!')
                    Matching_flag == False
                    break

        print()
        print('Stacks AB Matching:', Matching_flag)
#------------------------------------------------------------------------
       

        '''==========================|  WARNING!  |============================='''
        '''======================! CODE TESTING AREA !=========================='''
        '''====================================================================='''
        
        #print('\n'*3)
        
        #print('Old:')        
        #print('old Stack A:',newStack[Num_stack_A].stack)
        #print('old Stack B:',newStack[Num_stack_B].stack)
        #print()
        #print('twins')
        #print('Dublicate Stack A:', Stack_A.stack)
        #print('Dublicate Stack B:', Stack_B.stack)
        #print()
        #print()


        #if Stack_A.size() == Stack_B.size():
            #print('\n -Size:  "Ok"   A == B  ECVAAAAAAAAAAAAAAAAAAAL!!!!!!!!!!!\n')
            #print('Continue...' )           
        #else:
            #print('\n -Size: "NOT!"  A != B  NOOOOOOOOOOOOOOOOOOOOOOT ECVAL! \n')
            #print('Exit from Stack Matching')

            #Matching_flag = False
            
            #return Matching_flag

    
        #if Stack_A.top() == Stack_B.top():
            #print('ECVAAAAAAAAAAAAAAAAAAAL!!!!!!!!!!!')

        
        #print('pop A & B')
        #Stack_A.pop()
        #Stack_B.pop()
        #print()
        #print()

        
        #print('twins:')
        #print('Dublicate Stack A:', Stack_A.stack)
        #print('Dublicate Stack B:', Stack_B.stack)
        #print()
        #print('Old:')
        #print('old Stack A:',newStack[Num_stack_A].stack )
        #print('old Stack B:',newStack[Num_stack_B].stack )        

        
        #print('\n'*5)

        ''' it works!! '''
        
        '''====================================================================='''
        '''====================|  END OF TESTING AREA  |========================'''
        '''====================================================================='''



        
    elif manage == '12':
        try:
            print('Service function:')
            print('Matching_flag =', Matching_flag)
        except:
            print('status: dismissed ')
        
    elif manage == '11':
        print('Service function:')
        print('Determination of compliance')

        Stack4  = _Stack(1,'abc',0.5)#!
        Stack5  = _Stack(1,'abe',0.5)#!
        
        print(Stack4.stack) #!
        print(Stack5.stack) #!

        
        #------------------------------------
        a = Stack4.top()#!
        b = Stack5.top()#!

        if a == b:
            print('  Верхние элементы РАВНЫ')
        else:
            print('  Верхние элементы НЕ РАВНЫ')
            print('  Cтеки HE идентичны! - XXX')
            return
        
        Stack4.pop()
        Stack5.pop()


        #------------------------------------
        a = Stack4.top()
        b = Stack5.top()

        if a == b:
            print('Верхние элементы РАВНЫ')
        else:
            print('  Верхние элементы НЕ РАВНЫ')
            print('  Cтеки HE идентичны! - XXX')
            return
        Stack4.pop()
        Stack5.pop()


        #------------------------------------
        a = Stack4.top()
        b = Stack5.top()

        if a == b:
            print('Верхние элементы РАВНЫ')
        else:
            print('  Верхние элементы НЕ РАВНЫ')
            print('  Cтеки HE идентичны! - XXX')
            return
        Stack4.pop()
        Stack5.pop()        

            
        #------------------------------------
        len_a = Stack4.size()
        len_b = Stack5.size()

        if len_a == 0 and len_b == 0:
            print() 
            print('  Cтеки идентичны! - VVV')
        else:
            print()
            print('  Cтеки HE идентичны! - XXX')


    elif manage == '6':
        print('Create New Empty Stack:')


        newStack.append(_Stack())

    elif manage == '7':
        print(newStack[0])
        for i in range(1,(len(newStack))):
            print(f' {i}: {newStack[i].stack}') 


    elif manage == '8':
        
        print(f'\nLength of Stack #{Stack.name} =', Stack.size())
        

    elif manage == '9':
        print(f'Clear Stack #{Stack.name}:')
        Stack.clear()

        
    elif manage == '0':
        print('1 - Stack #1')
        print('2 - Stack #2')
        print('3 - Stack #3')

        choice = input('Choose Number of Stack -> ')
        if choice == '0':
            print('<<<exit from Choice Stack submenu')
            return
        try:
            num = int(choice)
                
            Stack = newStack[num]
                
        except:    
            print('\nNot found!')
            return
        
        print(f'\nStack #{choice}:', Stack.stack)   


    elif manage == '10':
        run_flag = False
        print('Thanks for using!')
        print('''
                           ______
        |\_______________ (_____\\______________
HH======#H###############H#######################
        ' ~""""""""""""""`##(_))#H\"  ""Y##########
                         )))    \#H\      `"Y#####
                         )))     }#H)
                        )))
                         "
''')
        

        c = input()
        
while run_flag == True:
    manage_menu()







