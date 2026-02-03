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
# Date         :15/10/2025
##
import math
# your statement follows
def check_palindrome(test_string):
    SL = test_string.lower()
    SLN = list()
    for i in range(len(SL)):    ##delete non alphabet
        if SL[i].islower() == True:
            SLN.append(SL[i])
    ##print("".join(SLN))##checking

    flag = 0
    for i in range(math.ceil(len(SLN)/2)):
        if SLN[i] != SLN[len(SLN)-i-1]:
            flag = 1

    if flag == 0:
        return True
    else:
        return False
        
    
    
            

def check_isogram(test_string):
    SL = test_string.lower()
    SLN = list()
    for i in range(len(SL)): 
        if SL[i].islower() == True:
            SLN.append(SL[i])
    ##print("".join(SLN))##checking

    flag = 0
    for i in range(len(SLN)):
        if SLN.count(SLN[i]) > 1:
            flag = 1

    if flag == 0:
        return True
    else: 
        return False
    

def join(original_string, inserted_list):
    STRL = list()
    STRL.append(inserted_list[0])
    for i in range(1,len(inserted_list)):
        STRL.append(original_string)
        STRL.append(inserted_list[i])

    STR = '' ## list --> string
    for s in STRL:
        STR += '' + s
    return STR

def replace_last(test_string, old, new):
    SL = test_string.lower() ##alllowercase
    SLL = list()
    OLDL = old.lower()
    op = 0 ## indicator for old string 
    sp = -1 ## indicator for rewrite location

    for i in range(len(test_string)):
        if SL[i] == OLDL[op]:
            ##print(op, SL[i])
            op += 1
            if op == len(old):
                sp = i - op + 1
                op = 0 ## reset
        else:
            op = 0 ##reset
    ##print(sp)

    if sp != -1:
        SLL.append(test_string[0:sp])
        SLL.append(new)
        SLL.append(test_string[sp+len(old):len(test_string)])
    else:
        SLL.append(test_string)

    ##print("".join(SLL))
    STR = '' ## list --> string
    for s in SLL:
        STR += '' + s
    return STR


    

if __name__ == '__main__':
    test_str1 = "Was it a car or a cat I saw?"
    test_str2 = "Alice was born in 2000 and born in hong kong."
    print(check_palindrome(test_str1))
    print(check_palindrome(test_str2))
    print(check_isogram(test_str2))
    print(join("-", ["a","b","c"]))
    print(replace_last(test_str2, "born", "lived"))
    print(replace_last(test_str2, "now", "before"))
