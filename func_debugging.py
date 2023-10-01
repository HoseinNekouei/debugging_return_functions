
from functools import wraps

# create a decorator
def tracer(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)    
        print(f'{func.__name__}, ({args!r},{kwargs!r}) -> {result!r} ')

        return result
    return wrapper


@tracer
#return n-th of Fibonachi number
def fibonachi(n = 0):
    """ Return the n-th of Fibonachi number """
    if n in (0,1):
        return n
    else:
        return fibonachi(n-1) + fibonachi(n-2)
    
# call function and show debugging by decorator
fibonachi(n = 5)

print(f'Name of function: {fibonachi.__name__}') 
print(f'The docstring is: {fibonachi.__doc__}')
