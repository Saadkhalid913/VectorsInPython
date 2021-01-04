'''
2 dimentional Vector class by Saadkhalid913
'''

import numpy as np
import matplotlib.pyplot as plt 
import math

__all__ = ["Vector"]

# CONSTANTS 
pi = math.pi

class Vector(object):
    '''
    Vector class with instance attributes x, y, x-component, y-component, Magnitude, Theta - Terminal angle of vector in radians

    - Supports +, -, +=, -=, == operators 
    - Class attribute "scale" serves as scale for plotting vectors
    '''
    scale = 100 

    def __init__(self, x_comp: int, y_comp: int,  x=0, y=0,):


        self.x, self.y = x, y 
        self.x_comp, self.y_comp = x_comp, y_comp
        self.Magnitude = math.sqrt(abs(x_comp) ** 2 + abs(y_comp) ** 2)

        if x_comp == 0:
            self.theta = pi/2
        elif y_comp == 0:
            self.theta = 0
        elif x_comp >= 0 and y_comp >= 0:
            self.theta = math.atan(y_comp/x_comp)
        elif x_comp < 0 and y_comp < 0:
            self.theta = math.atan(y_comp/x_comp) + pi
        elif x_comp < 0 and y_comp >= 0:
            self.theta = pi + math.atan(y_comp/x_comp)
        elif x_comp >= 0 and y_comp < 0:
            self.theta = 2 * pi + math.atan(y_comp/x_comp)

    def __repr__(self):
        return str(
            [(self.x, self.y), self.x_comp, self.y_comp])
        
    def __str__(self):
        return str(
            [(self.x, self.y), self.x_comp, self.y_comp])
        
    def __add__(self,v2):
        return Vector(
            self.x_comp + v2.x_comp,
            self.y_comp + v2.y_comp,
            self.x,
            self.y)
    
    def __sub__(self, v2):
        return Vector(
            self.x_comp - v2.x_comp,
            self.y_comp - v2.y_comp,
            self.x,
            self.y)
        
    def __iadd__(self, v2):
        return self + v2 
    
    def __isub__(self, v2):
        return self - v2

    def __eq__(self, v2):
        if str(self) == str(v2):
            return True
        return False 

    def plot(self,plot, c="b"):
        '''
        Takes 2 kwargs plot, c
        plot: instance of matplotlib.pyplot module or subplot class 
        c: Takes name of any named color of matplotlib module as type str()
        '''
        plot.quiver([self.x], [self.y], self.x_comp, self.y_comp, color=[c], scale=Vector.scale)