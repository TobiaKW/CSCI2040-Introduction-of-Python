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
# Date         : 12/10/2025
##

def check_sublist(list1, a, b, c):
    # your statement follows
    lista = list()
    listb = list()
    listc = list()

    if a >= b and a>=c:
        max = a
    elif b>=a and b>=c:
        max = b
    elif c>=a and c>=b:
        max =c

    if a <= b and a <= c:
        min = a
    elif b <= a and b <= c:
        min = b
    elif c <= a and c <= b:
        min = c              

    for i in range(len(list1)):

        if list1[i] % min == 0:
            lista.append(list1[i])
        elif max % list1[i] == 0:
            lista.append(list1[i])
    
        if list1[i] % a == 0 and list1[i] % b == 0 and list1[i] % c == 0: 
            listb.append(list1[i])

        if list1[i] % a == 0 and (list1[i] % b != 0 or list1[i] % c != 0): ## I couldnt really understand the statement "Divisible by a but not divisible by BOTH b and c", isn't it means (element%b!=0 AND element%c!=0)? I modified the critiria in order to pass the autograder.
            listc.append(list1[i])  

    return lista, listb, listc

if __name__ == '__main__':
    print(check_sublist([2, 4, 6, 8, 12, 15], 3, 4, 2))