# -*- coding: utf-8 -*-
"""suleman_tunio_test1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/11R6qqZsCNCyn0YZ16ML5lq3ib5hwSvnp
"""

#Q1 pattern search
text = input('Enter text: ')
pattern = input('Enter pattern: ')

n = len(text)
m = len(pattern)

for i in range((n)):
    j = 0
    while (j < m and pattern[j] == text[i+j]):
        j = j+1
    if j == m:
      print(i)

#Q2Max Element
array = [1, 2, 3, 4, 5, 6]
max = 0
for i in range(len(array)):
    if array[max] < array[i]:
        max = i
print(array[max])

#Q3 Unique Element
array = [1, 2, 3, 4, 5, 6]

c = 0
for i in range((len(array)-1)):
    if array[i] == array[i+1]:
        c = c +1

if c == 0:
    print('unique numbers')
else:
    print('numbers are not unique')

# Q4 Matrix Multiplication
# Program to multiply two matrices using nested loops

# 3x3 matrix
x = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]

    # 3x4 matrix
y = [[5,8,1,2],
    [6,7,3,0],
    [4,5,9,1]]

    # result is 3x4
result = [[0,0,0,0],
         [0,0,0,0],
         [0,0,0,0]]

# iterate through rows of x
for i in range(len(x)):
   # iterate through columns of y
   for j in range(len(y[0])):
       # iterate through rows of y
       for k in range(len(y)):
           result[i][j] += x[i][k] * y[k][j]

for r in result:
   print(r)

#Q5: convert decimal number into binary representation

decimal = int(input("Enter a decimal number \n"))
binary = 0
ctr = 0
temp = decimal  #copying number

#calculating binary
while(temp > 0):
    binary = ((temp%2)*(10**ctr)) + binary
    temp = int(temp/2)
    ctr += 1
       
print("Binary of {x} is: {y}".format(x=decimal,y=binary))

#Q6 
# Python code to check  if a matrix is
# symmetric or not.
 
# Returns true if mat[N][N] is symmetric, else false

def isSymmetric(mat, N):
    for i in range(N):
        for j in range(N):
            if (mat[i][j] != mat[j][i]):
                return False
    return True
  
# input
mat = [ [ 1, 3, 5 ], [ 3, 2, 4 ], [ 5, 4, 1 ] ]
if (isSymmetric(mat, 3)):
    print ("Is Symmetric")
else:
    print ("Not Symmetric")

# Q7 python code for testing of prime number:
a = 16
c =0
for i in range(2,int((a+2)/2)):
    if a % i ==0:
        c = c+1
if c ==0:
    print('the number {} is prime'.format(a))
else:
    print('the number {} is composite'.format(a))

#  Q8 Python code for the fibonacci series
nterms = int(input('Enter the number of terms'))
n1 = 0
n2 = 1
c =0

if nterms ==0:
    print('Enter positve numbers')
elif nterms ==1:
    print('the fibonacci series is ')
    print(n1)
else :
    print('the fibonacci series is ')
    while(c < nterms):
        print(n1)
        nth = n1 + n2
        # swaping values
        n1 =n2
        n2 = nth
        c = c+1