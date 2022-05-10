
def largest_total(lists):

    largest_sum = 0
    list_index = -1
    for i, a_list in enumerate(lists, 0):
        list_sum = sum(a_list)
        if list_sum > largest_sum:
            list_index = i
            largest_sum = list_sum
    return lists[list_index]
    # return list with largest sum



if __name__ == '__main__':
    list0 = [18, 200, 37, 98, 45, 1000, -10, 0, 8, 15]
    list1 = [5, 10, 2, 9, 100000]
    list2 = [8, 48, 1, 14, 800]
    list3 = [100, 200, 300]
    list4 = [100000, 200000]
    list5 = [1000000]
    print(largest_total([list0, list1, list2, list3, list4]))

