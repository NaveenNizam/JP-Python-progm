'''num= int (input('Enter a Number :  '))
if num%2 == 0:
    print('The Number is EVEN')
else:
    print('The Number is ODD') '''

a = [1,1,2,3,5,8,13,21,34,55,89]
print(a)
print('Length of List is :  ', len(a))
sum =0
for v in range (len(a)):
    sum = sum + a [v]
print('Total of List is :  ',sum)
print('The LARGEST Number in list is ',max(a))
b=[]
five = 5
for v in range(0,len(a)):
    if a[v] <= five:
      b.append (a[v])
print('The elements of the list are less than',b)
