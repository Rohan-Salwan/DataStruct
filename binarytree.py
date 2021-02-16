class node:
    def __init__(self,data):
        self.data = data
        self.left= None
        self.right=None

class tree:
    def __init__(self):
        self.root = None
        
    def create(self):
        x=input('insert data otherwise press -1 to pass')
        if x == '-1':
            return None
            pass
        else:
            x = node(x)
            print('enter left node for', x.data)
            x.left = self.create()
            print('enter right node for', x.data)
            x.right=self.create()
            return x

    def insertion(self):
        self.root= self.create() 
    
    def view(self):
        self.root1=self.traverse(self.root)
    
    def traverse(self,x):
        if self.root==None:    
            print('tree is empty')
        else:    
            if x == None:
                return None
                pass
            else:
                print(x.data)
                self.traverse(x.left)
                self.traverse(x.right)

    def dell(self):
        x=input()
        z=input()
        self.root=self.deletion(z,x,self.root)


    def deletion(self,z,x,t):
        if t == None:
            return None
            pass
        else:
            if t.data==x:
                t.data=z
            t.left =self.deletion(z,x,t.left)
            t.right=self.deletion(z,x,t.right)
            return t
    
    def pop(self):
        cap=input('')
        self.root=self.pop1(self.root,cap)


    def pop1(self,j,m):
        if j==None:
            return None
        else:
            if j.data==m:
                if j.left==None and j.right==None:
                    return None
            j.left=self.pop1(j.left,m)
            j.right=self.pop1(j.right,m)
            return j


                           








b = tree()
b.insertion()
b.view()
b.pop()
print('')
b.view()


