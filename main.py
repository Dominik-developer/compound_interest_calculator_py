
import os
import platform

# screen cleaning function
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
                print("Wrong data typed in, try again! \n")
                toNumber()

        except ValueError:
            print("Wrong data typed in, try again! \n")
            toNumber()

    except ValueError:
        print("Wrong data typed in, try again! \n")
        toNumber()

def fromNumber():

    try:
        startMoney = float(input("How much money you have on start? "))
        
        try:
            years = int(input("How many years will the process last (only full years, no 1.5)? "))

            try:
                percent = float(input("What is the interest percent? "))

                pastYears = 0

                currentMoney = startMoney

                interesPercent = percent / 100 + 1

                #algorithm
                for pastYears in range(years):

                    currentMoney = currentMoney * interesPercent

                    pastYears = pastYears + 1


                #rounding numbers
                roundMoney = round(currentMoney, 2)
            
                print(f"In {years} year/years and you will have {roundMoney}. \n")

            except ValueError:
                print("Wrong data typed in, try again! \n")
                fromNumber()

        except ValueError:
            print("Wrong data typed in, try again! \n")
            fromNumber()

    except ValueError:
        print("Wrong data typed in, try again! \n")
        fromNumber()

def menu():

    print('Compound interest calculator in python\n')
    print('1 - count years needed to gain given amount \n')
    print('2 - count how much you will earn after given time \n')

    try:
        choice = int(input("Choose which type of calculations you would like to do: "))

        if choice == 1:
            clear_screen()
            toNumber()
        elif choice == 2:
            clear_screen()
            fromNumber()
        else:
            print("Wrong data typed in, try again! \n")
            menu()
     
    except ValueError:
        clear_screen()
        print("Wrong data typed in or wrong number chosen, try again! \n")
        menu()
    
    print('--------------------\n')

#start

menu()