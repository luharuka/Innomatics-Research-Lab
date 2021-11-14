# Enter your code here. Read input from STDIN. Print output to STDOUT

import re
n= int(input())
for i in range (0,n):
    validity = "Invalid"
    temp = "".join(sorted(input()))
    if len(temp)==10:
        if re.search(r'[a-zA-Z0-9]',temp):
            if re.search(r'[A-Z]{2}',temp) and re.search(r'[0-9]{3}',temp):
                if (re.search(r'(.)\1',temp) == None):
                    validity = "Valid"
    print(validity)
