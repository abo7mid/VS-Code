class MathDojo:
    
    
    def __init__(self):
        self.result = 0
    

    def add(self,num,*nums):
        self.result += num
        for i in nums:
            self.result += i
        # print(self.result)
        return self


    def subtract(self,num,*nums):
        self.result -= num
        for i in nums:
            self.result -= i
        # print(self.result)
        return self



md = MathDojo()
x = md.add(10,10).add(5,5).add(7,3).subtract(10,10).subtract(5,5).subtract(3,7).result
print(x)