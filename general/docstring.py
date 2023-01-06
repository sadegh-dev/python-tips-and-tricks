"""
    We write Docstring to explain the function or class

    Multi-line descriptions are called Docstring.
"""



"""
    Docstring is placed at the highest level of function or class.

    - The first line should be a brief description 
    that starts with a capital letter 
    and then the sentence ends with a Point.

    - The second line is empty.

    - The third line should include additional explanations.

"""

class className:
    """this is Docstring for Person class.

    this class is for testing and is empty
    """

def funcName(name):
    """this docstring for doing function.

    this function is for testing and is empty
    """





"""
    In the Python code with the following command, 
    this description will be displayed.
"""

# access class Docstring
help(className)

# access function Docstring [way1]
help(funcName)

# access function Docstring [way2]
print(funcName.__doc__)