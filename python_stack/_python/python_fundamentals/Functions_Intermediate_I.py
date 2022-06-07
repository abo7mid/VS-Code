
import random
from timeit import repeat
def randint(min=0,max=100):

    if min > max :
        return "min is greater than max"
    elif max < min:
        return "max is less than min"
    else:
    # If no arguments are provided, the function should return
    # a random integer between 0 and 100.
        if min == 0 and max == 100:
            num = random.random() * max + min 
            # print("no arquments")
            return round(num)
        
        # If only a max number is provided, the function should return 
        # a random integer between 0 and the max number
        if max != 100 and min == 0:
            num = random.random() * max + min 
            # print("only max")
            return round(num)
        # if only a min number is provided, the function should return
        # a random integer between the min number and 100
        if min != 0 and max == 100:
            num = random.random() * max + min
            # print("only min")
            return round(num)
        # if both a min and max number are provided, the function should return
        #  a random integer between those 2 values
        if max != 100 and min != 0:
            # print("both min and max")
            num = random.random() + min * max -1
            return round(num)


print(randint(min=1,max=10))


