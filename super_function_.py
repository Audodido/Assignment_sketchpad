# https://www.youtube.com/watch?v=MBbVq_FIYDA

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Square(Rectangle):
    def __init__(self, length, width):
        super().__init__(length, width)

    def area(self):
        return self.length * self.width

class Cube(Rectangle):
    def __init__(self, length, width, height):
        super().__init__(length, width)
        self.height = height

    def volume(self):
        return self.length * self.width * self.height


class A:

    def feature1(self):
        return "Feature 1 working"

class B(A): 

    def feature2(self):
        return "Feature 2 working"

    def thing(self):
        return 85000



# square = Square(3,3)
# cube = Cube(3,3,3)

# c = B()

# print(square.area())
# print(cube.volume())

# print(c.feature1())


# class Super:
#         def method(self):
#             print('in Super.method')
# class Sub(Super):
#     def method(self):                    # Override method
#         print('starting Sub.method')     # Add actions here
#         Super.method(self)               # Run default action
#         print('ending Sub.method')

# s = Sub()
# s.method()


# create an instance of each class with a for loop

instances = []

for klass in Rectangle, Square, Cube:
    if klass == Cube:
        obj = klass(10, 20, 30)
        instances.append(obj)
        # print(obj.volume())
    else:
        obj = klass(10, 20)
        instances.append(obj)    
        # print(obj.area())

#if i is an insance of the Cube class
for i in instances:
    if isinstance(i, Cube):
        #print("YES")
        print(i.volume())
    else:
        print(i.area())



##inheritance vs. composition (is-a vs. has-a)
#https://www.youtube.com/watch?v=0mcP8ZpUR38