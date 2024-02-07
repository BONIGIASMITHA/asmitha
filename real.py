#divison of 2 real numbers
a=input("enter the real number")
b=input("enter second number")
if type((a)==int or float):
	if(type(b)==int or float):
		div=(float(a)/float(b))
		print("div=",div)
else:
	print("error")
#dot product of a vector
l=[]
m=[]
s=0
n=int(input("enter the elements"))
for i in range(n):
	a=int(input("enter number"))
	b=int(input("enter another number"))
	l.append(a)
	m.append(b)
print("list l=",l)
print("list m",m)
for i in range(len(l)):
	s=s+l[i]*m[i]
print(s)
#det of a matrix....check whether it is a square matrix 
R=int(input("enter a number"))
C=int(input("enter a number"))
matrix=[]
print("enter the entries row wise")
for i in range(R):
	a=[]
	for j in range(R):
		a.append(int(input()))
	matrix.append(a)
for i in range(R):
	for j in range(C):
		print(matrix[i][j],end=" ")
	print()
det=matrix[0][0]*matrix[1][1]-matrix[0][1]*matrix[1][0]
print("det of a matrix",det)
#dot product
a=[1,2,3]
b=[7,8,9]
dot_product=sum(x*y for x,y in zip(a,b))
print("dot product",dot_product")
