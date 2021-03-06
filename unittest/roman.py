# http://diveintopython3.problemsolving.io/unit-testing.html
import re 


roman_numeral_map = (('M',  1000),
                     ('CM', 900),
                     ('D',  500),
                     ('CD', 400),
                     ('C',  100),
                     ('XC', 90),
                     ('L',  50),
                     ('XL', 40),
                     ('X',  10),
                     ('IX', 9),
                     ('V',  5),
                     ('IV', 4),
                     ('I',  1))


roman_numeral_pattern = re.compile('''
    ^                   # beginning of string
    M{0,3}              # thousands - 0 to 3 Ms
    (CM|CD|D?C{0,3})    # hundreds - 900 (CM), 400 (CD), 0-300 (0 to 3 Cs),
                        #            or 500-800 (D, followed by 0 to 3 Cs)
    (XC|XL|L?X{0,3})    # tens - 90 (XC), 40 (XL), 0-30 (0 to 3 Xs),
                        #        or 50-80 (L, followed by 0 to 3 Xs)
    (IX|IV|V?I{0,3})    # ones - 9 (IX), 4 (IV), 0-3 (0 to 3 Is),
                        #        or 5-8 (V, followed by 0 to 3 Is)
    $                   # end of string
    ''', re.VERBOSE)



class OutOfRangeError(ValueError):  
    pass     

class NotAnInteger(ValueError):
    pass

class InvalidRomanNumeral(ValueError):
    pass



def to_roman(n):
    """takes an int and returns its Roman numeral equivalent"""
    
    if n > 3999:
        raise OutOfRangeError('Number out of range — must be 3999 or lower.')
        
    if n <= 0:
        raise OutOfRangeError('Number out of range — must be above zero.')

    if not isinstance(n, int):
        raise NotAnInteger('# must be an integer not a float.')


    result = ''

    for numeral, integer in roman_numeral_map:
        while n >= integer:
                result += numeral
                n -= integer
                # print('subtracting {0} from input, adding {1} to output'.format(integer, numeral))
                # print(result)
    return result



def from_roman(s):
    """takes a roman numeral as a str and returns its int equivalent"""
    
    if not roman_numeral_pattern.search(s):
        raise InvalidRomanNumeral('Invalid Roman numeral: {}'.format(s))

    result = 0
    index = 0

    for numeral, integer in roman_numeral_map:
        while s[index:index+len(numeral)] == numeral:
            result += integer
            index += len(numeral)
    
    return result



to_roman_table = [ None ]
from_roman_table = {}


for integer in range(1, 4000):
    roman_numeral = to_roman(integer)          
    to_roman_table.append(roman_numeral)       
    from_roman_table[roman_numeral] = integer

for key, val in from_roman_table.items():
    print(key, val)