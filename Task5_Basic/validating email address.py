# Enter your code here. Read input from STDIN. Print output to STDOUT
import email.utils
import re

for i in range(int(input())):
    
    a, b = map(str,email.utils.parseaddr(input()))
    
    validEmail = re.search(r'^[a-zA-Z]+[a-zA-Z0-9_.-]+[@][a-zA-Z]+[.][a-zA-Z]{1,3}$', b)
   
    if validEmail:
        print(email.utils.formataddr((a, b)))
