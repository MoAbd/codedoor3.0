# Enter your code here. Read input from STDIN. Print output to STDOUT
n, clas = raw_input().split()
n, clas = [int(n), int(clas)]
c = [int(i) for i in raw_input().split()]
def classes(n,c,clas):
	for i in c :
		if n <= i :
			return n
		else:
			n = n-i
print(classes(n,c,clas))
