# Alex -=ASKIN=- Askinazi 
# askinazialex@gmail.com
# ID: 346318009
# +972538535530

#Exercise _ for INT college

# ( Part A )


''' Linked List CSV-EDITOR ''' # for  CSV-files # July 2022

'''
1. Add Item to End
2. Add Item to Head
3. Delete Item
4. Count Items
5. Print Items 
6. Find Item (Searching)
7. Save Items to txt-file
8. Delete First (Head) Item
9. Delete Last Item

'''


class Node:
    print('init Node')
    def __init__(self, data, next = None):
        print(f'Was born "{data}"\n')
        self.data = data
        self.next = next
           


class _CSVEditor():
    print('init class _CSVEditor')

    def __init__(self):
        print('Creating Object "CSVEditor"')
        
        self.head = None

        
    def AddEND(self,value):
        print('Add Item to End:', value)

        newItem = Node(value)
        
        if self.head is None:
            self.head = newItem
            return
        
        lastItem = self.head
        
        while (lastItem.next):
            lastItem = lastItem.next
            
        lastItem.next = newItem
        

        
    def AddHEAD(self, value):
        print('Add Item to HEAD')

        
        #newItem = Node(value)
        new_node = Node(value)

        
        #new_node.ref = self.start_node
        new_node.next = self.head


        #self.start_node= new_node
        self.head = new_node

        
    def del_1(self):
        
        if self.head == None:
            print('The list has no element to delete')
            return
        
        self.head = self.head.next
        self.Print()

        
    def del_last(self):
                
        if self.head is None:
            print('The list has no element to delete')
            return     

        count = 0
        current = self.head
        
        while current is not None:
            count += 1
            current = current.next
            
        if count == 1:
           #print('Attention!!')
            current = self.head              
            i = 0

            while current is not None:
                #print (f'[{i}]', f'{i+1}.' , current.data)
                i += 1                
                delete = current.data  
                self.Delete(delete)                
                return
        
        n = self.head       

        
        while n.next.next is not None:
            n = n.next
        n.next = None
        
        self.Print()        

        pass


        
    def Delete(self, delete):

        if self.head == None:
            print('The list has no element to delete')
            return
        
        if self.head.data == delete:
            print(f'Deleted Item: <{delete}>')
            self.head = self.head.next
            self.Print()
            return

    
        headcat = self.head
        
        if headcat is not None:
            if headcat.data == delete:
                self.head = head.next
                headcat = None
                return
                
        while headcat is not None:
            if headcat.data == delete:
                break

            lastcat = headcat
            headcat = headcat.next

            
        if headcat == None:
            print('Not found!')
            return

        
        lastcat.next = headcat.next
        headcat = None            

        self.Print()
        


    def Count(self):
        print('Count Items')

        count = 0
        current = self.head 
        while current is not None:
            count += 1
            current = current.next
        print('Summ of Items is:', count)


    def Print(self):
        print('Print "LINKED LIST" Items:')
        print("-----")
        
        current = self.head  
        
        i = 0

        while current is not None:
            print (f'[{i}]', f'{i+1}.' , current.data)
            i += 1
            current = current.next
            
        print("-----")

   
    def Find(self, search):
        print(f'Search Item: <{search}>')
        i = 0
        lastItem = self.head
        
        while (lastItem):
            if search == lastItem.data:
                print(f'\nGott him!-> [{i}] {i+1}.', lastItem.data)
                return True
            else:
                lastItem = lastItem.next
                i += 1
        return False



    def Save(self):
        
        
        with open("CSVEditor.csv", "w") as file:
            pass
        
        with open("CSVEditor-txt.txt", "w") as file:
            pass


        lastItem = self.head

        while (lastItem):  
            with open("CSVEditor-txt.txt", "a") as file:
                file.write(str(lastItem.data) + '\n')
            lastItem = lastItem.next
            
        while (lastItem):           
            with open("CSVEditor.csv", "a") as file:
                file.write(str(lastItem.data) + '\n')
            lastItem = lastItem.next

        print('Saved to CSV-file')         
        print('Saved to TXT-file') 
        
    def Exit(self):
        global run_flag
        print('Exit')
        run_flag = False

    

    def Menu(self):
        
        select = input('\nSelect-> ')

        if select == '1':
            value = input('Input value -> ')
            CSVEditor.AddEND(value)
            pass
        
        if select == '2':
            value = input('Input value -> ')
            CSVEditor.AddHEAD(value)
            pass
        
        if select == '3':
            delete = input('Delete -> ')
            CSVEditor.Delete(delete)        
            pass
        
        if select == '4':
            CSVEditor.Count()          
            pass
        
        if select == '5':
            CSVEditor.Print()
            pass
    
        if select == '6':
            search = input('Search -> ')
            CSVEditor.Find(search)        
            pass

        if select == '7':
            CSVEditor.Save()        
            pass

        if select == '8':
            CSVEditor.del_1()        
            pass
        
        if select == '9':
            CSVEditor.del_last()        
            pass

        
        if select == '0':
            CSVEditor.Exit()
            pass




    
CSVEditor = _CSVEditor()

names = 'Jack','Bob','Piter','Samantha','Megan'


#print(names[0])
#print(type(names))


for i in names:
    CSVEditor.AddEND(i)



#        Run Function       |

print('''
1. Add Item to End
2. Add Item to Head
3. Delete Item
4. Count Items
5. Print Items 
6. Find Item (Searching)
7. Save Items to txt-file
8. Delete First (Head) Item
9. Delete Last Item
''')

run_flag = True

while run_flag == True:
    CSVEditor.Menu()
#                           |



print('\n\nOut App Area\n\n')








