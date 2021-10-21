import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

tree = {}
for _ in range(n): 
    root, left, right = input().rstrip().split() 
    tree[root] = (left, right)


def preorder(node): 
    if node == '.': 
        return 
    print(node, end = "") 
    preorder(tree[node][0]) 
    preorder(tree[node][1]) 

def inorder(node): 
    if node == '.': 
        return 
    inorder(tree[node][0]) 
    print(node, end = "") 
    inorder(tree[node][1]) 
    
def postorder(node): 
    if node == '.':
        return 
    postorder(tree[node][0]) 
    postorder(tree[node][1]) 
    print(node, end = "")

preorder('A')
print("") 
inorder('A') 
print("") 
postorder('A')

