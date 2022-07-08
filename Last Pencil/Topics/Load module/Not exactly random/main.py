from random import seed
from random import randint

# place `import` statement at top of the program


# don't modify this code or variable `n` may not be available
n = int(input())

# put your code here
seed(a=n, version=2)
print(randint(-100, 100))
