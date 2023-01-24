import statistics


my_list = [364, 373, 358, 394, 378, 379, 357, 364, 350, 363, 392, 368, 359, 375, 399, 365, 379, 357, 380]

'''Finding mean value using the formula:
    mean = sum(my_list)/len(my_list)'''
print(f"Mean value is {statistics.mean(my_list)}")

'''Finding median value using the formula:
    if len(my_list) % 2 != 0:
        median = my_list[len(my_list) // 2]
    else:
        median = (my_list[len(my_list) // 2] + my_list[len(my_list) // 2 + 1]) / 2'''
print(f"Median is {statistics.median(my_list)}")

'''To find mode value you need a dictionary and for loop:
    counter = {}
    for i in my_list:
        if i in counter:
            counter[i] += 1
        else:
            counter[i] = 1
    mode = counter[sorted(counter, key=counter.get, reverse=True)[:1][0]]'''
print(f"Mode of set is {statistics.multimode(my_list)}")

'''To find standard deviation you first need to find the variance using the formula:
    variance = sum([(x-mean(my_list) ** 2 for x in my_list]) / len(my_list)
   Then you can find standard deviation using the formula:
    stdev = sqrt(variance)'''
print(f"Standard deviation is {statistics.stdev(my_list)}")
