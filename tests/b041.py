"""
Should emit:
B041 - on lines 6-11
"""

test = {'yes': 1, 'yes': 2}
test = {1: 1, 1: 2}
test = {'yes': 1, 'yes': 2, 'no': 2, 'no': 3}
test = {'yes': 1, 'yes': 2, 'yes': 3}
test = {True: 1, True: 2}
test = {None: 1, None: 2}

# non-constant or non-duplicate keys are ignored
x = 1
test = {x: 1, x: 2}
test = {(1, 2): 1, (1, 2): 2}
test = {1: 1, 2: 2}
