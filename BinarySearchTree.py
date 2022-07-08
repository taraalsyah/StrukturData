class Node:
    def __init__(self,data=None):
        self.left = None
        self.right = None
        self.data = data
    def insert(self,d):
        if self.data:
            if d < self.data:
                if self.left is None:
                    self.left = Node(d)
                else:
                    self.left.insert(d)
            elif d > self.data:
                if self.right is None:
                    self.right = Node(d)
                else:
                    self.right.insert(d)
        else:
            self.data = d
    def search(self,value):
        if value == self.data:
            print(f'data anda ada yeay!!! = {self.data}')
        else:
            if value < self.data:
                if self.left:
                    self.left.search(value)
                else:
                    print('data tidak di temukan')
            elif value > self.data:
                if self.right:
                    self.right.search(value)
                else:
                    print('data tidak di temukan')

    def printData(self):
        if self.left:
            self.left.printData()
        print(self.data)

        if self.right:
            self.right.printData()            

root = Node()
root.insert(10)
root.insert(4)
root.insert(1)
root.insert(9)
root.insert(7)
root.printData()
root.search(4)