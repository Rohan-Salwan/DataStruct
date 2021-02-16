class node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
        self.id=None
class hash1:
    def __init__(self,size):
        self.size=size
        self.hashtable=self.low()

    def low(self):
        self.t=[]
        for b in range(self.size):
            self.t.append([])
        return self.t
    
    def insertion(self,key,value):
        value=node(value)
        value.id=key
        if key == str(key):
           key =2*len(key)
        index=key%len(self.t)
        if self.hashtable[index]==[]:
            self.hashtable[index].append(value)
        else:
            value.next=self.hashtable[index][0]
            self.hashtable[index].insert(0,value)
    
    def searching(self,secret):
        self.d=secret
        if secret==str(secret):
            secret=2*len(secret)
        i=secret%len(self.t)
        if self.hashtable[i]==[]:
            print('value doesnot exist')
        elif self.hashtable[i][0].id==self.d:
            print(self.hashtable[i][0].data)
        elif self.hashtable[i][0].id!=self.d:
            bb=self.hashtable[i][0]
            while bb.next!=None:
                if bb.next.id==self.d:
                    print(bb.next.data)
                    break
                else:
                    bb=bb.next 



    

l=hash1(20)
l.insertion(20201,'bhai')
l.insertion(20321,3214)
l.insertion('jai','game')
l.insertion(67321,'lol')
l.insertion(30301,'cod')
l.searching(30301)
l.searching(20321)
l.searching('jai')
l.searching(67321)
l.searching(20201)
            




