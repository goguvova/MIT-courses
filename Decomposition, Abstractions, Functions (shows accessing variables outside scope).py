#########################
## EXAMPLE: shows accessing variables outside scope
#########################
def f(y):
    x = 1
    x += 1
    print(x)
x = 5
f(x)
print(x)

def g(y):
    print(x)
    print(x+1)
x = 5
g(x)
print(x)

def h(y):
    pass
    #x += 1 #leads to an error without line `global x` inside h
x = 5
h(x)
print(x)

