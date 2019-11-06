#!/usr/bin/python3

from sys import stdin


class Node:
    def __init__(self):
        self.children = []
        self.ratatosk = False  # ekstra
        self.visited = 0  # hm
        self.level = 0


def dfs(root):
    if root.ratatosk:
        return 0
    nodes_to_visit = [root]
    level = 0
    while nodes_to_visit:  # while listen ikke er tom
        print(nodes_to_visit)
        currentnode = nodes_to_visit[len(nodes_to_visit) - 1]  # siste i stack
        if currentnode.ratatosk:
            return level
        currentnode.visited=1
        if currentnode.children:  # hvis den har barn legg de til i stack
            nodes_to_visit.extend(currentnode.children)  # extend= append bare ikke array
            level = level + 1
        else:
            if currentnode.visited:  # gå opp et hakk
                nodes_to_visit.pop()  # Betyr at det er en parent over
                level = level - 1
            if (not level):
                nodes_to_visit.pop()
                print("sadsdads")
    return None

def dfs_b(root):
    root.visted=1
    nodes_to_visit = [root]
    level = 1
    while(nodes_to_visit):
        currentnode = nodes_to_visit.pop()
        if currentnode.ratatosk: 
            return currentnode.level
        for child in currentnode.children:
            if child.visited==0:
                child.level=currentnode.level+1
                nodes_to_visit.append(child)
                currentnode.visited=1
    return None

def bfs(root):
    if root.ratatosk:
        return 0
    nodes_to_visit = [root]
    while nodes_to_visit:  # while listen ikke er tom
        currentnode = nodes_to_visit.pop()  # siste i stack
        for child in currentnode.children:
            if child.visited == 0:
                child.level = currentnode.level + 1
                child.visited = 1
                if child.ratatosk:
                    return child.level
                nodes_to_visit.insert(0, child) 
        currentnode.visited = 2
    return None




funksjon = stdin.readline().strip()
number_of_nodes = int(stdin.readline())
nodes = []
for i in range(number_of_nodes):
    nodes.append(Node())
start_node = nodes[int(stdin.readline())]
ratatosk_node = nodes[int(stdin.readline())]
ratatosk_node.ratatosk = True
for line in stdin:
    number = line.split()
    temp_node = nodes[int(number.pop(0))]
    for child_number in number:
        temp_node.children.append(nodes[int(child_number)])

if funksjon == 'dfs':
    print(dfs_b(start_node))
elif funksjon == 'bfs':
    print(bfs(start_node))
elif funksjon == 'velg':
    print(bfs(start_node))
