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
# Date         : 25/9/2025
##


# Prompt the user to enter a string
s = input('Enter a string: ') 
slow = s.lower()
# Enter your code here

low = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
vowel = ["a","e","i","o","u"]
presence = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

counta = 0
countb = 0
countc = 0

for i in range(26):
    counta = counta + slow.count(low[i])
    presence[i] = slow.count(low[i])
    if slow.count(low[i]) >= 1:
        countb = countb + 1
    #print(i, presence[i])

for i in range(5):
<<<<<<< HEAD
    if slow.count(vowel[i])>=1:
        ##print("counted", i)
=======
<<<<<<< HEAD
    if slow.count(low[i])>=1:
=======
    if slow.count(vowel[i])>=1:
        ##print("counted", i)
>>>>>>> 8a7f2f8 (updated)
>>>>>>> b807e14 (updated)
        countc = countc + 1

fnrl = '#'
for i in range(len(s)):
    if  slow[i].isalpha() == True: ##equals to s.isalpha()
        if presence[ord(slow[i])-97] == 1:
            fnrl = slow[i]
            break
        
       


# Print the results
print('The number of alphabetic letters in \"' + s + '\":', counta)
print('The number of distinct alphabetic letters in \"' + s +'\":', countb)
print('The number of vowels in \"' + s + '\":', countc)
if fnrl == '#':
    print('The first non-repeating alphabetic letter in \"' + s + '\": N/A')
else:
    print('The first non-repeating alphabetic letter in \"' + s + '\":' , fnrl)