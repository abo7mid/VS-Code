listofNum = [5,2,1,8,4,3,6,7]

minimum_value = 0
new_list = []
counter = 0
for i in range(0,len(listofNum)):
    if listofNum[i] < listofNum[i+1]:
        print(i)
        # new_list[counter] = listofNum[i]
        # counter = counter +1
        # print(new_list)


# javascript code below!  
# var arr = [1,3,5,7];
# var temp = arr[0];
# arr[0] = arr[1];
# arr[1] = temp;
# copy
# If this code looks like a lot of work for a simple swap, good news! Python provides a one-liner way to swap:

# # python code below!
# arr = [1,3,5,7]
# arr[0], arr[1] = arr[1], 