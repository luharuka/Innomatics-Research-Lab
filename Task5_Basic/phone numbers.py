# Enter your code here. Read input from STDIN. Print output to STDOUT

test = int(input())
for i in range(test):
    string  = input()
    if(len(string)==10 and string[0] in ['9', '8', '7'] and string.isnumeric()):
        print("YES")
    else:
        print("NO")
