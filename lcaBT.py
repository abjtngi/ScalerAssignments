# Definition for a  binary tree node
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

def isValPresent(root, val):
	if root is None:
		return False

	if root.val == val:
		return True
	
	return isValPresent(root.left, val) or isValPresent(root.right, val)


def findlca(root, lca, x, y):
	if root is None:
		return False, lca
	if root.val == x or root.val == y:
		return True, root
	left, lca = findlca(root.left, lca, x, y)
	right, lca = findlca(root.right, lca, x, y)

	if left and right:
		lca = root

	return (left or right), lca


class Solution:
	# @param A : root node of tree
	# @param B : integer
	# @param C : integer
	# @return an integer
	def lca(self, A, B, C):
		lca = None
		if isValPresent(A, B) and isValPresent(A, C):
			lca = findlca(A, lca, B, C)[1]
		
		return lca


if __name__ == '__main__':
	root = TreeNode(1)
	print(Solution().lca(root, 1, 1).val)
