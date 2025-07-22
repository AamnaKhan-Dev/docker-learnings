class Circle:
    def __init__(self, radius):
        self.radius=radius
        
    #works as variable
    @property
    def area(self):
        return 3.14*(self.radius**2)
    
    @property
    def circumference(self):
        return 2*3.14*self.radius
       
        # self.area = 3.14*(self.radius**2)
        # self.circumference = 2*3.14*self.radius
        
    # def area(self):
    #     return 3.14*(self.radius**2)
    
    # def circumference(self):
    #     return 2*3.14*self.radius
     
    
    

circle1 = Circle(5) #calling class
print(circle1.area)