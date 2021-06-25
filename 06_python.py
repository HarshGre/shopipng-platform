#python program to find the factorial of a number 
print('This is a simple program to find the factorial of any positive number.')
num_1=int(input('Enter the number: '))
a =1
if num_1<0:
    print('Sorry, factorial does not exist for negative numbers')
elif num_1==0:
    print('The factorial is 1')
else :
    for i in range(1,num_1):
        factorial=num_1*i
        print(factorial)