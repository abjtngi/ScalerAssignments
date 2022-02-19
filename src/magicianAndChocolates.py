'''
https://www.scaler.com/academy/mentee-dashboard/class/14745/assignment/problems/362?navref=cl_tt_nv
'''

from heapq import heapify, heappop, heappush


class Solution:
	# @param A : integer
	# @param B : list of integers
	# @return an integer
	def nchoc(self, A, B):
		maxChocolatesEaten = 0
		p = pow(10,9) + 7
		if len(B) == 0:
			return 0
		B = [-x for x in B]
		heapify(B)
		for _ in range(A):
			if len(B) == 0:
				break
			chocolatesInMaxBag = -1 * heappop(B)
			maxChocolatesEaten += (chocolatesInMaxBag % p)
			replacementChocolates = chocolatesInMaxBag // 2
			heappush(B, -replacementChocolates)
		
		return maxChocolatesEaten%p


if __name__ == '__main__':
	A = 10
	B = [ 2147483647, 2000000014, 2147483647 ]
	print(Solution().nchoc(A, B))
