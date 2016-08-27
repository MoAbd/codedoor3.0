'''
You are give a list of sentences and a number of characters, it’s required to get the number of sentences in the group that start with these characters.

Input Format

N(the number of sentences)
The sentence to complete
sentence 1
sentence 2
...
sentence N

Constraints

1 <= N < 1000
1 <= the length of a sentence < 1000

Output Format

the number of sentences starting with the given sentence

'''
# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(raw_input())
match = raw_input()
length = len(match)
l = 0
for i in range(n):
    x = raw_input()
    if match == x[0:length]:
        l+=1
print l
