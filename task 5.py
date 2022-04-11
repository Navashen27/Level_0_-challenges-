def area_of_triangle(x, y, z):
    s = 0.5 * (x + y + z)
    s1 = s - x
    s2 = s - y
    s3 = s - z
    s4 = s1 * s2 * s3
    pre_area = s * s4
    area = sqrt(pre_area)
    return area
