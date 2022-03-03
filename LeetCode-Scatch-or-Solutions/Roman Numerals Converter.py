class RomanNumerals:  # this is a solution to one of the leetcode problem

    def to_roman(self, val):
        integer = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
        roman_numeral = ['I', 'IV', 'V', 'IX', 'X', 'XL', 'L', 'XC', 'C', 'CD', 'D', 'CM', 'M']
        ans = ''
        i = 12

        while val:
            div = val // integer[i]
            val = val % integer[i]
            ans += roman_numeral[i] * div
            i += -1

        return ans

    def from_roman(self, roman_num):
        roman_num_dict = {'I': 1,
                          'V': 5,
                          'X': 10,
                          'L': 50,
                          'C': 100,
                          'D': 500,
                          'M': 1000}
        if len(roman_num) == 1:
            return roman_num_dict[roman_num]

        prev = roman_num[0]
        value = roman_num_dict[prev]

        for letter in range(1, len(roman_num)):
            if roman_num_dict[roman_num[letter]] > roman_num_dict[prev]:
                value += roman_num_dict[roman_num[letter]] - 2 * roman_num_dict[prev]
                prev = roman_num[letter]
            else:
                value += roman_num_dict[roman_num[letter]]
                prev = roman_num[letter]

        return value


converter = RomanNumerals()
print(converter.to_roman(1977))
print(converter.from_roman('MCMLXXVII'))
