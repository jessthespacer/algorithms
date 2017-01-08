# format for point: tuple (x, y)

def length(point1, point2):
	return ((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)**0.5
	
def area_triangle(point1, point2, point3):
	a = length(point1, point2)
	b = length(point1, point3)
	c = length(point2, point3)
	s = (a + b + c)/2
	return (s * (s - a) * (s - b) * (s - c))**(0.5)

def area_polygon(points_list):
	base_point = points_list.pop()
	area = 0
	for n in range(len(points_list) - 1):
		area += area_triangle(base_point, points_list[n], points_list[n + 1])
	return area

points = [(0, 0), (2, 0), (3, 1), (3, 2), (1, 2)]	# area: 4.5 units^2
print(area_polygon(points))