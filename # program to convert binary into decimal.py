#program to convert binary into decimal numbers and vice-versa 

N = int(input ("Enter the number: "))
bn = 0


while N > 0 :
    rem = (N%2)
    if rem == 0:
        bn = bn + "0"
        N = N/2
    else :
        bn = bn + "1"
        N = (N-1)/2
print(bn)









