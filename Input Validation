# Decorator for input validation
def validate_positive_integers(func):
    def wrapper(*args):
        for arg in args:
            if not isinstance(arg, int) or arg <= 0:
                print("Error: All arguments must be positive integers.")
                return
        return func(*args)
    return wrapper


# Function to be decorated
@validate_positive_integers
def multiply(a, b):
    print("Product =", a * b)


# Main Program
multiply(5, 10)    # Valid input
multiply(8, -2)    # Invalid input
multiply(4, 2.5)   # Invalid input
