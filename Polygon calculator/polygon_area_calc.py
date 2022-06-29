class Rectangle:
    'Class to define rectangle'
    rectangleCount = 0
    
    def __init__(self, width = 1, height = 1):
        self.width = width
        self.height = height
        Rectangle.rectangleCount += 1
    
    def set_width(self, new_width):
        self.width = new_width

    def set_height(self, new_height):
        self.height = new_height

    def get_area(self, minus_width = 0, minus_height = 0):
        return (self.width - minus_width) * (self.height - minus_height)
    
    def get_perimeter(self):
        return 2 * self.width + 2 * self.height
    
    def get_diagonal(self):
        return (self.width**2 + self.height**2)**.5
    
    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "\nToo big for picture\n"
        
        picture = "\n"
        for i in range(self.height):
            for j in range(self.width):
                picture += "*"
            picture += "\n"
        return picture
    
    def get_amount_inside(self, width_small, height_small):
        rec_inside = Rectangle(width_small, height_small)
        amount = round(self.get_area(self.width % width_small, self.height % height_small) / rec_inside.get_area())
        return amount, rec_inside.get_picture()
        del rec_inside
    
    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"
    
    def __repr__(self):
        return f"Rectangle(width={self.width}, height={self.height})"
    
    def __del__(self):
        Rectangle.rectangleCount -= 1
    
rec1 = Rectangle()
rec1.set_width(4)
rec1.set_height(3)

area1 = rec1.get_area()
perimetr1 = rec1.get_perimeter()
diagonal1 = rec1.get_diagonal()
picture1 = rec1.get_picture()
shape_in_shape1, pic_shish = rec1.get_amount_inside(3, 2)

print("Number of rectangles:", Rectangle.rectangleCount)   #rec1.rectangleCount ~ Rectangle.rectangleCount
print()
print(rec1)
print("Area:", area1)
print("Perimetr:", perimetr1)
print("Diagonal:", diagonal1)
print(picture1)
print("Number of small rectangles to fit inside big rectangle:", shape_in_shape1)
print(pic_shish)



class Square(Rectangle):
    'Class to define square (child of Rectangle class)'
    squareCount = 0
    
    def __init__(self, side = 1):
        self.width = side
        self.height = side
        Rectangle.rectangleCount += 1
        Square.squareCount += 1
        
    def set_side(self, new_side):
        self.width = new_side
        self.height = new_side
        
    def set_width(self, new_side):
        self.width = new_side
        self.height = new_side

    def set_height(self, new_side):
        self.width = new_side
        self.height = new_side
    
    def __str__(self):
        return f"Square(side={self.width})"
    
    def __repr__(self):
        return f"Square(side={self.width})"

squ1 = Square()
squ1.set_side(6)

area1 = squ1.get_area()
perimetr1 = squ1.get_perimeter()
diagonal1 = squ1.get_diagonal()
picture1 = squ1.get_picture()
shape_in_shape1, pic_shish = squ1.get_amount_inside(3, 2)

print("-----------------------")
print("Number of rectangles:", Rectangle.rectangleCount)
print("Number of squares:", Square.squareCount)
print()
print(squ1)
print("Area:", area1)
print("Perimetr:", perimetr1)
print("Diagonal:", diagonal1)
print(picture1)
print("Number of small squares to fit inside big square:", shape_in_shape1)
print(pic_shish)
