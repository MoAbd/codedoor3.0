'''
It's required to make a templating engine that takes a template and substitute the variables in it. The variables are present in the templates in the form {{some_variable}}. The variables can be nested, so for {{some_{{second_variable}}}} second_variable will be evaluated first and then the other one will be evaluated.

Input Format

N(number of variables) M(Numbers of lines for a template)
variable 1 (in the form of `variable_name=value`)
variable 2 (in the form of `variable_name=value`)
...
variable N
Template consisting of M lines

Constraints

0 <= N, M < 1000
1 <= length of a line, variable definition < 1000

Output Format

the parsed template

'''
# Enter your code here. Read input from STDIN. Print output to STDOUT
n, m = raw_input().split()
n = int(n)
m = int(m)

temp = []
var = []

if n == 0:
    print raw_input()

         
else:     
    for i in range(n):
        var.append(raw_input())
    var = dict(i.split('=') for i in var)
    
    for i in range(m):
        temp.append(raw_input())
        x = temp[i]
        counter = x.count('}}')
        for i in range(counter):
            end = x.find('}}')
            begin = x.find('{{')

            if end + 2 == len(x):
                begin = x.rfind('{{')
                x = x[:begin] + var[x[begin+2 : end]] + x[end+2:]

            elif x[end+2] == '{':
                begin = x.find('{{')
                x = x[:begin] + var[x[begin+2 : end]] + x[end+2:]
                
            else :
                begin = x.rfind('{{')
                x = x[:begin] + var[x[begin+2 : end]] + x[end+2:]
             
        print x
