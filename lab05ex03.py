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

# Your work here

import matplotlib.pyplot as plt
             

labels = ['Rent', 'Food', 'Transport', 'Utilities', 'Entertainment']
sizes = [1200, 450, 200, 150, 250] 
colors = ['gold', 'lightcoral', 'lightskyblue', 'lightgreen', 'mediumpurple']
explode = (0.05, 0, 0, 0, 0) 

plt.figure(figsize=(8, 8))
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%')
plt.title("Monthly Expense Distribution", pad=20)
plt.axis('equal')

plt.savefig('expense_pie.png')
plt.show() 