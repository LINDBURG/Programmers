class BT:
    def __init__(self, data, x, x_min, x_max):
        self.data = data
        self.x = x
        self.left = None
        self.right = None
        self.x_min = x_min
        self.x_max = x_max
        
def preorder(node, idx, lst):
    lst.append(node[idx].data)
    if node[idx].left != None:
        preorder(node, node[idx].left, lst)
    if node[idx].right != None:
        preorder(node, node[idx].right, lst)
    
def postorder(node, idx, lst):
    if node[idx].left != None:
        postorder(node, node[idx].left, lst)
    if node[idx].right != None:
        postorder(node, node[idx].right, lst)
    lst.append(node[idx].data)
    
def solution(nodeinfo):
    for i,j in enumerate(nodeinfo):
        j.insert(0,i+1)
    nodeinfo.sort(key= lambda x:(-x[2], x[1]))
    #print(nodeinfo)
    
    node = []
    target = nodeinfo.pop(0)
    node.append(BT(target[0],target[1], 0,100000))
    start = 0
    end = len(node)
    #print(node[0].data)
    
    while nodeinfo:
        y = nodeinfo[0][2]
        cnt = 0
        while nodeinfo:
            if nodeinfo[0][2] == y:
                target = nodeinfo.pop(0)
                #print(target)
                for parent in range(start,end):
                    if node[parent].x_min < target[1] < node[parent].x:
                        node[parent].left = end + cnt
                        node.append(BT(target[0], target[1], node[parent].x_min, node[parent].x))
                        cnt += 1
                        start = parent
                        #print("left")
                        break
                    elif node[parent].x < target[1] < node[parent].x_max:
                        node[parent].right = end + cnt
                        node.append(BT(target[0], target[1], node[parent].x, node[parent].x_max))
                        cnt += 1
                        start = parent
                        #print("right")
                        break
            else:
                start = end
                end = len(node)
                break
    #print(node)
    
    pre = []
    post = []
    preorder(node, 0, pre)
    postorder(node, 0, post)
    #print(pre)
    #print(post)
    
    return [pre, post]


