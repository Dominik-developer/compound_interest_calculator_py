
# screen cleaning function
import os
import platform

def clear_screen():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

    #egzample variables
    a = 120000
    n=20000
    i=0


def toNumber():
    while(n < 79000000):

        n = n*1.04
        n = n+20000
        i = i+1
        print(n)
    
    
'''
def fromNumber():
    for i in range(2):
        a= a *1.06 
        a = a + 0
    print(a)
'''



clear_screen()

print('compound interest calculator in python')
print('Choose which type of calculations you would like to do:')

toNumber()
