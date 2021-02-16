import array

class ram:
    def __init__(self,size):
        self.q = array.array('i',())
        self.size = size

    def enque(self,item):
        if len(self.q) > self.size:
            print('queue is full')
        elif self.size < 0:
            print('invalid size')
        else:
            self.q.append(item)
    
    def deque(self):
        if len(self.q)<0:
            print('underflow condition')
        else:
            self.q.pop(0)

    def view(self):
        if len(self.q)<0:
            print('queue is empty')
        else:
            for e in self.q:
                print(e)


d = ram(6)
d.enque(5)
d.enque(60)
d.enque(700)
d.enque(9000)
d.enque(30000)
d.view()
print('')
d.deque()
d.view()
