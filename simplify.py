import math
import argparse

parser = argparse.ArgumentParser(description='Given two numbers, return the simplified ratio of the two')

# Add a positional arguments
parser.add_argument('num1', type=int, help='first number')
parser.add_argument('num2', type=int, help='second number')

# Parse the command-line arguments
args = parser.parse_args()

# Access the parsed positional arguments
num1 = args.num1
num2 = args.num2

# Calculate the greatest common divisor using math.gcd()
gcd = math.gcd(num1, num2)

num1_simplified = num1 // gcd
num2_simplified = num2 // gcd

# Display the result
print(f"{num1_simplified}:{num2_simplified}")