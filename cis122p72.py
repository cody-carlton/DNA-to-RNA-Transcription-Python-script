'''
CIS 122 Winter 2022 Project 7-2
Title: TESTING AND DEBUGGING
Author: Cody Carlton
Credits: [Credit all non-class sources of significant help]
Description: using import doctest change functions to correctly output according to
docstring within funcitons
'''

import doctest

####
#(1) RAT WEIGHT
#### 
def rats(weight, p):
    '''(weight: float, p: float) -> None

    Print number of weeks it will
    take for a rat to weigh 2 times
    as much as its original weight
    (weight) if it gains weight at
    rate p percent per week.

    >>> rats(10, 10)
    The rat weighs 21.4 after 8 weeks.
    '''
    weeks = 0
    rate = p * .01
    initial_weight = weight # assignment statement added for initial weight 
    
    while weight < (2 * initial_weight) : # changed weight to initial weight
        weight += weight * rate
        weeks = weeks + 1 # changed wks to weeks
        
    weight = round(weight, 1)
    print(f'The rat weighs {weight} after {weeks} weeks.')
    return

####
#(2) FIND MINIMUM DIGIT
####
def min_digit(number):
    '''(number: int) -> int

    Find the minimum digit (value) 
    of the digits in a non-negative integer.
    Return the result

    >>> min_digit(45312)   #normal min 1 max 5
    1
    >>> min_digit(834)     #normal min 3 max 8
    3
    >>> min_digit(5)       #sequence length 1-min,max 5
    5
    >>> min_digit(101010101010)    #only 0s and 1s-min 0 max 1
    0
    >>> min_digit(97542)   #reverse order-min 2 max 9
    2
    >>> min_digit(123456789)# all the numbers, sorted-min 1 max 9
    1
    '''
    # removed number % 10 and number = number // 10 from begining of code
    mmin = 9 # set mmin = 9 instead of 0
                
    while number > 0: # set while loop to run while number is greater than 0     
        digit = number % 10
        # removed number = number // 10 and placed it at end of while loop
        if mmin > digit:
            mmin = digit
        number = number // 10
   
    return mmin

def min_main():
    '''minimum digit driver'''
    n = int(input('Enter a non-negative integer: ')) #added int(input to take integer as input 
    mmin = min_digit(n) # changed minimum to mmin and added n to min_digit() functionto run integer n through min_digit funciton
    print(f'The minimum digit in {n} is {mmin}.') #changed number to n and minimum to match mmin variable from min_digit funciton
  
    return

####
#(3) MINUTES TO YEARS
####
def minutesToHours(minutes):
    '''(minutes: number) -> float

    convert input minutes to hours;
    return hours

    >>> minutesToHours(60)
    1.0
    >>> minutesToHours(90)
    1.5
    >>> minutesToHours(0)
    0.0
    '''
    hours = minutes / 60
    hours = round(hours, 2) 
    return hours # changed print statement to return hours instead of printing                 
    
def hoursToDays(hours):
    '''(hours: int) -> float

    convert input hours to days;
    return days

    >>> hoursToDays(24)
    1.0
    >>> hoursToDays(100)
    4.17
    >>> hoursToDays(0)
    0.0
    '''
    days = hours / 24
    days = round(days, 2) #added assignment to round days to two decimal places
    return days # deleted print

def daysToYears(days):
    '''(days: int) -> float

    convert input days to yearss;
    return years

    >>> daysToYears(365)
    1.0
    >>> daysToYears(100)
    0.27
    >>> daysToYears(0)
    0.0
    '''
    # deleted asignment statement that set days = 365
    years = days / 365
    years = round(years, 2)
    return years

def minutesToYears(m):
    '''(m: int) -> float

    input number m minutes is converted to
    equivalent number of years. return years.
    call auxiliary functions to do each step

    >>> minutesToYears(525600)
    1.0
    >>> minutesToYears(5256000)
    10.0
    >>> minutesToYears(394200)
    0.75
    >>> minutesToYears(0)
    0.0
    '''
    hours = minutesToHours(m) # assiged variable hours, days and years to return values of function outputs    
    days = hoursToDays(hours)      
    years = daysToYears(days)

    return years # changed y to years in order to properly dispay correct return value

print(doctest.testmod())
