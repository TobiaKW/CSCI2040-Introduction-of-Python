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

def convolve(image, kernel):
    ## Enter your code here
    for i in range(image.shape[0] - kernel.shape[0] + 1):
        for j in range(image.shape[1] - kernel.shape[1] + 1):
            submatrix = image[i:i+kernel.shape[0], j:j+kernel.shape[1]]
            conv_value = np.sum(submatrix * kernel)
            if i == 0 and j == 0: ## init
                convolved_image = np.zeros((image.shape[0]-kernel.shape[0]+1, image.shape[1]-kernel.shape[1]+1))
            convolved_image[i, j] = conv_value
            
    return convolved_image  # a 2D numpy multi-dimension array


if __name__ == '__main__':
    # simple test case
    test_img = np.array([[1, 2, 3],
                         [4, 5, 6],
                         [7, 8, 9]])

    test_kernel = np.array([[1, 0],
                            [0, 1]])

    print(test_img)
    output = convolve(test_img, test_kernel)
    print(output)
