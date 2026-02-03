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
# Date         : 26/9/25
##

### Enter your code here
import math

valid = 0
h = 0
while valid == 0:
    h =  int(input("Enter h: "))
    if h%2 == 0:
        print("Diamond requires an odd h!")
    elif h<=1 or h>30:
        print("Invalid input for h!")
    else:
        valid = 1

spacing = h//2
center = 0
for i in range(h//2):
    for j in range(spacing):
        print(" ", end='')
    print("/", end='')
    for k in range(center):
        print(" ", end='')
    print("\\")
    spacing = spacing - 1
    center = center + 2

print("|", end='')
for k in range(center):
    print(" ", end='')
print("|")

spacing = spacing + 1
center = center - 2

for i in range(h//2):
    for j in range(spacing):
        print(" ", end='')
    print("\\", end='')
    for k in range(center):
        print(" ", end='')
    print("/")
    spacing = spacing + 1
    center = center - 2