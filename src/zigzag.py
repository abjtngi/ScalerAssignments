class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Solution:

    def zigzag(self, root):

        if root is None:
            return

        # stacks for current and next level
        cst = list()
        nst = list()

        # boolean to check direction of printing
        l2r = True

        cst.append(root)

        while len(cst) > 0:
            t = cst.pop()
            print('{0} '.format(t.data), end='')

            if l2r:
                if t.left:
                    nst.append(t.left)
                if t.right:
                    nst.append(t.right)
            else:
                if t.right:
                    nst.append(t.right)
                if t.left:
                    nst.append(t.left)

            if len(cst) == 0:
                l2r = not l2r
                tst = cst
                cst = nst
                nst = tst
                print()


if __name__ == '__main__':
    root = Node(15)
    root.left = Node(10)
    root.right = Node(25)
    root.right.left = Node(20)
    root.right.right = Node(27)
    s = Solution()
    s.zigzag(root)