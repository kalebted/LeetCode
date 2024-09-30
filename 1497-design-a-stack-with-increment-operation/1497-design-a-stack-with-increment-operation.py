class CustomStack:

    def __init__(self, maxSize: int):
        self.max_size = maxSize
        self.stack = []
        self.inc = []

    def push(self, x: int) -> None:
        if len(self.stack) >= self.max_size:
            return

        self.stack.append(x)
        self.inc.append(0)

    def pop(self) -> int:
        if len(self.stack) == 0:
            return -1
        
        x = self.stack.pop()
        delta = self.inc.pop()
        if len(self.inc) > 0:
            self.inc[-1] += delta
        x += delta
        return x

    def increment(self, k: int, val: int) -> None:
        if k - 1 >= len(self.inc):
            if len(self.inc) > 0:
                self.inc[-1] += val
        else:
            self.inc[k - 1] += val


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)