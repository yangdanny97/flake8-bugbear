# Simple case
{'yes': 1, 'yes': 2}  # error

# Duplicate keys with bytes vs unicode in Python 3
{b'a': 1, u'a': 2}  # error
{1: b'a', 1: u'a'}  # error

# Duplicate keys with bytes vs unicode in Python 2
{b'a': 1, u'a': 2}  # error

# Duplicate values in Python 2
{1: b'a', 1: u'a'}  # error

# Multiple duplicate keys
{'yes': 1, 'yes': 2, 'no': 2, 'no': 3}  # error

# Duplicate keys in function call
def f(thing):
    pass
f({'yes': 1, 'yes': 2})  # error

# Duplicate keys in lambda function
(lambda x: {(0, 1): 1, (0, 1): 2})  # error

# Duplicate keys with tuples
{(0, 1): 1, (0, 1): 2}  # error

# Duplicate keys with int and float
{1: 1, 1.0: 2}  # error

# Duplicate keys with booleans
{True: 1, True: 2}  # error

# Duplicate keys with None
{None: 1, None: 2}  # error

# Duplicate keys with variables
a = 1
{a: 1, a: 2}  # error

# Duplicate values with variables
a = 1
b = 2
{1: a, 1: b}  # error

# Duplicate values with same variable value
a = 1
b = 1
{1: a, 1: b}  # error

# Duplicate keys with same values
{'yes': 1, 'yes': 1}  # error

# Non-duplicate keys
{'yes': 1, 'no': 2}  # safe

# Non-duplicate keys with tuples having the same first element
{(0, 1): 1, (0, 2): 1}  # safe

# Non-duplicate keys in function call
def test_func(thing):
    pass
test_func({True: 1, None: 2, False: 1})  # safe

# Non-duplicate keys with bool and None
{True: 1, None: 2, False: 1}  # safe

# Non-duplicate keys with different ints
{1: 1, 2: 1}  # safe

# Duplicate keys with differently-named variables
test = 'yes'
rest = 'yes'
{test: 1, rest: 2}  # safe

# Non-duplicate tuple keys
{(0, 1): 1, (0, 2): 1}  # safe

# Duplicate keys with instance attributes
class TestClass:
    pass
f = TestClass()
f.a = 1
{f.a: 1, f.a: 1}  # safe
