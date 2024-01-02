
d1 = {'p':1, 'y':2}
d2 = {'t':0, 'h':4}
d3 = {'h':5, 'o':6, 'n':7}

y, *x = d3
print(f'y unpacked to: {y} and x to: {x}')
print([*d1, *d2, *d3])
print({*d1, *d2, *d3})

# single * unpacks keys and ** unpacks keys and values
print({**d3})

l1 = [1, 2, 3]
s = 'abc'
print([*l1, *s])



# %%
# This is how arguments are passed to fun parameters

a, *b , c = 1,2,3,4,5,6
print(a, b, c )

print(sum(b))

def my_func(a, b, *args):
    print(f'a: {a}, b: {b}, args: {args}')

my_func(1,2,3,4,5,6)

def my_func2(*args):
    print(f'args: {args}')

my_func2(1,2,3,4,5,6)

# Anything after * has to be keyword arg
def my_func3(a, *args, c):
    print(f'a: {a}, c: {c}, args: {args}')

my_func3(1,2,3,4,5,c=6)


# Anything after * has to be a keyword arg
def my_func4(a, *args, **kwarg):
    print(f'a: {a}, args: {args}, kwargs: {kwarg}')

my_func4(1,2,3,4,5, x=41, y=42)

# alternatively
my_dict = {"x":41, "y":42 }
my_func4(1,2,3,4,5, **my_dict)

# * indicates end of positional args
def my_func5(a, b=10, *, d, e=20):
    print(a, b, d, e)

my_func5(1, d=3)

# just a * means no positional args are possible
# and no args would be scooped out by *
def my_func6(* , a, b):
    print(a, b)

my_func6(a=2, b=3)

# below means no positional args possible, first keyword arg
# goes to d and rest are scopped by **kwargs
' def func(*, d, **kwargs)'

# %%

# Function defs along with default values are set when function object is created not at run time
import time
import datetime 
def my_log(msg, * , dt=datetime.datetime.now(datetime.UTC)):
    print(f'{dt}: {msg}')
    print("sleeping for 5 seconds")
    time.sleep(5)
    print(f'{dt}: {msg}')
    print("Why are timestamps the same ?")

my_log('Message has time stamp')

# FID

def my_log(msg, * , dt=None):
    dt = dt or datetime.datetime.now(datetime.UTC)
    print(f'{dt}: {msg}')

my_log('Message has time stamp')
# %%
# annotations and doc strings are stored with the object.
def my_func(a:'str1', b:'str2'='brk') -> 'string concat':
    '''This function takes a string and adds brk to it'''
    return a + " " + b

print(my_func('hello'))
print(my_func.__doc__)
print(my_func.__annotations__)
# %%

my_func.__doc__ = "Docs now changed"
print(help(my_func))
print(my_func('kavery'))
print(my_func.__doc__)
# %%

# LAMBDA FUNCTION
# ' lambda [parameter list]: expression '
# dont add [] to parameters list, ':' indicates end of parameters
# expression is evaluated and returned.a
# Lambdas cant have annotations, or assigments in expression.

# use a labda expression to sort an iterable in random order
import random
sorted([1,2,3,4,5], key=lambda x: random.random())


# %%

# FUNCTION INTROSPECTION

# this is a function to test function instrospection.
# introspection means - to introspect code using code.
def my_func(a: "mandatory positional", 
            b: "Optional Positional"=1,  
            c=2, 
            *args: "scoops all positionals", 
            kw1: "mandatory key word", 
            kw2=100, 
            kw3=200, 
            **kwargs: "scoops all key words"):
    """This function does nothing"""
    i = 10
    j = 20
    return a

print(dir(my_func))   
print(f'docs: {my_func.__doc__}')
print(f'annotations: {my_func.__annotations__}')
print(f'name: {my_func.__name__}')
print(f'Defaults: {my_func.__defaults__}')
print(f'KW Defaults: {my_func.__kwdefaults__}')
print(f'Code: {my_func.__code__}')
print(f'Code_Name: {my_func.__code__.co_name}')
print(f'Code_Arg_count: {my_func.__code__.co_argcount}: Counts only positional args')
print(f'Code_Var_Names: {my_func.__code__.co_varnames}Gives class vars too.')

# %%

# INSPECT MODULE

import inspect
a = 10
print(f'\na is a function: {inspect.isfunction(a)}')
print(f'\nmy_func is a function: {inspect.isfunction(my_func)}')

class MyClass:
    def f(self):
        pass

my_obj = MyClass()
print(f'\nmy_obj.f is a function: {inspect.isfunction(my_obj.f)}')
print(f'\nmy_obj.f is a Method:: {inspect.ismethod(my_obj.f)}')

print(f'\nSource Code :\n{inspect.getsource(my_func)}')
print(f'\nModule of sin function: {inspect.getmodule(math.sin)}')

print(f'\nComments preceding the function:\n{inspect.getcomments(my_func)}')
print(f'\nFunction Signature:\n{inspect.signature(my_func)}')

print(f'\nSignature_more properties:\n {type(inspect.signature(my_func).parameters)}\n')

for param in inspect.signature(my_func).parameters.values():
    print(f'Name :{param.name}')
    print(f'Default :{param.default}')
    print(f'Annotation :{param.annotation}')
    print(f'Kind :{param.kind}')
    print('-----------------------')



# %%
# Lets try what position only args are
print(help(divmod))
# a '/' in function parameters indicate everything before it has to be postion only
for param in inspect.signature(divmod).parameters.values():
    print(f'Name :{param.name}')
    print(f'Default :{param.default}')
    print(f'Annotation :{param.annotation}')
    print(f'Kind :{param.kind}')
    print('-----------------------')
# %%

# CALLABLES
# Any object taht can be called using () operator
# Allways return a value 
print(f'is my_obj.f a callable: {callable(my_obj.f)}\n')
print(f'is upper a callable: {callable(str.upper)}\n')
print(f'is 10 a callable: {callable(10)}\n')

# %%
# Higher order Functions take as argument or return another function
# example: map, sorted (takes key which is a function), filter.

l = [2, 3, 4]
def sq(x):
    return x**2

# Takes in 2 args, 1st one Sq , 2nd list l
print(list(map(sq, l)))

def add_list(x, y):
    return x + y

# now since add_list takes 2 args, map has to be provided 2 lists, 
# map stops at shortest iterable, notice longer len of sencond list.
print(list(map(add_list, l, [10, 11, 12, 13, 15])))

# FILTER take 1 func and one iterable and determines if we take in or discard an item of iterable

print(list(filter(lambda x: x % 2 == 0, l)))

# if None is passed the filter just evaluates truthy/falsy value of iterable
l = [-1,[], ['a', 'b'], None, 3, 4]
print(list(filter(None, l)))

# MAP and FILTER return iterables, so not reusable once drained.

# %%
# REDUCING FUNCTIONS: recombine an iterable recursively, ending up with single value
from functools import reduce

l = [5, 8, 6, 10 ,9]
x = reduce(lambda a, b: a if a > b else b, l)
print(x)

print(reduce(lambda a, b: a+b, l))
print(reduce(lambda a, b: a*b, l))

# Reduce works on any iterable
l = 'pythonbharath'
print(reduce(lambda a,b : a if a>b else b, l))
print(reduce(lambda a, b: a + "~"+b, {'python','is','awsome'}))

# %%
# any(iterable) -> True if any element is truthy else false
# all(iterable) -> True if every element truthy else false

print(f'any: {any(['a',[1, 2],{}])}')
print(f'all: {all(['a',[1, 2],{}])}')

# %%

# PARTIAL FUNCTIONS
from functools import partial

def my_func(a, b, c):
    return(a, b, c)

# partial functions reduce no of arguments required for a function
def f(x, y):
    return my_func(10, x, y)

print(f(20, 30))

# can also do this as 
f = lambda x, y: my_func(10, x, y)
print(f(20, 30))

# of use functools
f = partial(my_func, 10)
print(f(20, 30))

f = partial(my_func, 10, 20)
print(f(30))


# %%
