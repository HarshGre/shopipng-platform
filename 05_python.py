#program to perform all basic functions of a calculator

print('This is a simple program to perform basic calculator operation between any two numbers')
print("For addition enter 'A'","For subtraction enter 'S'","For multiplication enter 'M'","For division enter 'D'",sep='\n')
num_1=float(input('Enter the first number: '))
num_2=float(input('Enter the second number: '))
oper=input("Enter the operation: ")
if oper=='A':
    sum_1=num_1+num_2
    print('The sum of the numbers is:',sum_1)
elif oper=='S':
    sum_1=num_1-num_2
    print('The difference of the numbers is:',sum_1)
elif oper=='M':
    sum_1=num_1*num_2
    print('The product of the numbers is:',sum_1)
elif oper=='D':
    sum_1=num_2/num_1
    print('The division of the numbers is:',sum_1)
else :
    print('{Invalid character}')