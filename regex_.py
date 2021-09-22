# http://diveintopython3.problemsolving.io/regular-expressions.html



    # ^ matches the beginning of a string.
    # $ matches the end of a string.
    # \b matches a word boundary.
    # \d matches any numeric digit.
    # \D matches any non-numeric character.
    # x? matches an optional x character (in other words, it matches an x zero or one times).
    # x* matches x zero or more times.
    # x+ matches x one or more times.
    # x{n,m} matches an x character at least n times, but not more than m times.
    # (a|b|c) matches exactly one of a, b or c.
    # (x) in general is a remembered group. You can get the value of what matched by using the groups() method of the object returned by re.search. 


import re

# pattern = '^M?M?M(cat|dog)$'
# val = re.search(pattern, 'MMcat')
# print(val)

# phonePattern = re.compile(r'^(\d{3})-(\d{3})-(\d{4})$')
# val = re.search(phonePattern, "800-222-3122").groups()
# print(val)

#---------

#using comments via .VERBOSE 
phonePattern = re.compile(r'''
                # don't match beginning of string, number can start anywhere
    (\d{3})     # area code is 3 digits (e.g. '800')
    \D*         # optional separator is any number of non-digits
    (\d{3})     # trunk is 3 digits (e.g. '555')
    \D*         # optional separator
    (\d{4})     # rest of number is 4 digits (e.g. '1212')
    \D*         # optional separator
    (\d*)       # extension is optional and can be any number of digits
    $           # end of string
    ''', re.VERBOSE)

val = phonePattern.search('work 1-(800) 555.1212 #1234').groups()
print(val)
