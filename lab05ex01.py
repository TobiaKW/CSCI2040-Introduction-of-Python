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
# Student Name : Wong Cheuk Yin 
# Student ID   : 1155192671
# Class/Section: CSCI2040
# Date         : 4/12/25
##

import numpy as np

def extract_submatrix(matrix, rows_to_remove, cols_to_remove):
    ## Enter your code here
    tmp = np.delete(matrix, rows_to_remove, axis=0)
    submatrix = np.delete(tmp, cols_to_remove, axis=1)
    return submatrix


if __name__ == '__main__':
    # simple test case
    test = np.array([[1, 2, 3],
                     [4, 5, 6],
                     [7, 8, 9]])

    print(test)

    output = extract_submatrix(test, [0], [1])
    print(output)
