from queue import Queue

ROOT = 'root'


class Node:
	def __init__(self, preco):
		self.preco = preco
		self.left = None
		self.right = None

	def __str__(self):
		return str(self.preco)


class BinaryDollarTree:
    def __init__(self, preco=None, acrescimo=None, decrescimo=None, periodo=None):
        if preco:
            preco = Node(preco)
            self.root = preco
        else:
            self.root = None
        self.preco = float(preco)
        self.acrescimo = float(acrescimo)
        self.decrescimo = float(decrescimo)
        self.periodo = int(periodo)

        for period in range(1, self.periodo + 1):
            self.precoMaior = self.preco * (1 + self.acrescimo)
            self.insert(self.precoMaior)
            self.pecoMenor = self.preco * (1 - self.decrescimo)
            self.insert(self.pecoMenor)


    def insert(self, value):
        parent = None
        x = self.root
        while(x):
            parent = x
            if value < x.preco:
                 x = x.left
            else:
                x = x.right
        if parent is None:
            self.root = Node(value)
        elif  value < parent.preco:
            parent.left = Node(value)
        else:
            parent.right = Node(value)


    def search(self, value):
        return self._search(value, self.root)


    def _search(self, value, node):
        if node is None:
            return node
        if node.preco == value:
            return BinaryDollarTree(node)
        if value < node.preco:
            return self._search(value, node.left)
        return self._search(value, node.right)


   # percurso em ordem simétrica
    def inorder_traversal(self, node=None):
        if node == None:
            node = self.root
        if node.left:
            self.inorder_traversal(node.left)
        print(node, end=' ')
        if node.right:
            self.inorder_traversal(node.right)


    def posorder_traversal(self, node=None):
        if node == None:
            node = self.root
        if node.left:
            self.posorder_traversal(node.left)
        if node.right:
            self.posorder_traversal(node.right)
        print(node)


    def hight(self,node=None):
        if node == None:
            node = self.root
        hleft = 0
        hright = 0
        if node.left:
            hleft = self.hight(node.left)
        if node.right:
            hright = self.hight(node.right)
        print(node)
        if hright > hleft:
            return hright + 1
        return hleft + 1


    def levelorder_traversal(self, node=ROOT):
        if node == ROOT:
            node = self.root

        queue = Queue()
        queue.push(node)
        while len(queue):
            node = queue.pop()
            if node.left:
                queue.push(node.left)
            if node.right:
                queue.push(node.right)
            print(node, end=" ")
        print()



if __name__ == "__main__":
    # tree = postorder_example_tree()
    # print("Percurso em pós ordem:")
    # tree.posorder_traversal()
    # print(f'Altura: {tree.hight()}')

    import random

    random.seed(77)

    def ramdom_tree():
        values = random.sample(range(1, 1000), 42)
        tree = BinaryDollarTree()
        for v in values:
            tree.insert(v)
        return tree


    def exemple_tree():
        values = [61, 89, 66, 43, 51, 16, 55, 11, 79, 77, 82, 32]
        tree = BinaryDollarTree()
        for v in values:
            tree.insert(v)
        return tree



    bst = exemple_tree()
    bst.inorder_traversal()

    print('\n-----')
    bst.levelorder_traversal()

