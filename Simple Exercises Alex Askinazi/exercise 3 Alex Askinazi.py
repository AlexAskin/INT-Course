# Aleksander Askinazi
# 346318009
# Targil 3 for INT college


import random

#targil 1:
print('\nTargil 1\n')

for i in range(500,1001):
    print(i,end=' | ')

#targil 2:
print('\n\nTargil 2\n')

my_list = []

for i in range(1,11):
    print('Append to List Number:', i)
    my_list.append(i)

print('\nList =',my_list)

print("\nSum of List's Numbers =", sum(my_list))


#targil 3:
print('\n\nTargil 3\n')



def randomList():
    num_list = []
    stopper = 0
    patient_list = []
    for i in range(1,17):
        num = random.randint(372,410)
        num /= 10
        round(num, 1)
                
        num_list.append(num)
        temp_value = (f'Patient #{i} temperature: {num}°C')
        patient_list.append(temp_value)

    mort = random.randint(0, (len(patient_list)-1))
    num_list[mort] = -4
    patient_list[mort] = f'Patient #{mort+1} temperature:   -4°C'
    #for t in range(len(num_list)):    
        #print(num_list[t])          
    for j in range(len(patient_list)):    
        print(patient_list[j])

        
    #print('\nList of Patient\'s =', num_list)
    summ_t = sum(num_list)
    print("\nSum of the List of Patient's temperature =", round(summ_t,1))
    return(num_list)


num_list = randomList()


def listAverage(num_list):
    
    num_list_medivial = sum(num_list)/len(num_list)
    summ_t = sum(num_list)
    summ_t =round(summ_t,1)
    num_list_medivial = round(num_list_medivial,1)
    print(f'\nCalculation of Average Temperature: ({summ_t} / {len(num_list)} = {num_list_medivial})')
    return num_list_medivial

medivial_temp = listAverage(num_list)

print(f'\nThe Average temperature of patients in the hospital = {medivial_temp}°C')

if  medivial_temp < 37.1:
    print('\nAll Patients are healthy!!! \nLet the Patients goes home!')
else:
    print('\nRepeat all measurements!!!\nNow!')



#targil 4:
print('\n\nTargil 4\n')

my_name = 'Alex'

#my_str = ('Hellow', 'my' ,'name', 'is', my_name, 'and', 'I', 'love', 'programming', 'in', 'Python!')
my_str = (f'Hello my name is {my_name} and I love programming in Python!')
print(my_str)
print('\nLength of string:', len(my_str),'\n')

print(my_str[0 : 6] + my_str[26 : 27] + my_str[32 : 55])
print(my_str[17 : 22] + my_str[28 : 33] + my_str[-7 : -1])
print(my_str[43 : 36: -1] + 'a'+ my_str[36 : 33: -1] + my_str[33 : 32: -1].title() + my_str[32 : 27:-1] + 'e' + my_str[21 : 16: -1])

#print('abcd'[0 : 55 : 1])
#ok_str = my_str[0], my_str[8 :11]
#print(my_str[0],my_str[8 :11])
#for i in ok_str:
    #print(i,end='')
#print(ok_str)





#targil 5:
print('\n\nTargil 5\n')



def printCase(some_text, var):
    if var == 0:
        some_text = 'var = 0: ' + some_text
        print(some_text.lower())
    elif var == 1:
        some_text = 'var = 1: ' + some_text
        print(some_text.upper())        
    else:
        some_text = f'var = {var}: ' + some_text
        print(some_text.title())
    return(some_text)


some_text = 'I know that I know nothing!'

print('VAR = 0 - for lower case')
print('VAR = 1 - for UPPER case')
print('VAR = "123/abc" - Title case')

var = input('VAR = ')

try:
    var = int(var)
except:
    var = var
    
printCase(some_text, var)

#printCase(some_text, 0) 




