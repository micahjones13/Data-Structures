from dll_stack import Stack
from dll_queue import Queue
import sys
sys.path.append('../queue_and_stack')


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree | key and value are same in these.
    def insert(self, value):
        if value < self.value:
            # go left
            # if there is nothing to the left
            if not self.left:
                # insert it. It's a binary search tree.
                self.left = BinarySearchTree(value)
            # if there is something there, keep going until there isn't!
            else:
                self.left.insert(value)
        else:
            # go right
            if not self.right:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not

    def contains(self, target):
        if self.value == target:
            return True

        if target < self.value:
            # go left
            if not self.left:
                # it's not here
                return False
            else:
                return self.left.contains(target)
        else:
            # target > value, go right
            if not self.right:
                return False
            else:
                return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        # just keep going right until you can't, then return that value
        if not self.right:
            return self.value
        return self.right.get_max()

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    # just modifying values, so no need to return the recursion call
    def for_each(self, cb):
        cb(self.value)

        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass


"""
CLASS NOTES
Left subtree of a node contains only nodes with keys lessar than the node's key.
THe right subtree of a node contains only nodes with keys greater than the node's key.
The left and right subtree each must also be a binary search tree.

To search a given key in binary search, we first compare it with root if the key is presten at root, return it. If key is greater
than the root, we recur for right subtree of root node. otherwise recur for left

If smaller, left. Bigger or Equal, right.
Doesn't need to be balanced.
When deleting, smaller child becomes parent
Deleting root is special. When deleting root, it's replaced by highest node on left side.
Root starts as first node and stays unless deleted
Each node is a root for another binary search tree

"""
