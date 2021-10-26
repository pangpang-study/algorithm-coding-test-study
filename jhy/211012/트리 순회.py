import sys
from types import prepare_class

input = sys.stdin.readline

global pre_result, in_result, post_result
pre_result, in_result, post_result = "", "", ""

def preorder(index):
    global pre_result
    node = nodes[index][0]

    left, right = nodes[index][1][0], nodes[index][1][1]
    
    if nodes[index] != '.':
        pre_result += node
        if left != '.':
            preorder(ord(left) - ord("A"))
        if right != '.':
            preorder(ord(right) - ord("A"))

def inorder(index):
    global in_result
    node = nodes[index][0]

    left, right = nodes[index][1][0], nodes[index][1][1]
    
    if nodes[index] != '.':
        if left != '.':
            inorder(ord(left) - ord("A"))
        in_result += node
        if right != '.':
            inorder(ord(right) - ord("A"))

def postorder(index):
    global post_result
    node = nodes[index][0]

    left, right = nodes[index][1][0], nodes[index][1][1]
    
    if nodes[index] != '.':
        if left != '.':
            postorder(ord(left) - ord("A"))
        if right != '.':
            postorder(ord(right) - ord("A"))
        post_result += node

n = int(input())

nodes = [''] * n

for i in range(n):
    node, left, right = map(str, input().split())

    nodes[ord(node) - ord("A")] = ([node, [left, right]])
    #0번지는 A의 관계 리스트 ... n - 1번지는 (A + N - 1)의 관계 리스트

preorder(0)
inorder(0)
postorder(0)

print(pre_result)
print(in_result)
print(post_result)