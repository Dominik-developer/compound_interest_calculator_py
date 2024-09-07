
# screen cleaning function
import os
import platform

def clear_screen():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')


# logic functions

def toNumber():

    try:
        endMoney = float(input("How much money you want to have at the end? "))
        
        try:
            startMoney = float(input("How much money you have on start? "))

            try:
                percent = float(input("What is the interest percent? "))

                # convertion of variables 
                currentMoney = startMoney

                interesPercent = percent / 100 + 1

                #algorithm
                while( currentMoney < endMoney):

                    years = 0
                    
                    currentMoney = currentMoney * interesPercent
                    years = years + 1

                #rounding numbers
                roundMoney = round(currentMoney, 2)
            
                print(f"You will exceed {endMoney} in {years} year/years, at the end you will have {roundMoney}. \n")

            except ValueError:
                print("Wrong data type in, try again!")

        except ValueError:
            print("Wrong data type in, try again!")

    except ValueError:
        print("Wrong data type in, try again!")

def fromNumber():

    print('from number function, will appear here later')



print('compound interest calculator in python\n')
'''print('Choose which type of calculations you would like to do: ')'''
print()
print('--------------------\n')

toNumber()


