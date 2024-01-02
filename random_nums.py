# %%
import random

random.seed(42)
data = [random.randint(1,10) for i in range(100)]

def plot_freq(data):
    fr_data = {}
    for el in data:
        fr_data[el] = fr_data.get(el, 0) + 1

    for el in sorted(fr_data):
        print(f'{el:>2}| {"*" * fr_data[el]}' )


plot_freq(data)
# %%
random.seed(42)
data = [random.randint(1,10) for i in range(10_000_000)]
def plot_freq2(data):
    fr_data = {}
    for el in data:
        fr_data[el] = fr_data.get(el, 0) + 1

    tot = sum([v for k,v in fr_data.items()])

    for el in sorted(fr_data):
        print(f'{el:>2}| {fr_data[el] / tot * 100 :4.1f}%' )

plot_freq2(data)

# %%

# Shuffling is in-place shuffle of a mutable sequence
random.seed(42)

l = [1, 2, 3, 4, 5]
random.shuffle(l)
print(l)

# Choice/Choices to choose 1/more el from a sequence, WITH replacement
l = [1, 2, 3, 4, 5]
for _ in range(5):
    print(random.choice(l))

for _ in range(5):
    print(random.choices(l, k=3))


# Weighted Choice allows assigment of weight to each el of seq to assign prob of them getting chosen.abs
wt = [.01, .01, .01, .96, .01]
for _ in range(5):
    print(random.choices(l, weights=wt ,k=3))


# Sample to choose 1 or more el from a seq, WITHOUT replacement
for _ in range(5):
    print(random.sample(l,4))



# %%

# DECIMAL module uses more precise repr of decimals

#Below returns negaive
0.1 + 0.1 +0.1 == 0.3

import decimal
# if we pass float its allready approx
print(decimal.Decimal(0.1))
print(decimal.Decimal('0.1'))




# %%
