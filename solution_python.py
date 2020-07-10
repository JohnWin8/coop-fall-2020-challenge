class EventSourcer():
    # Do not change the signature of any functions

    def __init__(self):
        self.value = 0
        self.list = [self.value]
        self.undone = []

    def add(self, num: int):
        self.list.append(num)
        self.value += num
        if len(self.undone) > 0:
            self.undone.pop()

    def subtract(self, num: int):
        self.add(0-num)

    def undo(self):
        if len(self.list) <= 1:
            return
        remove = self.list.pop()
        self.undone.append(remove)
        self.value -= remove
    
    def redo(self):
        if len(self.undone) < 1:
            return
        remove = self.undone.pop()
        self.list.append(remove)
        self.value += remove

    def bulk_undo(self, steps: int):
        for i in range(steps):
            self.undo()

    def bulk_redo(self, steps: int):
        for i in range(steps):
            self.redo()