class MyCircularDeque(object):

    def __init__(self, k):
        
        self.k = k
        self.deque = []
        
    def insertFront(self, value):
        if len(self.deque) < self.k:
            self.deque.insert(0,value)
            return True
        
        return False
        
    def insertLast(self, value):
        if len(self.deque) < self.k:
            self.deque.append(value)
            return True
        
        return False
        
    def deleteFront(self):
        if self.deque:
            self.deque.pop(0)
            return True
        
        return False
        
    def deleteLast(self):
        if self.deque:
            self.deque.pop()
            return True
        
        return False        

    def getFront(self):
        if self.deque:
            return self.deque[0]
    
        return -1

    def getRear(self):
        
        return self.deque[-1] if self.deque  else -1
    
        
    def isEmpty(self):
        
        return False if self.deque  else True
       
    def isFull(self): 
        
        return True if (len(self.deque) == self.k) else False
