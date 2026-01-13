# main.py
# Polygon Area Calculator


class Rectangle:
    def __init__(self, width, height):
        # Initialize the width and height attributes
        self.width = width
        self.height = height

    def set_width(self, width):
        # Update the width attribute
        self.width = width

    def set_height(self, height):
        # Update the height attribute
        self.height = height

    def get_area(self):
        # Calculate area: width * height
        return self.width * self.height

    def get_perimeter(self):
        # Calculate perimeter: 2 * (width + height)
        return 2 * (self.width + self.height)

    def get_diagonal(self):
        # Calculate diagonal: (width^2 + height^2)^0.5
        return (self.width ** 2 + self.height ** 2) ** .5

    def get_picture(self):
        # Return a string representing the shape using lines of '*'
        # If width or height is larger than 50, return "Too big for picture."
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        
        picture = ""
        # Loop for the number of rows (height)
        for i in range(self.height):
            # Add a row of '*' equal to width, plus a newline
            picture += "*" * self.width + "\n"
        return picture

    def get_amount_inside(self, shape):
        # Calculate how many times the passed shape fits inside this one
        # Use integer division (//)
        return (self.width // shape.width) * (self.height // shape.height)

    def __str__(self):
        # Return string representation: Rectangle(width=5, height=10)
        return f"Rectangle(width={self.width}, height={self.height})"
    

class Square(Rectangle):
    def __init__(self, side):
        # Initialize the Square using the Rectangle's __init__ method
        # Pass 'side' for both width and height
        super().__init__(side, side)

    def set_side(self, side):
        # Update both width and height to the new side length
        self.width = side
        self.height = side

    def set_width(self, side):
        # Override set_width to ensure the square shape is maintained
        self.set_side(side)

    def set_height(self, side):
        # Override set_height to ensure the square shape is maintained
        self.set_side(side)

    def __str__(self):
        # Return string representation: Square(side=9)
        return f"Square(side={self.width})"


if __name__ == "__main__":
    # ... (Keep existing Rectangle tests)
    rect = Rectangle(10, 5)
    print(rect.get_area())
    rect.set_height(3)
    print(rect.get_perimeter())
    print(rect)
    print(rect.get_picture())

    # --- NEW LINES: Test the Square class ---
    sq = Square(9)
    print(sq.get_area())
    sq.set_side(4)
    print(sq.get_diagonal())
    print(sq)
    print(sq.get_picture())

    # Test interaction between Rectangle and Square
    rect.set_height(8)
    rect.set_width(16)
    print(rect.get_amount_inside(sq))