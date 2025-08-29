class Robot:
    def __init__(self, name):
        self.name = name
        self.position = [0,0]
        print("My Name is", self.name)
    
    def walk(self,x):
        self.position[0] = self.position[0] + x
        print("New Posistion:", self.postion[0])

class Robot_dog(Robot):
    def make_noise(self):
        print("woof woof!")

class Robot_Cat(Robot):
    def make_noise(self):
        print("Meow!!")

my_robot_dog = Robot_dog("Max")
my_robot_cat = Robot_Cat("Dotty")