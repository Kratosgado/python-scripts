"""
RenoldsCalculator:
    functions{
    __init__ : constructor
    calculate_reynolds_number: calculates and returns renynolds_number
    calculate_cross_sectional_area : calculates area for each shape
    calculate_wetted_perimeter : calculates perimeter for each shape
    }
"""

class ReynoldsCalculator:
    PI = 3.14159 # define a constant for pi

    # define a constructor for the class
    def __init__(self, shape, dimension):
        self.shape = shape
        self.dimension = dimension

    def calculate_reynolds_number(self, velocity, density, viscosity):
        area = self.calculate_cross_sectional_area() # calculate the area
        wetted_perimeter = self.calculate_wetted_perimeter() # calculate the wetted perimeter

        hydraulic_diameter = 4 * area / wetted_perimeter # calculate the hydraulic diameter

        # calculate and return reynolds number
        reynolds_number = (velocity * hydraulic_diameter * density) / viscosity 
        return reynolds_number

    def calculate_cross_sectional_area(self):
        if self.shape == 'circular':
            radius = self.dimension / 2
            return self.PI * radius ** 2
        
        elif self.shape == 'square':
            return self.dimension ** 2
        
        elif self.shape == 'rectangular':
            length, width = self.dimension
            return length * width
        
        elif self.shape == 'channel':
            length, width = self.dimension
            return length * 0.5 * width

    def calculate_wetted_perimeter(self):
        if self.shape == 'circular':
            radius = self.dimension / 2
            return 2 * self.PI * radius
        elif self.shape == 'square':
            return 4 * self.dimension
        elif self.shape == 'rectangular':
            length, width = self.dimension
            return 2 * (length + width)
        elif self.shape == 'channel':
            length, width = self.dimension
            return length * width


# Example usage
velocity = 2.0
density = 1000
viscosity = 0.001

circular_tube = ReynoldsCalculator('circular', 0.05)
square_duct = ReynoldsCalculator('square', 0.1)
rectangular_duct = ReynoldsCalculator('rectangular', (0.2, 0.1))
channel = ReynoldsCalculator('channel', (0.15, 0.05))

print("Reynolds Number for Circular Tube:", circular_tube.calculate_reynolds_number(velocity, density, viscosity))
print("Reynolds Number for Square Duct:", square_duct.calculate_reynolds_number(velocity, density, viscosity))
print("Reynolds Number for Rectangular Duct:", rectangular_duct.calculate_reynolds_number(velocity, density, viscosity))
print("Reynolds Number for Channel:", channel.calculate_reynolds_number(velocity, density, viscosity))
