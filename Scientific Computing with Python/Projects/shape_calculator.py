"""
Created for Free Code Camp project.
    
https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/polygon-area-calculator
"""
# Rectangle class
class Rectangle:
    # Initialize object
    def __init__(self,width,height):
        self.width = width
        self.height = height
    # Set width method
    def set_width(self,width):
        self.width = width
    # Set height method    
    def set_height(self,height):
        self.height = height
    # Get area method
    def get_area(self):
        return self.width * self.height
    # Get perimeter method
    def get_perimeter(self):
        return self.width*2 + self.height*2
    # Get diagonal method
    def get_diagonal(self):
        return (self.width**2 + self.height**2) ** .5
    # Get picture method - 'draws' shape using asteriks
    def get_picture(self):
        if self.height > 50 or self.width > 50:
            return "Too big for picture."
        pic = ""
        row = "*"*self.width
        for i in range(self.height):
            pic += row + '\n'
        return (pic)
    # Method to find how many of another shape can fit inside this shape.
    # Instruction specifed the other shape could NOT rotate.
    # Hence you cannoted just divided the areas of the shapes. 
    def get_amount_inside(self,other_shape):
        if other_shape.width > self.width or other_shape.height > self.height:
            return 0
        else:
            width_factor = int(self.width/other_shape.width)
            height_factor = int(self.height/other_shape.height)
            return width_factor * height_factor
    # Print / string representation method
    def __str__(self):
        return "Rectangle(width="+str(self.width)+", height="+str(self.height)+")"

# Square class, inherits from Rectangle class
class Square(Rectangle):
    # Initialize object
    def __init__(self,side):
        self.width = side
        self.height = side
     # Set width method   
    def set_width(self,width):
        self.width = width
        self.height = width
    # Set height method
    def set_height(self,height):
        self.height = height
        self.width = height
    # Set side method
    def set_side(self,side):
        self.width = side
        self.height = side
    # Print / string representation method
    def __str__(self):
        return "Square(side="+str(self.width)+")"