# Given an array of integers nums, 
# a lucky integer is an integer which has a frequency in the array equal to its value.
# Return a lucky integer in the array. If there are multiple lucky integers return the largest of them. If there is no lucky integer return -1.
# Example 1:
# Input: nums = [2,2,3,4]					
# Output: 2
# Explanation: The only lucky number in the array is 2 because frequency[2] == 2.
# Example 2:
# Input: nums = [1,2,2,3,3,3]
# Output: 3
# Explanation: 1, 2 and 3 are all lucky numbers, return the largest of them.

def lucky_count(array):
    lucky_dict ={} #O(1)
    max_list = [] #O(1)
    
    for num in array: #O(N)
        if num not in lucky_dict: #O(1)
            lucky_dict[num]= 1 #O(1)
        else:
            lucky_dict[num]+=1 #O(1)
#     return lucky_dict

    for numb in lucky_dict: #O(N)
#         print(num) 
        if numb == lucky_dict[numb]: #O(1)
            max_list.append(numb) #O(1)
#     print(max_list)
    if max_list == []: #O(1)
        return -1 #O(1)
    return max(max_list) #O(N)


print (lucky_count([2,3,3]))
    

#O(3N) --> #O(N)