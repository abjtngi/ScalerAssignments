'''
https://www.scaler.com/academy/mentee-dashboard/class/14745/assignment/problems/1243?navref=cl_tt_lst_sl
'''

from heapq import heappush, heappop


class MaxHeap:
    def __init__(self):
        self.heap = []

    def push(self, val):
        heappush(self.heap, -val)
    
    def pop(self):
        return -1*heappop(self.heap)

    def peek(self):
        return -1*self.heap[0]


class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        maxHeap = MaxHeap()
        res = []
        for i in range(len(A)):
            k = A[i]
            maxHeap.push(k)
            if i < 2:
                res.append(-1)
                continue
            largestThree =  []
            for _ in range(3):
                largestThree.append(maxHeap.pop())
            product = largestThree[0] * largestThree[1] * largestThree[2]
            for i in range(3):
                maxHeap.push(largestThree[i])
            res.append(product)

        return res


if __name__ == '__main__':
    A = [1, 2, 3, 4, 5]
    print(Solution().solve(A))
