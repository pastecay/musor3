#1
n=int(input())
i=1
while i**2<=n:
    print(i**2)
    i+=1
#или же
n = int(input())
i = 1
while i*i <= n and not print(i*i):
    i += 1
#2
n = int(input())
m = 1
i = 0
while m <= n:
    if m==n:
        print(i)
        break
    else:
        m = m*2
        i = i+1
if m > n:
    print("No")
#3
x = int(input())
y = int(input())
day = 0
while y - x >= 0:
    x *= 0,1
    day += 1
print(day)
#4
K = 0
while int(input()) != 0:
    K += 1
print(K)
#5
a=int(input())
b=int(input())
k=0
if b>a:
    k+=1
a=b
while b!=0:
    b=int(input())
    if b>a:
        k+=1
    a=b
print(k)
#6
a=int(input())
b=int(input())
if a>b:
    max1=a
    max2=b
else:
    max1=b
    max2=a
while b!=0:
    b=int(input())
    if b>max1:
        max2=max1
        max1=b
    elif b>max2:
        max2=b
print(max2)
#7
while i < n:
	f1, f2 = f2, f1 + f2 
	print(f2, end=' ') 
	i += 1
print()
#8
p=int(input())
c=1
b=0
while p!=0:
    v=int(input())
    p,v=v,p
    if v==p:
        c+=1
    if c>b:
        b=c
    if p!=v:
        c=1
print(b)
#9
n = input().split()
chet = []
for i in range(len(n)):
    n[i] = int(n[i])
    # print(n[i])
    if (i - 1) % 2 != 0:
        chet.append(str(n[i]))
print(' '.join(chet))
#10
a = [int(s) for s in input().split()]
for i in range(1,len(a)):
    if a[i]>a[i-1]:
        print(a[i])
#11
a = [int(s) for s in input().split()]
mx=a[0]
mi=0
for i in range(1,len(a)):
    if a[i]>mx:
        mx=a[i]
        mi=i
print(mx,mi)
#12
a = [int(i) for i in input().split()]
x = int(input())
pos = 0
while pos < len(a) and a[pos] >= x:
    pos += 1
print(pos + 1)
#13
a= [ 1, 2, 5, 0, 7, 3, 2 ] 
print( a )
    
for i in range( 0, len( a ) - 1, 2 ):
    a[ i ], a[i + 1] = a[i + 1], a[i]
    
print( a )
#14
a = [{min(a): max(a), max(a): min(a)}.get(x, x) for x in a]
#15
a = [7, 6, 5, 4, 3, 2, 1]
k = 2
result = a[:k] + a[k + 1:]
print(result)
#16
a=[int(i) for i in input().split()]
k,c=[int(e) for e in input().split()]
a.insert(k,c)
a=(" ".join([str(i)for i in a]))
print(a)
#17
n = 8
x = [0] * n
y = [0] * n
result = 'NO'
for i in range(n):
    x[i], y[i] = [int(j) for j in input().split()]
for i in range (n):
    for j in range(i+1,n):
        if x[i] == x[j] or y[i] == y[j] or abs(x[i] - x[j]) == abs(y[i] - y[j]):
            result = 'YES'
print(result)