"""
    * the 'break' statement is a way to exit the loop 
    and stop it completely.

    * the 'break' command should be placed in conditional command, 
    so that if the condition is met, it will stop the loop execution.

"""


# EX 1 :

for x in range(10):
    if x == 5 :
        print("the loop stopped.")
        break
    print(x)