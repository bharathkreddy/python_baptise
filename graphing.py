# %%
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt 

# plt.subplots returns a figure and axes, if we draw more than 1 axes on a fig then a tuple is returned for axes.
fig, ax = plt.subplots()  # Create a figure containing a single axes.


# plot the points on axes.
x_pts = np.linspace(-2 * np.pi, 2 * np.pi, 100)
y_pts = np.sin(x_pts)
ax.plot(x_pts, y_pts, label='sin')  # Plot some data on the axes.# %%
ax.plot(x_pts, np.cos(x_pts), label='cos')

# X, Y labels, title and legend.
ax.set_xlabel("-2pi to 2pi")
ax.set_ylabel("Trig functions")
ax.set_title('Sin & Cos waves')
ax.legend()

# %%
# Multiple axes on same figure

# see styles and use one.
print(mpl.style.available)
mpl.style.use('seaborn-v0_8-dark')


# 2 rows & 1 col, axs is now a tupple of two axes. 
# We can also specify figsize.
fig,axs = plt.subplots(2, 1, figsize=(8, 6))
print(repr(axs))

x_pts = np.linspace(-2 * np.pi, 2 * np.pi, 100)
axs[0].plot(x_pts, np.sin(x_pts), label='sin(x)')
axs[1].plot(x_pts, np.cos(x_pts), label='cos(x)')

axs[1].set_xlabel("-2pi < x < 2pi")
axs[0].set_ylabel("Sin(x)")
axs[1].set_ylabel("Cos(x)")
axs[0].set_title('Trignometric functions')

# %%
from dateutil import parser

df = pd.read_csv('python-fundamentals-main/19 - Text Files/02 - Reading Text Files/DEXUSEU.csv')
df.info()  # Both columns are objects! Lets fix this
df.describe(include='all') # we see a '.' appearing 55 times in the second col

dates = np.array(df['DATE'].apply(parser.parse))

# Some rates have '.' these would error out, we can handle errors
# by coercing them to null values
rates = pd.to_numeric(df['DEXUSEU'], errors='coerce')
rates[rates.isnull()]  # has manu NaN

# instead of dropping we can interpoalte rates
rates = rates.interpolate(method='linear')
rates[rates.isnull()]

# %%
# %%
# %%
