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

# Prompt the user to enter a string
s = list(input("Enter a string: "))
#print(len(s))

# Display the options to the user
print("Choose a transformation:")
print("1. Toggle case")
print("2. Shift letters by +1")
print("3. Mirror the string")
print("4. Collapse consecutive duplicates")

# Get the user's choice
choice = int(input("Enter your choice: "))
# Apply the selected transformation
if choice == 1:
    for i in range(len(s)):
        if s[i].islower() == True:
            s[i] = s[i].upper()
        elif s[i].isupper() == True:
            s[i] = s[i].lower()
elif choice == 2:
    for i in range(len(s)):
        if s[i].isalpha() == True and s[i] != 'Z' and s[i] != 'z':
            s[i] = chr(ord(s[i]) + 1)
        elif s[i] == 'Z':
            s[i] = 'A'
        elif s[i] == 'z':
            s[i] = 'a'
elif choice == 3:
    smirror = ['NA'] * len(s)
    for i in range(len(s)):
        smirror[i] = s[len(s)-i-1]
    ##print("".join(smirror))
    s = s + ['|'] + smirror
elif choice == 4:
    scollapse =['NA'] * len(s)
    deleted = int(0)
    for i in range(len(s)):
        if i+1 < len(s):
            #print("checked",i)
            if s[i+1] != s[i]:
                scollapse[i-deleted] = s[i]
            else:
                deleted = deleted + 1
        else:
            #print("checked",i)
            scollapse[i-deleted] = s[i]
        #print("".join(scollapse)) 
    s[0:len(s)-deleted] = scollapse[0:len(s)-deleted-1] 
    s[len(s)-deleted:len(s)-1] = [''] * deleted 
    #print("".join(s))   
else:
    print("Invalid choice. No transformation applied.")
    ###

# Print the transformed string
print("Transformed string:", "".join(s))
print("Transformation complete. Goodbye!")
