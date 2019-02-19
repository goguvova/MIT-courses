"""
class_list=[[["peter","parker"],[]],[["bruce","wayne"],[100.0,74.0,89.0]]]

def get_stats(class_list):
    new_stats=[]
    for i in class_list:
        new_stats.append([i[0],i[1],avg(i[1])])
    return new_stats

def avg(grades):
    try:
        return sum(grades)/len(grades)
    except ZeroDivisionError:
        print("warning:no grades data")
        return 0.0
print(get_stats(class_list))
"""

    
    

class Coordinate(object):
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __str__(self):
        """ Returns a string representation of self """
        return "<" + str(self.x) + "," + str(self.y) + ">"
#    def distance(self,other):
        """ returns distance """
#        x_dist=(self.x-other.x)**2
#        y_dist=(self.y-other.y)**2
#        return(x_dist + y_dist)**0.5
    
c=Coordinate(3,4)
origin = Coordinate(0,0)
#print(c.x, origin.x)
#print(c.distance(origin))
#print(Coordinate.distance(c, origin))
#print(origin.distance(c))
print(c)

