'''
One of the most famous cyphers of all time is Vigenère cipher. It uses a key to encrypt a message applying shifting of the letters of the message according to the corresponding indexes of the letters of the key, if the key is shorter than the message, we use the key over and over again until the full message is encrypted.

Let's say we the alphabet we have consists of 26 letters ignoring the case of the letters, a space, a comma and a dot. the characters take indexes 1 to 26, the space, comma and the dot take 27, 28 and 29 respectively.

Given a message and a key from our alphabet, what is the generated cypher. (with all output letters in lowercase)

Input Format

The key in a single line
The message in a single line

Constraints

The key and the message only contain letters from the alphabet
1 <= length of the key, message < 1000

Output Format

The encrypted message

'''
# Enter your code here. Read input from STDIN. Print output to STDOUT
key = raw_input()
key = key.lower()
key = [i for i in key]
message = raw_input()
message = message.lower()
def cypher(keys, message):
    x='abcdefghijklmnopqrstuvwxyz ,.'
    x=[i for i in x]
    reference=dict(zip(x,range(1,30)))
    enc=[]
    k = 0
    val = 0
    for i in range(len(message)):
        k = keys[i%len(keys)]
        val = reference[k]+ reference[message[i]]
        enc.append(x[(val%29) -1])
return "".join(enc)

print(cypher(key,message))
