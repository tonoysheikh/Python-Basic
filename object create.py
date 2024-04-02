class person:
    def __init__(self , name , id):
        self.name=name
        self.id=id
    def func(self):
        print("Welcome",self.name)

obj = person("salman" , 3012)
obj.func()       