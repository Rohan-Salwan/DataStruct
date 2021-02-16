class stack:
    def __init__(self,size): 
        self.stack = []
        self.size = size
    
    def push(self,item):
        if len(self.stack) == self.size:
            print('stack overflow')
        else:
            self.stack.append(item)

    def pop(self):
        if len(self.stack) == 0:
            print('stack underflow')
        else:
            self.stack.pop()

    def peek(self):
        if self.stack==0:
            print('stack is empty')
        else:
            b=len(self.stack)-1
            e=self.stack[b]
            return e
                

    def display(self):
        if len(self.stack) == 0:
            print('stack is empty')
        else:
            for e in self.stack:
                print(e)
    
    def Empty(self):
        if self.stack==[]:
            return True
        else:
            return False

j=stack(50)
j.push(32)
j.push(16)
j.push(22)
j.push(11)
j.peek()
            
