"""
    Everything like strings, lists and even functions are objects.
"""


"""
    We can even cast the function in a variable
"""

def hello():
    print('say hello!')


hi = hello()

hi()
# >>> 'say hello!'

hello()
# >>> 'say hello!'