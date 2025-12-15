
# Legacy Calculator (Python 2 style + deprecated usage)

import imp  # Deprecated module
import commands  # Deprecated module (removed in Python 3)

def add(a, b):
    print "Adding numbers"  # Python 2 print statement
    return a + b

def subtract(a, b):
    return a - b

if __name__ == "__main__":
    result = add(5, 3)
    print "Result is:", result
