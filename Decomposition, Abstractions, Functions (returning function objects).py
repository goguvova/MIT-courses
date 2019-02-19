#########################
## EXAMPLE: returning function objects
#########################
def f():
    def x(a, b):
        return a+b
    return x
    
# the first part, f(), returns a function object
# then apply that function with parameters 3 and 4
val = f()(3,4)
print(val)

