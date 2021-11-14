# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
string=int(input())
for _ in range(string):
      pattern1=re.compile(r'(?<= )(&&)(?= )')
      pattern2=re.compile(r'(?<= )(\|\|)(?= )')
      print(pattern2.sub('or', pattern1.sub('and', input())))







