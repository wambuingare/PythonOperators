import math

class Circle:
    def __init__(self,r):
        self.r = r     
    def area(self):
     C = math.pi*self.r**2
     return C


class Square:
    def __init__(self,a):
        self.a = a
    def area(self):
      S=(self.a)*(self.a)
      return S


class Rectangle:
    def __init__(self,w,l):
        self.w = w
        self.l = l
    def area(self):
      P = self.w*self.l
      return P

class Sphere:
    def __init__(self,r):
        self.r = r
    def area(self):
        R = math.pi*self.r*self.r*self.r
        return R
           
            
         

       