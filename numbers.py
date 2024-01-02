# %%
# TUPPLES ARE IMMUTABLE

# Tupples are immutable but if underlying obj is mutable that underlying obj can mutate
# see memory addr of the tupple post mutation

t = ([1, 2], [3, 4])
print(t, type(t), hex(id(t)))

t[0].append(5)
print(t, type(t), hex(id(t)))

# %%
# STRINGS ARE IMMUTABLE

my_var = 'kavery'
print(my_var, type(my_var), hex(id(my_var)))

# Methods on my_var returns new strings.
print(my_var.capitalize()) 
print(my_var, type(my_var), hex(id(my_var)))

# my_var[0]= 'b' : Leads to a `TypeError`
# Below new string reassigned to my_var hence addr changes.
my_var = my_var + 'Manki'
print(my_var, type(my_var), hex(id(my_var)))

# %%
a = "Bharath_is_a_bad_boy"
b = "Bharath_is_a_bad_boy"
hex(id(a)) == hex(id(b))
   
# %%
a = int("1010")
b = int("1010", base=2)
c = int("1010", base=16)
print(f"a: {a}, b: {b}, c:{c}")

# %%
a = 0b1010
print(f'Type of a: {type(a)}, decimal: {a}, octal: {oct(a)}, Hex: {hex(a)}')

# %%
a = 10
b = 3
print(f'{a} mod {b} = {a % b}, {a} // {b} = {a//b}')

# Now see this
a = -10
b = 3
print(f'{a} mod {b} = {a % b}, {a} // {b} = {a//b}')

# modulo and floor divide allways satisfy this eq
# a = b * (a //b ) + (a % b)
# a//b is floor if a/b not integer portion of a/b
# Floor of 'a' is largest integer < = a i.e. floor -3.74 = -4 and NOT -3 
# %%
0.1 + 0.1 + 0.1 == 0.3
# above is because 0.1 cannot be represented as a finite binary digits
# binary of (0.1)base10 is 0.0001100110011...(0011 repeats infinitely)

print(f'0.1 internally is : {0.1:.25f}')
print(f'0.3 internally is : {0.3:.25f}')

# HOW to solve for this ? 


# Try ABSOLUTE TOLERANCE
a = 0.1 + 0.1 + 0.1
b = 0.3

print(f'a(0.1+0.1+0.1)) - b(0.3) = {a - b:.25f}')

a = 10000.1 + 10000.1 + 10000.1
b = 30000.3
print(f'a(10000.1*3) - b(30000.3) = {a - b:.25f}')

# First one is 17th digit after decimal pt and second one is 12th

# TRY RELATIVE TOLERANCE
# Tolerance is a %'age of the larger number. 
a = 0.0000001
b = 0 
# now tolereance if 1% , 10% or any % of a, its allways going to be < a
# and diff is allways a !
# hence rel. toleance wont work !

# MATH MODULE HAS A FUNCTION
import math
a = 10000.1 + 10000.1 + 10000.1
b = 30000.3
print(f'{a}, {b}, close: {math.isclose(a, b)}')

# Below evals false as we have not mentined abs_tolerance,
# Math fun defaults to rel_tol: 1e-9, abs_tol: 0.0
a = 0.000001
b = 0.000002
print(f'{a}, {b}, close: {math.isclose(a, b)}')

a = 0.000001
b = 0.000002
print(f'{a}, {b}, close: {math.isclose(a, b, abs_tol=1e-05)}')

a = 0.01
b = 0.02 
# These two are not close! we dont want them to be equal
print(f'{a}, {b}, close: {math.isclose(a, b, abs_tol=1e-05)}')

# %%
# %%
