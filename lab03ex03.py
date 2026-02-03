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


import pickle

dict = None
dict2 = None

def load_data(file_name):
    # file_name is the name of data file (e.g., \texttt{followers.pydata})
    # Enter your code here
    result = { }
    f = open(file_name, 'rb')
    result = pickle.load(f)
    f.close()

    return result

def query_following(user_name):
    # Enter your code here
    global dict
    if dict is None:
        dict = load_data('followers.pydata')
    result = []
    for item in dict:
        if user_name in dict[item]:
            result.append(item)
    return result

def update():
    # Enter your code here
    global dict
    if dict is None:
        dict = load_data('followers.pydata')

    if 'Steve Culver' in dict:                      # avoid KeyError
        del dict['Steve Culver']
    for item in dict:
        if "Steve Culver" in dict[item]:
            dict[item].remove("Steve Culver")       ##list.remove(x) >> removes the first occurrence of x from the list
    dict['Anne Smelcer'] = ['Christine Phillips', 'Charles Mason', 'Tim Lathrop']
    f = open('followers-updated.pydata', 'wb')
    pickle.dump(dict, f)
    f.close()

    


def get_num_of_followers():
    # Enter your code here
    global dict2
    if dict2 is None:
        dict2 = load_data('followers-updated.pydata')
    answer_dict = { }
    for item in dict2:
        answer_dict[item] = len(dict2[item])
    return answer_dict

if __name__ == "__main__":
    # you can test your function by using the following
    dict = load_data('followers.pydata')

    following = query_following('Laura Murray')
    print(following)

    update()
    dict2 = load_data('followers-updated.pydata')
    print(dict2['Anne Smelcer'])

    answer_dict = get_num_of_followers()
    print(answer_dict['Anne Smelcer'])