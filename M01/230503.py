import math
import numpy as np  #For arrays and matrix

if 1:
    def compute_length(degree):
        sin = math.sin(math.radians(degree))
        length = sin*(360/degree)
        return length
    print(compute_length(30))


if 1:
    def compute_area(degree):
        sin_degree = math.sin(math.radians(degree))
        cos_degree = math.cos(math.radians(degree))
        area_degree = sin_degree*cos_degree/2
        area = (360/degree)*area_degree
        return area
    print(compute_area(30))


if 1:
    def get_y(x): 
        '''
        This function aims to compute y when x is given
        y = sqrt(r^2 - x^2)
        '''
        y = np.sqrt(1-x*x)
        return y
    
    #set delta_x, delta_x cang nho thi viec tinh dien tich cang chinh xac
    delta_x = 0.001

    #get the values of x
    #Tao array voi vi tri bat dau la -1, vi tri ket thuc la (1+delta_x), buoc nhay la delta_x
    segments = np.arange(-1, 1+delta_x,delta_x)

    #compute rectangle widths
    begin = segments[0:-1]
    end = segments[1:]
    width = end - begin

    #compute heights
    y = get_y(begin)

    #Compute area
    area = np. sum(width*y)
    print(area*2)

