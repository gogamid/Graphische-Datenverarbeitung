#python3 window_to_viewport.py

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


def transform(n,a,b,c,d):
    res=(((n-a)/(b-a))*(d-c))+c
    print(res)
# Driver Code
if __name__ == '__main__':

    #(x_w, y_w,
    # x_wmax, y_wmax, x_wmin, y_wmin,
    # x_vmax, y_vmax, x_vmin, y_vmin)
    
	# WindowtoViewport(3, -1,10, 4, -2,-4 , 640, 440, 40, 40)
    
    for n in [0.2,0.4,-0.8]:
        transform(n,-1,1,0,1)
    
	
