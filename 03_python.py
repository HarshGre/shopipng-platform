#program to convert temperature from fahrenheit to celsius and vice versa
#(0°C × 9/5) + 32 = 32°F
print("How do you want to convert the temperature ?","For celsius to fahrenheit enter 'C' and for fahrenheit to celsius enter 'F'",sep='\n')
T=input('Enter C or F: ')
if T=='C':
    c=float(input('Enter the value of temperature in Celsius: '))
    fun_1=(c*9/5)+32
    print('The temperature in Fahrenheit is:',fun_1,'F')
elif T=='F':
    f=float(input('Enter the value of temperature in Fahrenheit: '))
    fun_2=(f-32)*5/9
    print('The temperature in Celsius is:',fun_2,'C')
else:
    print('{Invalid character}')