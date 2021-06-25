#manipulating list data ie., adding and deleting data
'''
list=[1,2]
print('list before append',list)
list.append(3)
print('list after append',list)
list.extend([4,5,6,7,8])
print('list after extend',list)
list1=["Harsh","Nisha"]
list2=list+list1
print(list2)
del list2[0:8]
print('list after delete',list2)
'''
'''
i = 0

for r in range(1,10,2):
    i = i + r

print (i)
'''

student_1 = []
student_2 = []
student_3 = []
student_4 = []
student_5 = []

student_1.append('English-->25')
student_1.append('Maths-->18')
student_1.append('Science-->28')

student_2.append('English-->16')
student_2.append('Maths-->15')
student_2.append('Science-->27')

student_3.append('English-->17')
student_3.append('Maths-->21')
student_3.append('Science-->25')

student_4.append('English-->20')
student_4.append('Maths-->24')
student_4.append('Science-->10')

student_5.append('English-->03')
student_5.append('Maths-->26')
student_5.append('Science-->30')

print(student_1,student_2,student_3,sep='\n')




