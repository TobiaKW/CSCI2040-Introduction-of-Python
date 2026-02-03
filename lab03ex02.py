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

def quicksort(a):
    # Enter your code here
    if len(a) <= 1:
        return a
    else:
        pivot = a[0]
        less_than_pivot = [x for x in a[1:] if x <= pivot]
        greater_than_pivot = [x for x in a[1:] if x > pivot]
        return quicksort(less_than_pivot) + [pivot] + quicksort(greater_than_pivot)


if __name__ == "__main__":
    # you can test your function by using the following
    print(quicksort([1, 2, 4, 5, 1, 3, 2, -1]))
