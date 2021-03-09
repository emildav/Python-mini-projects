
from forex_python.converter import CurrencyRates, CurrencyCodes
import os 

def convert_temp(number, choice):
    if choice == '1':  # if celsius to fahrenheit

        return (number * 9/5) + 32

    elif choice == '2':  # if fahrenheit to celsius

        return round(((number - 32) * 5/9), 5)

def convert_curr(curr1, curr2, amount):
    currencies = {'1':'USD', '2':'EUR', '3':'RUB'}
    
    symb = CurrencyCodes()
    c = CurrencyRates()
    result = round(c.convert(currencies[curr1], currencies[curr2], amount), 2)
    symb_curr1 = symb.get_symbol(currencies[curr1])
    symb_curr2 = symb.get_symbol(currencies[curr2])

    return "\t{} {} to {} is {} {}".format(amount, symb_curr1, currencies[curr2], result, symb_curr2)

def convert_distance(unit_one, unit_two, number):

    rates = {'1':0.001, '2':0.01, '3':1, '4':1000, '5':0.3048} # 1-mm, 2-sm, 3-km, 4-m, 5-foot
    
    return round((number * rates[unit_one] / rates[unit_two]), 4)

def convert_again():
    ans = ''
    while ans.lower() not in ['y', 'n']:
        ans = input('\tDo you want to continue? y n: ')
    
    if ans.lower() == 'n':
        return None
    else:
        return True

answer = True
while answer:
    os.system('cls')
    answer = input(
                   """
    What do you want to convert?:
        1. Temperature
        2. Currency
        3. Distance
        4. Exit

    """)

    if answer == '1':
        print('\tTEMPERATURE')
        answer = ''
        while answer not in ['1', '2']:
            answer = input("""
    Choose the option: 
        1. Celsius to Fahrenheit
        2. Fahrenheit to Celsius        
                    """)
        
        number = ''
        while number.isdigit() == False:
            number = input('Enter a number: ')

        print(convert_temp(int(number), answer))

        answer = convert_again()

    elif answer == '2':
        print('\tCURRENCY')
        curr1 = ''
        curr2 = ''
        amount = ''

        while curr1 not in ['1','2','3']:
            curr1 = input("""
    Choose the first currency:
        1. USD
        2. EUR
        3. RUB
                """)
        while curr2 not in ['1','2','3']:
            curr2 = input("""
    Choose the second currency:
        1. USD
        2. EUR
        3. RUB
                """)
        while amount.isdigit() == False:
            amount = input('\tEnter an amount: ')

        print(convert_curr(curr1, curr2, int(amount)))

        answer = convert_again()

    elif answer == '3':
        print('\tDISTANCE')
        unit_one = ''
        unit_two = ''
        number = ''

        while unit_one not in ['1', '2', '3', '4', '5']:
            unit_one = input("""
    Choose the first unit:
        1. Millimeter
        2. Sentimeter
        3. Meter
        4. Kilometer
        5. Foot

                """)
        while unit_two not in ['1', '2', '3', '4', '5']:
            unit_two = input("""
    Choose the second unit:
        1. Millimeter
        2. Sentimeter
        3. Meter
        4. Kilometer
        5. Foot

                """)
        while number.isdigit() == False:
            number = input('Enter a number: ')

        print(convert_distance(unit_one, unit_two, int(number)))

        answer = convert_again()

    elif answer == '4':
        print('\tGOODBYE')
        answer = None
    else:
        print('\tNot valid choice. Try again')
