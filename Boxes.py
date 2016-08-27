'''
You are given the dimensions of a number of boxes. Each box can have a different dimension from the others. If we want to put the boxes on top of each others, what will be the lowest height the boxes can occupy.

Input Format

N(the number of boxes)
x y z of the box number 0
x y z of the box number 1
...
x y z of the box number N

Constraints

1 <= N < 1000
1 <= x, y, z < 10000

Output Format

The minimum height of the boxes

'''
# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(raw_input())
height = 0
for i in range(n):
    l =[int(i) for i in raw_input().split()]
    height += min(l)
print height
