'''
This is exactly like mergeKSortedLists with one difference: The ListNode definition provided by Scaler does not have __lt__ defined. 
So first traverse through lists to reconstruct them as orderable listnodes and then use the same algorithm 
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self) -> str:
        return f'{self.val} -> {str(self.next)}'


class OListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __lt__(self, other):
        return self.val <= other.val

    def __repr__(self) -> str:
        return f'{self.val} -> {str(self.next)}'


from heapq import heappush, heappop
class Solution:
    # @param A : list of linked list
    # @return the head node in the linked list
    def mergeKLists(self, A):
        # setattr(ListNode, "__lt__", lambda self, other: self.val <= other.val)
        n = len(A)
        minHeap = []
        oA = []
        for listNode in A:
            ohead = OListNode(listNode.val)
            oCurrNode = ohead
            while listNode:
                oCurrNode.next = OListNode(listNode.val)
                oCurrNode = oCurrNode.next
                listNode = listNode.next
            oA.append(ohead.next)
        for listNode in oA:
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
    tc = TestCaseCreator()
    A = tc.getKLists("10 9 8 20 38 44 55 65 66 79 87 2 68 72 5 5 55 61 73 89 2 30 73 4 28 73 84 96 3 54 82 83 5 15 33 38 94 100 1 4 5 22 32 42 64 86 2 11 78")
    for listHead in A:
        print(listHead)
    mergeListHead = Solution().mergeKLists(A)
    curr = mergeListHead
    while curr:
        print(curr.val, end=" -> ")
        curr = curr.next
