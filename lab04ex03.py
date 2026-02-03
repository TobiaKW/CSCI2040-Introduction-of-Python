# You can change how list1 is initialized (e.g., list1 = list(...)); list1 = [] is just a placeholder to prevent syntax errors.

# 3a Basic List Comp (list1 & list2)
list1 = [x for x in range(1, 20) if x % 2 == 1]
list2 = [x for x in range(1, 20) if int(x ** 0.5) ** 2 == x]
# 3b Conditional List Comp (list3)
list3 = [0 if x < 0 else x for x in range(-5, 6)]
# 3c 2D List Comprehension (list4)
list4 = [["{}*{}={}".format(x,y,x*y) for x in range(1,y+1)] for y in range(1,5)]

if __name__ == "__main__":
    print(list1)
    print(list2)
    print(list3)
    print(list4)

