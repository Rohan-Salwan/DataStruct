class node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class tree:
    def __init__(self):
        self.root=None

    def insertion(self):
        while 0 < 1:
            z=int(input())
            l=node(z)
            if z!= -1:
                self.root=self.create(l,self.root)
            elif z== -1:
                break
            else:
                pass

    def create(self,x,t):
        if t==None:
            t=x
        elif t.data >= x.data:
            t.left=self.create(x,t.left)
        else:
            t.right=self.create(x,t.right)
        return t

    
    def view(self):
        self.root1=self.traverse(self.root)

    def traverse(self,x):
        if self.root == None:
            print('tree is empty')
        else:
            if x==None:
                return None
                pass
            else:
                print(x.data)
                self.traverse(x.left)
                self.traverse(x.right)
                    
    def deletion(self):
        kp=int(input(''))
        self.root=self.r(self.root,kp)

    def findmax(self,m,temp):
        if m.right==None:
            self.temp=m
            return None
        else:
            m.right=self.findmax(m.right,temp)
            return m

    def r(self,kk,x):
        if kk==None:
            return None
        else:
            if kk.data==x:
                if kk.right==None and kk.left==None:
                    return None
                elif kk.left!=None and kk.right!=None:
                    broo=node(0)
                    self.findmax(kk.left,broo)
                    lool=self.temp
                    kk.data =lool.data
                    kk.left=self.r(kk.left,lool.data)
                else:
                    if kk.left==None and kk.right!=None:
                        kk=kk.right
                    else:
                        kk.left!=None and kk.right==None
                        kk=kk.left
        kk.left=self.r(kk.left,x)
        kk.right=self.r(kk.right,x)
        return kk

                

                





c = tree()
c.insertion()
c.view()
