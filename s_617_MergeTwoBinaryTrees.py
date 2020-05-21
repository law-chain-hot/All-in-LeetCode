"""
# {My own explanation of this problem}
# {2020.05.13}
# {Method: 1}
# {Recursion}

We can traverse both given tree by recursion

At every step, we check if the current node exists for both given trees.
If they both exist, we add them up, the sum is the value of the current node in the output tree.

And At every step, we call the original function with both left children of both given tree. 
The result of the function is considered as the left child of the current node. 

And also, in the same way, call the original function again with the right children. 

Finally, we return the new node, which is the root of new merged tree

"""


class Solution:
    def mergeTrees(self, t1, t2):

        # base case: t1 or t2 doesn't exist
        if not t1:
            return t2
        if not t2:
            return t1

        # t1 and t2 both exist
        ans = TreeNode(t1.val + t2.val)  
        ans.left = self.mergeTrees(t1.left, t2.left)
        ans.right = self.mergeTrees(t1.right, t2.right)

        return ans





"""
We can traverse both the given trees in a preorder fashion. At every step, 
we check if the current node exists(isn't null) for both the trees. If so, 
we add the values in the current nodes of both the trees and update the 
value in the current node of the first tree to reflect this sum obtained. 
At every step, we also call the original function mergeTrees() with the left 
children and then with the right children of the current nodes of the two trees. 
If at any step, one of these children happens to be null, we return the child 
of the other tree(representing the corresponding child subtree) to be added as 
a child subtree to the calling parent node in the first tree. At the end, the 
first tree will represent the required resultant merged binary tree.
"""


"""
Complexity Analysis
    - Time complexity : O(m). 
        A total of mm nodes need to be traversed. Here, mm represents the minimum number of nodes from the two given trees.

    - Space complexity : O(m) 
        The depth of the recursion tree can go upto mm in the case of a skewed tree. In average case, depth will be O(logm)O(logm).
"""

