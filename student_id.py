"""
Given a school with a number of classes. Every class has a specific number of students in it. Students are sorted alphabetically inside classes and among them. Every student has a local id, which is his index in the class If we sort it alphabetically, and a global id which is its index among the school. ID’s always start from 1. Given a list of numbers of students in each class, and the global id of a student. what is the local id of that student?

Input Format

N(student global id) M(Number of classes)
A space seperated list of number of students in each class

Constraints

1 <= N < total number of students
1 <= M < 1000
1 <= number of students in a class < 1000

Output Format

a single number containing the student local id
"""
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
