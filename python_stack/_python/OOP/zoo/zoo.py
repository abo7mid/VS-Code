from lion import Lion
from tiger import Tiger

class Zoo:
    def __init__(self,zoo_name):
        self.animals = []
        self.name = zoo_name
    
    
    def add_lion(self,name):
        self.animals.append(Lion(name))

    def add_tiger(self,name):
        self.animals.append(Tiger(name))

    def print_all_info(self):
        for animal in self.animals:
            animal.disply_info()


zoo1 = Zoo("Ahmed's Zoo")
# zoo1.add_tiger('Rajah')
zoo1.add_lion('Simba')

zoo1.print_all_info()