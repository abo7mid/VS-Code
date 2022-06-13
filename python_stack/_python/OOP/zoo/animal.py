class Animals:
    def __init__(self,name,age,health,happiness):
        self.name = name
        self.age = age
        self.health = health
        self.happiness = happiness

    
    def display_info(self):
        animlInfo = [self.name, self.age, self.health, self.happiness]
        print(animlInfo)
    
    def feed(self,health=10,happiness=10):
        self.health += health
        self.happiness += happiness
