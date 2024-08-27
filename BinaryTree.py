class Node:
    def __init__(self, data):
        self.value = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

tree = BinaryTree()

noeud1 = Node(1)
noeud2 = Node(2)
noeudA = Node('a')
noeudB = Node('b')
noeud2.left = noeudA
noeud2.right = noeudB
noeud3 = Node(3)

tree.root = noeud1
noeud1.left = noeud2
noeud1.right = noeud3
