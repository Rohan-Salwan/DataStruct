class node:
    def __init__(self,data):
        self.data = data
        self.next =None

class stack:
    def __init__(self):
        self.head = None

    def push(self,item):
        newnode = node(item)
        if self.head ==None:
            self.head = newnode
        else:
            newnode.next = self.head
            self.head = newnode



    def pop(self):
        if self.head ==None:
            print('stack is empty')
        else:
            self.head =self.head.next

    def view(self):
        if self.head == None:
            print('stack is empty')
        else:
            temp = self.head
            while temp!=None:
                print(temp.data)
                temp = temp.next
    
    def peek(self):
        if self.head ==None:
            print('stack is empty')
        else:
            print(self.head.data)
    
        
    



        
lol = stack()
lol.push(9)
lol.push(900)
lol.push(1900)
lol.push('bhai')
lol.push(2200)
lol.view()
print('')
lol.peek()
lol.view()
print('')
lol.pop()
lol.peek()
lol.view()

