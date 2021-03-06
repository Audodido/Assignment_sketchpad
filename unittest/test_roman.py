from unittest import result
import roman
import unittest


class KnownValues(unittest.TestCase):               
    
    known_values = ( (1, 'I'),
                     (2, 'II'),
                     (3, 'III'),
                     (4, 'IV'),
                     (5, 'V'),
                     (6, 'VI'),
                     (7, 'VII'),
                     (8, 'VIII'),
                     (9, 'IX'),
                     (10, 'X'),
                     (50, 'L'),
                     (100, 'C'),
                     (500, 'D'),
                     (1000, 'M'),
                     (31, 'XXXI'),
                     (148, 'CXLVIII'),
                     (294, 'CCXCIV'),
                     (312, 'CCCXII'),
                     (421, 'CDXXI'),
                     (528, 'DXXVIII'),
                     (621, 'DCXXI'),
                     (782, 'DCCLXXXII'),
                     (870, 'DCCCLXX'),
                     (941, 'CMXLI'),
                     (1043, 'MXLIII'),
                     (1110, 'MCX'),
                     (1226, 'MCCXXVI'),
                     (1301, 'MCCCI'),
                     (1485, 'MCDLXXXV'),
                     (1509, 'MDIX'),
                     (1607, 'MDCVII'),
                     (1754, 'MDCCLIV'),
                     (1832, 'MDCCCXXXII'),
                     (1993, 'MCMXCIII'),
                     (2074, 'MMLXXIV'),
                     (2152, 'MMCLII'),
                     (2212, 'MMCCXII'),
                     (2343, 'MMCCCXLIII'),
                     (2499, 'MMCDXCIX'),
                     (2574, 'MMDLXXIV'),
                     (2646, 'MMDCXLVI'),
                     (2723, 'MMDCCXXIII'),
                     (2892, 'MMDCCCXCII'),
                     (2975, 'MMCMLXXV'),
                     (3051, 'MMMLI'),
                     (3185, 'MMMCLXXXV'),
                     (3250, 'MMMCCL'),
                     (3313, 'MMMCCCXIII'),
                     (3408, 'MMMCDVIII'),
                     (3501, 'MMMDI'),
                     (3610, 'MMMDCX'),
                     (3743, 'MMMDCCXLIII'),
                     (3844, 'MMMDCCCXLIV'),
                     (3888, 'MMMDCCCLXXXVIII'),
                     (3940, 'MMMCMXL'),
                     (3999, 'MMMCMXCIX')) 

    def test_to_roman_known_values(self):           
        
        for integer, numeral in self.known_values:
            result = roman.to_roman(integer)       
            self.assertEqual(numeral, result) 
            

    # def test_from_roman_known_values(self):
    #     '''from_roman should give known result with known input'''
    #     for integer, numeral in self.known_values:
    #         result = roman.from_roman(numeral)
    #         self.assertEqual(integer, result)



class ToRomanBadInput(unittest.TestCase):
    
    def test_range_error(self):
        #The unittest.TestCase class provides the assertRaises method, which takes the following arguments: 
        # the exception you???re expecting, the function you???re testing,
        self.assertRaises(roman.OutOfRangeError, roman.to_roman, 4000)


    def test_too_small(self):
        self.assertRaises(roman.OutOfRangeError, roman.to_roman, -1)

    
    def test_non_integer(self):
        self.assertRaises(roman.NotAnInteger, roman.to_roman, .23)


    def test_blank_input(self):
        self.assertRaises(roman.InvalidRomanNumeral, roman.from_roman, ' ')


class RoundtripCheck(unittest.TestCase):

    def test_round_trip(self):
        '''from_roman(to_roman(n))==n for all n'''

        for integer in range(1, 4000):
            numeral = roman.to_roman(integer)
            result = roman.from_roman(numeral)
            self.assertEqual(integer, result)




if __name__ == "__main__":

    unittest.main()
