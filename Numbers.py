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

""" Functions"""
def sumofnums(num1,num2,num3):
    return(num1+num2+num3)

def differenceofnums(num1,num2):
    return(num1-num2)

def productofnums(num1,num2):
    return(num1*num2)

def divisionofnums(num1,num2):
    return(round(num1/num2,2))

i_num1 = 0
i_num2 = 0
i_num3 = 0
i_num1 = int(input("Please Enter First Integer Num :"))
i_num2 = int(input("Please Enter Second Integer Num :"))
i_num3 = int(input("Please Enter Third Integer Num :"))

i_sum_of_numbers = 0
i_product_of_numbers  = 0
i_difference_of_numbers = 0
f_sum_div_by_third = 0.0

#****** Required Calculations
i_sum_of_numbers = sumofnums(i_num1,  i_num2, i_num3)

i_difference_of_numbers = differenceofnums( i_num1, i_num2)

i_product_of_numbers = productofnums(i_num1 , i_num3)

f_sum_div_by_third = divisionofnums(i_sum_of_numbers, i_num3 ) #Potential Divide By 0

print(f"Sum Of Number {i_num1} , Number {i_num2} and Number {i_num3} is {i_sum_of_numbers}")
print(f"Difference in Number {i_num1} and Number {i_num2} Is {i_difference_of_numbers}")
print(f"Product Of Number {i_num1} and Number {i_num3} Is {i_product_of_numbers}")
print(f"Sum of Numbers \"{i_num1}\", \"{i_num2}\", \"{i_num3}\" Dividied By \"{i_num3}\" is {f_sum_div_by_third}" )
