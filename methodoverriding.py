'''
A function is independent.
A method is a function that belongs to a class/object.
'''
class Phone:
    def __init__(self):
        print("I am a Phone class")

class Samsung(Phone):
    # pass
    ## here we use method over ride 
    def __init__(self):
        super().__init__()                      # here we call super class __init__ method 
        print("I am Samsung class")

s = Samsung()