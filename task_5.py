def triangle_area(val1,val2,val3):
 area = (val1+val2+val3)/2
 return (area*(area-val1)*(area-val2)*(area-val3)) ** 0.5
print(triangle_area(15,20,15))
