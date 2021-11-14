# Enter your code here. Read input from STDIN. Print output to STDOUT

import re 

def is_valid(cc):
    pattern = r"[456]\d{3}(-?\d{4}){3}$"
    pattern2 = r"((\d)-?(?!(-?\2){3})){16}"
    if re.match(pattern,cc) and re.match(pattern2,cc):
        return True
    else:return False

for _ in range(int(input())):
    cc = input()
    if is_valid(cc):
        print('Valid')
    else:
        print('Invalid')
