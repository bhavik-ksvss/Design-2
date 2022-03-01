class MyQueue:

    def __init__(self):
        self.stk1=[]
        self.stk2=[]
        

    def push(self, x: int) -> None:
            
        self.stk1.append(x)
            
    def pop(self) -> int:
        if self.stk2:
            return self.stk2.pop()
        else:
            while self.stk1:
                self.stk2.append(self.stk1.pop())
            return self.stk2.pop()

    def peek(self) -> int:
        if self.stk2:
            return self.stk2[-1]
        else:
            while self.stk1:
                self.stk2.append(self.stk1.pop())
                
        return self.stk2[-1]

    def empty(self) -> bool:
        if len(self.stk1)==0 and len(self.stk2)==0:
            return True
        return False
