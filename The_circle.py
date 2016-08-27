'''
A game that consists of a specific number of players forming a circle, we start at the first member and count to a specific number in a list and then the user that we stop on gets out of the game, continuing from the next user and counting to the second number of that list and a player gets removed. And we keep doing that until we only have a single player and then he is considered the winner of the game.

Input Format

N(number of people)
A space seperated list of numbers counted in each turn

Constraints

1 <= N < 1000
0 <= the number counted in each turn < 10000

Output Format

The number of the winning player

'''
# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(raw_input())
m = [int(i) for i in raw_input().split()]
def count(n,m):
    players = range(1,n+1)
    location= 0
    for i in m :
        location = (location + i - 1) % n
        players.pop(location)
        n -= 1
        if n == 1 :
        return players[0]
print(count(n,m))
