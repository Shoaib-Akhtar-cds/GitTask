#********  Requirement  *****
#get three different integer numbers input
#sum three numbers
# subtract 2nd number from first
#multiply 3rd number by first
#sum all three numerbers divide by 3rd number

#pseudocode
#declare and initialize 3 integer variable
#get first input check for number
#get 2nd input check for number and not equal to 1st number
#get 3rd input check for number and not equal to 1st number and not equal to 0
#declare and initialize sum, difference, product and average variables
#clculate sum of all, difference in 1st and second, product of of 3rd and first, sum divided by third Num
#display numbers and results of calculation

iNum1 = 0
iNum2 = 0
iNum3 = 0
iNum1 = int(input("Please Enter First Integer Num :"))
iNum2 = int(input("Please Enter Second Integer Num :"))
iNum3 = int(input("Please Enter Third Integer Num :"))

iSumOfNumbers = 0
iProductOfNumbers  = 0
iDifferenceOfNumbers = 0
fSumDivByThird = 0.0

#****** Required Calculations
iSumOfNumbers = iNum1 + iNum2 + iNum3
iDifferenceOfNumbers = iNum1 - iNum2
iProductOfNumbers = iNum1 * iNum3
fSumDivByThird = round(iSumOfNumbers / iNum3 ,2) #Potential Divide By 0

print(f"Sum Of Number {iNum1} , Number {iNum2} and Number {iNum3} is {iSumOfNumbers}")
print(f"Difference in Number {iNum1} and Number {iNum2} Is {iDifferenceOfNumbers}")
print(f"Product Of Number {iNum1} and Number {iNum3} Is {iProductOfNumbers}")
print(f"Sum of Numbers \"{iNum1}\", \"{iNum2}\", \"{iNum3}\" Dividied By \"{iNum3}\" is {fSumDivByThird}" )
