newList = []
def countdown(num):
    for i in range(num,0-1,-1):
        newList.append(i)
        # print(i)
    return newList 

print(countdown(5))





def print_and_return(list):
    print(list[0])
    return list[1]

secondItem = print_and_return([1,2])






def first_plus_length(list):
    return list[0] + len(list)

first_plus_length([1,2,3,4,5])





def values_greater_than_second(list):
    newList = []
    if len(list) < 2:
        # print("false")
        return False
    for i in range(0,len(list)):
        if list[i] > list[1]:
            newList.append(list[i])
    print("new list values",len(newList))
    return newList

print(values_greater_than_second([5]))




def length_and_value(size,value):
    list = []
    for i in range(0,size):
        list.append(value)
    return list

print(length_and_value(6,2))