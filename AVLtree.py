class node:
    def __init__(self,data):
        self.data =data
        self.left=None
        self.right=None
        self.height=1

class avlbst:
    def __init__(self):
        self.root = None

    def insertion(self):
        while 0<1:
            l = int(input(''))
            if l == -1:
                break
            else:
                self.root=self.b(self.root,l)


    def maxx(self,a,b):
        if a < c:
            return b
        else:
            return a

    def height(self,n):
        if n==None:
            return 0
        else:
            return n.height

    def balance(self,kk):
        if kk==None:
            return 0
        else:
            return self.height(kk.left) - self.height(kk.right)


    def b(self,x,item):
        if x==None:
            newnode=node(item)
            x=newnode
        elif item < x.data:
            x.left=self.b(x.left,item)
        elif item>x.data:
            x.right=self.b(x.right,item)
        x.height = 1 + self.maxx(self.height(x.left),self.height(x.right))
        balance1 = self.balance(x)
        if balance1 > 1 and item < x.left.data:
            return self.rightrotation(x)
        if balance1 < -1 and item > x.right.data:
            return self.leftrotation(x)
        if balance1 > 1 and item > x.left.data:
            x.left = self.leftrotation(x.left)
            return self.rightrotation(x)
        if balance1 < -1 and item < x.right.data:
            x.right = self.rightrotation(x.right)
            return self.leftrotation(x)
        return x

    def rightrotation(self,mm):
        a=mm.left
        c=a.right
        a.right=mm
        mm.left=c
        mm.height= 1 + self.maxx(self.height(mm.left),self.height(mm.right))
        a.height= 1 + self.maxx(self.height(a.left),self.height(a.right))
        return a
        
    def leftrotation(self,x):  
        jj=x.right
        t=jj.left
        jj.left=x
        x.right=t
        jj.height = 1 + self.maxx(self.height(jj.left),self.height(jj.right))
        x.height= 1 + self.maxx(self.height(x.left),self.height(x.right))
        return jj

    def view(self):
        self.root1=self.traverse(self.root)

    def traverse(self,v):
        if self.root==None:
            print('tree is empty')
        else:
            if v==None:
                return None
            else:
                print(v.data)
                print('height')
                print(v.height)
                print('')
                self.traverse(v.left)
                self.traverse(v.right)

    def numbermax(self,c):
        self.temp=node(0)
        while c.right!=None:
            c=c.right
        self.temp=c



    def deletion(self):
        gh =int(input(''))
        self.root=self.wipe(self.root,gh)

    def wipe(self,d,ff):
        if self.root == None:
            print('tree is empty')
        else:
            if d==None:
                return None
            else:
                if ff < d.data:
                    d.left=self.wipe(d.left,ff)
                elif ff > d.data:
                    d.right =self.wipe(d.right,ff)
                if ff == d.data:
                    if d.left==None and d.right ==None:
                        return None
                    elif d.left ==None and d.right!=None:
                        d=d.right
                    elif d.left!=None and d.right ==None:
                        d=d.left
                    elif d.left!=None and d.right != None:
                        self.numbermax(d.left)
                        d.data=self.temp.data
                        self.wipe(self.root,self.temp.data)
                    else:
                        pass
                balancee=self.balance(d)
                if balancee > 1 and ff < d.left.data:
                    return self.rightrotation(d)
                if balancee < -1 and ff > d.right.data:
                    return self.leftrotation(d)
                if balancee > 1 and ff > d.left.data:
                    d.left = self.leftrotation(d.left)
                    return self.rightrotation(d)
                if balancee < -1 and ff < d.right.data:
                    d.right=self.rightrotation(d.right)
                    return self.leftrotation(d)
            return d





b = avlbst()
b.insertion()
b.deletion()
b.view()
