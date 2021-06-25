#Lists in python

# part 1  {counting and printing list elements}

'''
list7=['1','2','e','f','r','p','y','o','h']

n = len(list7)     #len() counts the total number of elements in the list

for i in list7:    #method 1
    print(i)
print('The total number elements in the list are:',n)

for i in range(n):   #method 2
    print(list7[i])
print('Total number of characters are: ')
print(n)  
'''

# part 2 {changing list data}
'''
subjects=['Hindi','English','Maths','History']

temporary=subjects
temporary[0]='Sanskrit'

print(temporary)
print(subjects)
'''

# Part 3   {adding different Lists}

'''
List1 = [1,2,3,4,5]
List2 = [5,6,7,8,9]
List3 = List1 + List2
print (List3)
'''
# part 4 {membership testing in python}

'''
x = 'python'
print('o' in x)
list1 = [10,20,30,40,50,60,70]
print(10 in list1, 22 in list1)
print(22 not in list1)

for numbers in list1:
    print(numbers)
'''
# part 5 {Indexing}

'''
list1 = ['Red','Green','Blue','White','Black','Orange','Violet']
print(list1[2],list1[-2],list1[-4],sep='\n')

import copy
list2 = copy.copy(list1)
print(list2)

  # nested list 
list3 = [1,2,3,4,['a','b','c'],[5,6,7,8,9],]
print(list3)

print(list3[4][2])
'''

# part 6 {slicing}
'''
  #list[start:stop:step]

marshmello = 493729702373
list1 = [100,50.57,"Radhika","Shaurya",900,897.60,30,58,'harsh','nisha',['alan walker',marshmello]]

print(list1[1:5])
print(list1[2:10:2])
print(list1[20:40])  #empty list
'''

# Part 7 built-in-functions

   # Append{use to add elements} ---> list.append(elem)
'''
l1 = [20,30,40,50,30,38,47]
print(l1)
l1.append(19999)
print(l1)
l1.append('The intro - by xx')
print(l1)
l1.append(['harsh',"astrophysicist"])
print(l1)
'''

# =====================PROJECT-01====================#
# program to find the second largest element in a list 'num'
'''
print('======First we will create the list======')
n = int(input('Enter the number of elements: '))
i = 0
num = []
while i<n:
    print('Enter the element no.',i + 1,": ")
    add = int(input())
    num.append(add)
    i = i+1
print("The original list is: ",end=' ')
for i in range(n):
    print(num[i],end=' ')
if (num[0] > num[1]):
    m, m2 = num[0], num[1]
else:
    m, m2 = num[1], num[0]
for x in num[2:]:
    if x>m2:
        if x>m:
            m2, m = m, x
        else:
            m2 = x
print()
print("The second largest number in the list is:",m2)

'''
















