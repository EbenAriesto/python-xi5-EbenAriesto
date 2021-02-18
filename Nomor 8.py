# python program to find the LCM of two input numbers

# this function computes GCD
def compute_gcd(x, y):
    while(y):
        x, y = y, x % y
    return x

# this function computes LCM
def compute_lcm(x, y):
    lcm = (x * y) // compute_gcd(x, y)
    return lcm

num1 = 12
num2 = 20

print("The LCM is", compute_lcm(num1, num2))