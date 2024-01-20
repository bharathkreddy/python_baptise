
# ZIP & ZIP_LONGEST FUNCTION 

# %%
l1 = ["a", "b", "c"]
l2 = [1, 2, 3, 4]

zip_l1_l2 = zip(l1, l2)
# Zip produces a generator and stops at shortest of things zipped.
print(list(zip_l1_l2))
# %%

from itertools import zip_longest

zip_long = zip_longest(l1, l2, fillvalue='FilledValue')
print(list(zip_long))
# %%

# ZIP STRICT MODE 

l1 = (i ** 2 for i in range(3))
l2 = (i ** 3 for i in range(4))

# If we want to ensure we are zipping similar size objects, we CAN'T do: if len(obj1) == len(obj2) then zip
# WHY? What if one of these objects is a generator or iterator, by doing len we are exhausing the Generator or Iterator
# Zip provides an argument for this, If strict is true and one of the arguments is exhausted before the others, raise a ValueError.

zip_strict = zip(l1, l2, strict=True)
print(list(zip_strict))
# %%
