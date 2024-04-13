#Method 1 make a new list and get median of new list
def find_median_sorted_arrays_method_one(nums1,nums2):
    total_nums = len(nums1) + len(nums2)
    
    odd_length = total_nums % 2 == 1
    #Get the value of half the length of list rounded down
    half_length = (int)(total_nums / 2)

    new_sorted_array = []
    
    #iterate number of times equal to length of new list
    for i in range(total_nums):
        if nums1[0] <= nums2[0]:
            #add smallest in nums1 to new list
            new_sorted_array.append(nums1[0])
            #remove the first element (smallest number) in nums1
            nums1 = nums1[1:]
            #if nums1 empty make new element larger than largest in nums2
            if len(nums1) == 0:
                nums1 = [nums2[-1] + 1]
        else:
            #add smallest in nums2 to new list
            new_sorted_array.append(nums2[0])
            #remove the first element (smallest number) in nums2
            nums2 = nums2[1:]
            #if nums2 empty make new element larger than largest in nums1
            if len(nums2) == 0:
                nums2 = [nums1[-1] + 1]
    
    #if length is odd median is middle element
    if odd_length:
        median = new_sorted_array[half_length]
    #if length is even median is average of the 2 middle elements
    else:
        median = (new_sorted_array[half_length - 1] + new_sorted_array[half_length]) / 2
    
    return median


#Method 2 (less memory usage) get the correct indices for middle 2 elements
#Do not create new list
def find_median_sorted_arrays_method_two(nums1,nums2):
    total_nums = len(nums1) + len(nums2)
    
    even_length = total_nums % 2 == 0
    half_length = (int)(total_nums / 2)
    
    #current index of nums1
    n = 0
    #current index of nums2
    m = 0
    median = 0
    
    for i in range(total_nums):        
        if nums1[n] <= nums2[m]:
            # If total nums is even and at the index before half length add to median
            if i == half_length - 1 and even_length:
                median += nums1[n]
            #if at correct index add to meidan and break out of loop
            elif i == half_length:
                median += nums1[n]
                break
            
            #if nums1 index too large add element to it larger than nums2 largest number
            if n == len(nums1) - 1:
                nums1.append(nums2[-1]+1)
            n += 1
            
        else:
            if i == half_length - 1 and even_length:
                median += nums2[m]
            elif i == half_length:
                median += nums2[m]
                break
                
            if m == len(nums2) - 1:
                nums2.append(nums1[-1]+1)            
            m += 1
    
    #if even length average the two indices used.
    if even_length:
        median = median/2
        
    return median
