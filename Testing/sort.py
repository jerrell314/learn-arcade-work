# Swap number
# my_list = [15, 57, 14, 33, 72, 79, 26, 56, 42, 40]
# print(my_list)
# temp = my_list[0]
# my_list[0] = my_list[2]
# my_list[2] = temp
# # only in python you can swp this way
# # my_list[0], my_list[2] = my_list[2], my_list[0]
# print(my_list)

# 15 57 14 33 72 79 26 56 42 40

# 14 is smallest, swap 14 to pos 0
# 14 57 15 33 72 79 26 56 42 40

# 15 is next smallest, swap 15 to pos 1
# 14 15 57 33 72 79 26 56 42 40

# 26 is next smallest, swap 26 to pos 2
# 14 15 26 33 72 79 57 56 42 40

# 33 is the next smallest, swap 33 to pos 3
# 14 15 26 33 72 79 57 56 42 40

# 40 is the next smallest, swap 40 to pos 4
# 14 15 26 33 40 79 57 56 42 72
#SELECTION sort all cases
# n = 10, 10 *5 = 50
# n = 100, 100 * 50 = 5,000
# n = 1000, 1000 * 50 = 500,000
# n * (n / 2) = n^2 / 4

#INSERTION sort average
# n = 10, 10 * 2.5  = 25
# n = 100, 100 * 25 = 2500
# n = 1000, 1000 * 250 = 250,000
# n * (n / 4) = n^2 / 4

#Insertion sore best case
# n = 10, 10 * 1  = 10
# n = 100, 100 * 1 = 100
# n = 1000, 1000 * 1 = 1000
# n

# This is SELECTION sort. I am SELECTING the smallest and swapping

def selection_sort(my_list):
    for cur_pos in range(len(my_list)): # runs 100 times
        min_pos = cur_pos
        for scan_pos in range(cur_pos + 1, len(my_list)):# runs 50 times
            if my_list[scan_pos] < my_list[min_pos]:
                min_pos = scan_pos

        temp = my_list[min_pos]
        my_list[min_pos] = my_list[cur_pos]
        my_list[cur_pos] = temp


my_list = [15, 57, 14, 33, 72, 79, 26, 56, 42, 40]
selection_sort(my_list)
print(my_list)


# INSERTION SORT

def insertion_sort(my_list):
    for key_pos in range(1, len(my_list)): # Runs 100 times
        key_value = my_list[key_pos]
        scan_pos = key_pos - 1
        while (scan_pos >= 0) and (my_list[scan_pos] > key_value): # Worst case average 50, on average it runs 25
            my_list[scan_pos + 1] = my_list[scan_pos]
            scan_pos -= 1

        my_list[scan_pos + 1] = key_value


my_list = [15, 57, 14, 33, 72, 79, 26, 56, 42, 40]
insertion_sort(my_list)
print(my_list)
