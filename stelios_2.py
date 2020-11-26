import math

class Airplane:
    def __init__(self, initX, initY, consumption, initF):
        self.initX = initX
        self.initY = initY
        self.consumption = consumption
        self.initF = initF

    def __repr__(self):
        return (f'Airplane({self.initX!r}, ' f'{self.initY!r}, ' f'{self.consumption!r}, '
                f'{self.initF!r})') 

    def GoTo(self, a, b):
        # i consume 10 littres per 1 km
        
        a1 = self.distance(self.initX, a, self.initY, b)
        #print (a1)
        # plane consumes consumption per km, so total consumption for trip would be a1(km) x comsumption per Km 
        if a1 * self.consumption  < self.initF:
            #print(a1 * self.consumption)
            #print(self.initF)
            self.initX = a
            self.initY = b
            self.initF = self.initF - a1 * self.consumption
            #print(self.initF)
            # return (Airplane(self.initX, self.initY, self.consumption, self.initF), 
            return True
        else:
            #return False
            #return (Airplane(self.initX, self.initY, self.consumption, self.initF), 
            return False
        
        

        #return (f'Airplane({self.radius!r}, {a}, ' f'{self.consumption!r}, '
        #        f'{self.initF!r})') 
        
        #return (self.radius,self.initY) 
    
    #def area(self, a, b):
    
    def extra_fuel(self, d):
        self.initF = d + self.initF
        #print(d)
        #return (Airplane(self.initX, self.initY, self.consumption, self.initF))
        

    @staticmethod
    def distance(x2,x1,y2,y1):
        return (math.sqrt((x2-x1)**2 + (y2-y1)**2))
    
  



def test_answer():
#assert inc(3) == 5
    airplane_position = Airplane(2,3,6,37)
    airplane_position.GoTo(5,6)  
    #assert airplane_position.GoTo(5,6) == True
    assert str(airplane_position) == 'Airplane(5, 6, 6, 11.54415587728429)'



