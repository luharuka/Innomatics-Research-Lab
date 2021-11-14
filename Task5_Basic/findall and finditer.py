# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
string_array = '[qwrtypsdfghjklzxcvbnm]'
a = re.findall('(?<=' + string_array +')([aeiou]{2,})' + string_array, input(), re.I)
print('\n'.join(a or ['-1']))
