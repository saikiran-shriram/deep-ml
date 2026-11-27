def count_common_unique(list1, list2):
    # list1: list of strings
    # list2: list of strings
    # return an integer
    from collections import Counter
    count = 0
    l1 = Counter(list1)
    l2 = Counter(list2)
    for i in l1 :
        if l1[i] == 1 and l2[i] == 1 :
            count += 1
    return count
