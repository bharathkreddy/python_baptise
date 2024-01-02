# %%
import math
from numbers import Number

class Circle:
    """Creates a cricle with area and perimeter methods"""
    def __init__(self, radius):
        if radius < 0 or not isinstance(radius, Number):
            raise ValueError("Circle Radius cannot be negative or non integer")
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return math.pi * self.radius * 2

    def __str__(self):
        return f'{self.__class__.__name__} of radius {self.radius}'
    
    def __eq__(self, other_circle):
        return self.radius == other_circle.radius

    def __lt__(self, other_circle):
        if isinstance(other_circle, Circle):
            return self.radius < other_circle.radius
        raise TypeError(f"'<' not supported between instances of '{self.__class__.__name__}' and '{other_circle.__class__.__name__}'")

    
# %%
c1 = Circle(10.1)
c2 = Circle(10)
c3 = Circle(12)

print(hex(id(c1)), repr(c1))
print(hex(id(c2)), repr(c2))

print(c1 is c2)
print(c1 == c2)
print(c1 < c3)
print(c1 > c1)
print(c1 < 3)


# %%
# With bare attributes, these are exposed to being set arbitarily by caller.
# NOTE radius is an attribute and hence can be used as .radius instead of .radius(), but area is a method and has to be called as .area()
c1 = Circle(10)
print(c1.radius, c1.perimeter())
c1.radius = 's'
print(c1.__dict__)


# %%
# GETTER: Read only property 
## a. Define a method, with name of the property
## b. decorate the method with @property

class Circle:
    """Creates a cricle with area and perimeter methods"""
    def __init__(self, radius):
        if radius < 0 or not isinstance(radius, Number):
            raise ValueError("Circle Radius cannot be negative or non integer")
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return math.pi * self.radius * 2

    def __str__(self):
        return f'{self.__class__.__name__} of radius {self.radius}'
    
    def __eq__(self, other_circle):
        return self.radius == other_circle.radius

    def __lt__(self, other_circle):
        if isinstance(other_circle, Circle):
            return self.radius < other_circle.radius
        raise TypeError(f"'<' not supported between instances of '{self.__class__.__name__}' and '{other_circle.__class__.__name__}'")

# Decorate any function with @property to turn it from a function into a property
c = Circle(1)
print(c.radius)
c.radius = -10  #<- Blows up as the property is readonly.


# %%
# Setter method to allow changes to variables post instantiation

class Circle:
    """Creates a cricle with area and perimeter methods"""
    def __init__(self, radius):
        if radius < 0 or not isinstance(radius, Number):
            raise ValueError("Circle Radius cannot be negative or non integer")
        self._radius = radius

    @property
    def radius(self):
        print('Radius getter called...')
        return self._radius

    @radius.setter
    def radius(self, new_radius):
        print('Radius setter called...')
        if new_radius < 0 or not isinstance(new_radius, Number):
            raise ValueError("Circle Radius cannot be negative or non integer")
        self._radius = new_radius

    @property
    def area(self):
        print('Area property called...')
        return math.pi * (self.radius ** 2)

    @property
    def perimeter(self):
        return math.pi * self.radius * 2

    def __str__(self):
        return f'{self.__class__.__name__} of radius {self.radius}'
    
    def __eq__(self, other_circle):
        return self.radius == other_circle.radius

    def __lt__(self, other_circle):
        if isinstance(other_circle, Circle):
            return self.radius < other_circle.radius
        raise TypeError(f"'<' not supported between instances of '{self.__class__.__name__}' and '{other_circle.__class__.__name__}'")


c = Circle(1)
print(c.radius)
try:
    c.radius = -10 
except ValueError as e:
    print(f"{e}")

c.radius = 10
print(c.radius)
print(c.area)  #this calls area property which in turn calls getter to get the radius values.

# this gives us control on attributes of a class. However if someone wants to change _radius - they can. 
# Python is concenting adults world of no locks on door but having _ in front of a variable indicates that its a private var.
# Area is a calculated property and hence makes sense NOT to have a setter for it.
# without a setter we cant do below. 
c.area = 100
print(c.area)

# %%

# we can get rid of duplicate code in __init__ and setter methods by 
# calling the setter from __init__ directly and build checks only in setter.

class Circle:
    """Creates a cricle with area and perimeter methods"""
    def __init__(self, radius):
        self.radius = radius

    @property
    def radius(self):
        print('Radius getter called...')
        return self._radius

    @radius.setter
    def radius(self, new_radius):
        print('Radius setter called...')
        if not isinstance(new_radius, Number) or new_radius < 0:
            raise ValueError("Circle Radius cannot be negative or non integer")
        self._radius = new_radius

    @property
    def area(self):
        print('Area property called...')
        return math.pi * (self.radius ** 2)

    @property
    def perimeter(self):
        return math.pi * self.radius * 2

    def __str__(self):
        return f'{self.__class__.__name__} of radius {self.radius}'
    
    def __eq__(self, other_circle):
        if isinstance(other_circle, Circle):
            return self.radius < other_circle.radius
        raise TypeError(f"'=' not supported between instances of '{self.__class__.__name__}' and '{other_circle.__class__.__name__}'")

    def __lt__(self, other_circle):
        if isinstance(other_circle, Circle):
            return self.radius < other_circle.radius
        raise TypeError(f"'<' not supported between instances of '{self.__class__.__name__}' and '{other_circle.__class__.__name__}'")

c = Circle(1) # <- This calls a setter via __init__ method
print(c.radius, c.area)
c.radius = 10
print(c.radius, c.area)

# to ensure below work, we have to first check the isinstance then the negative check.
# this is because, if we do negative check first then 's' is compared against 0 which throws
# str cant be compared to 0 error !
c = Circle('s')

# IMPORTANT NOTE
## we cannot do return self.radius in getter as this would again call the getter which returns a call back to getter
## This would cause infinite recursion.
## return a private variable in getter.

# %%
"""
Write a custom class that will be used to model a single bank account.
Your class should implement functionality to:
- allow initialization with values for `first_name`, `last_name`, `account_number`, `balance`, `is_overdraft_allowed`
- keep track of a "ledger" that keeps a record all transactions (just use a list to keep track of this)
    - at a minimum it should keep track of the transaction date (the current UTC datetime) and the amount 
    (positive, or negative to indicate deposits/withdrawals) 
    - later you could add tracking the running balance as well.
- provide read-only properties for `first_name`, `last_name`, `account_number` and `balance`
- provide a property to access the ledger in such a way that a user of this class cannot mutate the ledger directly
- provide a read-write property for `is_overdraft_allowed` that indicates whether overdrafts are allowed on the account.
- provide methods to debit (`def withdraw`) and credit (`def deposit`) transactions that:
    - verify withdrawals against available balance and `is_overdraft_allowed` flag
        - if withdrawal is larger than available balance and overdrafts are not allowed, 
        this should raise a custom `OverdraftNotAllowed` exception.
        - if transaction value is not positive, this should raise a `ValueError` exception 
        (we have separate methods for deposits and withdrawals, and we expect the value to be positive in both cases 
        - one will add to the balance, one will subtract from the balance).
    - add an entry to the ledger with a current UTC timestamp (positive or negative to indicate credit/debit)
    - keeps the available balance updated
- implements a good string representation for the instance (maybe something like `first_name last_name (account_number): balance`
- Two accounts should be considered equal if the account numbers are the same.
"""

# %%
from numbers import Number
import datetime

class OverdraftNotAllowedError(Exception):
    pass


class BankAccount:
    """Bank account class, allows credit and debit methods and has first_name, last_name, bal and overdraft properties"""
    def __init__(self, first_name, last_name, account_number, balance=0, is_overdraft_allowed=False):
        self._first_name = first_name
        self._last_name = last_name
        self._account_number = account_number
        self._balance = balance
        self.is_overdraft_allowed = is_overdraft_allowed
        self._ledger = []

    @property
    def ledger(self):
        return self._ledger

    @property
    def first_name(self):
        return self._first_name

    @property
    def last_name(self):
        return self._last_name

    @property
    def account_number(self):
        return self._account_number

    @property
    def balance(self):
        return self._balance

    @property
    def is_overdraft_allowed(self):
        return self._is_overdraft_allowed

    @is_overdraft_allowed.setter
    def is_overdraft_allowed(self, od_bool):
        if not isinstance(od_bool, bool):
            raise ValueError("OverDraft should be a boolean True or False.")
        self._is_overdraft_allowed = od_bool

    def deposit(self, amount):
        if not isinstance(amount, Number):
            raise TypeError("Amount to deposit should be a number.")
        if amount < 0:
            raise ValueError("Amount to deposit cant be negative.")
        self._balance += amount
        self._ledger.append(f'+ {datetime.datetime.now(datetime.UTC)}: {amount}')

    def withdraw(self, amount):
        if not isinstance(amount, Number):
            raise TypeError("Amount to withdraw should be a number.")
        if amount < 0:
            raise ValueError("Amount to withdraw cant be negative.")
        if amount > self.balance and not self.is_overdraft_allowed:
            raise OverdraftNotAllowedError("Overdraft now allowed for your account.")
        self._balance -= amount
        self._ledger.append(f'- {datetime.datetime.now(datetime.UTC)}: {amount}')

    def __str__(self):
        return f'{self.first_name} {self.last_name} ({self.account_number}): {self.balance}'

    def __eq__(self, other_BankAccount):
        if not isinstance(other_BankAccount, BankAccount):
            raise TypeError(f"{self.__class__.__name__} and {other_BankAccount.__class__.__name__} cannot be compared")
        return self.account_number == other_BankAccount.account_number

# %%
my_acc = BankAccount('Bharath', 'Reddy', 999)
print(f'name: {my_acc.first_name} {my_acc.last_name}, Acc_no: {my_acc.account_number}, Bal: {my_acc.balance}, OD: {my_acc.is_overdraft_allowed}, \n Ledger: {my_acc.ledger}')

my_acc.deposit(100)
print(f'name: {my_acc.first_name} {my_acc.last_name}, Acc_no: {my_acc.account_number}, Bal: {my_acc.balance}, OD: {my_acc.is_overdraft_allowed}, \n Ledger: {my_acc.ledger}')

my_acc.withdraw(25)
print(f'name: {my_acc.first_name} {my_acc.last_name}, Acc_no: {my_acc.account_number}, Bal: {my_acc.balance}, OD: {my_acc.is_overdraft_allowed}, \n Ledger: {my_acc.ledger}')

my_acc.is_overdraft_allowed = True
print(f'name: {my_acc.first_name} {my_acc.last_name}, Acc_no: {my_acc.account_number}, Bal: {my_acc.balance}, OD: {my_acc.is_overdraft_allowed}, \n Ledger: {my_acc.ledger}')

my_acc.withdraw(95)
print(f'name: {my_acc.first_name} {my_acc.last_name}, Acc_no: {my_acc.account_number}, Bal: {my_acc.balance}, OD: {my_acc.is_overdraft_allowed}, \n Ledger: {my_acc.ledger}')

my_acc_2 = BankAccount("Kavery", "Manki", 999)
my_acc_3 = BankAccount("Kavery", "Manki", 991)

print(my_acc, my_acc_2)
print(my_acc == my_acc_2)
print(my_acc == my_acc_3)
print(my_acc == "999")

# %%


# %%
