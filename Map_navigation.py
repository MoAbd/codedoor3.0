'''
A map of 2d tiles and a user that can be on any tile of it. He starts from the tile (0,0) facing upward (in the direction of (0, +n)) Starts moving according to two patterns that are used alternatively, applying the first pattern in his first turn, the second pattern on his second turn, then the first pattern and so on, until he reaches his destination after a specific number of movements. Patterns are defined using the following letters: * r: to turn right without moving * l: to turn left without moving * f: to move forward a single tile

Input Format

P1(the first pattern) P2(the second patter) N(the numebr of turns)

Constraints

The patterns contain oly the letters r, l and f
1 <= pattern length < 10
0 <= Number of turns < 100

Output Format

X(the x coordinate) Y(the y coordinate)
(seperated with spaces)

'''
# Enter your code here. Read input from STDIN. Print output to STDOUT
t1, t2, n = raw_input().split()
l = [t1,t2]
n = int(n)
pos=[0,0]
j = 0
d = 0
for i in range(n):
    j=l[i%2]
    for k in j:
        if 'r'==k  :
            d = (d+1) % 4
        elif 'l' ==k:
            d = 4 - (d+1)
        elif 'f' ==k:
            if d == 0 :
                pos[1] +=1
            elif d == 1 :
                pos[0] +=1
            elif d == 2 :
                pos[1] -=1
            elif d == 3 :
                pos[0] -= 1
print pos[0], pos[1]
