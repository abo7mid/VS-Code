
    # Biggie Size - Given a list, write a function that changes all positive numbers in the list to "big".
    #     Example: biggie_size([-1, 3, 5, -5]) returns that same list, but whose values are now [-1, "big", "big", -5]
    # Count Positives - Given a list of numbers, create a function to replace the last value with the number of positive values. (Note that zero is not considered to be a positive number).
    #     Example: count_positives([-1,1,1,1]) changes the original list to [-1,1,1,3] and returns it
    #     Example: count_positives([1,6,-4,-2,-7,-2]) changes the list to [1,6,-4,-2,-7,2] and returns it
    # Sum Total - Create a function that takes a list and returns the sum of all the values in the list.
    #     Example: sum_total([1,2,3,4]) should return 10
    #     Example: sum_total([6,3,-2]) should return 7
    # Average - Create a function that takes a list and returns the average of all the values.x
    #     Example: average([1,2,3,4]) should return 2.5
    # Length - Create a function that takes a list and returns the length of the list.
    #     Example: length([37,2,1,-9]) should return 4
    #     Example: length([]) should return 0
    # Minimum - Create a function that takes a list of numbers and returns the minimum value in the list. If the list is empty, have the function return False.
    #     Example: minimum([37,2,1,-9]) should return -9
    #     Example: minimum([]) should return False
    # Maximum - Create a function that takes a list and returns the maximum value in the list. If the list is empty, have the function return False.
    #     Example: maximum([37,2,1,-9]) should return 37
    #     Example: maximum([]) should return False
    # Ultimate Analysis - Create a function that takes a list and returns a dictionary that has the sumTotal, average, minimum, maximum and length of the list.
    #     Example: ultimate_analysis([37,2,1,-9]) should return {'sumTotal': 31, 'average': 7.75, 'minimum': -9, 'maximum': 37, 'length': 4 }
    # Reverse List - Create a function that takes a list and return that list with values reversed. Do this without creating a second list. (This challenge is known to appear during basic technical interviews.)
    #     Example: reverse_list([37,2,1,-9]) should return [-9,1,2,37]




def biggie_size(list1):
    replaced = []
    # this also works
    # for j in range(0,len(list1)):  
    #     if list1[j] > 0:
    #         list1[j] = "big"
    #         replaced.append(list1[j])
    #     else:
    #         replaced.append(list1[j])
    # return replaced
        
    for i in list1:
        if i > 0:
            replaced.append("big")
        else:
            replaced.append(i)
    return replaced

print(biggie_size([-1,5,2,-2,-3,10,20,-4]))





def count_positives(alist):
    posValues = 0
    for i in alist:
        if i > 0:
            posValues=posValues+1
    alist[-1] = posValues
    return alist

print(count_positives([1,6,-4,-2,-7,4]))
# print(count_positives([-1,1,1,1]))



def sum_total(alist):
    total = 0
    for i in alist:
        ## ATTENTION HERE ## 
        # do not use total=+i which is equal to total=(+1)
        total+=i  #total = total + i
    return total

print(sum_total([6,3,-2]))





def average(alist):
    sum = 0
    for i in alist:
        sum = sum +i
    return sum/len(alist)

print(average([1,2,3,4]))






def length(alist):
    return len(alist)

print(length([1,2,3,4]))





def minimum(alist):
    if not alist:
        return False
    min = alist[0]
    for i in alist:
        if int(i) < min:
            min = i
    return min

# alist = []
print(minimum([50,100,150]))




def maximum(alist):
    if  not alist:
        return not True  # :) variety helps
    min = alist[0]
    for i in alist:
        if int(i) > min:
            min = i
    return min


alist = []
print(maximum(alist))




def ultimate_analysis(alist):
    dictionary = {
                'sumTotal': sum_total(alist),
                "average": average(alist),
                "minimum": minimum(alist),
                "maximum": maximum(alist),
                "length": length(alist)
                }


    # dictionary['sumTotal'] = 5     update if the key exsits
    # dictionary['key1'] = 'value1'  adding if the key not exists
    # dictionary['key2'] = ['value2']
    # dictionary['key3'] = ['value3','value4']
    return dictionary

print(ultimate_analysis([1,2,3]))




def revers_list(alist):
    counter = 0
    for i in range(len(alist),0,-1): #[1,2,3]
        alist[counter] = i 
        counter+=1
    return alist
        


print(revers_list([1,2,3])) # this function makes me sweat


