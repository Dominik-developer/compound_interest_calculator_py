
# screen cleaning function
import os
import platform

def clear_screen():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

    #egzample variables
    '''a = 120000
    n=20000
    i=0'''

# logic functions

def toNumber():

    try:
        endMoney = float(input("How much money you want to have at the end? "))
        
        try:
            startMoney = float(input("How much money you have on start?"))

            try:
                percent = float(input("What is the interest percent?"))

                # convertion of variables 
                currentMoney = startMoney

                interesPercent = percent + 1 

                while( currentMoney < endMoney):
                    

                    currentMoney = currentMoney * interesPercent
                    years = years + 1

                    '''
                    n = n*1.04
                    n = n+20000
                    i = i+1
                    print(n)
                    '''

                    print(f"You will achive {endMoney} in {years}, at the end you will have {currentMoney}")

            except ValueError:
                print("Wrong data type in, try again!")

        except ValueError:
            print("Wrong data type in, try again!")

    except ValueError:
        print("Wrong data type in, try again!")

 

    while(n < 79000000):

        n = n*1.04
        n = n+20000
        i = i+1
        print(n)
    
    
'''
def fromNumber():

    try:
        number = float(input(" "))


        print(f"Masz {number} lat.")
    except ValueError:
        print("Wrong data type in, try again!")

    for i in range(2):
        a= a *1.06 
        a = a + 0
    print(a)
'''



clear_screen()

print('compound interest calculator in python')
print('Choose which type of calculations you would like to do:')



