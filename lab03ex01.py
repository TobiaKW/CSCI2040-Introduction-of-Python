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
# Date         : 29/10/2025
##

def unique_once(input_list):
    result = list()
    for item in input_list:
        if input_list.count(item) == 1:
            result.append(item)
    return result

if __name__ == '__main__':
    # you can test your function by using the following
    input_list = ['apple', 'banana', 'apple', 'orange', 'banana', 'grape']
    print(input_list)
    output_list = unique_once(input_list)
    print(output_list)

