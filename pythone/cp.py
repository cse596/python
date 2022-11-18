class BST:
  def __init__(self,key):
    self.key = key
    self.lchild = None
    self.rchild = None
  
  def insert(self,data):
    if self.key is None:
      self.key=data
      return 
    if self.key==data:
      return    
    if self.key>data:
      if self.lchild:
        self.lchild.insert(data)
      else:
        self.lchild=BST(data)
    else:
      if self.rchild:
        self.rchild.insert(data)
      else:
        self.rchild=BST(data)
 
  def search(self,data):
    if self.key==data:
      print("node is found")
      return
    if data<self.key:
      if self.lchild:
        self.lchild.search(data)
      else:
        print("node is not present in tree")
    else:
      if self.rchild:
        self.rchild.search(data)
      else:
        print("node is not present in tree")
 
  def delete(self,data):
    if self.key is None:
      print("Tree is empty")
      return
    if data<self.key:
      if self.lchild:
        self.lchild=self.lchild.delete(data)
      else:
        print("given node is not present in tree")
    elif data>self.key:
      if self.rchild:
        self.rchild=self.rchild.delete(data)
      else:
        print("given node is not present in tree")
    else:
      if self.lchild is None:
        temp=self.rchild
        self=None
        return temp
      if self.rchild is None:
        temp=self.lchild
        self=None
        return temp
      node=self.rchild
      while node.lchild:
        node=node.lchild
      self.key=node.key
      self.rchild=self.rchild.delete(node.key)
    return self
 
  def inorder(self):
    if self.lchild:
      self.lchild.inorder()
    print(self.key,end=" ")
    if self.rchild:
      self.rchild.inorder() 
 
  def preorder(self):
    print(self.key,end=" ")
    if self.lchild:
      self.lchild.preorder()
    if self.rchild:
      self.rchild.preorder()  
 
  def postorder(self):
    if self.lchild:
      self.lchild.postorder()
    if self.rchild:
      self.rchild.postorder()
    print(self.key,end=" ") 

root=BST(10)
list=[45, 15, 79, 90, 10, 55, 12, 20, 50]
for i in list:
  root.insert(i)
 
print("SEARCH OPERATION\n")
root.search(90)
root.search(1)
 
print("\nBST TRAVERSALS- INORDER,PREORDER, POSTORDER\n")
print("Inorder Traversal",end=" ")
root.inorder()
print("\n")
print("Preorder Traversal",end=" ")
root.preorder()
print("\n")
print("Postorder Traversal",end=" ")
root.postorder()
 
print("\nDELETION OPERATION - case 1\n")
root.delete(12)
print("\nInorder Traversal",end=" ")
root.inorder()
print("\n")
print("Preorder Traversal",end=" ")
root.preorder()
print("\n")
print("Postorder Traversal",end=" ")
root.postorder()
 
print("\nDELETION OPERATION - case 2\n")
root.delete(55)
print("\n Inorder Traversal",end=" ")
root.inorder()
print("\n")
print("Preorder Traversal",end=" ")
root.preorder()
print("\n")
print("Postorder Traversal",end=" ")
root.postorder()
 
print("\nDELETION OPERATION - case 3\n")
root.delete(45)
print("\n Inorder Traversal",end=" ")
root.inorder()
print("\n")
print("Preorder Traversal",end=" ")
root.preorder()
print("\n")
print("Postorder Traversal",end=" ")
root.postorder()
