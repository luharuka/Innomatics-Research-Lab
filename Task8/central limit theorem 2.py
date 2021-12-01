# Enter your code here. Read input from STDIN. Print output to STDOUT
from math import sqrt, erf
dec = 4
def cum_prob(z):
    return 0.5 * (1 + erf(z / sqrt(2)))

maximum = 250
avg = 2.4
std = 2
n = 100

z = (maximum - n * avg) / (sqrt(n) * std)

print(round(cum_prob(z),dec))