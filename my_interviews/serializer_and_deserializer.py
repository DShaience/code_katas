"""
Interview at video-indexer.
Asked to serialize/deserialize a binary tree

"""

"""
 *               1
 *             /  \
 *           11    22
 *          / \      \
 *        13   14     23


Initial discussion about the serialize/deserialize solution
We discussed how to generally approach the problem. Using recursion for serialization, and seeing
that we read it correctly afterwards

    return str(current) + sep + recursion(left) + sep + recursion(right)
    1,11,13,None,None,14,None,None,22,None,23,None,None
    # 1 -> 11 -> 13 -> [None,None], 14 -> [None, None], 22
"""

if __name__ == '__main__':
    my_binary_tree = [1, [11, [13, [None, None]], [14, [None, None]]],
                         [22, [None, [23, [None, None]]]]]

    def serializer(node):
        if node.value is None:
            return "None"
        return [str(node.val)+","+serializer(node.left)+","+serializer(node.right)]

    """
    Serialization
    ------------------------------------- 
    I used a recursive method to serialize the values of each node, using a separator between values.
    Each leaf is marked by having [None, None] "children".
    """

    my_tree_str = "1,11,13,None,None,14,None,None,22,None,23,None,None"
    my_tree_arr = my_tree_str.split(',')

    """
    Deserialization
    ------------------------------------- 
    For the deserializer, I tried to initially work with a recursive approach, but saw that it would be 
    difficult to do the separation for left/right in my attempted solution.
    
    Instead I might have adopted a iterative approach.
    Assuming each node has to have 2 children (including the terminal [None, None]),
    a better approach *might* have been to create left, right empty lists for the root value,
    then assign left-values until hitting Nones. Then return to the most recent node that had empty list,
    and assign values to it, until hitting Nones, etc.
    I haven't tested this approach, but this might have been the next approach I'd try, if time allowed.  
    """





