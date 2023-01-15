"""
    These functions return the results automatically 
    and there is no need to write the RETURN keyword.
"""

"""
    Work on the list :
        - If the input of lambda is a list,
        its output is also a list.

        - The answer must be used by : list(map(lambda ...) )
"""

# name_function = lambda data_in : doing on data_inputs



########
# EX 1 #
########

# normal 

def add(x,y):
    return x+y


# lambda

add = lambda x,y : x+y

print(add(2,5))
print(add(33,46))



########
# EX 2 #
########

data = [1,2,3,4,5,6,7,8,9]


# normal 

def multi(x):
    return x*x

print(list(map(multi ,data)))

# lambda 

print( list( map( lambda y: y*y ,data ) ) )




########
# EX 3 #
########

data = [(1,'B'),(3,'D'),(8,'C'),(5,'E'),(7,'A')]


# sort by number

print(sorted(data))


# sort by Alphabet

print( sorted(data, key=lambda y:y[1]) )