"""
cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that pair.
For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.
Implement car and cdr.
"""

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair


def car(func):
    def left(a,b):
        return a
    return func (left)

def cdr (func):
    def right (a,b):
        return b
    return func (right)

print(car (cons(3,4)))
print (cdr(cons(3,4)))

"""
cons(3,4) is called first, which returns pair. 

the parameter in the car function, func, is now the pair function

At the end of the car function, we return the parameter func with our left function as the parameter. 
Since func is our pair function, we are returning the pair function with the left function as the parameter

We now execute the pair function, with the paramter f as our left function.
We return f(a,b), which means that we are returning the value that is returned when left(a,b) is executed

When left(a,b) is executed, we return the 'a' value
"""
