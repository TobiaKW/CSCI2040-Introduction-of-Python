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
# Date         : 27/9/25
##

# lab01ex04.py

# ----------------------
# Stage 1: Accumulation Function
# ----------------------
annual_rate = float(input("Enter the annual interest rate (r%): "))
n = int(input("Enter the number of compounding periods per year (n = 1, 2, 4, 12): "))
t = int(input("Enter the number of years (t): "))
r = annual_rate / 100.0

# Compute accumulation function a(t) and print the result
a_t = pow((1 + (r/n)),(n*t))
print("Accumulation function a(t) after", t, "years: {:.6f}".format(a_t))

# ----------------------
# Stage 2: Principal and Interest Calculation
# ----------------------
P = float(input("Enter the principal amount ($P): "))
Ptemp = P
Pprev = P
year_interest = float(0)

for i in range(t):
    Ptemp = P * pow((1 + (r/n)),(n*(i+1)))
    year_interest = Ptemp - Pprev
    print("Interest Earned in Year " + str(i+1) + ': ${:.2f}'.format(year_interest))
    Pprev = Ptemp

# ----------------------
# Summary
# ----------------------

print("Summary Report:" )
print("Total Interest Earned: ${:.2f}".format(Ptemp-P))
print("Final Balance: ${:.2f}".format(Ptemp))
