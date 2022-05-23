def area_of_triangle(x,y,z):
    semi_perimeter = (1/2)*(x+y+z)
    Area = (semi_perimeter*(semi_perimeter-x)*(semi_perimeter-y)*(semi_perimeter-z))**(1/2)
    
    return Area
