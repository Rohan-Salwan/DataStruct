class node:
    def __init__(self, data):
        self.data = data
        self.next = None


class linkedlist:
    def __init__(self):
        self.start = None


    def frontinsertion(self, value):
        if self.start == None:
            self.start = value
        else:
            value.next = self.start
            self.start = value
    

    def tailinsertion(self,value):
        if self.start ==None:
            self.start = value
            self.tail = value
        else:
            self.temp = self.start
            self.tail = self.start
            while self.temp.next!=None:
                self.tail = self.temp
                self.temp = self.temp.next
            self.tail=self.temp
            self.temp.next = value
            self.tail=self.temp.next




    def bigO1insertionlast(self,jk):
        if self.start == None:
            self.start=jk
            self.tail=jk
        else:
            self.tail.next=jk
            self.tail=self.tail.next 
            

    def view(self):
        if self.start == None:
            print('linked list is empty')
        else:
            temp = self.start
            while temp != None:
                print(temp.data)
                temp = temp.next

    
    def frontdeletion(self):
        if self.start == None:
            print('linked list is empty')
        else:
            self.start = self.start.next

    
    def lastdeletion(self):
        if self.start == None:
            print('list is empty')
        else:
            temp = self.start
            prev = self.start
            while temp.next!=None:
                prev = temp
                temp = temp.next
            prev.next = None


    def deletionofnextelementofvalue(self,value):
        if self.start == None:
            print('list is empty')
        elif value == 0:
            temp = self.start
            self.start = temp.next
        else:
            temp = self.start
            i = 0
            while (temp is not None):
                if i == value -1:
                    if temp.next is not None:
                        temp.next=temp.next.next
                        print('value deleted')
                        return
                    else:
                        break
                temp = temp.next
                i += 1
            print('value not found')


    def count(self):
            self.sum = 0
            temp = self.start
            while temp.next!=None:
                temp = temp.next
                self.sum+=1


     
    def deletionofnextelement(self,value):
        self.count()
        if self.start == None:
            print('list is empty')
        else:
            if value > self.sum:
                print('value not found')
            elif value == 0:
                temp = self.start
                self.start = temp.next
            else:
                temp = self.start
                i = 1
                while (i <= value - 1):
                    temp = temp.next
                    i+=1
                l = temp.next
                temp.next = l.next

    
    def specificinsertion(self,value):
        self.count()
        if value > self.sum:
            print('value not found')
        else:
            newnode = node(800)
            temp = self.start
            i = 1
            while i <= value:
                temp = temp.next
                i+=1
            l = temp.next
            temp.next = newnode
            newnode.next = l 




node1 = node(50)
node2 = node('bhai')
node3 = node(110)
node4 = node(150)
node5 = node('shiki')
node6 = node(234)
llist = linkedlist()
llist.bigO1insertionlast(node1)
llist.bigO1insertionlast(node2)
llist.bigO1insertionlast(node3)
llist.bigO1insertionlast(node4)
llist.bigO1insertionlast(node5)
llist.bigO1insertionlast(node6)
llist.view()
