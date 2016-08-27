'''
You have an array of crates and you want to divide the crates while preserving their order so they get moved to another location in a number of vans. So you want to make sure that every van gets to carry the same weight. Given an array of crate weights in their order and the number of vans, find if the crates can be divided equally on the vans while preserving the order or not.

Input Format

The input will be in the form
N(number of vans) M(number of crates)
A list of crate's weight

Constraints

1 <= N < 500
1 <= M < 1000
0 <= crate weight < 1000

Output Format

true or false
'''
# Enter your code here. Read input from STDIN. Print output to STDOUT
n, m = raw_input().split()

n, m = [int(n), int(m)]
w = [int(i) for i in raw_input().split()]
def weights(n,m,w):
	s = sum(w)
	if not s%n :
	    avg = s / n
	    new_avg=avg
	    for i in w :
	        new_avg = new_avg - i
	        if new_avg == 0:
	           new_avg = avg
	           n -= 1

    		elif new_avg < 0 :
	             return 'false'
