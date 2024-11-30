class new_node:
    def __init__(self,data):
        self.data= data
        self.beside= []
    
    def new_beside(self,beside):
        self.beside.append(beside)

def stack_dfs(initiate):
    structure=[initiate]
    explore= set()
    while structure:
        curr= structure.pop()
        if curr not in explore:
            print(curr.data)
            explore.add(curr)
            structure.extend(curr.beside[::-1])
            
class BT_Node:
    def __init__(self, data):
        self.data= data
        self.left= None
        self.right= None
    @staticmethod
    def Inorder_t(root):
        if root:
            BT_Node.Inorder_t(root.left)
            print(root.data)
            BT_Node.Inorder_t(root.right)
    @staticmethod
    def preorder_t(root):
        if root:
            print(root.data)
            BT_Node.preorder_t(root.left)
            BT_Node.preorder_t(root.right)
        
    @staticmethod
    def postorder_t(root):
        if root:
            BT_Node.postorder_t(root.left)
            BT_Node.postorder_t(root.right)
            print(root.data)

node1= new_node("A")
node2= new_node("B")
node3= new_node("C")
node4= new_node("D")
node5= new_node("E")
node1.beside.extend([node2,node5])
node2.beside.append(node3)
node3.beside.append(node4)

print("DFS traversal:")
stack_dfs(node1)
root= BT_Node(1)
root.left= BT_Node(2)
root.right= BT_Node(3)
root.left.left= BT_Node(4)
root.right.right= BT_Node(5)

print("\nInorder traversal:")
BT_Node.Inorder_t(root)
print("\nPreorder traversal:")
BT_Node.preorder_t(root)
print("\nPostorder traversal:")
BT_Node.postorder_t(root)