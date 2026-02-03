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
# Student ID   : 1155292671
# Class/Section: CSCI2040
# Date         : 13/10/2025
##

import math

# your statement follows
def check_invalid(triangle):
    ##print(triangle[0], triangle[1], triangle[2])
    if triangle[0]+triangle[1] <= triangle[2] or triangle[0]+triangle[2] <= triangle[1] or triangle[1]+triangle[2] <= triangle[0]:
        ##print("invalid")
        return True
    else:
        ##print("valid")
        return False

def is_acute_triangle(triangle):
    if check_invalid(triangle) == True:
        return False
    else:
        if triangle[0] >= triangle[1] and triangle[0]>=triangle[2]:
            if pow(triangle[0],2) < pow(triangle[1],2) + pow(triangle[2],2):
                return True
            else:
                return False
        elif triangle[1] >= triangle[0] and triangle[1]>=triangle[2]:
            if pow(triangle[1],2) < pow(triangle[0],2) + pow(triangle[2],2):
                return True
            else:
                return False
        elif triangle[2] >= triangle[0] and triangle[2]>=triangle[1]:
            if pow(triangle[2],2) < pow(triangle[0],2) + pow(triangle[1],2):
                return True
            else:
                return False


def area(triangle):
    if check_invalid(triangle) == True:
        return 0
    else:
        s = (triangle[0]+triangle[1]+triangle[2])/2
        a = math.sqrt(s * (s-triangle[0]) * (s-triangle[1]) * (s-triangle[2]))
        return a



def radius(triangle):
    if check_invalid(triangle) == True:
        return (0,0)
    else:
        s = (triangle[0]+triangle[1]+triangle[2])/2
        a = math.sqrt(s * (s-triangle[0]) * (s-triangle[1]) * (s-triangle[2]))
        inc = (2*a) / (triangle[0]+triangle[1]+triangle[2])
        outc = (triangle[0]*triangle[1]*triangle[2])/(4*a)
        return (outc, inc)



if __name__ == '__main__':
    t1=(3,4,5)
    print(area(t1))
    print(is_acute_triangle(t1))
    print(radius(t1))
    t2=(3,6,1)
    print(check_invalid(t2))