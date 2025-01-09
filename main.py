""" This is for Pylint
It has been updated multiple times
"""

A1 = 1
B1 = 10

for i in range (A1, B1):
    print("Hello World")

C = 1
C = C + 1

def a(a1):
    """ 
    This is just for analysing the Working of Pylint 
    """
    print(a1)
    # Comment
    for j in range(10):
        b = 20
        d = a1+b
    print(j)
    return d

B2 = a(1)
print(B2)

if A1 == B1:
    print(True)
else:
    print(False)
print("Hello World") # This is a comment
