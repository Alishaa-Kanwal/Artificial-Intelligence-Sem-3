def bfs(graph, initiate):
    explored= set()
    to_explore= [initiate]
    while to_explore:
        curr= to_explore.pop(0)
        if curr not in explored:
            explored.add(curr)
            print(curr)
            for neighbor in graph[curr]:
                if neighbor not in explored:
                    to_explore.append(neighbor)
graph={
    'A':['B','C'],
    'B':['D','E'],
    'C':['F'],
    'D':[],
    'E':['F'],
    'F':[]
}
print("BFS graph without queue")
bfs(graph,'A')
class A:
    def __init__(self,name):
        self.name= name
        self.children= []
    def add_child(self,child):
        self.children.append(child)
    
    def bfsClass(initiate):
        explored= set()
        to_explore= [initiate]
        while to_explore:
            curr= to_explore.pop(0)
            if curr not in explored:
                explored.add(curr)
                print(curr.name)
                for child in curr.children:
                    if child not in explored:
                        to_explore.append(child)

a= A('A')
b= A('B')
c= A('C')
d= A('D')
e= A('E')
f= A('F')
a.add_child(b)
a.add_child(c)
b.add_child(d)
b.add_child(e)
c.add_child(f)
e.add_child(f)
print("BFS class without queue")
A.bfsClass(a)