#Taking height of Pascal's triangle(n) as an input
n=int(input())
#Declaring a list 'a' to store elements of Pascal's triangle
a=[]
#Storing elements of Pascal's triangle in a list named 'a'
a.append([0,1,0])
for i in range(1,(n+1)):
  a.append([0])
  for j in range(1,len(a[i-1])):
    t=a[i-1][j-1] + a[i-1][j]
    a[i].append(t)
  a[i].append(0)
#Declaring and Initializing a variable named 'sp' to manage spacing while printing Pascal's triangle
sp=n-1
#Printing of n rows of Pascal's triangle
for i in range(n):
  for k in range(sp):
    print(' ',end=' ')
  for j in range(1,(len(a[i])-1)):
    print(a[i][j],' ',end=' ')
  print('\n')
  #Decrement in spacing after printing of each row
  sp=sp-1
#i, j, k are used as loop variables and for indexing

