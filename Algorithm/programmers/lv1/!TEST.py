test1 = ['a', 'b', 'c']
# test = {0: 'a', 1: 'b', 3: 'c'}
dict_test1 = {}
# callings = [b, c, c] -> c 1등, b 2등, a 3등
test2 = {'a': 0, 'b': 1, 'c': 2}

for i in range(len(test2)):
    count_callings = i - test2[test1[i]]
    if count_callings in dict_test1:
        print(dict_test1[count_callings])# = dict_test1[count_callings].append([test1[i]])
        print(dict_test1[count_callings].insert(0, test1[i]))
    else:
        dict_test1[count_callings] = [test1[i]]
print(dict_test1)