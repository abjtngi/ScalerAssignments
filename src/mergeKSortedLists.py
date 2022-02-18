# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __lt__(self, other):
        return self.val <= other.val

    def __repr__(self) -> str:
        return f'{self.val} -> {str(self.next)}'
    '''
    def __gt__(self, other):
        return ((self.val) > (other.val))
  
    def __le__(self, other):
        return ((self.val) <= (other.val))
  
    def __ge__(self, other):
        return ((self.val) >= (other.val))
  
    def __eq__(self, other):
        return (self.val == other.val)

    def __repr__(self):
        return self.val
    '''
    

from heapq import heappush, heappop
class Solution:
    # @param A : list of linked list
    # @return the head node in the linked list
    def mergeKLists(self, A):
        # setattr(ListNode, "__lt__", lambda self, other: self.val <= other.val)
        n = len(A)
        minHeap = []
        for listNode in A:
            if listNode:
                heappush(minHeap, listNode)
        head = ListNode(None)
        currListNode = head
        while minHeap:
            minListNode = heappop(minHeap)
            currListNode.next = minListNode
            currListNode = currListNode.next
            if minListNode and minListNode.next:
                heappush(minHeap, minListNode.next)
        
        return head.next


class TestCaseCreator:
    def __init__(self) -> None:
        self.valList = []
        self.kLists = []

    def createValListFromValString(self, valString) -> bool:
        valString = valString.strip()
        try:
            self.valList = [int(x) for x in valString.split(" ")]
        except Exception as e:
            print(f'unexpected error occured: {str(e)}')
            return False
        return True

    def createKLists(self):
        if not self.valList:
            return
        numOfLists = self.valList[0]
        i = 1
        for _ in range(numOfLists):
            numOfNodes = self.valList[i]
            i += 1
            listHead = ListNode(self.valList[i])
            currNode = listHead
            i += 1
            for _ in range(numOfNodes-1):
                currNode.next = ListNode(self.valList[i])
                currNode = currNode.next
                i += 1
            self.kLists.append(listHead)
        return True

    def getKLists(self, valString):
        self.createValListFromValString(valString)
        self.createKLists()
        return self.kLists


if __name__ == '__main__':
    l1Head = ListNode(4)
    l1Head.next = ListNode(11)
    l2Head = ListNode(2)
    l2Head.next = ListNode(40)
    l3Head = ListNode(1)
    l3Head.next = ListNode(21)
    l3Head.next.next = ListNode(33)
    mergeListHead = Solution().mergeKLists([l1Head, l2Head, l3Head])
    curr = mergeListHead
    while curr:
        print(curr.val)
        curr = curr.next
    tc = TestCaseCreator()
    A = tc.getKLists("10 9 8 20 38 44 55 65 66 79 87 2 68 72 5 5 55 61 73 89 2 30 73 4 28 73 84 96 3 54 82 83 5 15 33 38 94 100 1 4 5 22 32 42 64 86 2 11 78")
    for listHead in A:
        print(listHead)
    mergeListHead = Solution().mergeKLists(A)
    curr = mergeListHead
    while curr:
        print(curr.val, end=" -> ")
        curr = curr.next
    