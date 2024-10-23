def triangle_def(side_1,side_2,side_3):
    if side_1 == side_2 == side_3:
        return("Your triangle is an Equilateral")
    elif side_1 != side_2 == side_3:
        return("Your triangle is an Isoceles")
    elif side_2 != side_3 == side_1:
        return("Your triangle is an Isoceles")
    elif side_1 == side_2 != side_3:
        return("Your triangle is an Isoceles")
    elif side_1 != side_2 != side_3:
        return("Your triangle is a scalene")
side_1 = int(input("Enter the value of your first side of the triangle: "))
side_2 = int(input("Enter the value of your second side of the triangle: "))
side_3 = int(input("Enter the value of your third side of the triangle: "))
determined = triangle_def(side_1,side_2,side_3)
print(determined)