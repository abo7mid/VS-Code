local_var = "magical unicorns"

def square(z) -> str:
    return (z*z)
    
class User:
    def __init__(self,name):   #what is this code -> None:
        self.name = name
    def say_hello(self):
        return "hello"
print(square(5))

user = User("anna")
print(user.name)
print(user.say_hello())
print(__name__)



if __name__ == "__main__":
    print("the file is being executed directly")
    print("do some tests and debugging")
else:
    print("The file is being executed because it is imported by another file. The file is called: ", __name__)
    print("this is a good to go code and there should not be any tests and debugging")
  