import tripy
# Polygon can be clockwise or counter-clockwise
# polygon = [(-3,1), (3, 1), (2, -2.5), (6.5, -1.5), (8,2.5), (3,6), (-1.5,3),(-3,5)]
polygon = [(1,7), (3, 2), (7, 1), (12,4), (9,6), (8,9), (6,5)]
triangles = tripy.earclip(polygon)

for i in triangles: 
    print (i)