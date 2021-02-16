import StackArray

class node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class tree:
    def __init__(self):
        self.root=None

    
    def add(self):
        while 0<1:
            data=int(input())
            if data==-1:
                break
            else:
                self.root=self.insertion(self.root,data)


    def insertion(self,r,data):
        x=node(data)
        if r==None:
            self.t=x
            return x
        else:
            while r!=None:
                if r.data<x.data:
                    if r.right==None:
                        r.right=x
                        break
                    else:    
                        r=r.right
                else:
                    if r.left==None:
                        r.left=x
                        break
                    else:    
                        r=r.left
            return r

    def traverse(self):
        self.c(self.t)



    def view(self,o):
        if o==None:
            return None
        else:
            print(o.data)
            self.view(o.left)
            self.view(o.right)


    def view1(self,lion):
        while lion!=None:
            if lion.data<lion.left.data:
                la(lion)
                lion=lion.right
        ladisplay()
        print('')
    
    def c(self,r):
        if r==None:
            return None
        lamp= StackArray.stack(50)
        lamp.push(r)
        while (lamp.Empty()==False):
            r=lamp.peek()
            print(r.data)
            lamp.pop()
            if (r.right):
                lamp.push(r.right)
            if (r.left):
                lamp.push(r.left)

                                       
            

    


            


            



                


b=tree()
b.add()
b.traverse()
