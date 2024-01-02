# %%
from collections import namedtuple

# Named Tupple returns a class (subclass of tupple)
# name of this class is first arg passd. in below case Point2d
# it is customary to assign this class returned to a variable with same name as class name
Point2d = namedtuple('Point2d',['x', 'y'])

#now Point2d is a class which can be intantiated
pt1 = Point2d(10, 20)
print(f'str of pt1: {pt1}')
print(f'Type of pt1: {type(pt1)}')
print(f'Instance of tupple: {isinstance(pt1, tuple)}')

# contents of tupple can be accessed as
print(f'Fields of named tupple pt1: {pt1._fields}')
print(f'Values of pt1: {pt1.x}, {pt1.y}')

# Just like Tupple we can iterate using index 
# or also use keys to get values.
print(f'Index retreival: {pt1[0]}, {pt1[1]}')


# %%
# We get all methods of tupple available to named tuple

CityData = namedtuple('CityData',['city', 'country', 'population'])

city1 = CityData('London', 'UK', 56_000_000)
city2 = CityData('Paris', 'FR', 1000_000)
city3 = CityData('London', 'UK', 56_000_000)

print(f'Compare city1 and city3: {city1 == city3}')
print(f'Are city1 and city3 same : {city1 is city3}')
print(f'Compare city1 and city2: {city1 == city2}')


# %%
# Since named tuple is just a tuple we can access it as:
print(f'{tuple(city1)}')
print(f'{city1}')
# %%

# named tuples can be unpacked the same way as tuples
StockTicker = namedtuple('StockTicker',['Ticker', 'year', 'month', 'day', 'open', 'high', 'low', 'close'])
DJIA = StockTicker('DJIA', 2018, 1, 25, 26_313, 26_458, 26_260, 26_393)
symbol, *_, low, close = DJIA
print(f'Symbol: {symbol}, low: {low}, close: {close}')
print(f'Rest of unpacked values: {_}')

# %%
# named tuples are immutable. Below will lead to AttributeError: cant set attribute
DJIA.close = 100
# but we can create a new one just like making a new string

# %%
print(DJIA._fields)
print(StockTicker._fields)

# %%

# we can see tuple as an ordered dict
a = DJIA._asdict()
print(type(a))
print(a)
# %%

# lets say we got closing prince wrong on DJIA
print(f'Existing DJAI: {DJIA}')

new_closing = 26_400

*existing, _ = DJIA

print(f'Correct fields: {existing}, Incorrect: {_}')

DJIA = StockTicker(*existing, new_closing)
print(f'Modified close price DJAI: {DJIA}')

# %%

# What if open price was wrong, unpacking would be difficult now 
# we can now use slicing

print(f'Existing DJAI: {DJIA}')
pre_open = DJIA[:4]
post_open = DJIA[5:]
new_open = 26_3999

# we have to create a new tuple / iterable, to create a tuple
# We have to pass new_open as a tupple to add  to pre and post 
new_values = pre_open + (new_open, ) + post_open
print(f'New Value iterable: {new_values}')

DJIA = StockTicker(*new_values)
print(f'Modified open price DJAI: {DJIA}')

# Alternatively use ._make method and pass an iterable to make a new instance.
DJIA_2 = StockTicker._make(new_values)
print(f'DJIA_2: {DJIA_2}')

# we see both DJIA and DJIA_2 are equal
print(f"DJIA == DJAI_2: {DJIA == DJIA_2}")

# %%

# Lets say we want to change day and the High price ? 
# Above both methods are cumbersom and error prone
# named tuples have _replace instance method. Here passed keyword must match an existing one.

print(f'Existing DJAI: {DJIA}')
DJIA = DJIA._replace(day=26, open=36_399)
print(f'Modified DJAI: {DJIA}')

# %%

# if i have to create a new name tuple class but with prev day closing as well

# use _fields to extract fields from existing named tuple
existing_fields = StockTicker._fields
new_fields = existing_fields + ('prev_close', )

NewTicker = namedtuple('NewTicker', new_fields)

print(f'Fields of this new class: {NewTicker._fields}\n')

# We can even put DJIA in this new class
DJIA_new = NewTicker(*DJIA, 36_399)

print(f'DJIA: {DJIA}\n')
print(f'DJIA_new: {DJIA_new}\n')

# %%
# We can add docs to named tuples
Point2D = namedtuple('Point2D',['x', 'y'])

# so named tuples have some repr/str representation
print(help(Point2D))

# They also have doc strings
pt1 = Point2d(x=10, y=20)
print(help(pt1))
Point2D.__doc__ = 'Named Tupple for a point in 2D'
Point2D.x.__doc__ = 'x coordinate'
Point2D.y.__doc__ = 'y coordinate'
print(help(Point2D))

# %%
def my_func(a, b=10, c=20):
    print(a, b, c)

print(help(my_func))
my_func.__defaults__ = (1, 3, 5)
print(help(my_func))

# %%
# +1-2368869763

# Create a named tuple from a dict
# below 2nd arg to named tuple can be any iterable, i am using this instead of a list.
RGBstyle = namedtuple('RGBstyle', 'red green blue')
my_dict = {
    'red': 255,
    'green': 60,
    'blue': 100
}

# '**' : unpacks my_dic as key value pairs 
color1 = RGBstyle(**my_dict)
print(color1)


# %%
# lets covert this list of dictionaries to a named tupple
# usecase: data read from some api or database

data_list = [
    {'key1':1, 'key2':2},
    {'key1':3, 'key2':4},
    {'key1':5, 'key2':6, 'key3':7},
    {'key2':100}
]

# %%
# extract all unique keys,
DBData = namedtuple('DBData', {y for x in data_list for y in x})
# create a default args for named tuple
DBData.__new__.__defaults__ = (None, ) * len(struc_fields)

# unpack named args to create a named tuple
tuple_list = []
for d in data_list:
    tuple_list.append(DBData(**d))   

print(f'Tupple list : {tuple_list}')


# %%
