# Alex -=ASKIN=- Askinazi
# askinazialex@gmail.com
# t/z: 346318009'
# +972538535530

#Exercise "Python Tkinter GUI
# Released: 09.08.2022


#    MODULES:   |
from tkinter import *
from tkinter import messagebox

import csv

csv_file = 'myCSV.csv'

#   for sha256 encoding password:  |
import hashlib

#password = 'vitalythebest'
#result = hashlib.sha256(password.encode())
#print(result.hexdigest())


#        functions:         |


def Message():
    mes_text = 'Hello, ' + e1.get() + ' ' + e2.get() + '!'
    
    if checkboxVar1.get() == 1:
        messagebox.showinfo('MessageBOX',mes_text.upper())
    else:
        messagebox.showinfo('MessageBOX',mes_text) 


def NewFile():
    print('New File')
    messagebox.showinfo("App", "New File")


def OpenFile():
    print('Open File')
    messagebox.showinfo("App", "Open File")

    
def Exit():
    print('Exit <Yes/No>')
    
    response = messagebox.askyesno("Exit", "Sure for Exit from App?")
    
    if response == True:
        exit()
    else:
        pass


def About():
    messagebox.showinfo("App", "This App made by Alex Askin")


def SaveCSV():
    global user_data_valid_flag
    global user_inputs
    global missed_data


    user_data_valid_flag = True

    user_gender = ''

    if r.get() == 1:
        user_gender = 'Men'
    elif r.get() == 2:
        user_gender = 'Women'
    

    user_inputs =[
        [e1.get(),"Name"],
        [e2.get(),"Last Name"],
        [e3.get(),"@mail"],
        [user_gender,"Gender"],
        [e5.get(),"Login"],
        [e6.get(),"Password"]
    ]
    
    missed_data = ''
    
    print()
    
    for i in range(len(user_inputs)):     
        if user_inputs[i][0] == '':
            print(f"Enter your {user_inputs[i][1]}")
            missed_data += f"Enter your {user_inputs[i][1]}\n"
            user_data_valid_flag = False
        
    
    if user_data_valid_flag == False:
        return
    else:
        print('Save to ' + csv_file)


    password = e6.get()
    result = hashlib.sha256(password.encode())
    #result.hexdigest()
    
    with open(csv_file,'a') as fd_csv:
        csv_writer = csv.writer(fd_csv, delimiter=",", lineterminator="\n")
        csv_writer.writerow([e1.get(),e2.get(),e3.get(),user_gender,e5.get(),result.hexdigest()])


def ReadCSV():

    with open(csv_file,'r') as fd_csv:
        csv_reader = csv.reader(fd_csv, delimiter=",")

        #next(csv_reader) # skip the first line

        for line in csv_reader:
            print(line)


def ReadLastStringCSV():
    with open(csv_file,'r') as fd_csv:
        csv_reader = csv.reader(fd_csv, delimiter=",")
        csv_reader_list = []
        for line in csv_reader:
            csv_reader_list.append(line)   
        print(csv_reader_list[-1])


def ShowName():
    print(e1.get(),e2.get())
    lebel2=Label(root,text = ' '*64+'\n', font=('Segoe UI',16),fg='#50E3C2')
    lebel2.configure(bg='#271F3D')
    lebel2.grid(row=2,column=1)
    
    lebel2=Label(root,text = f'{e1.get()} {e2.get()}\n', font=('Segoe UI',16),fg='#50E3C2')
    lebel2.configure(bg='#271F3D')
    lebel2.grid(row=2,column=1)


def Register():
    SaveCSV()    # SAVE USER DATA TO CSV-FILE
    
    if user_data_valid_flag == True:
        ReadLastStringCSV()
        messagebox.showinfo('App','Registration completed!')
        top.destroy()
    else:
        messagebox.showinfo('App','Please, input your data:\n' + missed_data)

        

def Reg():
    global top
    global e1,e2,e3,e5,e6, r
    global checkboxVar1

    top = Toplevel()
    
    l1=Label(top,text = 'First Name: ')
    l2=Label(top,text = 'Last Name: ')
    l3=Label(top,text = '@mail: ')
    l4=Label(top,text = 'Sex: ')
    l5=Label(top,text = 'Login: ')
    l6=Label(top,text = 'Password: ')

    l1.grid(row=1,column=0,columnspan=3)
    l2.grid(row=2,column=0,columnspan=3)
    l3.grid(row=3,column=0,columnspan=3)
    l4.grid(row=4,column=0,columnspan=3)
    l5.grid(row=5,column=0,columnspan=3)
    l6.grid(row=6,column=0,columnspan=3)

    #    Entry Bars:
    e1 = Entry(top)
    e2 = Entry(top)
    e3 = Entry(top)
    #e4 = Entry(top)
    e5 = Entry(top)
    e6 = Entry(top)

    e1.grid(row=1,column=3)
    e2.grid(row=2,column=3)
    e3.grid(row=3,column=3)
    #e4.grid(row=4,column=3)
    e5.grid(row=5,column=3)
    e6.grid(row=6,column=3)


    #    RadioButtons:  |

    r = IntVar()
    
    rb1 = Radiobutton(top, text="Male", variable=r, value=1)
    rb1.grid(row=4,column=3)
    
    rb1 = Radiobutton(top, text="Female", variable=r, value=2)
    rb1.grid(row=4,column=4)
    

    #      Buttons:     |
    button1 = Button(top, text='    Ok    ', font=('Segoe UI',14, "bold"),fg='#FFFFFF', command=Register)
    button1.configure(bg='#1DCE0D')
    button1.grid(row=7, column=1)

    #      Extended Buttons:     |
    button1 = Button(top, text='Show Message', command=Message)
    button1.configure(bg='#1CC9FE')
    button1.grid(row=9, column=0)

    button2 = Button(top, text='Save CSV', command=SaveCSV)
    button2.configure(bg='#1CC9FE')
    button2.grid(row=9, column=1)

    button3 = Button(top, text='Read CSV', command=ReadCSV)
    button3.configure(bg='#1CC9FE')
    button3.grid(row=9, column=2)

    button4 = Button(top, text='Show Name', command=ShowName)
    button4.configure(bg='#1CC9FE')
    button4.grid(row=9, column=3)


    # Checkbutton  |
    checkboxVar1 = IntVar()
    checkbox1 = Checkbutton(top,text='Var1/Var2',variable=checkboxVar1,onvalue=1,offvalue=0)
    checkbox1.grid(row=10,column=0)


def LoginIn():
    global top1
    global e_login, e_password
    
    print('Login in')

    top1 = Toplevel()
    
    l1=Label(top1,text = 'Login ')
    l2=Label(top1,text = 'Password ')
 
    l1.grid(row=1,column=0,columnspan=3)
    l2.grid(row=2,column=0,columnspan=3)
 
    e_login = Entry(top1)
    e_password = Entry(top1,show="*")
    
    e_login.grid(row=1,column=3)
    e_password.grid(row=2,column=3)

    #      Buttons:     |
    button1 = Button(top1, text='  Ok  ',font=('Segoe UI',12), command=CheckLogin)
    button1.configure(bg='#ACC9AE')
    button1.grid(row=7, column=1)    
 
    
def CheckLogin(): 
    if e_login.get() == '' and e_password.get() == '':
        messagebox.showinfo('App','Please, input your Login and Password!')
        return
    
    print(f'Check Login "{e_login.get()}"')
    if e_login.get() == '':
        messagebox.showinfo('App','Please, input your Login!')
        return

    print(f'Check Password "{e_password.get()}"')
    if e_password.get() == '':
        messagebox.showinfo('App','Please, input your Password!')
        return


    result = 0 # Result of searching!
    
    password = e_password.get()
    hexpassword = hashlib.sha256(password.encode())
    #hexpassword.hexdigest()

    with open(csv_file,'r') as fd_csv:
        csv_reader = csv.reader(fd_csv, delimiter=",")
        
        for line in csv_reader:
            if e_login.get() == line[4] and hexpassword.hexdigest() == line[5]:
                result += 1
                print('Login found! +1')
                break

 
    print(result)
    if result == 0:
        print('Login or Password NOT Found!')
        messagebox.showinfo('App','Login or Password NOT Found!')
        return
    elif result == 1:
        print('Wellcome!')
        messagebox.showinfo('Wellcome!',f'Wellcome back {e_login.get()}!')


        l1=Label(root,text = '            364 Studio            \nWellcome,', font=('Segoe UI',18),fg='#50E3C2')
        l1.grid(row=1,column=1)
        l1.configure(bg='#271F3D')


        lebel2=Label(root,text = ' '*64+'\n', font=('Segoe UI',16),fg='#50E3C2')
        lebel2.configure(bg='#271F3D')
        lebel2.grid(row=2,column=1)
        
        lebel2=Label(root,text = f'{e_login.get()}!\n', font=('Segoe UI',16),fg='#50E3C2')
        lebel2.configure(bg='#271F3D')
        lebel2.grid(row=2,column=1)

        
        result = 0
        top1.destroy()


def ColorTheme():
    global color,user_color_choice
    print('Color Theme Choice')

    top2 = Toplevel()
    top2 .title('Colour Theme Menu')
    top2.geometry('220x150+300+300')
    #top2.configure(bg='#271F3D')
    #   Drop Menu:    |
    
    user_color_choice = StringVar()
    
    label_drop = Label(top2,text="Color:")
    label_drop.grid(row=0,column=0)
    
    drop = OptionMenu(top2, user_color_choice,'Red','Blue','Green')
    drop.grid(row=0,column=3,columnspan=1)

    
    #      Buttons:     |
    button1 = Button(top2, text=' Show ',font=('Segoe UI',12), command=ShowColor)
    button1.configure(bg='#ACC9AE')
    button1.grid(row=3, column=1)
    

def ShowColor():
    print(f'Show Color: {user_color_choice.get()}')
    
    topColor = Toplevel()
    topColor.title('Show Choiced Colour')
    topColor.geometry('250x250+350+450')
    if user_color_choice.get() == 'Green':
        topColor.configure(bg='green')
    elif user_color_choice.get() == 'Red':
        topColor.configure(bg='red')
    elif user_color_choice.get() == 'Blue':
        topColor.configure(bg='blue')        
    

#         App Tkinter configure!     :

root = Tk()

checkboxVar1 = IntVar()

#  Main Window configure |
root.title('-=App=- for INT Python course')
root.geometry('690x270+600+300')
root.configure(bg='#271F3D')

#   Context Menu:    |
menu = Menu(root)
root.config(menu=menu)

file_menu = Menu(menu)
menu.add_cascade(label='File',menu=file_menu)
file_menu.add_command(label='File',command=NewFile)
file_menu.add_command(label='Open',command=OpenFile)
file_menu.add_command(label='Exit',command=Exit)

help_menu = Menu(menu)
menu.add_cascade(label='Help',menu=help_menu)
help_menu.add_command(label='About',command=About)


#   Labels     |
l1=Label(root,text = '            364 Studio            \n', font=('Segoe UI',18),fg='#50E3C2')
lebel2=Label(root,text = 'REGISTER or LOGIN\n', font=('Segoe UI',16),fg='#50E3C2')


l1.grid(row=1,column=1)
lebel2.grid(row=2,column=1)

l3=Label(root,text = ('    '*12), font=('Segoe UI',20))
l3.grid(row=3,column=1)

l1.configure(bg='#271F3D')
lebel2.configure(bg='#271F3D')
l3.configure(bg='#271F3D')

#      Buttons:     |
button5 = Button(root, text=' REGISTER ',font=('Segoe UI',14),fg='#271F3D', command=Reg)
button5.configure(bg='#50E3C2')
button5.grid(row=3, column=0)

button6 = Button(root, text='   LOGIN   ', font=('Segoe UI',14),fg='#271F3D', command=LoginIn)
button6.configure(bg='#50E3C2')
button6.grid(row=3, column=3)

button7 = Button(root, text='Color Theme', font=('Segoe UI',10),fg='#50E3C2',command=ColorTheme)
button7.configure(bg='#271F3D')

button7.grid(row=0,column=0)


#     run app     |
root.mainloop()





