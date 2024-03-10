doc = """
RenoldsCalculator:
   private variable: 
      area, wetted_perimeter
   private functions:
      calculate_cross_sectional_area
      calcultate_wetted_perimeter
   public function:
      get_area
      get_wetted_perimeter
      calculate_reynolds_number

Classes inheriting ReynoldsCalculator
   ReynoldsCircle
   ReynoldsSquare
   ReynoldsRectangle
   ReynoldsChannel
"""

class ReynoldsCalculator:
    PI = 3.14159 # define a constant for pi

    def __str__(self) -> str:
        doc

    # define a constructor for the class
    def __init__(self, shape, dimension):
        self.shape = shape
        self.dimension = dimension

        # calculate area and wetted perimeter upon instance creation
        self.__area = self.__calculate_cross_sectional_area()
        self.__wetted_perimeter = self.__calculate_wetted_perimeter()

   # function to calculate and return reynolds number
    def calculate_reynolds_number(self, velocity, density, viscosity):
        hydraulic_diameter = 4 * self.__area / self.__wetted_perimeter # calculate the hydraulic diameter

        # calculate and return reynolds number
        reynolds_number = (velocity * hydraulic_diameter * density) / viscosity 
        return reynolds_number

   # function to calculate cross sectional area for each shape
    def __calculate_cross_sectional_area(self):
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

   # function to calculate wetted perimeter for each shape
    def __calculate_wetted_perimeter(self):
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

   # function to get private area variable      
    def get_area(self):
        return self.__area
    
    # function to get private wetted perimeter variable
    def get_wetted_perimeter(self):
        return self.__wetted_perimeter


# create a classes that inherits from ReynoldsCalculator 
class ReynoldsCircle(ReynoldsCalculator):
   def __init__(self, diameter):
      super().__init__( "circular", diameter)

class ReynoldsSquare(ReynoldsCalculator):
    def __init__(self, length):
        super().__init__("square", length)

class ReynoldsRectangle(ReynoldsCalculator):
    def __init__(self, length, breadth):
        super().__init__("rectangular", (length, breadth))

class ReynoldsChannel(ReynoldsCalculator):
    def __init__(self, length, breadth):
        super().__init__("channel", (length, breadth))

   
   

# Example usage
velocity = 2.0
density = 1000
viscosity = 0.001



circular_tube = ReynoldsCircle(0.05)
square_duct = ReynoldsSquare(0.1)
rectangular_duct = ReynoldsRectangle( 0.2, 0.1)
channel = ReynoldsChannel(0.15, 0.05)

print("Reynolds Number for Circular Tube:", circular_tube.calculate_reynolds_number(velocity, density, viscosity))
print("Reynolds Number for Square Duct:", square_duct.calculate_reynolds_number(velocity, density, viscosity))
print("Reynolds Number for Rectangular Duct:", rectangular_duct.calculate_reynolds_number(velocity, density, viscosity))
print("Reynolds Number for Channel:", channel.calculate_reynolds_number(velocity, density, viscosity))