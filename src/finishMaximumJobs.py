'''
https://www.scaler.com/academy/mentee-dashboard/class/14520/assignment/problems/9291/?navref=cl_pb_nv_tb
'''
class Job:
    def __init__(self, startTime, endTime, interval):
        self.startTime = startTime
        self.endTime = endTime
        self.interval = interval


class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def solve(self, A, B):
        n = len(A)
        jobList = []
        for i in range(n):
            startTime = A[i]
            endTime = B[i]
            interval = endTime - startTime
            jobList.append(Job(startTime, endTime, interval))
        jobList.sort(key=lambda x: x.endTime)
        maxJobs = 0
        latestEndTime = 0
        for job in jobList:
            if job.startTime >= latestEndTime:
                maxJobs += 1
                latestEndTime = job.endTime
        
        return maxJobs


if __name__ == '__main__':
    A = [ 1, 5, 7, 1 ]
    B = [ 7, 8, 8, 8 ]
    print(Solution().solve(A, B))