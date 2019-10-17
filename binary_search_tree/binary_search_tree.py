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
        if node.left:
            self.in_order_print(node.left)
        print(node.value)
        if node.right:
            self.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal

    def bft_print(self, node):
        """
        make a queue
        add start node to queue
        while queue not empty
        pop front item
        do the thing(print, ect)
        if left:
            add left
        if right:
            add right
        """
        self.queue = Queue()
        self.queue.enqueue(node)
        while self.queue.size > 0:
            popped = self.queue.dequeue()
            print(popped.value)
            if popped.left:
                self.queue.enqueue(popped.left)
            if popped.right:
                self.queue.enqueue(popped.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        """
         create stack - use dll stack
         push start node to stack
         while stack > 0
         pop top item in stack
         do the thing(print)
         if left child
             push left to stack
         if right child 
         push right to stack

        """
        self.stack = Stack()
        self.stack.push(node)
        # print(self.stack.size, 'size')
        while self.stack.size > 0:
            popped = self.stack.pop()
            print(popped.value)
            if popped.left:
                self.stack.push(popped.left)
            if popped.right:
                self.stack.push(popped.right)

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT

    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass


# test = BinarySearchTree(5)
# test.insert(2)
# test.insert(8)
# test.insert(4)
# test.dft_print(test)
# test1 = BinarySearchTree(1)
# test1.insert(8)
# test1.insert(7)
# test1.insert(6)
# test1.insert(3)
# test1.insert(4)
# test1.insert(2)
# # test1.bft_print(test1)
# test1.in_order_print(test1)
# print("1\n2\n3\n4\n5\n6\n7\n8\n")

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

Traversal vs Search:
Traversal you're done when you've visited everything
Search you're done when you find what you're looking for

Depth: All the way to the end of a path until you're done. Ie, go right until you can't anymore. Then go back one node, go the other 
way until you can't! Then go back until there are new places, and then repeat.
Try to go Right. 
If you can, go right.
If no right, go left. If you can't go left, go back.

*When using a stack, make sure to pop the item you're done with or else infinite loop

Printing in order from samllest to largest? Which way should you go then? left or right?
Psuedo Code:
create stack - use dll stack
push start node to stack
while stack > 0
pop top item in stack
do the thing(print)
if left child
    push left to stack
if right child 
    push right to stack


Breadth First Search: 
Go left and right before you go deeper.
Goes by layers
Recursion here doesn't work, gotta do iterativley 
Rules: 
    go left and right, find new paths, the go back until you've found everthing a each layer
Pseudocode:
    make a queue
    add start node to queue
    while queue not empty
        pop front item
        do the thing(print, ect)
        if left:
            add left
        if right:
            add right
        

"""
