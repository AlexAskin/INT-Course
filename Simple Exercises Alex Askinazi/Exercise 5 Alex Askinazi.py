# Alex -=ASKIN=- Askinazi 
# askinazialex@gmail.com
# t/z: 346318009
# +972538535530

#Exercise 5 for INT college
# (Range on Nubmers)
# (Count ASCII symbols)


#targil 1:
# (Range on Nubmers)
print('\nTargil 1\n')



def NumRange():
    try:
        num_in_range = int(input('Please, Enter your Number in Range 0:10,000-> '))
        print(num_in_range)
        if num_in_range in range (0,10001):
            print(f'Your Number {num_in_range} is in Range 0:10,000!')
            print('Welldone!')

            print('\nRepeat - press "1"')
            print(' Exit  - press Enter')
            
            begin = input()
            
            if begin == '1': NumRange()
            else: return
            
        else: 
            print(f'Your Number {num_in_range} is OUT of Range 0:10,000!')
            print('Please, try again! ->')
            NumRange()
    except:
        print('Your Number is INCORRECT!')
        print('Please, try again! ->')
        NumRange()
    
NumRange()





#targil 2:
# (Count ASCII symbols)
print('\nTargil 2\n')


for i in range(32, 128):
    #print(i)
    print(chr(i), end=' ')
    if i % 10 == 0:
        print()

print('\n')


def String_count():
    num = 0
    let = 0

    let_up = 0
    let_low = 0

    sym = 0
    out = 0

    str_tumle = tuple(input('Please, type your String-> '))

    b = range(0,32) # Unprintable Character
    c = range(32,48) # Symbol
    a = range(48,58) # Numbers
    d = range(58,65) # Symbol
    g = range(65,91) # Upper Letter
    e = range(91,97) # Symbol
    h = range(97,123) # Lower Letter
    f = range(123,127) # Symbol

    for j in str_tumle:
        #print(j,'=', ord(j))
        if ord(j) in a:
            print(j,'is Number')
            num += 1
            
        elif ord(j) in b:
            print(j,'is Unprintable Character')
            sym += 1
            
        elif ord(j) in c or ord(j) in d or ord(j) in e or ord(j) in f:
            print(j,'is Symbol')
            sym += 1  
            
        elif ord(j) in g:
            print(j,'is Upper Letter')
            let += 1
            let_up += 1
            
        elif ord(j) in h:
            print(j,'is Lower Letter')
            let += 1
            let_low += 1
        else:
            print(j,'is out of U.S. ASCII')
            out += 1
     
    print('\nNumbers:', num)
    print('Letters:', let)
    print(f'(Upper Letters: {let_up})')
    print(f'(Lower Letters: {let_low})')

    print('Symbols:', sym)

    if out > 0:
        print('Out chr:', out, '(out of U.S. ASCII)')
        
    print('\nLength =', len(str_tumle),'\nSumma  =', num + let + sym + out)


    some_text = ''
    for i in str_tumle: some_text += i

    print('\nPlease, choose case VAR:')
    print('VAR = 0 - for print your String in Lower case')
    print('VAR = 1 - for print your String in UPPER case')
    print('VAR = "123/abc" - for print your String in Title case')

    var = input('VAR = ')

    try:
        var = int(var)
    except:
        var = var
        
    if var == 0:
        some_text = 'var = 0: ' + some_text
        print(some_text.lower())
    elif var == 1:
        some_text = 'var = 1: ' + some_text
        print(some_text.upper())        
    else:
        some_text = f'var = {var}: ' + some_text
        print(some_text.title())



    print('\nRepeat - press "1"')
    print(' Exit  - press Enter')
            
    begin = input()
            
    if begin == '1': String_count()
    else: return

String_count()









