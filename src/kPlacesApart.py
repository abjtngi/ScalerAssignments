from heapq import heappop, heappush

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def solve(self, A, B):
        n = len(A)
        resList = []
        minHeap = []
        for i in range(n):
            heappush(minHeap, A[i])
            if len(minHeap) == (B+1):
                resList.append(heappop(minHeap))
        while minHeap:
            resList.append(heappop(minHeap))
        
        return resList



if __name__ == '__main__':
    print(Solution().solve([25, 16, 11, 31, 28, 20, 3, 8], 6))