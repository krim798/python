class coordinate(object):
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def distance(self,other):
        x_diff_sq=(self.x-other.x)**2
        y_diff_sq=(self.y-other.y)**2
        return(x_diff_sq + y_diff_sq)**0.5
    def __add__(self,other):
        new_coord = coordinate(self.x+other.x, self.y+other.y)
        return new_coord
    def __sub__(self,other):
        new_coord = coordinate(self.x-other.x, self.y-other.y)
        return new_coord
    def __eq__(self,other):
        if isinstance(other,coordinate):
            return (self.x==other.x and self.y==other.y)
    def __lt__(self,other):
        if isinstance(other,coordinate):
            return (self.distance(other)<1e-6)
    def __len__(self):
        return len(self)
    def __str__(self):
        return "<"+str(self.x)+","+str(self.y)+">"

c=coordinate(2,3)
origin= coordinate(0,0)
print(c.x)
print(origin.y)
print(c.distance(coordinate(5,6)))
print(c)
print(type(c.__str__))
print(isinstance(c,coordinate))
print(c+coordinate(5,6))
print(c-coordinate(5,6))
print(c==coordinate(2,3))
print(c<coordinate(2,4))
