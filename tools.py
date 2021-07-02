import tripy
import sys
import pandas as pd
from plotnine import ggplot, aes, geom_polygon, geom_segment, geom_point

# Function for window to viewport transformation
def WindowtoViewport(x_w, y_w,
                     x_wmax, y_wmax,x_wmin, y_wmin, x_vmax,
					y_vmax, x_vmin, y_vmin):
							
	# point on viewport
	# calculating Sx and Sy
	sx = (x_vmax - x_vmin) / (x_wmax - x_wmin)
	sy = (y_vmax - y_vmin) / (y_wmax - y_wmin)

	# calculating the point on viewport
	x_v = x_vmin + ((x_w - x_wmin) * sx)
	y_v = y_vmin + ((y_w - y_wmin) * sy)

	print("The point on viewport:(", int(x_v),
								",", int(y_v), ")")

#tranforms point from range [a,b] to [c,d]
def transform(n,a,b,c,d):
    res=(((n-a)/(b-a))*(d-c))+c
    print(round(res,2))
    
# Driver Code
if __name__ == '__main__':
	action = sys.argv[1]
	if action == "wtv":
		#(x_w, y_w,
		# x_wmax, y_wmax, x_wmin, y_wmin,
		# x_vmax, y_vmax, x_vmin, y_vmin)
		WindowtoViewport(3, -1,10, 4, -2,-4 , 640, 40, 40, 440)
	elif action == "transform":
    # tranforms point n from range [a,b] to [c,d]
		a=-1
		b=1
		c=0
		d=1
		for n in [0.2,0.4,-0.8]:
			transform(n,a,b,c,d)
	elif action == "triangle":
		# Polygon can be clockwise or counter-clockwise
		# polygon = [(-3,1), (3, 1), (2, -2.5), (6.5, -1.5), (8,2.5), (3,6), (-1.5,3),(-3,5)]
		polygon = [(1,7), (3, 2), (7, 1), (12,4), (9,6), (8,9), (6,5)]
		triangles = tripy.earclip(polygon)
  		df=make_frame_from_triangles(triangles)
		(ggplot(df, aes(x='x', y='y')) + geom_point(color='red') + geom_segment(aes(x='x', y='y', xend='xend', yend='yend')))

		for i in triangles: 
			print (i)
		
