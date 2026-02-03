##
# CSCI2040 Introduction to Python
#
# I declare that the assignment here submitted is original
# except for source material explicitly acknowledged,
# and that the same or closely related material has not been
# previously submitted for another course.
# I also acknowledge that I am aware of University policy and
# regulations on honesty in academic work, use of AI tools,
# and of the disciplinary guidelines and procedures applicable
# to breaches of such policy and regulations, as contained in
# the website.
#
# University Guideline on Academic Honesty:
#   http://www.cuhk.edu.hk/policy/academichonesty/
#
# Student Name : WONG CHEUK YIN
# Student ID   : 1155192671
# Class/Section: CSCI2040
# Date         : 13/10/2025
##

def roman_to_decimal(s):
    # your statement follows
    rom_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100} ## Dictionary!
    n = 0
    temp = 0
    for i in range(len(s)):
        if i == 0:
            current = rom_val.get(s[i])
            temp = temp + current
            ##print(n, temp)
        else:
            current = rom_val.get(s[i])
            prev = rom_val.get(s[i-1])
            if current == prev:
                temp = temp + current
                ##print(n, temp)
            elif current < prev:
                n = n + temp
                temp = current
                ##print(n, temp)
            elif current > prev:
                n = n - temp + current
                temp = 0
                ##print(n, temp)
    n = n + temp
    return n

def add_two_roman(roman1, roman2):
    values = roman_to_decimal(roman1) + roman_to_decimal(roman2)
    return values

if __name__ == '__main__':
    print(roman_to_decimal('XCVII'))
    print(add_two_roman('LXXIV', 'XXIIII'))