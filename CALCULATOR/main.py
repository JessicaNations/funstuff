
'''This program is a simple calculator'''
 
#Set variable for loop
again = True
 
#Run calculator until again is False
while again:
     #Input 2 numbers
     firstNum = int(input("Enter first number: "))
     secondNum = int(input("Enter second number: "))
    
     #Input Operation desired
     print"Enter operation you want to run."
     print"A - Addition"
     print"S - Subtraction"
     print"M - Multiplication or"
     oper = raw_input("D - Division: ")
    
     #Determine if trying to divide by zero
     if oper == "D" and secondNum == 0: 
        print"ERROR: Start again"
     else:
        #Perform calculations
        if oper == "A":
            answer = firstNum + secondNum
            print firstNum, " + ", secondNum, " = ", answer
        elif oper == "S":
            answer = firstNum - secondNum
            print firstNum, " - ", secondNum, " = ", answer
        elif oper == "M":
            answer = firstNum * secondNum
            print firstNum, " * ", secondNum, " = ", answer
        elif oper == "D":
            answer = firstNum / secondNum
            print firstNum, " / ", secondNum, " = ", answer
        else: 
            print"ERROR: invalid entry"
    
     #Ask to run again?
     YN = raw_input("Would you like to try again?")
     if YN == "N":
        again = False
        

'''End of program'''


Rex McKanry 6369228289 mckanry@stchas.edu
Assistant professor and dept. chair of computer science (CPT)

Copy all to temporarily save work

Python is format drive 
var - can change
constant - can change
input - information "end user" provides
loops - repeats
decision making - divert flow

labs.codecademy.com 
# single line comment won't affect code
camelCapitalization  
int - integer 
print = run
elif/if/else - operation steps
New line of code must indent to line up with previous line for corresponding function
'''Comments for you'''



