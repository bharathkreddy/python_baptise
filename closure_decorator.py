# LEXICAL SCOPE OF A VARIABLE: The portion of code where the name/binding is defined.
# NAMESPACE is where these bindings are stored. Every scope has its own namespace.
#  - BUILT-IN SCOPE: print, true , false etc, available everywhere to be used. 
#  - - GLOBAL SCOPE: module scope, spans a single file. 
#  - - - LOCAL SCOPE: Functions when defined, python would determine variable's scope, when function is called - the scope is created

# Python doesnt create scopes for code blocks or loops like for and while loops.
# %%
# when a function is done running all local scope bindings are destoryed
# At compile time, python looks at a function and anything that has an assignment, will be counted as local var. 
# At run time these local vars are created, and rest are looked up in below order
# Local Scope >> NON-local enclosing chains >> Global >> Built-in

a = 100

def my_func1():
    print(a)

# At compile time a was deemed a global var and hence prints 100
my_func1()

def my_func2():
    a = 10
    print(a)

# At compile time since 'a' has assigment - it is deemed local variable and prints 10
my_func2()

# this function will get "UnboundLocalError", since at compile time "a" has assigment and hence is deemed local
# But at run time we are calling print(a) before defining a , hence python cant find "a" in local scopes namespace.
def my_func3():
    print(a)
    a = 1
    print(a)

# %%
# GLOBAL keyword : to access a global namespace variable inside a local scope.

# prints a = 100 as a is global , modifies global a and prints 1
def my_func4():
    global a
    print(a)
    a = 1
    print(a)

my_func4()

# Global 'a' modified to 1 by function and now 'a' = 1
print(a)

# if a var is defined as global, the var need not exist, python will create this at runtime
# the var : brk_var doesnt exist, but created at runtime, determined to be global at compile time.
def my_func5():
    global brk_var
    brk_var = "hello brk"
    print('function run')

my_func5()
print(brk_var)
# %%
# NON LOCAL keyword is used to access variables from enclusing local scopes. 

a = 10

def outer_func():
    a = 100

    def inner_func():
        print(a)
    
    inner_func()

# Prints out 'a' = 100 , this was fetched from ENCLOSING SCOPE of local scope which called it.
# here inner_func calls it , and python cant find a in that scope and looks at enclosing space.
outer_func()

a = 10
def outer_func():

    def inner_func():
        print(a)
    
    inner_func()

# Now 'a' cant be found in enclusing scope hence python looks at global scope.
outer_func()

# %%
# MODIFYING a NONLOCAL variable

a = 10
def outer_func():
    a = 'hello'

    def inner_func():
        a = 'BRK'
        print(f'Called by inner_func: {a}')

    inner_func()
    print(f'Called by outer_func: {a}')

outer_func()
print(f'called from Module: {a}\n')

# FREE VARIABLE : are NON LOCAL vars (vars in outer func) refered inside a scope of a nested function.
# GLOBAL var left untouched and non-local var changed by inner function.
a = 10
def outer_func():
    a = 'hello'

    def inner_func():
        nonlocal a
        a = 'BRK'
        print(f'Called by inner_func: {a}')

    inner_func()
    print(f'Called by outer_func: {a}')

outer_func()
print(f'called from Module: {a}\n')


# since a in outer_func is 
a = 10
def outer_func():
    global a
    a = 'hello'

    def inner_func():
        nonlocal a
        a = 'BRK'
        print(f'Called by inner_func: {a}')

    inner_func()
    print(f'Called by outer_func: {a}')

outer_func()
print(f'called from Module: {a}\n')

# %%

# CLOSURES

# the free variable x lives outside inner name space but is bound to it. 

def outer():
    x = 'python'
    
    def inner():
        print(f'{x} rocks !!')
    
    inner()

outer()

# %%
# What if instead of calling inner() we just return it ? 

def outer():
    x = 'python'
    
    def inner():
        print(f'{x} rocks !!')
    
    return inner

a = outer()
print(type(a))
# when we do this - "a" REMEMBERS x despite outer() going out of scope / finished running.
a()

# this is because when we return "inner" we return function inner + assiciated free variables 
# this inner + associated free variables is called 'CLOSURE'

# %%

# INTUITION FOR CLOSURES

# the LABEL 'x' is in two different scopes but allways references the SAME value = 'python'.
# The way python does it, is by creating an object called CELL. 
# CELL contains memory addr of free variable, in our case to string 'python'
# now outer x is pointed to CELL which points to 'python'
# inner x also points to CELL which points to 'python' 

def outer():
    x = 'python'
    print(f'Memory of {x} : {hex(id(x))}')

    def inner():
        print(f'Memory of {x} : {hex(id(x))}')
        
    return inner

fn = outer()
fn()
# SEE THE CELL OBJECT point to STR OBJECT and memory addr of STR OBJ.
print(f'closure object: {fn.__closure__}')
print(f'Free variables: {fn.__code__.co_freevars}')
# %%

def counter():
    count = 0

    def inner():
        nonlocal count
        count += 1
        print(count)

    return inner

f1 = counter()
f2 = counter()

# Notice CELLS for each closure is pointing to same memory of count
print(f'closure object: {f1.__closure__}')
print(f'Free variables: {f1.__code__.co_freevars}')

print(f'closure object: {f2.__closure__}')
print(f'Free variables: {f2.__code__.co_freevars}')

# count is seperate for both f1 and f2, but now see where the CELLS point to. 
# This happens because every time a function is called , it creates a new scope
# in our case COUNTER was called twice ( one each for f1 and f2)
# each of these created different scopes and closures returned were in different scopes.
f1()
f1()
f2()

# This is because f1 and f2 are diff runs of counter and hence create diff scope and each scope has its own variable called count.
print(f'closure object: {f1.__closure__}')
print(f'closure object: {f2.__closure__}')

# %%
# example of shared scope for closures

def counter():
    count = 0

    def inner1():
        nonlocal count
        count += 1
        print(count)
    
    def inner2():
        nonlocal count
        count += 1
        print(count)

    return inner1, inner2

f1, f2 = counter()

f1()
f1()
f1()
f2()

# SAME CELL for both f1 and f2 as they were created at same scope when outer was called.
# both closures are refereing to same COUNT
print(f'closure object: {f1.__closure__}')
print(f'closure object: {f2.__closure__}')

# CLOSURE IS CREATED WHEN FUNCTION IS CREATED.
# FREE VARIABLES ARE EVALUATED WHEN THE FUNCTION IN THE CLOSURE IS CALLED.

# %%

# MISTAKE
# since all closures were created in same scope all adders were created with same CELL pointint to n.
def create_adders():
    adders = []
    for n in range(1, 4):
        adders.append(lambda x: x+n)
    return adders

adders = create_adders()
  
for adder in adders:
    print(f'{adder}, Closure: {adder.__closure__}, free var: {adder.__code__.co_freevars}')

# cell not points to n = 3 as taht was the the last n of range. and adders have same CELL which points to n.
for addr in adders:
    print(addr(10))

for adder in adders:
    print(f'{adder}, Closure: {adder.__closure__}, free var: {adder.__code__.co_freevars}')

# %%
# Difference between above and below is, functions when run create different scopes each time
# while loops or lambda functions do not create a different scope. 

def outer(n):
    def inner(x):
        return x + n
    return inner

adders = []
for n in range(1, 4):
    adders.append(outer(n))

for adder in adders:
    print(f'{adder}, Closure: {adder.__closure__}, free var: {adder.__code__.co_freevars}')
    
for addr in adders:
    print(addr(10))
  
for adder in adders:
    print(f'{adder}, Closure: {adder.__closure__}, free var: {adder.__code__.co_freevars}')
# %%

# Lets write a class to average the inputs as they are added. 

class Averager:
    def __init__(self):
        self.sum = 0
        self.count = 0
    def add(self, number):
        self.sum += number
        self.count +=1
        return self.sum / self.count

a = Averager()
print(a.add(10))
print(a.add(20))
print(a.add(30))
# %%

# Lets write above class as a function
def Averager():
    sum = 0
    count = 0
    def add(number):
        nonlocal sum
        nonlocal count
        sum += number
        count += 1
        return sum / count

    return add

a = Averager()
print(a(10))
print(a(20))
print(a(30))


# %%

def Averager():
    sum = 0
    count = 0
    def add(number):
        nonlocal sum
        nonlocal count
        sum += number
        count += 1
        return sum / count

    return add

add = Averager()

a = Averager()
print(a(10))
print(a(20))
print(a(30))

# %%

# Lets write a class and closure to take a function and log time taken for function to execute
from time import perf_counter, sleep

class perf_monitor():
    def __init__(self):
        self.start = perf_counter()

    def poll(self):
        return perf_counter() - self.start

a = perf_monitor()
print(a.poll())

# %%
# instead of having to do a.poll() we can make a callable by adding __call__ magic method to the class.
from time import perf_counter, sleep

class perf_monitor():
    def __init__(self):
        self.start = perf_counter()

    def __call__(self):
        return perf_counter() - self.start

a = perf_monitor()
print(a())
sleep(5)
print(a())

# %%

# same thing in closure

def perf_monitor():
    start = perf_counter()
    def poll():
        return perf_counter() - start
    return poll

a = perf_monitor()
sleep(5)
print(a())
sleep(5)
print(a())


# %%

# Lets build a counter of a function to track how many times a function has been run.
# Step1: lets build a simple incrementer.

def counter(intial_value=0):
    def incrementer():
        nonlocal intial_value
        intial_value += 1
        return intial_value
    return incrementer

a = counter(2)
print(a, type(a), a.__closure__)
print(a())
print(a())
print(a())


# %%

# step 2: Lets expand this to take a function.
def add(a, b):
    return a + b

def mul(a, b):
    return a * b

func_counter = {}

def counter(fn):
    def incrementer(*args, **kwargs):
        global func_counter
        func_counter[fn.__name__] = func_counter.get(fn.__name__, 0) + 1
        return fn(*args, **kwargs)
    return incrementer

a = counter(add)
print(func_counter)
print(a(10, 20))
print(func_counter)
print(a(15, 5))
print(func_counter)
b = counter(mul)
print(b(15, 5))
print(func_counter)


# %%
# what if instead of 'a' and 'b' we replace them with function names ?
# we have modified the function to have more functionality without changing the code of function.

def add(a, b):
    return a + b

def mul(a, b):
    return a * b

print(add, type(add), add.__closure__)
print(mul, type(mul), mul.__closure__)


func_counter = {}

def counter(fn):
    def incrementer(*args, **kwargs):
        global func_counter
        func_counter[fn.__name__] = func_counter.get(fn.__name__, 0) + 1
        print(fn.__name__)
        return fn(*args, **kwargs)
    return incrementer


add = counter(add)
mul = counter(mul)
print(add, type(add), add.__closure__)
print(mul, type(mul), mul.__closure__)


print(add(1, 3))
print(add(100, 101))
print(mul(2, 7))
print(func_counter)

# %%

# DECORATORS ~~~~~

# 1. Takes a function as an argument. 
# 2. Returns a closure.
# 3. Closure usually accepts any combination of parameters. 
# 4. Runs some code in inner fn (closure)
# 5. The closure calls original function using args passed. 
# 6. Returns whatever is returned by that function call. 
# 7. In general if `func` is a decorator and we want to decorate `my_func` we do
#    my_func = func(my_func)
# 8. or use `@func` on top of my_func definition.

# we want to decorate add and mult to generate logs.
# Lets define a decorator and then decorate our functions

def logger(fn):
    count = 0
    def inner(*args, **kwargs):
        nonlocal count
        count += 1
        print(f"{fn.__name__} run {count} times")
        return fn(*args, **kwargs)

    return inner

def add(a, b):
    return a + b

def mult(a, b):
    return a * b

add = logger(add)
mult = logger(mult)
print(add(1, 5))
print(mult(11, 15))
print(add(7, 8))

# %%
# Alternate way of doing this would be

def logger(fn):
    count = 0
    def inner(*args, **kwargs):
        nonlocal count
        count += 1
        print(f"{fn.__name__} run {count} times")
        return fn(*args, **kwargs)

    return inner

@logger
def add(a, b):
    return a + b

@logger
def mult(a, b):
    return a * b

print(add(10, 5))
print(mult(11, 3))
print(add(4, 1))

# %%

# Problem with decorators is : function decorated always points to inner now
# we loose name, docstrings and everything associated with original function.

def logger(fn):
    count = 0
    def inner(*args, **kwargs):
        nonlocal count
        count += 1
        print(f"{fn.__name__} run {count} times")
        return fn(*args, **kwargs)

    return inner

@logger
def add(a, b):
    """Adds two numbers"""
    return a + b


def mult(a, b):
    """Multiplies two numbers"""
    return a * b


print(add.__name__)
print(add.__doc__)
print(help(add))

print('\n\nMULT is not decorated and retains its name, and doc strings\n\n')
print(mult.__name__)
print(mult.__doc__)
print(help(mult))
print(mult.__doc__)
# %%

# HOW TO FIX THIS ~~~~~~~~~
import inspect

def logger(fn):
    """decorator for a function"""
    count = 0
    def inner(*args, **kwargs):
        """Inner function of the decorator"""
        nonlocal count
        count += 1
        print(f'Function {fn.__name__} called {count} times')
        return fn(*args, **kwargs)
    inner.__doc__ = fn.__doc__
    inner.__name__ = fn.__name__
    return inner 

@logger
def add(a, b):
    """Returns addition of two args passed"""
    return a + b

@logger
def mult(a, b):
    """Returns multiplication of two args passed"""
    return a * b

print(add(10,20))
print(add.__name__)
print(add.__doc__)
print(help(add))

print(mult(5, 7))
print(mult.__name__)
print(mult.__doc__)
print(help(mult))
print('\n\nBut what about function signature ?\n\n')
print(inspect.signature(add))
# %%
# Easier method to fix ~~~~~~~~~~
# the functools.wraps function. 

from functools import wraps
import inspect

def logger(fn):
    """decorator for a function"""
    count = 0
    def inner(*args, **kwargs):
        """Inner function of the decorator"""
        nonlocal count
        count += 1
        print(f'Function {fn.__name__} called {count} times')
        return fn(*args, **kwargs)
    # wraps(fn) returns a function wich takes another parameter (inner)
    inner = wraps(fn)(inner)
    return inner 

@logger
def add(a, b):
    """Returns addition of two args passed"""
    return a + b

print(add(10,20))
print(add.__name__)
print(add.__doc__)
print(help(add))
print(inspect.signature(add))
# %%
# wraps(fn) is also acting like a decorator and hence we can re-factor as 

from functools import wraps
import inspect

def logger(fn):
    """decorator for a function"""
    count = 0
    # this wraps decorator allows inner to modify doc string, signature, 
    # name etc of inner to match that of the function it is decorating
    @wraps(fn)
    def inner(*args, **kwargs):
        """Inner function of the decorator"""
        nonlocal count
        count += 1
        print(f'Function {fn.__name__} called {count} times')
        return fn(*args, **kwargs)

    return inner 

@logger
def add(a: int|float, b: int|float) -> int|float:
    """Returns addition of two args passed"""
    return a + b

print(add(10,20))
print(add.__name__)
print(add.__doc__)
print(help(add))
print(inspect.signature(add))


# %%

# DECORATOR FACTORY / DECORATORS THAT TAKE PARAMETERS
# Lets write a decorator that does 'n' reps of a function and returns avg time taken for function to run

from time import perf_counter
from functools import wraps

def timer(n):
    def timer_outer(fn):
        @wraps(fn)
        def timer_inner(*args, **kwargs):
            sum = 0
            count = 0
            for i in range(n+1):
                start_time = perf_counter()
                result = fn(*args, **kwargs)
                sum += perf_counter() - start_time
                count += 1       
            print(f'fn: {fn.__name__}, run time: {sum / count} secs over {n} runs.\n')
            
            return result

        return timer_inner

    return timer_outer

@timer(20)
def fact(n: int)-> int:
    """Returns factorial of an integer passed as argument"""
    res = 1
    for i in range(1,n+1):
        res *= i
    return res

x = fact(999)
print(help(fact))
print(inspect.signature(fact))


# %%
# Another example to see how to pass variables to a decorator.

from functools import wraps
import random

a = random.randint(1, 10)
b = random.randint(50, 100)

def my_dec_factory(a, b):
    def my_dec(fn):
        @wraps(fn)
        def inner(*args, **kwargs):
            print(f'ran with decorated func with decorator params:{a},{b}')
            print(f'fn: {fn.__name__}, docstring: {fn.__doc__}')
            return fn(*args, **kwargs)
        return inner
    return my_dec

@my_dec_factory(a, b)
def my_add(a: int, b: int) -> int:
    """adds two integers"""
    return a + b

print(f'result:{my_add(10, 11)}\n\n')
print(help(my_add))
# %%

# DECORATING A CLASS
import math 

def Point2D_extender(cls):
    if '__eq__' in dir(cls) and '__lt__' in dir(cls):
        cls.__ge__ = lambda self, other: not( self < other )
        cls.__le__ = lambda self, other: self < other or self == other
        cls.__gt__ = lambda self, other: not(self < other) and not (self == other)

    return cls

@Point2D_extender
class Point2d:
    def __init__(self, x: int, y: int) -> Point2d:
        self.x = x
        self.y = y

    @property
    def x(self):
        return self._x
    
    @x.setter
    def x(self, x):
        if isinstance(x, int|float):
            self._x = x
        else:
            raise NotImplemented("Coordinates take only int and float values")

    @property
    def y(self):
        return self._y
    
    @y.setter
    def y(self, y):
        if isinstance(y, int|float):
            self._y = y
        else:
            raise NotImplemented("Coordinates take only int and float values")

    def dist(self):
        return math.sqrt(self.x **2 + self.y **2)

    def __str__(self):
        return f'{self.__class__.__name__}(x={self.x}, y={self.y})'

    def __eq__(self, other_point):
        if isinstance(other_point, Point2d):
            return self.dist() == other_point.dist()
        else:
            raise NotImplemented(f'{self.__class__.__name__} and {other_point.__class__.__name__} not comparable')

    def __lt__(self, other_point):
        if isinstance(other_point, Point2d):
            return self.dist() < other_point.dist()
        else:
            raise NotImplemented(f'{self.__class__.__name__} and {other_point.__class__.__name__} not comparable')


p1 = Point2d(1, 1)
p2 = Point2d(2, 2)
p3 = Point2d(2, 2)

print(f'Similarity Test p2,p3: {p2 is p3}')
print(f'Equality Test p2,p3: {p2 == p3}')
print(f'Lessthan Test p1,p2: {p1 < p2}')
print(f'Lessthan Test p2,p1: {p2 < p1}')
print(f'Lessthan Test p2,p3: {p2 < p3}')
print(f'LESS THANK EQUAL IMPLEMENTED NOW {p1 <= p2}')

# %%

# Above pattern is so common (its called MONKEY PATCHING) that there is a functool method available

import functools

@functools.total_ordering
class Point2d:
    def __init__(self, x: int, y: int) -> Point2d:
        self.x = x
        self.y = y

    @property
    def x(self):
        return self._x
    
    @x.setter
    def x(self, x):
        if isinstance(x, int|float):
            self._x = x
        else:
            raise NotImplemented("Coordinates take only int and float values")

    @property
    def y(self):
        return self._y
    
    @y.setter
    def y(self, y):
        if isinstance(y, int|float):
            self._y = y
        else:
            raise NotImplemented("Coordinates take only int and float values")

    def dist(self):
        return math.sqrt(self.x **2 + self.y **2)

    def __str__(self):
        return f'{self.__class__.__name__}(x={self.x}, y={self.y})'

    def __eq__(self, other_point):
        if isinstance(other_point, Point2d):
            return self.dist() == other_point.dist()
        else:
            raise NotImplemented(f'{self.__class__.__name__} and {other_point.__class__.__name__} not comparable')

    def __lt__(self, other_point):
        if isinstance(other_point, Point2d):
            return self.dist() < other_point.dist()
        else:
            raise NotImplemented(f'{self.__class__.__name__} and {other_point.__class__.__name__} not comparable')


p1 = Point2d(1, 1)
p2 = Point2d(2, 2)
p3 = Point2d(2, 2)

print(f'Similarity Test p2,p3: {p2 is p3}')
print(f'Equality Test p2,p3: {p2 == p3}')
print(f'Lessthan Test p1,p2: {p1 < p2}')
print(f'Lessthan Test p2,p1: {p2 < p1}')
print(f'Lessthan Test p2,p3: {p2 < p3}')
print(f'<= IMPLEMENTED NOW {p1 <= p2}')


# %%

#