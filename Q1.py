def generator(s,c,g):
	for i in range(c):
		print(s,end=" ")
		s=s*g
	print(s)
a=int(input("Enter the starting number:"))
b=int(input("Enter the number of terms to be generated:"))
c=int(input("Enter the multipler:"))
generator(a,b,c)
