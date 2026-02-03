from functools import reduce
# You can change how list1 is initialized (e.g., list1 = list(...)); list1 = [] is just a placeholder to prevent syntax errors.

# 2a Using map(list1 & list2) # map(func, values)
list1 = list(map(lambda x: 2 ** x, range(1, 12)))
list2 = list(map(lambda x: x % 3, range(1, 12)))
# 2b Using filter (list3)  # filter(func, values)
list3 = list(filter(lambda x: x % 500 == 0, vehicle_numbers := [1500, 2000, 3000, 1600, 2400, 13600, 7, 110]))
# 2c Using reduce (list4) # reduce(func, values, initial)
list4 = reduce(lambda acc, s: acc + s.strip().upper() + " " , vehicle_names := ["Sedan", "SUV", "Pickup", "Minivan", "Van", "Semi ", "Bicycle ",
" Motorcycle "], "").strip()

if __name__ == "__main__":
    print(list1)
    print(list2)
    print(list3)
    print(list4)
