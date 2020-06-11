import math

class SegmentTree(object):

	def __init__(self, arr):
		self.arr = arr
		self.n = len(arr)
		st_height = math.ceil(math.log2(self.n))
		st_size = (2 * (2 ** st_height)) - 1
		self.st = [0]*st_size

	def constructHelper(self, st_start, st_end, st_index):
		if st_start == st_end:
			self.st[st_index] = self.arr[st_start]
			return self.st[st_index]
		
		mid = (st_start) + (st_end-st_start)//2

		self.st[st_index] =  min(self.constructHelper(st_start, mid, 2*st_index+1), \
			self.constructHelper(mid+1, st_end, 2*st_index+2))

		return self.st[st_index]

	def construct(self):
		self.constructHelper(0, self.n-1, 0)
		# return self.st

	def queryHelper(self, st_start, st_end, q_start, q_end, st_index):
		if q_start <= st_start and q_end >= st_end:
			return self.st[st_index]
		
		if q_start > st_end or q_end < st_start:
			return float('inf')
		
		mid = (st_start) + (st_end-st_start)//2
		return min(self.queryHelper(st_start, mid, q_start, q_end, 2*st_index+1),\
			self.queryHelper(mid+1, st_end, q_start, q_end, 2*st_index+2))

	def query(self, q_start, q_end):
		if q_start > q_end or q_start < 0 or q_end >= self.n:
			return float('inf')
		return self.queryHelper(0, self.n-1, q_start, q_end, 0)


def main():
	N = int(input())
	arr = [int(i) for i in input().strip().split()]
	st_pos = SegmentTree(arr)
	st_pos.construct()
	st_neg = SegmentTree([-1*num for num in arr])
	st_neg.construct()
	T = int(input())
	for _ in range(T):
		[x, y] = [int(i) for i in input().strip().split()]
		range_pos_min = st_pos.query(x, y)
		range_neg_max = -1*st_neg.query(x, y)
		bef_range_neg_max = -1*st_neg.query(0, x-1)
		aft_range_neg_max = -1*st_neg.query(y+1, N-1)
		answer = range_pos_min + max(bef_range_neg_max, aft_range_neg_max, (range_neg_max-range_pos_min)/2)
		print(answer*1.0)
main()