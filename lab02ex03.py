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

def Fib(n):
    c = 0
    p1 = 0
    p2 = 1
    if n > 0:
        for i in range(n):
            c = p1 + p2
            p2 = p1
            p1 = c
            ##print(i, c) ...tracing
    values = c
        
    return values

if __name__ == '__main__':
    print(Fib(5))
    print(Fib(10))
    print(Fib(15))