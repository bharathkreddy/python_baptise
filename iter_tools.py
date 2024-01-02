
# ZIP & ZIP_LONGEST FUNCTION 

# %%
l1 = ["a", "b", "c"]
l2 = [1, 2, 3, 4]

zip_l1_l2 = zip(l1, l2)
# Zip produces an iterable and stops at shortest of things zipped.
print(list(zip_l1_l2))
# %%

from itertools import zip_longest

zip_long = zip_longest(l1, l2, fillvalue='FilledValue')
print(list(zip_long))
# %%
