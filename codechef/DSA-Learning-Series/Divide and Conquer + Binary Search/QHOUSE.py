import sys
def get_square_base():
	l, r = 0, 1000
	value = r
	while l <= r:
		mid = (l+r)//2
		print('? %d %d'%(mid, 0))
		sys.stdout.flush()
		answer = input().strip()
		if answer == 'NO':			
			r = mid - 1
		else:
			value = mid
			l = mid + 1
	return value

def get_triangle_base(square_base):
	l, r = square_base, 1000
	value = r
	while l <= r:
		mid = (l+r)//2
		print('? %d %d'%(mid, 2 * square_base))
		sys.stdout.flush()
		answer = input().strip()
		if answer == 'NO':
			r = mid - 1
		else:
			value = mid
			l = mid + 1
	return value

def get_triangle_top(square_top):
	l, r = square_top, 1000
	value = r
	while l <= r:
		mid = (l+r)//2
		print('? %d %d'%(0, mid))
		sys.stdout.flush()
		answer = input().strip()
		if answer == 'NO':
			r = mid - 1
		else:
			value = mid
			l = mid + 1
	return value

square_base = get_square_base()
# print('square_base', square_base)
triangle_base = get_triangle_base(square_base)
# print('triangle_base', triangle_base)
triangle_top = get_triangle_top(2*square_base)
# print('triangle_top', triangle_top)
area = (2*square_base)**2 + (triangle_top-2*square_base)*triangle_base
print('! %d'%(area))
