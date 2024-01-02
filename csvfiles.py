# %%
import csv

# we see quote char getting ignored.
with open('actors.csv') as f:
    for row in f:
        print(row.split(","))
# %%
# we have to first open a file and create a reader obj
# Reader iterates through the file and we iterate though the reader
with open('actors.csv') as f:
    reader = csv.reader(f, delimiter=',', quotechar='"')
    for row in reader:
        print(row)
# %%
# The combo of demlimiter and quote char is often called a dialect

#list all existing dialetcts
print(csv.list_dialects())
# %%
with open('python-fundamentals-main/22 - CSV Module/03 - Dialects/actors.pdv') as f:
    reader = csv.reader(f, delimiter='|', quotechar="'", escapechar="\\", skipinitialspace=True)
    for row in reader:
        print(row)

# we can register these settings as a dialect
csv.register_dialect(
    'pdv',
    delimiter='|', 
    quotechar="'", 
    escapechar="\\", 
    skipinitialspace=True
)

print(csv.list_dialects())
with open('python-fundamentals-main/22 - CSV Module/03 - Dialects/actors.pdv') as f:
    reader = csv.reader(f, dialect='pdv')
    for row in reader:
        print(row)

# %%
