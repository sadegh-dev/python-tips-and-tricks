"""
    Everything like strings, lists and even functions are objects.
"""


"""
    We can even cast the function in a variable
"""

def hello():
    print('hello world!')


hi = hello()

hi()
# >>> 'hello world!'

hello()
# >>> 'hello world!'