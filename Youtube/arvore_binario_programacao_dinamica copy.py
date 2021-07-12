from queue import Queue

ROOT = 'root'

class Node:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

	def __str__(self):
		return str(self.data)

class BinaryTree:
    def __init__(self, data=None, node=None):
        if node:
            self.root = node
        elif data:
            node = Node(data)
            self.root = node
        else:
            self.root = None

    # percurso em ordem simétrica
    def simetric_traversal(self, node=None):
        if node == None:
            node = self.root
        if node.left:
            print('(', end=' ')
            self.simetric_traversal(node.left)
        print(node, end=' ')
        if node.right:
            self.simetric_traversal(node.right)
            print(')',end=' ' )


    def posorder_traversal(self,node=None):
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


    def inorder_traversal(self, node=None):
        if node == None:
            node = self.root
        if node.left:
            self.inorder_traversal(node.left)
        print(node, end=' ')
        if node.right:
            self.inorder_traversal(node.right)



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


class BinarySearchTree(BinaryTree):
    def insert(self, value):
        parent = None
        x = self.root
        while(x):
            parent = x
            if value < x.data:
                 x = x.left
            else:
                x = x.right
        if parent is None:
            self.root = Node(value)
        elif  value < parent.data:
            parent.left = Node(value)
        else:
            parent.right = Node(value)

    def search(self, value):
        return self._search(value, self.root)

    def _search(self, value, node):
        if node is None:
            return node
        if node.data == value:
            return BinarySearchTree(node)
        if value < node.data:
            return self._search(value, node.left)
        return self._search(value, node.right)


    # def search(self, value, node=0):
    #     if node is None:
    #         return node
    #     if node.data == value:
    #         return BinarySearchTree(node)
    #     if value < node.data:
    #         return self.search(value, node.left)
    #     return self.search(value, node.right)





def postorder_example_tree():
        tree = BinaryTree()

        n1 = Node('I')
        n2 = Node('N')
        n3 = Node('S')
        n4 = Node('C')
        n5 = Node('R')
        n6 = Node('E')
        n7 = Node('V')
        n8 = Node('A')
        n9 = Node('5')
        n0 = Node('3')


        n0.left = n6
        n0.right = n9
        n6.left = n1
        n6.right = n5
        n5.left = n2
        n5.right = n4
        n4.right = n3
        n9.left = n8
        n8.right = n7

        tree.root = n0

        return tree

if __name__ == "__main__":
    # tree = postorder_example_tree()
    # print("Percurso em pós ordem:")
    # tree.posorder_traversal()
    # print(f'Altura: {tree.hight()}')

    import random

    random.seed(77)

    def ramdom_tree():
        values = random.sample(range(1, 1000), 42)
        tree = BinarySearchTree()
        for v in values:
            tree.insert(v)
        return tree


    def exemple_tree():
        values = [61, 89, 66, 43, 51, 16, 55, 11, 79, 77, 82, 32]
        tree = BinarySearchTree()
        for v in values:
            tree.insert(v)
        return tree



    bst = exemple_tree()
    bst.inorder_traversal()

    print('\n-----')
    bst.levelorder_traversal()


    # print('\n-----')
    # itens = [1, 3, 981, 510, 1000]
    # for item in itens:
    #     r = bst.search(item)
    #     if r is None:
    #         print(item, 'não encontrado')
    #     else:
    #         print(r.root.data, 'encontrado')



    # def simetric_traversal(self, node=None):
    #     if node == None:
    #         node = self.root
    #     if node.left:
    #         print('(', end=' ')
    #         self.simetric_traversal(node.left)
    #     print(node, end=' ')
    #     if node.right:
    #         self.simetric_traversal(node.right)
    #         print(')',end=' ' )




  # tree = BinaryTree()
    # n1 = Node('a')
    # n2 = Node('+')
    # n3 = Node('*')
    # n4 = Node('b')
    # n5 = Node('-')
    # n6 = Node('/')
    # n7 = Node('c')
    # n8 = Node('d')
    # n9 = Node('e')

    # n6.left = n7
    # n6.right = n8
    # n5.left = n6
    # n5.right = n9
    # n3.left = n4
    # n3.right = n5
    # n2.left = n1
    # n2.right = n3

    # tree.root = n2

    # tree.simetric_traversal()
    # print()

