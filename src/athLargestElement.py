'''
https://www.scaler.com/academy/mentee-dashboard/class/14517/assignment/problems/989?navref=cl_tt_lst_sl
'''
from heapq import heappush, heappop
class Solution:
    # @param A : integer
    # @param B : list of integers
    # @return a list of integers
    def solve(self, A, B):
        res = []
        minHeap = []
        for num in B:
            heapSize = len(minHeap)
            if heapSize < A:
                res.append(-1)
                heappush(minHeap, num)
            else:
                if num > minHeap[0]:
                    heappop(minHeap)
                    heappush(minHeap, num)
                res.append(minHeap[0])
        
        return res


if __name__ == '__main__':
    print(Solution().solve(2, [15, 20, 99, 1]))
