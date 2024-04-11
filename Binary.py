class Binary:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def inOrderTraversal(node):
    if node is None:
        return
    inOrderTraversal(node.left)
    print(node.data, end=", ")
    inOrderTraversal(node.right)

root = Binary('14')
node1 = Binary('5')
node2 = Binary('15')
node3 = Binary('1')
node4 = Binary('2')
node5 = Binary('9')
node6 = Binary('6')
node7 = Binary('12')
node8 = Binary('21')

root.left = node1
root.right = node2

node1.left = node3
node1.right = node4

node2.left = node5
node2.right = node6

node3.left = node7
node3.right = node8

inOrderTraversal(root)
