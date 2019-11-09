class Circle:
    "Calculate the area and perimiter of a circle"

    def __init__(self, radius):
        self.radius = radius
        self.pi = 3.14159

    def area(self):
        return self.pi*(self.radius*self.radius)

    def perimeter(self):
        return self.pi*(2*self.radius)

#TODO: use math.pi instead of hardcoded pi
#TODO: round() the output

# sample 1
circle_1 = Circle(3)
print "Radius is: {0}, Area is: {1}, Perimeter is {2}".format(3, circle_1.area(), circle_1.perimeter())

# sample 2
circle_2 = Circle(8)
print "Radius is: {0}, Area is: {1}, Perimeter is {2}".format(8, circle_2.area(), circle_2.perimeter())

