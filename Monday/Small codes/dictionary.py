#!/usr/bin/env python
#
# Dictionaries are unsorted lists of (key,value) pairs.


# A simpler way to initialise dictionaries
# From Martelli 2005
# You want to construct a dictionary whose keys are literal strings, without having to
# quote each key.
data = dict(red=1, green=12, blue=356)
print "data =", data



# Example from the Python Tutorial 2.6.5
# Page 35 of the PDF.
#

tel = {'jack' : 4098, 'sape' : 4139}

# Adding one pair
tel['guido'] = 4127
print tel
# output:
# {'sape': 4139, 'jack': 4098, 'guido': 4127}

# Retrieving a value corresponding to given key
print tel['jack']
# 4098

# Deleting one entry, adding another
del tel['sape']
tel['irv'] = 4127
print tel
# output:
#{'jack': 4098, 'irv': 4127, 'guido': 4127}


# Print all the keys in the dictionary
print tel.keys()
# ['jack', 'irv', 'guido']

# Check if a key is present
print 'guido' in tel
# True

# The dict() constructor
print dict(  [('sape', 4139), ('guido', 4127), ('jack', 4098)]  )
# output:
# {'sape': 4139, 'jack': 4098, 'guido': 4127}
print dict( [(x,x**2) for x in (2,4,6)]  )
# {2: 4, 4: 16, 6: 36}

# Easier assignment when the keys are simple strings ('simple'=what?)
print dict(sape=4139, guido=4127, jack=4098)
# {'sape': 4139, 'jack': 4098, 'guido': 4127}


# Langtangen: 68
# Declare empty dictionary
y = {}

# Length of a dictionary
print len(tel)






