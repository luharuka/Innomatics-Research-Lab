# Enter your code here. Read input from STDIN. Print output to STDOUT

import re
string=input().strip()
mir = re.search(r'([a-zA-Z0-9])\1+',string)
print(mir.group(1) if mir else -1)
