#Taking number of fibonacci terms(n) as an input
n = int(input())
#Declaring and initializing an array 'a' for storing first n fibonacci terms
a = [0, 1]
#Storing rest n-2 fibonacci terms in an array 'a'
for i in range(2, n):
    a.append((a[i - 1] + a[i - 2]))
l = 0
c = 0
#Counting of number of rows required while printing Fibonacci triangle 
for i in range(0, n):
    c = c + 1
    if (c > l):
        l = l + 1
        c = 0
if (c > 0):
    l = l + 1
    c = 0
#Declaring and Initializing a variable named 'sp' to manage spacing while printing Fibonacci triangle
sp = l - 1
#Printing of Fibonacci triangle
for i in range(0, l):
    for k in range(sp):
        print(' ', end=' ')
    for j in range(0, i + 1):
        if (c == n):
            break
        print(a[c], ' ', end=' ')
        c = c + 1
    print('\n')
    #Decrement in spacing after printing of each row
    sp = sp - 1
#i, j, k are used as loop variables and for indexing


