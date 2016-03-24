__author__ = 'edwingsantos'

from BinarySearchDS.BinarySearchTree import BST

bst = BST()



bst.insert(45)
bst.insert(12)
bst.insert(-1)
bst.insert(0)
bst.insert(-9)

bst.traverseInOrder()
print("--"*50)
bst.remove(-1)
bst.traverseInOrder()
print("--"*50)
bst.remove(12)
bst.traverseInOrder()

print ("**" *50)
print (" MAX: %d" % bst.getMax())
print(" MIN: %d" % bst.getMin())