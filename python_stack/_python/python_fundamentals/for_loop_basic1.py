# # Basic
for i in range(0,150+1):
    print(i)
# # # # # #



# # Multiples of Five
for i in range(5,1000+1,5):
    print(i)
# # # # # #



# # Counting, the Dojo Way
for i in range(1,100+1):
    if i % 10 == 0:
        print("Coding Dojo")
    elif i % 5 == 0:
        print("Coding")
    # print(i / 5)
    else:
        print(i)
# # # # # #



# # Whoa. That Sucker's Huge
sum = 0
for i in range(0,500000+1):
    if i % 2 != 0:
        # print(i)
        sum = sum + i
print(sum)
# # # # # #



# # Countdown by Fours
for i in range(2018,0,-4):
    print(i)
# # # # # #



# # Flexible Counter
lowNum = 1
highNum= 100
mult = 3
for i in range(lowNum,highNum):
    if i % 3 == 0:
        print(i)
# # # # # #