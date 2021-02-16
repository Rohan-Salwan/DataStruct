class node:
    def __init__(self,data):
        self.name=data
        self.visited = False
        self.level=-1
        self.parent=None
        
class graph:
    def __init__(self,node):
        self.nodes=node
        self.adjlist={}
        for n in self.nodes:
            self.adjlist[n]=[]

    
    def addadj(self,v,adj):
        self.adjlist[v].append(adj)
    
    def bfsandshortestpath(self,src):
        src.visited=True
        out=[]
        ls=[]
        ls.append(src)
        while 0<1:
            if ls==[]:
                break
            else:    
                o=ls.pop(0)
                out.append(o)
                src=o
                for bb in self.adjlist[src]:
                    if bb.visited==False:
                        bb.visited=True
                        bb.parent=src
                        ls.append(bb)
        for jj in out:
            print(jj.name)
            
        to=out[3]
        print(to.name)
        while to.parent!=None:
            e=to.parent
            print(e.name)
            to=to.parent


    def dfsanddetectcycle(self,src):
        src.visited=True
        yo=[]
        output=[]
        sup=[]
        sup.append(src)
        while 0<1:
            if sup==[]:
                break
            else:
                k =sup.pop()
                output.append(k)
                for q in self.adjlist[k]:
                    if q.visited==False:
                        q.visited =True
                        sup.append(q)
                    elif q.visited ==True:
                        print('cycle detected')
                        yo.append(k.name)
                        yo.append(q.name)
        print(yo)
        for pp in output:
            print(pp.name)

    cat=[]

    def dfsrecursion(self,src):
        src.visited=True
        self.cat.append(src.name)
        for e in self.adjlist[src]:
            if e.visited==False:
                self.dfsrecursion(e)
                print(self.cat)
        

data='a'
a=node(data)
data='b'
b=node(data)
data='c'
c=node(data)
data='d'
d=node(data)
data='e'
e=node(data)
data = 'f'
f=node(data)
node = [a,b,c,d,e]
jo=graph(node)
jo.addadj(a,c)
jo.addadj(a,b)
jo.addadj(b,d)
jo.addadj(d,a)
jo.addadj(d,e)
jo.dfsrecursion(a)
