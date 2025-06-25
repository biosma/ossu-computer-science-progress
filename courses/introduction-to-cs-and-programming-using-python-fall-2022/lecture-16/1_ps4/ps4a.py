# Problem Set 4A
# Name:
# Collaborators:

from tree import Node # Imports the Node object used to construct trees

# Part A0: Data representation
# Fill out the following variables correctly.
# If correct, the test named test_data_representation should pass.
tree1 = Node(8, Node(2, Node(1), Node(6)), Node(10))
tree2 = Node(7, Node(2, Node(1), Node(5, Node(3), Node(6))),  Node(9, Node(8), Node(10)))
tree3 = Node(5, Node(3, Node(2), Node(4)), Node(14, Node(12), Node(21, Node(20), Node(26))))

def find_tree_height(tree):
    '''
    Find the height of the given tree
    Input:
        tree: An element of type Node constructing a tree
    Output:
        The integer depth of the tree
    '''
    if tree is None:
        return 0
    elif tree.left is None and tree.right is None:
        return 0
    else:
        return 1 + max(find_tree_height(tree.left), find_tree_height(tree.right))

# print(find_tree_height(tree1)) # should print 3
# print(find_tree_height(tree2)) # should print 3
# print(find_tree_height(tree3)) # should print 4

def find_tree_size(tree):
    '''
    Find the size of the given tree
    Input:
        tree: An element of type Node constructing a tree
    Output:
        The integer size of the tree
    '''
    if tree is None:
        return 0
    elif tree.left is None and tree.right is None:
        return 1
    else:
        return 1 + find_tree_size(tree.left) + find_tree_size(tree.right)

# max heap comparator
def compare_func(child_value, parent_value):
 if child_value < parent_value:
    return True
 return False
# min heap comparator
# def compare_func(child_value, parent_value):
#  if child_value > parent_value:
#     return True
#  return False

def is_heap(tree, compare_func):
    '''
    Determines if the tree is a max or min heap depending on compare_func
    Inputs:
        tree: An element of type Node constructing a tree
        compare_func: a function that compares the child node value to the parent node value
            i.e. op(child_value,parent_value) for a max heap would return True if child_value < parent_value and False otherwise
                 op(child_value,parent_value) for a min meap would return True if child_value > parent_value and False otherwise
    Output:
        True if the entire tree satisfies the compare_func function; False otherwise
    '''
    if tree is None:
        return True
    elif tree.left is None and tree.right is None:
        return True
    elif tree.left is None:
        return is_heap(tree.right, compare_func) and compare_func(tree.right.value, tree.value)
    elif tree.right is None:
        return is_heap(tree.left, compare_func) and compare_func(tree.left.value, tree.value)
    else:
        return compare_func(tree.left.value, tree.value) and compare_func(tree.right.value, tree.value) and is_heap(tree.left, compare_func) and is_heap(tree.right, compare_func)

# compare_func = lambda x,y: x < y
# tr1 = Node(15,Node(4,Node(3,None,Node(2)),Node(1)),Node(11,Node(10),Node(7,Node(5))))
# tr2 = Node(10,Node(7,None,Node(4,Node(3,None,Node(5)))))
# print(is_heap(tr2, compare_func), tr2)

if __name__ == '__main__':
    # You can use this part for your own testing and debugging purposes.
    # IMPORTANT: Do not erase the pass statement below if you do not add your own code
    pass
