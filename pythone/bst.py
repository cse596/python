from msilib.schema import SelfReg
from typing import Self


class BST:
    def _init_(self,key):
        self.key=key
        self.lchild=None
        self.rchild=None
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
            print("tree is empty")
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
                print("given node is npot present in tree")
        else:
            if self.lchild is None:
                temp=self.rchild
                self=None
                return temp
            if self.rchild is None:
                temp=self.rchild
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
            print(self.key,end="")
        if self.rchild:
            self.rchild.inorder()
    def preorder():
        print(Self.key,end="")
        if Self.lchild:
            Self.lchild.preorder()
        if Self.rchild()

        



        
